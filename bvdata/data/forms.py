from django.forms import ModelForm, BooleanField
from django.utils import timezone
from django.utils.translation import gettext as _

from .models import *


class TimeDateAsBooleanField(BooleanField):
    def clean(self, value):
        value = super(TimeDateAsBooleanField, self).clean(value)
        if value:
            return timezone.now()
        else:
            return None


class GastroForm(ModelForm):
    closed = TimeDateAsBooleanField(required=False)

    class Meta:
        model = Gastro
        fields = [
            'name',
            'street',
            'cityCode',
            'city',
            'latCoord',
            'longCoord',
            'telephone',
            'website',
            'email',
            'openingMon',
            'closingMon',
            'openingTue',
            'closingTue',
            'openingWed',
            'closingWed',
            'openingThu',
            'closingThu',
            'openingFri',
            'closingFri',
            'openingSat',
            'closingSat',
            'openingSun',
            'closingSun',
            'vegan',
            'comment',
            'commentEnglish',
            'commentOpen',
            'review_link',
            'closed',
            'text_intern',
            'district',
            'publicTransport',
            'handicappedAccessible',
            'handicappedAccessibleWc',
            'dog',
            'childChair',
            'catering',
            'delivery',
            'organic',
            'wlan',
            'glutenFree',
            'breakfast',
            'brunch',
            'seatsOutdoor',
            'seatsIndoor',
            'restaurant',
            'imbiss',
            'eiscafe',
            'cafe',
            'bar'
        ]
    
    def __init__(self, *args, **kwargs):
        super(GastroForm, self).__init__(*args, **kwargs)

        open = [
            'openingMon',
            'openingTue',
            'openingWed',
            'openingThu',
            'openingFri',
            'openingSat',
            'openingSun'
        ]

        close = [
            'closingMon',
            'closingTue',
            'closingWed',
            'closingThu',
            'closingFri',
            'closingSat',
            'closingSun'
        ]

        # change label opening
        for o in open:
            self.fields[o].label = _('opens')

        # change label closing
        for c in close:
            self.fields[c].label = _('closes')

        # add timepicker and format hh:mm
        timepicker = open + close
        for t in timepicker:
            self.fields[t].widget.attrs.update({'data-picker': 'timepicker'})
            self.fields[t].widget.attrs.update({'placeholder': 'HH:MM'})
            self.fields[t].widget.format = '%H:%M'
