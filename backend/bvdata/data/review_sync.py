import html
import re
import zoneinfo
from datetime import datetime
from typing import Dict, List, Optional, Tuple, TypedDict

import requests
from django.db import transaction
from django.utils.dateparse import parse_datetime

from bvdata.data.models import Review, ReviewImage

REVIEW_CATEGORY = 201
WORDPRESS_URL = f"https://berlin-vegan.de/wp-json/wp/v2/posts?categories={REVIEW_CATEGORY}&per_page=100"

ReviewTuple = Tuple[Review, List[ReviewImage]]


class DetailReviewDict(TypedDict):
    id: int
    updated: datetime


ReviewDict = Dict[str, DetailReviewDict]


def get_review_images(raw_content: str) -> List[ReviewImage]:
    pattern = re.compile(
        r'<img loading="lazy" width="(?P<width>\d+)" height="(?P<height>\d+)" src="(?P<url>.*?)" [^>]*/>'
    )
    images = re.finditer(pattern=pattern, string=raw_content)
    return [
        ReviewImage(
            height=int(image["height"]), width=int(image["width"]), url=image["url"]
        )
        for image in images
    ]


def get_review_text(raw_content: str) -> str:
    pattern = re.compile(r"<p>([^>]+)</p>")
    string_list = re.findall(pattern=pattern, string=raw_content)
    text = ""
    for string in string_list:
        string = html.unescape(string)
        string = string.replace("\xa0", "")
        if string.endswith(" "):
            text += string
        else:
            text += string + " "
    text = text.strip()
    return text


def fetch_review_data(url: str) -> dict:
    page = requests.get(url=url)
    return page.json()


def create_or_update_review_images(
    review: Review, images: List[ReviewImage]
) -> List[ReviewImage]:
    review_images = []
    for image in images:
        review_image, _ = ReviewImage.objects.update_or_create(
            review=review,
            url=image.url,
            defaults=dict(height=image.height, width=image.width),
        )
        review_images.append(review_image)
    return review_images


def delete_unused_review_images(review: Review, review_images: List[ReviewImage]):
    ReviewImage.objects.filter(review=review).exclude(
        id__in=[image.id for image in review_images]
    ).delete()


@transaction.atomic()
def create_or_update_locations_with_review(review_tuple: ReviewTuple) -> Review:
    review = review_tuple[0]
    review.save()
    review_images = create_or_update_review_images(
        review=review, images=review_tuple[1]
    )
    delete_unused_review_images(review=review, review_images=review_images)
    return review


def parse_datetime_berlin(datetime_str: str) -> Optional[datetime]:
    updated_naive = parse_datetime(datetime_str)
    if updated_naive is None:
        raise ValueError("Datetime string not well formatted")
    return updated_naive.replace(tzinfo=zoneinfo.ZoneInfo("Europe/Berlin"))


def get_review(json_data: dict, existing_review_id: Optional[int]) -> ReviewTuple:
    raw_content = json_data["content"]["rendered"]
    url = json_data["link"]
    images = get_review_images(raw_content=raw_content)
    text = get_review_text(raw_content=raw_content)
    updated = parse_datetime_berlin(json_data["modified"])
    review = Review(text=text, url=url, updated=updated)
    if existing_review_id is not None:
        review.id = existing_review_id
    return review, images


def get_existing_reviews_dict() -> ReviewDict:
    reviews = Review.objects.all()

    return {
        review.url: {"id": review.id, "updated": review.updated} for review in reviews
    }


def review_was_modified_or_does_not_exist(
    json_data: dict, existing_reviews_dict: ReviewDict
) -> bool:
    url = json_data["link"]
    if url not in existing_reviews_dict:
        return True

    updated = parse_datetime_berlin(json_data["modified"])
    if updated is None:
        return True

    existing_detail_review_dict: DetailReviewDict = existing_reviews_dict[url]
    if updated > existing_detail_review_dict["updated"]:
        return True
    return False


def import_reviews_from_wordpress():
    json = fetch_review_data(WORDPRESS_URL)
    existing_reviews_dict = get_existing_reviews_dict()
    new_review_list = []
    for json_data in json:
        if review_was_modified_or_does_not_exist(
            json_data=json_data, existing_reviews_dict=existing_reviews_dict
        ):
            review_id = existing_reviews_dict.get(json_data["link"], {}).get("id")
            review_tuple = get_review(
                json_data=json_data,
                existing_review_id=review_id,
            )
            review = create_or_update_locations_with_review(review_tuple=review_tuple)
            new_review_list.append(review)
