from typing import List

from django.contrib.auth import get_user_model
from django.db import migrations, models
from django.utils.translation import gettext_lazy as _

from bvdata.data.models import (
    GASTRO_BOOLEAN_ATTRIBUTE_CHOICES,
    GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES,
    BaseLocation,
    BooleanAttribute,
    LocationTypeChoices,
    OpeningHours,
    PositiveIntegerAttribute,
    Tag,
    WeekdayChoices,
)

OMNIVORE_VEGAN = 2
VEGETARIAN_VEGAN = 4
VEGAN_VEGAN = 5

VEGAN_CHOICE = (
    (OMNIVORE_VEGAN, "Ominvore (vegan labeled)"),
    (VEGETARIAN_VEGAN, "Vegetarian (vegan labeled)"),
    (VEGAN_VEGAN, "Vegan"),
)

NULLBOOLEAN_NULL = None
NULLBOOLEAN_TRUE = True
NULLBOOLEAN_FALSE = False

NULLBOOLEAN_CHOICE = (
    (NULLBOOLEAN_NULL, _("unknown")),
    (NULLBOOLEAN_TRUE, _("yes")),
    (NULLBOOLEAN_FALSE, _("no")),
)

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


class LegacyGastro(models.Model):
    id_string = models.CharField(_("unique id"), max_length=32, unique=True, blank=True)
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
    last_editor = models.ForeignKey(
        get_user_model(),
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        verbose_name=_("last editor"),
    )

    has_sticker = models.BooleanField(_("Sticker"), default=False)
    is_submission = models.BooleanField(_("Submission"), default=True)

    class Meta:
        db_table = "data_gastro"
        managed = False


def create_new_baselocation(legacy_gastro: LegacyGastro) -> BaseLocation:
    comment: str = legacy_gastro.comment if (legacy_gastro.comment is not None) else ""
    comment_english: str = (
        legacy_gastro.comment_english
        if legacy_gastro.comment_english is not None
        else ""
    )
    comment_opening_hours: str = (
        legacy_gastro.comment_open if legacy_gastro.comment_open is not None else ""
    )
    comment_public_transport: str = (
        legacy_gastro.public_transport
        if legacy_gastro.public_transport is not None
        else ""
    )
    text_intern: str = (
        legacy_gastro.text_intern if legacy_gastro.text_intern is not None else ""
    )
    new_gastro = BaseLocation.objects.create(
        id_string=legacy_gastro.id_string,
        type=LocationTypeChoices.GASTRO,
        created=legacy_gastro.created,
        updated=legacy_gastro.updated,
        last_editor_id=legacy_gastro.last_editor_id,
        name=legacy_gastro.name,
        street=legacy_gastro.street,
        postal_code=legacy_gastro.postal_code,
        city=legacy_gastro.city,
        latitude=legacy_gastro.latitude,
        longitude=legacy_gastro.longitude,
        telephone=legacy_gastro.telephone,
        website=legacy_gastro.website,
        email=legacy_gastro.email,
        vegan=legacy_gastro.vegan,
        comment=comment,
        comment_english=comment_english,
        comment_opening_hours=comment_opening_hours,
        comment_public_transport=comment_public_transport,
        review_link=legacy_gastro.review_link,
        closed=legacy_gastro.closed,
        text_intern=text_intern,
        has_sticker=legacy_gastro.has_sticker,
        is_submission=legacy_gastro.is_submission,
        submit_email=legacy_gastro.submit_email,
    )
    BaseLocation.objects.filter(id=new_gastro.id).update(
        created=legacy_gastro.created, updated=legacy_gastro.updated
    )
    return new_gastro


old_tags_mapping = {
    "bar": "bar",
    "cafe": "cafe",
    "eiscafe": "ice cream parlor",
    "imbiss": "snack bar",
    "restaurant": "restaurant",
}


def get_tags(legacy_gastro: LegacyGastro) -> List[Tag]:
    new_tags = []
    for old_tag in old_tags_mapping.keys():
        if getattr(legacy_gastro, old_tag):
            new_tags.append(Tag.objects.get_or_create(tag=old_tags_mapping[old_tag])[0])
    return new_tags


