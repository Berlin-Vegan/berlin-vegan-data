import re

from django.contrib.auth.models import User
from django.db import IntegrityError, models, transaction
from django.utils.translation import gettext_lazy as _

from bvdata.data.managers import GastroQuerySet
from bvdata.data.utils import get_random_string_32

__all__ = (
    "WeekdayChoices",
    "OpeningHours",
    "VEGAN_CHOICE",
    "SHOPPING_TAG_CHOICES",
    "GASTRO_TAG_CHOICES",
    "TAG_CHOICES",
    "Tag",
    "SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES",
    "GASTRO_BOOLEAN_ATTRIBUTE_CHOICES",
    "BooleanAttribute",
    "LocationTypeChoices",
    "BaseLocation",
    "NULLBOOLEAN_CHOICE",
    "PositiveIntegerAttribute",
    "GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES",
    "OMNIVORE_VEGAN",
    "VEGAN_VEGAN",
    "NULLBOOLEAN_NULL",
)


class WeekdayChoices(models.TextChoices):
    MONDAY = "MONDAY", "Monday"
    TUESDAY = "TUESDAY", "Tuesday"
    WEDNESDAY = "WEDNESDAY", "Wednesday"
    THURSDAY = "THURSDAY", "Thursday"
    FRIDAY = "FRIDAY", "Friday"
    SATURDAY = "SATURDAY", "Saturday"
    SUNDAY = "SUNDAY", "Sunday"


class OpeningHours(models.Model):
    location = models.ForeignKey(to="BaseLocation", on_delete=models.CASCADE)
    weekday = models.CharField(
        max_length=max(map(len, WeekdayChoices.values)), choices=WeekdayChoices.choices
    )
    opening = models.TimeField(null=True, blank=True)
    closing = models.TimeField(null=True, blank=True)

    class Meta:
        unique_together = ["weekday", "location"]
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_weekday_valid",
                check=models.Q(weekday__in=WeekdayChoices.values),
            )
        ]

    def __str__(self):
        return f"{self.location_id},{self.weekday},{self.opening},{self.closing}"


OMNIVORE_VEGAN = 2
VEGETARIAN_VEGAN = 4
VEGAN_VEGAN = 5

VEGAN_CHOICE = (
    (OMNIVORE_VEGAN, "Ominvore (vegan labeled)"),
    (VEGETARIAN_VEGAN, "Vegetarian (vegan labeled)"),
    (VEGAN_VEGAN, "Vegan"),
)

SHOPPING_TAG_CHOICES = (
    ("foods", "Foods"),
    ("clothing", "Clothing"),
    ("toiletries", "Toiletries"),
    ("supermarket", "Supermarket"),
    ("hairdressers", "Hairdressers"),
    ("sports", "Sports"),
    ("tattoostudio", "Tattoostudio"),
    ("accommodation", "Accommodation"),
)

GASTRO_TAG_CHOICES = (
    ("bar", "Bar"),
    ("cafe", "Cafe"),
    ("ice cream parlor", "Ice Cream Parlor"),
    ("snack bar", "Snack Bar"),
    ("restaurant", "Restaurant"),
)

TAG_CHOICES = SHOPPING_TAG_CHOICES + GASTRO_TAG_CHOICES


class Tag(models.Model):
    tag = models.CharField(
        max_length=max(map(len, dict(TAG_CHOICES))), choices=TAG_CHOICES, unique=True
    )

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_tag_valid",
                check=models.Q(tag__in=list(map(lambda x: x[0], TAG_CHOICES))),
            )
        ]

    def __str__(self):
        return self.tag


BASE_BOOLEAN_ATTRIBUTE_CHOICES = (
    ("organic", "Organic"),
    ("delivery", "Delivery"),
    ("handicapped_accessible", "Handicapped Accessible"),
)

SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES = BASE_BOOLEAN_ATTRIBUTE_CHOICES + (
    ("webshop", "Webshop"),
)

GASTRO_BOOLEAN_ATTRIBUTE_CHOICES = BASE_BOOLEAN_ATTRIBUTE_CHOICES + (
    ("handicapped_accessible_wc", "Handicapped Accessible WC"),
    ("dog", "Dog"),
    ("child_chair", "Child Chair"),
    ("catering", "Catering"),
    ("wlan", "Wlan"),
    ("gluten_free", "Gluten Free"),
    ("breakfast", "Breakfast"),
    ("brunch", "Brunch"),
)

