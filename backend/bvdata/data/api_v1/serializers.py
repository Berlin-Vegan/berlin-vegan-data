from django.contrib.auth import get_user_model
from rest_framework.serializers import ModelSerializer


class AccountProfileModelSerializer(ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ["id", "username", "email"]
        read_only_fields = ["id", "username"]