def get_boolean_attributes(legacy_gastro: LegacyGastro) -> List[BooleanAttribute]:
    attr_list: List[BooleanAttribute] = []
    for attr in dict(GASTRO_BOOLEAN_ATTRIBUTE_CHOICES):
        attr_list.append(
            BooleanAttribute.objects.get_or_create(
                name=attr, state=getattr(legacy_gastro, attr)
            )[0]
        )
    return attr_list


def get_positive_integer_attributes(
    legacy_gastro: LegacyGastro,
) -> List[PositiveIntegerAttribute]:
    attr_list: List[PositiveIntegerAttribute] = []
    for attr in dict(GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES):
        state = (
            getattr(legacy_gastro, attr)
            if getattr(legacy_gastro, attr) is not None
            and getattr(legacy_gastro, attr) >= 0
            else 0
        )
        attr_list.append(
            PositiveIntegerAttribute.objects.get_or_create(name=attr, state=state)[0]
        )
    return attr_list


def set_opening_hours(legacy_gastro: LegacyGastro, new_gastro: BaseLocation):
    OpeningHours.objects.update_or_create(
        location=new_gastro,
        weekday=WeekdayChoices.MONDAY,
        opening=legacy_gastro.opening_mon,
        closing=legacy_gastro.closing_mon,
    )
    OpeningHours.objects.update_or_create(
        location=new_gastro,
        weekday=WeekdayChoices.TUESDAY,
        opening=legacy_gastro.opening_tue,
        closing=legacy_gastro.closing_tue,
    )
    OpeningHours.objects.update_or_create(
        location=new_gastro,
        weekday=WeekdayChoices.WEDNESDAY,
        opening=legacy_gastro.opening_wed,
        closing=legacy_gastro.closing_wed,
    )
    OpeningHours.objects.update_or_create(
        location=new_gastro,
        weekday=WeekdayChoices.THURSDAY,
        opening=legacy_gastro.opening_thu,
        closing=legacy_gastro.closing_thu,
    )
    OpeningHours.objects.update_or_create(
        location=new_gastro,
        weekday=WeekdayChoices.FRIDAY,
        opening=legacy_gastro.opening_fri,
        closing=legacy_gastro.closing_fri,
    )
    OpeningHours.objects.update_or_create(
        location=new_gastro,
        weekday=WeekdayChoices.SATURDAY,
        opening=legacy_gastro.opening_sat,
        closing=legacy_gastro.closing_sat,
    )
    OpeningHours.objects.update_or_create(
        location=new_gastro,
        weekday=WeekdayChoices.SUNDAY,
        opening=legacy_gastro.opening_sun,
        closing=legacy_gastro.closing_sun,
    )


def build_new_gastro(legacy_gastro: LegacyGastro):
    new_gastro: BaseLocation = create_new_baselocation(legacy_gastro=legacy_gastro)
    new_tags: List[Tag] = get_tags(legacy_gastro=legacy_gastro)
    new_gastro.tags.set(new_tags)
    new_boolean_attrs: List[BooleanAttribute] = get_boolean_attributes(
        legacy_gastro=legacy_gastro
    )
    new_gastro.boolean_attributes.set(new_boolean_attrs)
    new_positive_integer_attrs: List[PositiveIntegerAttribute] = (
        get_positive_integer_attributes(legacy_gastro=legacy_gastro)
    )
    new_gastro.positive_integer_attributes.set(new_positive_integer_attrs)
    set_opening_hours(legacy_gastro=legacy_gastro, new_gastro=new_gastro)


def migrate_legacy_gastro(apps, schema_editor):
    legacy_gastros = LegacyGastro.objects.all()
    for old_location in legacy_gastros:
        build_new_gastro(old_location)


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0016_add_gastro_type_to_baselocation"),
    ]

    operations = [
        migrations.RunPython(
            code=migrate_legacy_gastro, reverse_code=migrations.RunPython.noop
        )
    ]
