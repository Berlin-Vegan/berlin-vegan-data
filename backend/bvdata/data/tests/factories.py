from factory import Faker, SubFactory, post_generation
from factory.django import DjangoModelFactory

from bvdata.data.models import (
    DISTRICT_CHOICES,
    NULLBOOLEAN_CHOICE,
    SHOPPING_BOOELAN_ATTRIBUTE_CHOICES,
    TAG_CHOICES,
    VEGAN_CHOICE,
    BaseLocation,
    BooleanAttribute,
    Gastro,
    LocationTypeChoices,
    OpeningHours,
    Tag,
    WeekdayChoices,
)

__all__ = (
    "GastroFactory",
    "TagFactory",
    "BooleanAttributesFactory",
    "BaseLocationFactory",
    "OpeningHoursFactory",
)


def get_nullboolean() -> Faker:
    return Faker(
        "random_element", elements=[nullbool[0] for nullbool in NULLBOOLEAN_CHOICE]
    )


class GastroFactory(DjangoModelFactory):
    name = Faker("company")
    street = Faker("street_address")
    postal_code = Faker("postalcode")
    city = Faker("text", max_nb_chars=20)
    latitude = Faker("latitude")
    longitude = Faker("longitude")
    telephone = Faker("phone_number")
    website = Faker("url")
    email = Faker("email")

    opening_mon = Faker("time_object")
    closing_mon = Faker("time_object")
    opening_tue = Faker("time_object")
    closing_tue = Faker("time_object")
    opening_wed = Faker("time_object")
    closing_wed = Faker("time_object")
    opening_thu = Faker("time_object")
    closing_thu = Faker("time_object")
    opening_fri = Faker("time_object")
    closing_fri = Faker("time_object")
    opening_sat = Faker("time_object")
    closing_sat = Faker("time_object")
    opening_sun = Faker("time_object")
    closing_sun = Faker("time_object")

    vegan = Faker(
        "random_element", elements=[declaration[0] for declaration in VEGAN_CHOICE]
    )
    comment = Faker("texts", nb_texts=3, max_nb_chars=400, ext_word_list=None)
    comment_english = Faker("texts", nb_texts=3, max_nb_chars=400, ext_word_list=None)
    review_link = Faker("url")
    closed = Faker("date")
    text_intern = Faker("texts", nb_texts=3, max_nb_chars=400, ext_word_list=None)

    district = Faker(
        "random_element", elements=[district[0] for district in DISTRICT_CHOICES]
    )
    public_transport = Faker("pystr", max_chars=255)
    handicapped_accessible = get_nullboolean()
    handicapped_accessible_wc = get_nullboolean()
    dog = get_nullboolean()
    child_chair = get_nullboolean()
    catering = get_nullboolean()
    delivery = get_nullboolean()
    organic = get_nullboolean()
    wlan = get_nullboolean()
    gluten_free = get_nullboolean()
    breakfast = get_nullboolean()
    brunch = get_nullboolean()
    seats_outdoor = Faker("random_int")
    seats_indoor = Faker("random_int")
    restaurant = Faker("boolean")
    imbiss = Faker("boolean")
    eiscafe = Faker("boolean")
    cafe = Faker("boolean")
    bar = Faker("boolean")
    comment_open = Faker("texts", nb_texts=3, max_nb_chars=400, ext_word_list=None)
    submit_email = Faker("email")
    has_sticker = Faker("boolean")
    is_submission = Faker("boolean")

    class Meta:
        model = Gastro


class TagFactory(DjangoModelFactory):
    tag = Faker("random_element", elements=[tag[0] for tag in TAG_CHOICES])

    class Meta:
        model = Tag


class BooleanAttributesFactory(DjangoModelFactory):
    name = Faker(
        "random_element",
        elements=[attribute[0] for attribute in SHOPPING_BOOELAN_ATTRIBUTE_CHOICES],
    )
    state = get_nullboolean()

    class Meta:
        model = BooleanAttribute


class BaseLocationFactory(DjangoModelFactory):
    type = Faker(
        "random_element", elements=[type[0] for type in LocationTypeChoices.choices]
    )
    last_editor = None
    name = Faker("company")
    street = Faker("street_address")
    postal_code = Faker("postalcode")
    city = Faker("text", max_nb_chars=20)
    latitude = Faker("pyfloat")
    longitude = Faker("pyfloat")
    telephone = Faker("phone_number")
    website = Faker("url")
    email = Faker("email")
    vegan = Faker(
        "random_element", elements=[declaration[0] for declaration in VEGAN_CHOICE]
    )
    comment = Faker("text", max_nb_chars=400)
    comment_english = Faker("text", max_nb_chars=400)
    comment_opening_hours = Faker("text", max_nb_chars=400)
    review_link = Faker("url")
    closed = Faker("date_object")
    text_intern = Faker("text", max_nb_chars=400, ext_word_list=None)
    is_submission = Faker("boolean")

    @post_generation
    def tags(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for tag in extracted:
                self.tags.add(tag)

    @post_generation
    def boolean_attributes(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for boolean_attribute in extracted:
                self.boolean_attributes.add(boolean_attribute)

    class Meta:
        model = BaseLocation


class OpeningHoursFactory(DjangoModelFactory):
    location = SubFactory(BaseLocationFactory)
    weekday = Faker(
        "random_element", elements=[weekday[0] for weekday in WeekdayChoices.choices]
    )
    opening = Faker("time_object")
    closing = Faker("time_object")

    class Meta:
        model = OpeningHours
