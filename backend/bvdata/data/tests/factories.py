from factory import Faker, SubFactory, post_generation
from factory.django import DjangoModelFactory

from bvdata.data.models import (
    NULLBOOLEAN_CHOICE,
    SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES,
    TAG_CHOICES,
    VEGAN_CHOICE,
    BaseLocation,
    BooleanAttribute,
    LocationTypeChoices,
    OpeningHours,
    PositiveIntegerAttribute,
    Review,
    ReviewImage,
    Tag,
    WeekdayChoices,
)

__all__ = (
    "BaseLocationFactory",
    "BooleanAttributesFactory",
    "OpeningHoursFactory",
    "ReviewFactory",
    "ReviewImageFactory",
    "TagFactory",
)


def get_nullboolean() -> Faker:
    return Faker(
        "random_element", elements=[nullbool[0] for nullbool in NULLBOOLEAN_CHOICE]
    )


class TagFactory(DjangoModelFactory):
    tag = Faker("random_element", elements=[tag[0] for tag in TAG_CHOICES])

    class Meta:
        model = Tag


class BooleanAttributesFactory(DjangoModelFactory):
    name = Faker(
        "random_element",
        elements=[attribute[0] for attribute in SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES],
    )
    state = get_nullboolean()

    class Meta:
        model = BooleanAttribute


class PositiveIntegerAttributesFactory(DjangoModelFactory):
    name = Faker(
        "random_element",
        elements=[attribute[0] for attribute in SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES],
    )
    state = get_nullboolean()

    class Meta:
        model = PositiveIntegerAttribute


class ReviewFactory(DjangoModelFactory):
    url = Faker("url")
    text = Faker("text", max_nb_chars=400)
    updated = Faker("date_time")

    class Meta:
        model = Review


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
    closed = Faker("date_object")
    text_intern = Faker("text", max_nb_chars=400, ext_word_list=None)
    is_submission = Faker("boolean")
    submit_email = Faker("email")

    review = SubFactory(ReviewFactory)

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
            for attr in extracted:
                self.boolean_attributes.add(attr)

    @post_generation
    def positive_integer_attributes(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for attr in extracted:
                self.positive_integer_attributes.add(attr)

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


class ReviewImageFactory(DjangoModelFactory):
    review = SubFactory(ReviewFactory)
    height = Faker("pyint")
    width = Faker("pyint")
    url = Faker("url")

    class Meta:
        model = ReviewImage
