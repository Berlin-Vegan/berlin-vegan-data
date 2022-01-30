import os
from datetime import datetime
from unittest import mock

import pytest
import pytz
from django.test import TestCase

from bvdata.data.models import Review, ReviewImage
from bvdata.data.review_sync import (
    ReviewDict,
    get_review_images,
    get_review_text,
    import_reviews_from_wordpress,
    review_was_modified_or_does_not_exist,
)
from bvdata.data.tests.factories import ReviewFactory, ReviewImageFactory


class TestReviewSync(TestCase):
    url1 = "https://test.de/review1"

    def setUp(self) -> None:
        self.path = os.path.dirname(os.path.realpath(__file__))
        with open(f"{self.path}/test_files/raw_review_content.txt") as f:
            self.raw_content = f.read()
        with open(f"{self.path}/test_files/review_text.txt") as f:
            self.expected_text = f.read()

    def test_get_text(self) -> None:
        text = get_review_text(self.raw_content)
        self.assertEqual(text, self.expected_text)

    def test_images(self) -> None:
        image_list = get_review_images(self.raw_content)
        self.assertEqual(len(image_list), 2)
        self.assertEqual(image_list[0].height, 768)
        self.assertEqual(image_list[0].width, 1152)
        self.assertEqual(image_list[0].url, "https://test.de/test1.jpg")
        self.assertEqual(image_list[1].height, 859)
        self.assertEqual(image_list[1].width, 1152)
        self.assertEqual(image_list[1].url, "https://test.de/test2.jpg")

    def test_review_was_modified_or_does_not_exist_not_exist(self) -> None:
        data = dict(
            link=self.url1,
        )
        review_dict = dict()
        self.assertEqual(
            review_was_modified_or_does_not_exist(
                json_data=data, existing_reviews_dict=review_dict
            ),
            True,
        )

    def test_review_was_modified_or_does_not_exist_broken_datetime_str(self) -> None:
        data = dict(link=self.url1, modified="2020-10-24T12:1")
        review_dict: ReviewDict = {
            self.url1: {"id": 1, "updated": datetime(year=2020, month=10, day=23)}
        }
        with pytest.raises(TypeError):
            review_was_modified_or_does_not_exist(
                json_data=data, existing_reviews_dict=review_dict
            )

    def test_review_was_modified_or_does_not_exist_modified(self) -> None:
        data = dict(link=self.url1, modified="2020-10-24T12:11:56")
        updated = pytz.timezone("Europe/Berlin").localize(
            datetime(year=2020, month=10, day=23), is_dst=None
        )
        review_dict: ReviewDict = {self.url1: {"id": 1, "updated": updated}}

        self.assertEqual(
            review_was_modified_or_does_not_exist(
                json_data=data, existing_reviews_dict=review_dict
            ),
            True,
        )

    def test_review_was_modified_or_does_not_exist_not_modified(self) -> None:
        data = dict(link=self.url1, modified="2020-10-24T12:11:56")
        updated = pytz.timezone("Europe/Berlin").localize(
            datetime(year=2020, month=10, day=24, hour=12, minute=11, second=56),
            is_dst=None,
        )
        review_dict: ReviewDict = {self.url1: {"id": 1, "updated": updated}}

        self.assertEqual(
            review_was_modified_or_does_not_exist(
                json_data=data, existing_reviews_dict=review_dict
            ),
            False,
        )

    @mock.patch("bvdata.data.review_sync.fetch_review_data")
    def test_import_reviews_from_wordpress_new(self, mock_fetch_review_data) -> None:
        mock_fetch_review_data.return_value = [
            dict(
                link=self.url1,
                content=dict(rendered=self.raw_content),
                modified="2020-10-24T12:11:56",
            )
        ]
        import_reviews_from_wordpress()
        imported_review = Review.objects.all().first()
        self.assertEqual(imported_review.url, self.url1)
        self.assertEqual(imported_review.text, self.expected_text)
        self.assertEqual(imported_review.reviewimage_set.all().count(), 2)

        try:
            ReviewImage.objects.get(
                review=imported_review,
                url="https://test.de/test1.jpg",
                height=768,
                width=1152,
            )
            ReviewImage.objects.get(
                review=imported_review,
                url="https://test.de/test2.jpg",
                height=859,
                width=1152,
            )
        except ReviewImage.DoesNotExist:
            self.fail("Review images are not correct persisted in db")

    @mock.patch("bvdata.data.review_sync.get_review")
    @mock.patch("bvdata.data.review_sync.create_or_update_locations_with_review")
    @mock.patch("bvdata.data.review_sync.fetch_review_data")
    def test_import_reviews_from_wordpress_exist_no_update(
        self, mock_fetch_review_data, mock_create_or_update_review, mock_get_review
    ) -> None:
        updated = pytz.timezone("Europe/Berlin").localize(
            datetime(year=2020, month=10, day=24, hour=12, minute=11, second=56),
            is_dst=None,
        )
        ReviewFactory(url=self.url1, updated=updated)
        mock_fetch_review_data.return_value = [
            dict(
                link=self.url1,
                content=dict(rendered=self.raw_content),
                modified="2020-10-24T12:11:56",
            )
        ]

        import_reviews_from_wordpress()
        mock_create_or_update_review.assert_not_called()
        mock_get_review.assert_not_called()

    @mock.patch("bvdata.data.review_sync.fetch_review_data")
    def test_import_reviews_from_wordpress_exist_update(
        self, mock_fetch_review_data
    ) -> None:
        updated = pytz.timezone("Europe/Berlin").localize(
            datetime(year=2019, month=10, day=24, hour=12, minute=11, second=56),
            is_dst=None,
        )
        review = ReviewFactory(url=self.url1, updated=updated)
        old_review_image = ReviewImageFactory(review=review)

        review_image_to_be_removed = ReviewImageFactory()

        mock_fetch_review_data.return_value = [
            dict(
                link=self.url1,
                content=dict(rendered=self.raw_content),
                modified="2020-10-24T12:11:56",
            )
        ]
        import_reviews_from_wordpress()

        updated_review = Review.objects.get(id=review.id)
        self.assertEqual(updated_review.text, self.expected_text)

        image_list = updated_review.reviewimage_set.all()
        self.assertEqual(len(image_list), 2)
        try:
            ReviewImage.objects.get(
                review=updated_review,
                url="https://test.de/test1.jpg",
                height=768,
                width=1152,
            )
            ReviewImage.objects.get(
                review=updated_review,
                url="https://test.de/test2.jpg",
                height=859,
                width=1152,
            )
        except ReviewImage.DoesNotExist:
            self.fail("Review images are not correct persisted in db")

        with pytest.raises(ReviewImage.DoesNotExist):
            ReviewImage.objects.get(id=old_review_image.id)

        with pytest.raises(Review.DoesNotExist):
            Review.objects.get(id=review_image_to_be_removed.id)
