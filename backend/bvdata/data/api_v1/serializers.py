from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer

from bvdata.data.models import Review, ReviewImage


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
