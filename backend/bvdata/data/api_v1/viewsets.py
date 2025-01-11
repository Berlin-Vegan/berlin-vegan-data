from django_filters import rest_framework as filters
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet

from bvdata.data.api_v1.serializers import (
    ImageSerializerDefault,
    ImageSerializerUpdate,
    ReviewSerializer,
)
from bvdata.data.filters import ImageFilter
from bvdata.data.models import Image, Review


class ReviewViewSet(ReadOnlyModelViewSet):
    queryset = Review.objects.all().prefetch_related("reviewimage_set")
    serializer_class = ReviewSerializer


class ImageViewSet(ModelViewSet):
    queryset = Image.objects.all().prefetch_related("location", "uploader")
    serializer_class = ImageSerializerDefault
    filter_backends = [filters.DjangoFilterBackend]
    filterset_class = ImageFilter

    def get_serializer_class(self):
        if self.action == "update":
            return ImageSerializerUpdate
        else:
            return ImageSerializerDefault

    def perform_create(self, serializer):
        serializer.validated_data["uploader"] = self.request.user
        super(ImageViewSet, self).perform_create(serializer)
