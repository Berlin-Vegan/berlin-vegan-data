from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.forms import BooleanField, HiddenInput, ModelForm, NumberInput
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from bvdata.data.models import Gastro, GastroSubmit


class DataAuthForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(DataAuthForm, self).__init__(*args, **kwargs)
        self.fields["username"].widget.attrs = {
            "class": "form-control",
            "placeholder": _("username"),
            "autofocus": "",
        }
        self.fields["password"].widget.attrs = {
            "class": "form-control",
            "placeholder": _("password"),
        }


class TimeDateAsBooleanField(BooleanField):
    def clean(self, value):
        value = super(TimeDateAsBooleanField, self).clean(value)
        if value:
            return timezone.now()
        else:
            return None


class BaseGastroForm(ModelForm):
    closed = TimeDateAsBooleanField(required=False)

    class Meta:
        model = Gastro
        fields = [
            "name",
            "street",
            "cityCode",
            "city",
            "latCoord",
            "longCoord",
            "telephone",
            "website",
            "email",
            "openingMon",
            "closingMon",
            "openingTue",
            "closingTue",
            "openingWed",
            "closingWed",
            "openingThu",
            "closingThu",
            "openingFri",
            "closingFri",
            "openingSat",
            "closingSat",
            "openingSun",
            "closingSun",
            "vegan",
            "comment",
            "commentEnglish",
            "commentOpen",
            "review_link",
            "closed",
            "text_intern",
            "district",
            "publicTransport",
            "handicappedAccessible",
            "handicappedAccessibleWc",
            "dog",
            "childChair",
            "catering",
            "delivery",
            "organic",
            "wlan",
            "glutenFree",
            "breakfast",
            "brunch",
            "seatsOutdoor",
            "seatsIndoor",
            "restaurant",
            "imbiss",
            "eiscafe",
            "cafe",
            "bar",
            "submit_email",
        ]

    def __init__(self, *args, **kwargs):
        super(BaseGastroForm, self).__init__(*args, **kwargs)

        open = [
            "openingMon",
            "openingTue",
            "openingWed",
            "openingThu",
            "openingFri",
            "openingSat",
            "openingSun",
        ]

        close = [
            "closingMon",
            "closingTue",
            "closingWed",
            "closingThu",
            "closingFri",
            "closingSat",
            "closingSun",
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

        self.fields["cityCode"].widget = NumberInput(attrs={"maxlength": 5})


class GastroForm(BaseGastroForm):
    class Meta(BaseGastroForm.Meta):
        fields = BaseGastroForm.Meta.fields + ["has_sticker"]


class GastroSubmitBaseForm(BaseGastroForm):
    class Meta(BaseGastroForm.Meta):
        model = GastroSubmit


class GastroSubmitForm(GastroSubmitBaseForm):
    class Meta(GastroSubmitBaseForm.Meta):
        model = GastroSubmit

    def __init__(self, *args, **kwargs):
        super(GastroSubmitForm, self).__init__(*args, **kwargs)

        self.fields["latCoord"].widget = HiddenInput()
        self.fields["longCoord"].widget = HiddenInput()
        self.fields["city"].widget.attrs["readonly"] = True
        self.fields["cityCode"].widget = NumberInput(attrs={"maxlength": 5})


class GastroSubmitEditForm(GastroSubmitBaseForm):
    class Meta(GastroSubmitBaseForm.Meta):
        model = GastroSubmit
        fields = GastroSubmitBaseForm.Meta.fields

    def __init__(self, *args, **kwargs):
        super(GastroSubmitEditForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].label = ""


class UserProfileChangeEmailForm(ModelForm):
    class Meta:
        model = User
        fields = ["email"]
