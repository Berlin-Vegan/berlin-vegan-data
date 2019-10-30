from factory import DjangoModelFactory, Faker

from bvdata.data.models import DISTRICT_CHOICES, BaseGastro, Gastro, GastroSubmit


def get_nullboolean() -> Faker:
    return Faker(
        "random_element",
        elements=[nullbool[0] for nullbool in Gastro.NULLBOOLEAN_CHOICE],
    )


class BaseGastroFactory(DjangoModelFactory):
    name = Faker("company")
    street = Faker("street_address")
    cityCode = Faker("postalcode")
    city = Faker("city")
    latCoord = Faker("latitude")
    longCoord = Faker("longitude")
    telephone = Faker("phone_number")
    website = Faker("url")
    email = Faker("email")

    openingMon = Faker("time")
    closingMon = Faker("time")
    openingTue = Faker("time")
    closingTue = Faker("time")
    openingWed = Faker("time")
    closingWed = Faker("time")
    openingThu = Faker("time")
    closingThu = Faker("time")
    openingFri = Faker("time")
    closingFri = Faker("time")
    openingSat = Faker("time")
    closingSat = Faker("time")
    openingSun = Faker("time")
    closingSun = Faker("time")

    vegan = Faker(
        "random_element",
        elements=[declaration[0] for declaration in Gastro.VEGAN_CHOICE],
    )
    comment = Faker("texts", nb_texts=3, max_nb_chars=400, ext_word_list=None)
    commentEnglish = Faker("texts", nb_texts=3, max_nb_chars=400, ext_word_list=None)
    review_link = Faker("url")
    closed = Faker("date")
    text_intern = Faker("texts", nb_texts=3, max_nb_chars=400, ext_word_list=None)

    district = Faker(
        "random_element", elements=[district[0] for district in DISTRICT_CHOICES]
    )
    publicTransport = Faker("pystr", max_chars=255)
    handicappedAccessible = get_nullboolean()
    handicappedAccessibleWc = get_nullboolean()
    dog = get_nullboolean()
    childChair = get_nullboolean()
    catering = get_nullboolean()
    delivery = get_nullboolean()
    organic = get_nullboolean()
    wlan = get_nullboolean()
    glutenFree = get_nullboolean()
    breakfast = get_nullboolean()
    brunch = get_nullboolean()
    seatsOutdoor = Faker("random_int")
    seatsIndoor = Faker("random_int")
    restaurant = Faker("boolean")
    imbiss = Faker("boolean")
    eiscafe = Faker("boolean")
    cafe = Faker("boolean")
    bar = Faker("boolean")
    commentOpen = Faker("texts", nb_texts=3, max_nb_chars=400, ext_word_list=None)
    submit_email = Faker("email")

    class Meta:
        model = BaseGastro


class GastroFactory(BaseGastroFactory):
    has_sticker = Faker("boolean")

    class Meta:
        model = Gastro


class GastroSubmitFactory(BaseGastroFactory):
    class Meta:
        model = GastroSubmit
