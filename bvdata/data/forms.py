from django.forms import ModelForm

from .models import *


class GastroForm(ModelForm):
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
            self.fields[o].label = 'opens'

        # change label closing
        for c in close:
            self.fields[c].label = 'closes'

        # add timepicker and format hh:mm
        timepicker = open + close
        for t in timepicker:
            self.fields[t].widget.attrs.update({'data-picker': 'timepicker'})
            self.fields[t].widget.format = '%H:%M'

