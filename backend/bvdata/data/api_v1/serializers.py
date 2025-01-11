from django.contrib.auth import get_user_model
from rest_framework.fields import CharField, SerializerMethodField
from rest_framework.serializers import ModelSerializer

from bvdata.data.models import BaseLocation, Image, Review, ReviewImage


class AccountProfileModelSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]
        read_only_fields = ["id", "username"]


class RemoteImagesSerializer(ModelSerializer):
    class Meta:
        model = ReviewImage
        fields = ["height", "width", "url"]
        read_only_fields = fields


class ReviewSerializer(ModelSerializer):
    images = RemoteImagesSerializer(source="reviewimage_set", many=True)

    class Meta:
        model = Review
        fields = ["id", "text", "images", "url"]
        read_only_fields = fields


class LocationIdStringField(CharField):
    def to_representation(self, value):
        return value.id_string


class ImageSerializerBase(ModelSerializer):
    location = LocationIdStringField()
    uploader = SerializerMethodField()

    class Meta:
        model = Image
        fields = [
            "id",
            "location",
            "image",
            "height",
            "width",
            "upload_date",
            "uploader",
            "description",
        ]
        read_only_fields = ["id", "height", "width", "upload_date", "uploader"]

    @staticmethod
    def get_uploader(obj):
        return obj.uploader.username if hasattr(obj.uploader, "username") else None


class ImageSerializerDefault(ImageSerializerBase):
    class Meta(ImageSerializerBase.Meta):
        pass

    def create(self, validated_data):
        validated_data["location"] = BaseLocation.objects.get(
            id_string=validated_data.get("location")
        )
        if (
            validated_data.get("description") == ""
            or validated_data.get("description") is None
        ):
            validated_data["description"] = validated_data.get("image").name
        return super(ImageSerializerDefault, self).create(validated_data=validated_data)


class ImageSerializerUpdate(ImageSerializerBase):
    class Meta(ImageSerializerBase.Meta):
        read_only_fields = ImageSerializerBase.Meta.read_only_fields + [
            "location",
            "image",
        ]

    def update(self, instance, validated_data):
        validated_data["location"] = BaseLocation.objects.get(
            id_string=validated_data.get("location")
        )
        return super(ImageSerializerUpdate, self).update(instance, validated_data)
