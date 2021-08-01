from typing import List

from django.db import migrations

from bvdata.data.models import (
    GASTRO_BOOELAN_ATTRIBUTE_CHOICES,
    GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES,
    BaseLocation,
    BooleanAttribute,
    Gastro,
    LocationTypeChoices,
    OpeningHours,
    PositiveIntegerAttribute,
    Tag,
    WeekdayChoices,
)


def create_new_baselocation(legacy_gastro: Gastro) -> BaseLocation:
    new_gastro = BaseLocation(
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
        comment=legacy_gastro.comment,
        comment_english=legacy_gastro.comment_english,
        comment_opening_hours=legacy_gastro.comment_open,
        review_link=legacy_gastro.review_link,
        closed=legacy_gastro.closed,
        text_intern=legacy_gastro.text_intern,
        has_sticker=legacy_gastro.has_sticker,
        is_submission=legacy_gastro.is_submission,
        submit_email=legacy_gastro.submit_email,
        comment_public_transport=legacy_gastro.public_transport,
    )
    new_gastro.save()
    return new_gastro


old_tags_mapping = {
    "bar": "bar",
    "cafe": "cafe",
    "eiscafe": "ice cream parlor",
    "imbiss": "snack bar",
    "restaurant": "restaurant",
}


def get_tags(legacy_gastro: Gastro) -> List[Tag]:
    new_tags = []
    for old_tag in old_tags_mapping.keys():
        if getattr(legacy_gastro, old_tag):
            new_tags.append(Tag.objects.get_or_create(tag=old_tags_mapping[old_tag][0]))
    return new_tags


def get_boolean_attributes(legacy_gastro: Gastro) -> List[BooleanAttribute]:
    attr_list: List[BooleanAttribute] = []
    for attr in dict(GASTRO_BOOELAN_ATTRIBUTE_CHOICES):
        attr_list.append(
            BooleanAttribute.objects.get_or_create(
                name=attr, state=getattr(legacy_gastro, attr)
            )[0]
        )
    return attr_list


def get_positive_integer_attributes(
    legacy_gastro: Gastro,
) -> List[PositiveIntegerAttribute]:
    attr_list: List[PositiveIntegerAttribute] = []
    for attr in dict(GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES):
        attr_list.append(
            PositiveIntegerAttribute.objects.get_or_create(
                name=attr, state=getattr(legacy_gastro, attr)
            )[0]
        )
    return attr_list


def set_opening_hours(legacy_gastro: Gastro):
    OpeningHours.objects.update_or_create(
        location=legacy_gastro,
        weekday=WeekdayChoices.MONDAY,
        opening=legacy_gastro.opening_mon,
        closing=legacy_gastro.closing_mon,
    )
    OpeningHours.objects.update_or_create(
        location=legacy_gastro,
        weekday=WeekdayChoices.TUESDAY,
        opening=legacy_gastro.opening_tue,
        closing=legacy_gastro.closing_tue,
    )
    OpeningHours.objects.update_or_create(
        location=legacy_gastro,
        weekday=WeekdayChoices.WEDNESDAY,
        opening=legacy_gastro.opening_wed,
        closing=legacy_gastro.closing_wed,
    )
    OpeningHours.objects.update_or_create(
        location=legacy_gastro,
        weekday=WeekdayChoices.THURSDAY,
        opening=legacy_gastro.opening_thu,
        closing=legacy_gastro.closing_thu,
    )
    OpeningHours.objects.update_or_create(
        location=legacy_gastro,
        weekday=WeekdayChoices.FRIDAY,
        opening=legacy_gastro.opening_fri,
        closing=legacy_gastro.closing_fri,
    )
    OpeningHours.objects.update_or_create(
        location=legacy_gastro,
        weekday=WeekdayChoices.SATURDAY,
        opening=legacy_gastro.opening_sat,
        closing=legacy_gastro.closing_sat,
    )
    OpeningHours.objects.update_or_create(
        location=legacy_gastro,
        weekday=WeekdayChoices.SUNDAY,
        opening=legacy_gastro.opening_sun,
        closing=legacy_gastro.closing_sun,
    )


def build_new_gastro(legacy_gastro: Gastro):
    new_gastro: BaseLocation = create_new_baselocation(legacy_gastro=legacy_gastro)
    new_tags: List[Tag] = get_tags(legacy_gastro=legacy_gastro)
    new_gastro.tags.set(new_tags)
    new_boolean_attrs: List[BooleanAttribute] = get_boolean_attributes(
        legacy_gastro=legacy_gastro
    )
    new_gastro.boolean_attributes.set(new_boolean_attrs)
    new_positive_integer_attrs: List[
        PositiveIntegerAttribute
    ] = get_positive_integer_attributes(legacy_gastro=legacy_gastro)
    new_gastro.positive_integer_attributes.set(new_positive_integer_attrs)
    set_opening_hours(legacy_gastro=legacy_gastro)


def migrate_legacy_gastro(apps, schema_editor):
    LegacyGastro = apps.get_model("data", "Gastro")
    legacy_gastros = LegacyGastro.objects.all()
    for old_location in legacy_gastros:
        build_new_gastro(old_location)


class Migration(migrations.Migration):

    dependencies = [
        ("data", "0016_add_gastro_type_to_baselocation"),
    ]

    operations = [migrations.RunPython(reverse_code=migrations.RunPython.noop)]
