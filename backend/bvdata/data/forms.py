from typing import Dict, List, Type, Union

from django.db import transaction
from django.forms import (
    BooleanField,
    HiddenInput,
    IntegerField,
    ModelForm,
    NullBooleanField,
    NumberInput,
    Select,
    TimeField,
)
from django.utils.translation import gettext_lazy as _

from bvdata.data.models import (
    GASTRO_BOOLEAN_ATTRIBUTE_CHOICES,
    GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES,
    NULLBOOLEAN_CHOICE,
    NULLBOOLEAN_NULL,
    VEGAN_VEGAN,
    BaseLocation,
    BooleanAttribute,
    LocationTypeChoices,
    OpeningHours,
    PositiveIntegerAttribute,
    Tag,
    WeekdayChoices,
)


class GastroSubmitForm(ModelForm):
    opening_mon = TimeField(required=False)
    opening_tue = TimeField(required=False)
    opening_wed = TimeField(required=False)
    opening_thu = TimeField(required=False)
    opening_fri = TimeField(required=False)
    opening_sat = TimeField(required=False)
    opening_sun = TimeField(required=False)
    closing_mon = TimeField(required=False)
    closing_tue = TimeField(required=False)
    closing_wed = TimeField(required=False)
    closing_thu = TimeField(required=False)
    closing_fri = TimeField(required=False)
    closing_sat = TimeField(required=False)
    closing_sun = TimeField(required=False)

    delivery = NullBooleanField(
        label=_("Delivery"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    organic = NullBooleanField(
        label=_("Organic"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    handicapped_accessible = NullBooleanField(
        label=_("Handicapped Accessible"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    handicapped_accessible_wc = NullBooleanField(
        label=_("Handicapped Accessible WC"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    dog = NullBooleanField(
        label=_("Dogs"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    child_chair = NullBooleanField(
        label=_("Child Chair"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    catering = NullBooleanField(
        label=_("Catering"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    wlan = NullBooleanField(
        label=_("Wifi"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    gluten_free = NullBooleanField(
        label=_("Gluten Free"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    breakfast = NullBooleanField(
        label=_("Vegan Breakfast"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )
    brunch = NullBooleanField(
        label=_("Brunch"),
        widget=Select(choices=NULLBOOLEAN_CHOICE),
        initial=NULLBOOLEAN_NULL,
        required=False,
    )

    restaurant = BooleanField(label=_("Restaurant"), initial=False, required=False)
    imbiss = BooleanField(label=_("Snack Bar"), initial=False, required=False)
    eiscafe = BooleanField(label=_("Ice Cream Parlor"), initial=False, required=False)
    cafe = BooleanField(label=_("Coffee Shop"), initial=False, required=False)
    bar = BooleanField(label=_("Bar"), initial=False, required=False)

    seats_indoor = IntegerField(label=_("Seats Indoor"), min_value=0, initial=0)
    seats_outdoor = IntegerField(label=_("Seats Outdoor"), min_value=0, initial=0)

    class Meta:
        model = BaseLocation
        fields = [
            "name",
            "street",
            "postal_code",
            "city",
            "latitude",
            "longitude",
            "telephone",
            "website",
            "email",
            "opening_mon",
            "closing_mon",
            "opening_tue",
            "closing_tue",
            "opening_wed",
            "closing_wed",
            "opening_thu",
            "closing_thu",
            "opening_fri",
            "closing_fri",
            "opening_sat",
            "closing_sat",
            "opening_sun",
            "closing_sun",
            "comment",
            "comment_english",
            "comment_opening_hours",
            "comment_public_transport",
            "handicapped_accessible",
            "handicapped_accessible_wc",
            "dog",
            "child_chair",
            "catering",
            "delivery",
            "organic",
            "wlan",
            "gluten_free",
            "breakfast",
            "brunch",
            "seats_outdoor",
            "seats_indoor",
            "restaurant",
            "imbiss",
            "eiscafe",
            "cafe",
            "bar",
            "submit_email",
        ]

    def __init__(self, *args, **kwargs):
        super(GastroSubmitForm, self).__init__(*args, **kwargs)
        self.fields["latitude"].widget = HiddenInput()
        self.fields["longitude"].widget = HiddenInput()
        self.fields["city"].widget.attrs["readonly"] = True
        self.fields["postal_code"].widget = NumberInput(attrs={"maxlength": 5})

        open = [
            "opening_mon",
            "opening_tue",
            "opening_wed",
            "opening_thu",
            "opening_fri",
            "opening_sat",
            "opening_sun",
        ]

        close = [
            "closing_mon",
            "closing_tue",
            "closing_wed",
            "closing_thu",
            "closing_fri",
            "closing_sat",
            "closing_sun",
        ]

        # change label opening
        for o in open:
            self.fields[o].label = _("Opens at")
            self.fields[o].widget.attrs.update({"data-picker": "timepicker-opens"})

        # change label closing
        for c in close:
            self.fields[c].label = _("Closes at")
            self.fields[c].widget.attrs.update({"data-picker": "timepicker-closes"})

        # add timepicker and format hh:mm
        timepicker = open + close
        for t in timepicker:
            self.fields[t].widget.attrs.update({"placeholder": "HH:MM"})
            self.fields[t].widget.format = "%H:%M"

    def save(self, commit=True):
        self.instance.type = LocationTypeChoices.GASTRO
        self.instance.vegan = VEGAN_VEGAN
        with transaction.atomic():
            instance = super(GastroSubmitForm, self).save(commit=True)
            self._save_opening_hours(instance=instance)
            self._save_tags(instance=instance)
            self._save_attrs(
                instance=instance,
                attr_keys=dict(GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES),
                attr_model=PositiveIntegerAttribute,
                attr_manager="positive_integer_attributes",
            )
            self._save_attrs(
                instance=instance,
                attr_keys=dict(GASTRO_BOOLEAN_ATTRIBUTE_CHOICES),
                attr_model=BooleanAttribute,
                attr_manager="boolean_attributes",
            )
        return instance

    def _save_opening_hours(self, instance: BaseLocation):
        OPENING_HOURS_PAIRS = {
            WeekdayChoices.MONDAY: ("opening_mon", "closing_mon"),
            WeekdayChoices.TUESDAY: ("opening_tue", "closing_tue"),
            WeekdayChoices.WEDNESDAY: ("opening_wed", "closing_wed"),
            WeekdayChoices.THURSDAY: ("opening_thu", "closing_thu"),
            WeekdayChoices.FRIDAY: ("opening_fri", "closing_fri"),
            WeekdayChoices.SATURDAY: ("opening_sat", "closing_sat"),
            WeekdayChoices.SUNDAY: ("opening_sun", "closing_sun"),
        }

        opening_hours = []
        for day, day_keys in OPENING_HOURS_PAIRS.items():
            opening_hours.append(
                OpeningHours(
                    location=instance,
                    weekday=day,
                    opening=self.cleaned_data[day_keys[0]],
                    closing=self.cleaned_data[day_keys[1]],
                )
            )
        OpeningHours.objects.bulk_create(opening_hours)

    def _save_tags(self, instance: BaseLocation):
        TAGS_SET = {
            "restaurant": "restaurant",
            "imbiss": "snack bar",
            "eiscafe": "ice cream parlor",
            "cafe": "cafe",
            "bar": "bar",
        }
        tags: List[Tag] = []
        for form_field, tag_name in TAGS_SET.items():
            tag = self.cleaned_data[form_field]
            if tag:
                tags.append(Tag.objects.get_or_create(tag=tag_name)[0])
        instance.tags.set(tags)

    def _save_attrs(
        self,
        instance: BaseLocation,
        attr_keys: Dict[str, str],
        attr_model: Type[Union[PositiveIntegerAttribute, BooleanAttribute]],
        attr_manager: str,
    ):
        attrs: List[attr_model] = []
        for attr_key in attr_keys:
            attr_value = self.cleaned_data[attr_key]
            attrs.append(
                attr_model.objects.get_or_create(name=attr_key, state=attr_value)[0]
            )
        getattr(instance, attr_manager).set(attrs)
