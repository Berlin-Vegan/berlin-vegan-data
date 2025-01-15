from datetime import time
from typing import Dict, List, Optional

from django.db.models import QuerySet
from django.http import HttpRequest

from bvdata.data.models import (
    BaseLocation,
    BooleanAttribute,
    OpeningHours,
    PositiveIntegerAttribute,
    WeekdayChoices,
)

BASE_DATA_FIELD_NAME_TO_FIELD_NAME: Dict[str, str] = {
    "telephone": "telephone",
    "website": "website",
    "email": "email",
    "comment": "comment",
    "comment_english": "commentEnglish",
    "comment_opening_hours": "openComment",
}

GASTRO_DATA_FIELD_NAME_TO_FIELD_NAME: Dict[str, str] = {
    **BASE_DATA_FIELD_NAME_TO_FIELD_NAME,
    "comment_public_transport": "publicTransport",
}

BOOLEAN_ATTRIBUTES_TO_FIELD_NAME: Dict[str, str] = {
    "organic": "organic",
    "handicapped_accessible": "handicappedAccessible",
    "delivery": "delivery",
    "handicapped_accessible_wc": "handicappedAccessibleWc",
    "dog": "dog",
    "child_chair": "childChair",
    "catering": "catering",
    "wlan": "wlan",
    "gluten_free": "glutenFree",
    "breakfast": "breakfast",
    "brunch": "brunch",
}


GASTRO_POSITIVE_INTEGER_ATTRIBUTES_TO_FIELD_NAME: Dict[str, str] = {
    "seats_outdoor": "seatsOutdoor",
    "seats_indoor": "seatsIndoor",
}


OPENING_HOUR_FIELD_NAME: Dict[str, str] = {
    WeekdayChoices.MONDAY: "otMon",
    WeekdayChoices.TUESDAY: "otTue",
    WeekdayChoices.WEDNESDAY: "otWed",
    WeekdayChoices.THURSDAY: "otThu",
    WeekdayChoices.FRIDAY: "otFri",
    WeekdayChoices.SATURDAY: "otSat",
    WeekdayChoices.SUNDAY: "otSun",
}


TAG_FIELD_NAME_TO_FIELD_NAME: Dict[str, str] = {
    "restaurant": "Restaurant",
    "bar": "Bar",
    "snack bar": "Imbiss",
    "cafe": "Cafe",
    "ice cream parlor": "Eiscafe",
    "foods": "foods",
    "clothing": "clothing",
    "toiletries": "toiletries",
    "supermarket": "supermarket",
    "hairdressers": "hairdressers",
    "sports": "sports",
    "tattoostudio": "tattoostudio",
    "accommodation": "accommodation",
}


def _build_boolean_attribute(value: Optional[bool]) -> int:
    if value is None:
        return -1
    elif value is True:
        return 1
    elif value is False:
        return 0


def time_to_str(time_obj: time) -> str:
    if time_obj:
        return time_obj.strftime("%H:%M")
    else:
        return ""


def _build_opening_hour_str(opening_hour: OpeningHours) -> str:
    opening_str = time_to_str(opening_hour.opening)
    closing_str = time_to_str(opening_hour.closing)
    return f"""{opening_str} - {closing_str}"""


def _add_not_none_empty(location_dict, data, json_field_name) -> None:
    if data is not None and data != "":
        location_dict.update({json_field_name: data})


def _build_opening_hours(closed, opening_hours: List[OpeningHours]) -> dict:
    if closed is not None:
        return {
            OPENING_HOUR_FIELD_NAME[weekday[0]]: ""
            for weekday in WeekdayChoices.choices
        }
    return {
        OPENING_HOUR_FIELD_NAME[opening_hour.weekday]: _build_opening_hour_str(
            opening_hour=opening_hour
        )
        for opening_hour in opening_hours
        if opening_hour.opening is not None
    }


def _build_base(location: BaseLocation, data_to_field_name: dict) -> dict:
    name = (
        location.name
        if location.closed is None
        else f"{location.name} - GESCHLOSSEN / CLOSED"
    )
    base_dict = dict(
        id=location.id_string,
        name=name,
        street=location.street,
        cityCode=location.postal_code,
        city=location.city,
        latCoord=location.latitude,
        longCoord=location.longitude,
        vegan=location.vegan,
        tags=[TAG_FIELD_NAME_TO_FIELD_NAME[tag.tag] for tag in location.tags.all()],
    )

    for data_field_name, json_field_name in data_to_field_name.items():
        _add_not_none_empty(
            location_dict=base_dict,
            data=getattr(location, data_field_name),
            json_field_name=json_field_name,
        )
    if location.closed:
        base_dict.pop("telephone", None)

    if location.review:
        base_dict.update(reviewURL=location.review.url.split("/")[-2])
        base_dict.update(review=location.review.text)

    base_dict.update(
        _build_opening_hours(
            closed=location.closed, opening_hours=location.openinghours_set.all()
        )
    )

    return base_dict


def _build_boolean_attributes(boolean_attrs: QuerySet[BooleanAttribute]) -> dict:
    return {
        BOOLEAN_ATTRIBUTES_TO_FIELD_NAME[attr.name]: _build_boolean_attribute(
            attr.state
        )
        for attr in boolean_attrs
        if attr.name in BOOLEAN_ATTRIBUTES_TO_FIELD_NAME
    }


def _build_positive_int_attributes(
    positive_int_attrs: List[PositiveIntegerAttribute],
) -> dict:
    return {
        GASTRO_POSITIVE_INTEGER_ATTRIBUTES_TO_FIELD_NAME[attr.name]: attr.state
        for attr in positive_int_attrs
    }


def _build_images(location: BaseLocation, request: HttpRequest) -> List[dict]:
    images_list = [
        dict(
            url=request.build_absolute_uri(image.image.url),
            width=image.width,
            height=image.height,
        )
        for image in location.image_set.all()
    ]
    if location.review:
        images_list = images_list + [
            dict(url=image.url, width=image.width, height=image.height)
            for image in location.review.reviewimage_set.all()
        ]
    return images_list


def build_gastro(location: BaseLocation, request: HttpRequest) -> dict:
    gastro_dict = _build_base(
        location=location, data_to_field_name=GASTRO_DATA_FIELD_NAME_TO_FIELD_NAME
    )
    gastro_dict.update(district="Berlin", created=location.created.strftime("%Y-%m-%d"))
    gastro_dict.update(_build_boolean_attributes(location.boolean_attributes.all()))
    gastro_dict.update(
        _build_positive_int_attributes(location.positive_integer_attributes.all())
    )
    gastro_dict.update(pictures=_build_images(location, request))
    return gastro_dict


def build_shopping(location: BaseLocation, request: HttpRequest) -> dict:
    shopping_dict = _build_base(
        location=location, data_to_field_name=BASE_DATA_FIELD_NAME_TO_FIELD_NAME
    )
    shopping_dict.update(_build_boolean_attributes(location.boolean_attributes.all()))
    shopping_dict.update(pictures=_build_images(location, request))
    return shopping_dict
