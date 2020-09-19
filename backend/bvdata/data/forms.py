from django.forms import HiddenInput, ModelForm, NumberInput
from django.utils.translation import gettext_lazy as _

from bvdata.data.models import Gastro


class GastroSubmitForm(ModelForm):
    class Meta:
        model = Gastro
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
            "vegan",
            "comment",
            "comment_english",
            "comment_open",
            "review_link",
            "text_intern",
            "district",
            "public_transport",
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
