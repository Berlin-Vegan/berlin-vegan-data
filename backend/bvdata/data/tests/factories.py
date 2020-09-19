from factory import DjangoModelFactory, Faker

from bvdata.data.models import DISTRICT_CHOICES, BaseGastro, Gastro


def get_nullboolean() -> Faker:
    return Faker(
        "random_element",
        elements=[nullbool[0] for nullbool in Gastro.NULLBOOLEAN_CHOICE],
    )


class BaseGastroFactory(DjangoModelFactory):
    name = Faker("company")
    street = Faker("street_address")
    postal_code = Faker("postalcode")
    city = Faker("city")
    latitude = Faker("latitude")
    longitude = Faker("longitude")
    telephone = Faker("phone_number")
    website = Faker("url")
    email = Faker("email")

    opening_mon = Faker("time")
    closing_mon = Faker("time")
    opening_tue = Faker("time")
    closing_tue = Faker("time")
    opening_wed = Faker("time")
    closing_wed = Faker("time")
    opening_thu = Faker("time")
    closing_thu = Faker("time")
    opening_fri = Faker("time")
    closing_fri = Faker("time")
    opening_sat = Faker("time")
    closing_sat = Faker("time")
    opening_sun = Faker("time")
    closing_sun = Faker("time")

    vegan = Faker(
        "random_element",
        elements=[declaration[0] for declaration in Gastro.VEGAN_CHOICE],
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

    class Meta:
        model = BaseGastro


class GastroFactory(BaseGastroFactory):
    has_sticker = Faker("boolean")
    is_submission = Faker("boolean")

    class Meta:
        model = Gastro
