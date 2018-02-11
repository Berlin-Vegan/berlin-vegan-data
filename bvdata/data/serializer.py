from rest_framework import serializers

from bvdata.data.models import Gastro


class GastroSerializer(serializers.ModelSerializer):
    district = serializers.SerializerMethodField()
    vegan = serializers.SerializerMethodField()
    handicappedAccessible = serializers.SerializerMethodField()
    handicappedAccessibleWc = serializers.SerializerMethodField()
    dog = serializers.SerializerMethodField()
    childChair = serializers.SerializerMethodField()
    catering = serializers.SerializerMethodField()
    delivery = serializers.SerializerMethodField()
    organic = serializers.SerializerMethodField()
    wlan = serializers.SerializerMethodField()
    glutenFree = serializers.SerializerMethodField()
    breakfast = serializers.SerializerMethodField()
    brunch = serializers.SerializerMethodField()

    openingMon = serializers.DateTimeField(format='%H:%M')
    closingMon = serializers.DateTimeField(format='%H:%M')
    openingTue = serializers.DateTimeField(format='%H:%M')
    closingTue = serializers.DateTimeField(format='%H:%M')
    openingWed = serializers.DateTimeField(format='%H:%M')
    closingWed = serializers.DateTimeField(format='%H:%M')
    openingThu = serializers.DateTimeField(format='%H:%M')
    closingThu = serializers.DateTimeField(format='%H:%M')
    openingFri = serializers.DateTimeField(format='%H:%M')
    closingFri = serializers.DateTimeField(format='%H:%M')
    openingSat = serializers.DateTimeField(format='%H:%M')
    closingSat = serializers.DateTimeField(format='%H:%M')
    openingSun = serializers.DateTimeField(format='%H:%M')
    closingSun = serializers.DateTimeField(format='%H:%M')

    class Meta:
        model = Gastro
        read_only_fields = [
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
            'closed',
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
            'bar',
        ]
        fields = read_only_fields

    def get_district(self, obj):
        return obj.get_district_display()

    def get_vegan(self, obj):
        return obj.get_vegan_display()

    def get_handicappedAccessible(self, obj):
        return obj.get_handicappedAccessible_display()

    def get_handicappedAccessibleWc(self, obj):
        return obj.get_handicappedAccessibleWc_display()

    def get_dog(self, obj):
        return obj.get_dog_display()

    def get_childChair(self, obj):
        return obj.get_childChair_display()

    def get_catering(self, obj):
        return obj.get_catering_display()

    def get_delivery(self, obj):
        return obj.get_delivery_display()

    def get_organic(self, obj):
        return obj.get_organic_display()

    def get_wlan(self, obj):
        return obj.get_wlan_display()

    def get_glutenFree(self, obj):
        return obj.get_glutenFree_display()

    def get_breakfast(self, obj):
        return obj.get_breakfast_display()

    def get_brunch(self, obj):
        return obj.get_brunch_display()
