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
    "SHOPPING_BOOELAN_ATTRIBUTE_CHOICES",
    "GASTRO_BOOELAN_ATTRIBUTE_CHOICES",
    "BooleanAttribute",
    "LocationTypeChoices",
    "BaseLocation",
    "Gastro",
    "DISTRICT_CHOICES",
    "NULLBOOLEAN_CHOICE",
    "PositiveIntegerAttribute",
    "GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES",
)


class BaseLocationID(models.Model):
    # id string
    id_string = models.CharField(_("unique id"), max_length=32, unique=True, blank=True)

    class Meta:
        abstract = True

    def save(self, **kwargs):
        if not self.id_string:
            return self.set_string(**kwargs)

        return super(BaseLocationID, self).save(**kwargs)

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
    ("accommodation", "accommodation"),
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

SHOPPING_BOOELAN_ATTRIBUTE_CHOICES = BASE_BOOLEAN_ATTRIBUTE_CHOICES + (
    ("webshop", "Webshop"),
)

GASTRO_BOOELAN_ATTRIBUTE_CHOICES = BASE_BOOLEAN_ATTRIBUTE_CHOICES + (
    ("handicapped_accessible_wc", "Handicapped Accessible WC"),
    ("dog", "Dog"),
    ("child_chair", "Child Chair"),
    ("catering", "Catering"),
    ("wlan", "Wlan"),
    ("gluten_free", "Gluten Free"),
    ("breakfast", "Breakfast"),
    ("brunch", "Brunch"),
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
        max_length=max(map(len, dict(SHOPPING_BOOELAN_ATTRIBUTE_CHOICES))),
        choices=SHOPPING_BOOELAN_ATTRIBUTE_CHOICES,
    )
    state = models.BooleanField(choices=NULLBOOLEAN_CHOICE, null=True)

    class Meta:
        unique_together = ["name", "state"]
        constraints = [
            models.CheckConstraint(
                name="%(app_label)s_%(class)s_name_valid",
                check=models.Q(
                    name__in=list(
                        map(lambda x: x[0], SHOPPING_BOOELAN_ATTRIBUTE_CHOICES)
                    )
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


class BaseLocation(BaseLocationID):
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


class BaseLocationOld(models.Model):
    created = models.DateTimeField(_("created"), auto_now_add=True)
    updated = models.DateTimeField(_("updated"), auto_now=True)
    name = models.CharField(_("Name of location"), max_length=100)
    street = models.CharField(_("Street / No"), max_length=100)
    postal_code = models.CharField(_("Postal code"), max_length=5)
    city = models.CharField(_("City"), max_length=20, default="Berlin")
    latitude = models.FloatField(_("latitude"))
    longitude = models.FloatField(_("longitude"))
    telephone = models.CharField(_("Telephone"), max_length=25, null=True, blank=True)
    website = models.URLField(_("Website"), null=True, blank=True)
    email = models.EmailField(_("E-mail"), null=True, blank=True)

    opening_mon = models.TimeField(_("opening monday"), null=True, blank=True)
    closing_mon = models.TimeField(_("closing monday"), null=True, blank=True)
    opening_tue = models.TimeField(_("opening tuesday"), null=True, blank=True)
    closing_tue = models.TimeField(_("closing tuesday"), null=True, blank=True)
    opening_wed = models.TimeField(_("opening wednesday"), null=True, blank=True)
    closing_wed = models.TimeField(_("closing wednesday"), null=True, blank=True)
    opening_thu = models.TimeField(_("opening thursday"), null=True, blank=True)
    closing_thu = models.TimeField(_("closing thursday"), null=True, blank=True)
    opening_fri = models.TimeField(_("opening friday"), null=True, blank=True)
    closing_fri = models.TimeField(_("closing friday"), null=True, blank=True)
    opening_sat = models.TimeField(_("opening saturday"), null=True, blank=True)
    closing_sat = models.TimeField(_("closing saturday"), null=True, blank=True)
    opening_sun = models.TimeField(_("opening sunday"), null=True, blank=True)
    closing_sun = models.TimeField(_("closing sunday"), null=True, blank=True)

    vegan = models.IntegerField(_("Vegan friendly"), choices=VEGAN_CHOICE)
    comment = models.TextField(_("Comment in German"), null=True, blank=True)
    comment_english = models.TextField(_("Comment in English"), null=True, blank=True)
    review_link = models.URLField(
        _("review link"), max_length=255, default="", blank=True
    )
    closed = models.DateField(_("closed"), null=True, default=None)
    text_intern = models.TextField(_("text intern"), null=True, blank=True)

    class Meta:
        abstract = True


# we are using the old berlin districts: https://de.wikipedia.org/wiki/Berliner_Bezirke#Zeit_der_Teilung_Berlins

CHOICE_CHA = "CHARLOTTENBURG"
CHOICE_FRI = "FRIEDRICHSHAIN"
CHOICE_HEL = "HELLERSDORF"
CHOICE_HOH = "HOHENSCHÖNHAUSEN"
CHOICE_KRE = "KREUZBERG"
CHOICE_KOP = "KÖPENICK"
CHOICE_LIC = "LICHTENBERG"
CHOICE_MAR = "MARZAHN"
CHOICE_MIT = "MITTE"
CHOICE_NEU = "NEUKÖLLN"
CHOICE_PAN = "PANKOW"
CHOICE_PRE = "PRENZLAUER BERG"
CHOICE_REI = "REINICKENDORF"
CHOICE_SCH = "SCHÖNEBERG"
CHOICE_SPA = "SPANDAU"
CHOICE_STE = "STEGLITZ"
CHOICE_TEM = "TEMPELHOF"
CHOICE_TIE = "TIERGARTEN"
CHOICE_TRE = "TREPTOW"
CHOICE_WED = "WEDDING"
CHOICE_WEI = "WEISSENSEE"
CHOICE_WIL = "WILMERSDORF"
CHOICE_ZEH = "ZEHLENDORF"

DISTRICT_CHOICES = [
    (CHOICE_CHA, "Charlottenburg"),
    (CHOICE_FRI, "Friedrichshain"),
    (CHOICE_HEL, "Hellersdorf"),
    (CHOICE_HOH, "Hohenschönhausen"),
    (CHOICE_KRE, "Kreuzberg"),
    (CHOICE_KOP, "Köpenick"),
    (CHOICE_LIC, "Lichtenberg"),
    (CHOICE_MAR, "Marzahn"),
    (CHOICE_MIT, "Mitte"),
    (CHOICE_NEU, "Neukölln"),
    (CHOICE_PAN, "Pankow"),
    (CHOICE_PRE, "Prenzlauer Berg"),
    (CHOICE_REI, "Reinickendorf"),
    (CHOICE_SCH, "Schöneberg"),
    (CHOICE_SPA, "Spandau"),
    (CHOICE_STE, "Steglitz"),
    (CHOICE_TEM, "Tempelhof"),
    (CHOICE_TIE, "Tiergarten"),
    (CHOICE_TRE, "Treptow"),
    (CHOICE_WED, "Wedding"),
    (CHOICE_WEI, "Weißensee"),
    (CHOICE_WIL, "Wilmersdorf"),
    (CHOICE_ZEH, "Zehlendorf"),
]


class BaseGastro(BaseLocationOld):
    district = models.CharField(
        _("District"), max_length=30, null=True, blank=True, choices=DISTRICT_CHOICES
    )
    public_transport = models.CharField(
        _("Public transport"), max_length=255, null=True, blank=True
    )

    handicapped_accessible = models.BooleanField(
        _("Wheelchair accessible"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    handicapped_accessible_wc = models.BooleanField(
        _("Wheelchair accessible toilet"),
        choices=NULLBOOLEAN_CHOICE,
        null=True,
        blank=True,
    )
    dog = models.BooleanField(
        _("Dogs allowed"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    child_chair = models.BooleanField(
        _("High chair"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    catering = models.BooleanField(
        _("Catering"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    delivery = models.BooleanField(
        _("Delivery service"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    organic = models.BooleanField(
        _("Organic"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    wlan = models.BooleanField(
        _("Wi-Fi"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    gluten_free = models.BooleanField(
        _("Gluten-free options"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    breakfast = models.BooleanField(
        _("Vegan Breakfast"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    brunch = models.BooleanField(
        _("Brunch"), choices=NULLBOOLEAN_CHOICE, null=True, blank=True
    )
    seats_outdoor = models.IntegerField(_("Seats outdoor"), null=True, blank=True)
    seats_indoor = models.IntegerField(_("Seats indoor"), null=True, blank=True)

    restaurant = models.BooleanField(_("Restaurant"), default=False)
    imbiss = models.BooleanField(_("Snack bar"), default=False)
    eiscafe = models.BooleanField(_("Ice cream parlor"), default=False)
    cafe = models.BooleanField(_("Café"), default=False)
    bar = models.BooleanField(_("Bar"), default=False)

    comment_open = models.TextField(_("Comment opening hours"), null=True, blank=True)

    submit_email = models.EmailField(_("Submitter e-mail"), default="", blank=True)

    class Meta:
        abstract = True


class Gastro(BaseLocationID, BaseGastro):
    last_editor = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("last editor"),
    )

    has_sticker = models.BooleanField(_("Sticker"), default=False)
    is_submission = models.BooleanField(_("Submission"), default=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ["name"]

    objects = GastroQuerySet.as_manager()

    # creates a dict of the model object
    def as_dict(self):
        gastro_dict = {}
        # must be in the dict and db
        gastro_dict.update(
            id=self.id_string,
            name=self.name,
            street=self.street,
            cityCode=self.postal_code,
            city=self.city,
            latCoord=self.latitude,
            longCoord=self.longitude,
            vegan=self.vegan,
            district=self.get_district_display(),
        )

        # opening hours
        if self.telephone is not None:
            gastro_dict.update(telephone=self.telephone)
        if self.website is not None:
            gastro_dict.update(website=self.website)
        if self.email is not None:
            gastro_dict.update(email=self.email)
        if self.opening_mon is not None:
            gastro_dict.update(
                otMon=str(self.opening_mon.strftime("%H:%M"))
                + " - "
                + str(self.closing_mon.strftime("%H:%M"))
            )
        if self.opening_tue is not None:
            gastro_dict.update(
                otTue=str(self.opening_tue.strftime("%H:%M"))
                + " - "
                + str(self.closing_tue.strftime("%H:%M"))
            )
        if self.opening_wed is not None:
            gastro_dict.update(
                otWed=str(self.opening_wed.strftime("%H:%M"))
                + " - "
                + str(self.closing_wed.strftime("%H:%M"))
            )
        if self.opening_thu is not None:
            gastro_dict.update(
                otThu=str(self.opening_thu.strftime("%H:%M"))
                + " - "
                + str(self.closing_thu.strftime("%H:%M"))
            )
        if self.opening_fri is not None:
            gastro_dict.update(
                otFri=str(self.opening_fri.strftime("%H:%M"))
                + " - "
                + str(self.closing_fri.strftime("%H:%M"))
            )
        if self.opening_sat is not None:
            gastro_dict.update(
                otSat=str(self.opening_sat.strftime("%H:%M"))
                + " - "
                + str(self.closing_sat.strftime("%H:%M"))
            )
        if self.opening_sun is not None:
            gastro_dict.update(
                otSun=str(self.opening_sun.strftime("%H:%M"))
                + " - "
                + str(self.closing_sun.strftime("%H:%M"))
            )

        # gastro comments
        if self.comment is not None:
            gastro_dict.update(comment=self.comment)
        if self.comment_english is not None:
            gastro_dict.update(commentEnglish=self.comment_english)
        if self.comment_open is not None:
            gastro_dict.update(openComment=self.comment_open)

        # gastro public transport
        if self.public_transport is not None:
            gastro_dict.update(publicTransport=self.public_transport)

        # gastro description
        if self.handicapped_accessible is None:
            gastro_dict.update(handicappedAccessible=-1)
        elif self.handicapped_accessible is True:
            gastro_dict.update(handicappedAccessible=1)
        elif self.handicapped_accessible is False:
            gastro_dict.update(handicappedAccessible=0)

        if self.handicapped_accessible_wc is None:
            gastro_dict.update(handicappedAccessibleWc=-1)
        elif self.handicapped_accessible_wc is True:
            gastro_dict.update(handicappedAccessibleWc=1)
        elif self.handicapped_accessible_wc is False:
            gastro_dict.update(handicappedAccessibleWc=0)

        if self.dog is None:
            gastro_dict.update(dog=-1)
        elif self.dog is True:
            gastro_dict.update(dog=1)
        elif self.dog is False:
            gastro_dict.update(dog=0)

        if self.child_chair is None:
            gastro_dict.update(childChair=-1)
        elif self.child_chair is True:
            gastro_dict.update(childChair=1)
        elif self.child_chair is False:
            gastro_dict.update(childChair=0)

        if self.catering is None:
            gastro_dict.update(catering=-1)
        elif self.catering is True:
            gastro_dict.update(catering=1)
        elif self.catering is False:
            gastro_dict.update(catering=0)

        if self.delivery is None:
            gastro_dict.update(delivery=-1)
        elif self.delivery is True:
            gastro_dict.update(delivery=1)
        elif self.delivery is False:
            gastro_dict.update(delivery=0)

        if self.organic is None:
            gastro_dict.update(organic=-1)
        elif self.organic is True:
            gastro_dict.update(organic=1)
        elif self.organic is False:
            gastro_dict.update(organic=0)

        if self.wlan is None:
            gastro_dict.update(wlan=-1)
        elif self.wlan is True:
            gastro_dict.update(wlan=1)
        elif self.wlan is False:
            gastro_dict.update(wlan=0)

        if self.gluten_free is None:
            gastro_dict.update(glutenFree=-1)
        elif self.gluten_free is True:
            gastro_dict.update(glutenFree=1)
        elif self.gluten_free is False:
            gastro_dict.update(glutenFree=0)

        if self.breakfast is None:
            gastro_dict.update(breakfast=-1)
        elif self.breakfast is True:
            gastro_dict.update(breakfast=1)
        elif self.breakfast is False:
            gastro_dict.update(breakfast=0)

        if self.brunch is None:
            gastro_dict.update(brunch=-1)
        elif self.brunch is True:
            gastro_dict.update(brunch=1)
        elif self.brunch is False:
            gastro_dict.update(brunch=0)

        if self.seats_outdoor is not None:
            gastro_dict.update(seatsOutdoor=self.seats_outdoor)
        if self.seats_indoor is not None:
            gastro_dict.update(seatsIndoor=self.seats_indoor)

        # tags fehlt in data import
        tags = []
        if self.restaurant is True:
            tags.append("Restaurant")
        if self.imbiss is True:
            tags.append("Imbiss")
        if self.eiscafe is True:
            tags.append("Eiscafe")
        if self.cafe is True:
            tags.append("Cafe")
        if self.bar is True:
            tags.append("Bar")
        gastro_dict.update(tags=tags)

        if self.review_link:
            gastro_dict.update(reviewURL=self.review_link.split("/")[-2])

        # name
        if self.closed:
            gastro_dict.update(name=f"{self.name} - GESCHLOSSEN / CLOSED")
            gastro_dict.update(otMon="")
            gastro_dict.update(otTue="")
            gastro_dict.update(otWed="")
            gastro_dict.update(otThu="")
            gastro_dict.update(otFri="")
            gastro_dict.update(otSat="")
            gastro_dict.update(otSun="")
            gastro_dict.pop("telephone", None)

        gastro_dict.update(created=self.created.strftime("%Y-%m-%d"))

        return gastro_dict
