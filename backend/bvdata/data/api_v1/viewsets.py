from rest_framework.viewsets import ReadOnlyModelViewSet

from bvdata.data.api_v1.serializers import ReviewSerializer
from bvdata.data.models import Review


class ReviewViewSet(ReadOnlyModelViewSet):
    queryset = Review.objects.all().prefetch_related("reviewimage_set")
    serializer_class = ReviewSerializer