ALL_BOOLEAN_ATTRIBUTE_CHOICES = (
    SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES + GASTRO_BOOLEAN_ATTRIBUTE_CHOICES
)

NULLBOOLEAN_NULL = None
NULLBOOLEAN_TRUE = True
NULLBOOLEAN_FALSE = False

NULLBOOLEAN_CHOICE = (
    (NULLBOOLEAN_NULL, _("unknown")),
    (NULLBOOLEAN_TRUE, _("yes")),
    (NULLBOOLEAN_FALSE, _("no")),
)


class BooleanAttribute(models.Model):
    name = models.CharField(
        max_length=max(map(len, dict(ALL_BOOLEAN_ATTRIBUTE_CHOICES))),
        choices=ALL_BOOLEAN_ATTRIBUTE_CHOICES,
    )
    state = models.BooleanField(choices=NULLBOOLEAN_CHOICE, null=True)

    class Meta:
        unique_together = ["name", "state"]
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_name_valid",
                check=models.Q(
                    name__in=list(map(lambda x: x[0], ALL_BOOLEAN_ATTRIBUTE_CHOICES))
                ),
            )
        ]


GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES = (
    ("seats_outdoor", "Seats Outdoor"),
    ("seats_indoor", "Seats Indoor"),
)


class PositiveIntegerAttribute(models.Model):
    name = models.CharField(
        max_length=max(map(len, dict(GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES))),
        choices=GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES,
    )
    state = models.PositiveIntegerField(default=0)

    class Meta:
        unique_together = ["name", "state"]
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_name_valid",
                check=models.Q(
                    name__in=list(
                        map(lambda x: x[0], GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES)
                    )
                ),
            )
        ]


class LocationTypeChoices(models.TextChoices):
    GASTRO = "GASTRO"
    SHOPPING = "SHOPPING"


class BaseLocation(models.Model):
    # id string
    id_string = models.CharField(_("unique id"), max_length=32, unique=True, blank=True)
    type = models.CharField(
        max_length=max(map(len, LocationTypeChoices.values)),
        choices=LocationTypeChoices.choices,
        editable=False,
    )
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    last_editor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("last editor"),
    )
    name = models.CharField(_("Name of location"), max_length=100)
    street = models.CharField(_("Street / No"), max_length=100)
    postal_code = models.CharField(_("Postal code"), max_length=5)
    city = models.CharField(_("City"), max_length=20, default="Berlin")
    latitude = models.FloatField(_("latitude"))
    longitude = models.FloatField(_("longitude"))
    telephone = models.CharField(_("Telephone"), max_length=25, null=True, blank=True)
    website = models.URLField(_("Website"), null=True, blank=True)
    email = models.EmailField(_("E-mail"), null=True, blank=True)

    vegan = models.IntegerField(_("Vegan friendly"), choices=VEGAN_CHOICE)
    comment = models.TextField(_("Comment in German"), default="", blank=True)
    comment_english = models.TextField(_("Comment in English"), default="", blank=True)
    comment_opening_hours = models.TextField(
        _("Comment opening hours"), default="", blank=True
    )
    comment_public_transport = models.TextField(
        _("Comment Public transport"), default="", blank=True
    )
    review_link = models.URLField(
        _("review link"), max_length=255, default="", blank=True
    )
    closed = models.DateField(_("closed"), null=True, default=None)
    text_intern = models.TextField(_("text intern"), default="", blank=True)
    has_sticker = models.BooleanField(_("Sticker"), default=False)
    is_submission = models.BooleanField(_("Submission"), default=True)
    submit_email = models.EmailField(_("Submitter e-mail"), null=True, blank=True)

    tags = models.ManyToManyField(Tag)
    boolean_attributes = models.ManyToManyField(BooleanAttribute)
    positive_integer_attributes = models.ManyToManyField(PositiveIntegerAttribute)

    objects = GastroQuerySet.as_manager()

    class Meta:
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_type_valid",
                check=models.Q(type__in=LocationTypeChoices.values),
            )
        ]

    def save(self, **kwargs):
        if not self.id_string:
            return self.set_string(**kwargs)

        return super(BaseLocation, self).save(**kwargs)

    def set_string(self, **kwargs):
        self.id_string = get_random_string_32()
        id_string_error_patter = re.compile(
            r"DETAIL:  Key \(id_string\)=\(.*\) already exists.$"
        )

        try:
            with transaction.atomic():
                return self.save(**kwargs)
        except IntegrityError as e:
            if id_string_error_patter.search(str(e)) is None:
                raise e
            return self.set_string(**kwargs)
