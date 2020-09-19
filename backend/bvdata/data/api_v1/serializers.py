from django.contrib.auth import get_user_model
from rest_framework.fields import BooleanField, ChoiceField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from bvdata.data.models import DISTRICT_CHOICES, Gastro


class GastroBaseSerializer(ModelSerializer):
    class Meta:
        model = Gastro
        fields = ["id_string", "name", "street", "postal_code", "city", "vegan"]


class GastroListSerializer(GastroBaseSerializer):
    has_review_link = BooleanField()

    class Meta(GastroBaseSerializer.Meta):
        fields = GastroBaseSerializer.Meta.fields + ["has_review_link"]


class GastroDetailSerializer(GastroBaseSerializer):
    last_editor = SerializerMethodField()
    district = ChoiceField(choices=DISTRICT_CHOICES)

    def get_last_editor(self, obj):
        return (
            obj.last_editor.username if hasattr(obj.last_editor, "username") else None
        )

    class Meta(GastroBaseSerializer.Meta):
        fields = [
            "id_string",
            "created",
            "updated",
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
            "review_link",
            "closed",
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
            "comment_open",
            "submit_email",
            "last_editor",
            "has_sticker",
            "is_submission",
        ] + GastroBaseSerializer.Meta.fields
        read_only_fields = ["id_string", "last_editor"]


class AccountProfileModelSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]
        read_only_fields = ["id", "username"]
