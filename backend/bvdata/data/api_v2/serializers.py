from django.db import models, transaction
from rest_framework.fields import (
    BooleanField,
    ChoiceField,
    DictField,
    ReadOnlyField,
    SerializerMethodField,
    TimeField,
)
from rest_framework.serializers import ListSerializer, ModelSerializer, Serializer

from bvdata.data.models import (
    SHOPPING_BOOELAN_ATTRIBUTE_CHOICES,
    SHOPPING_TAG_CHOICES,
    BaseLocation,
    BooleanAttribute,
    LocationTypeChoices,
    OpeningHours,
    Tag,
)

__all__ = (
    "TagShoppingListSerializer",
    "OpeningHoursSerializer",
    "ShoppingAttributeSerializer",
    "PrivateBaseLocationListSerializer",
    "PrivateShoppingDetailSerializer",
    "PublicShoppingDetailSerializer",
)

WEEKDAY_SERIALIZER_DEFAULT = {"opening": None, "closing": None}


class WeekdayField(DictField):
    def __init__(self, *args, **kwargs):
        super(WeekdayField, self).__init__(
            default=WEEKDAY_SERIALIZER_DEFAULT, *args, **kwargs
        )

    opening = TimeField()
    closing = TimeField()


class OpeningHoursSerializer(Serializer):
    monday = WeekdayField()
    tuesday = WeekdayField()
    wednesday = WeekdayField()
    thursday = WeekdayField()
    friday = WeekdayField()
    saturday = WeekdayField()
    sunday = WeekdayField()

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        ret = {
            day.weekday.lower(): {"opening": day.opening, "closing": day.closing}
            for day in iterable
        }
        return super(OpeningHoursSerializer, self).to_representation(ret)

    def to_internal_value(self, data):
        ret = super(OpeningHoursSerializer, self).to_internal_value(data=data)
        ret = [
            {
                "weekday": day.upper(),
                "closing": values["closing"],
                "opening": values["opening"],
            }
            for day, values in ret.items()
            if values.get("opening", None) or values.get("closing", None)
        ]
        return ret


class TagShoppingListSerializer(ListSerializer):
    child = ChoiceField(choices=SHOPPING_TAG_CHOICES)

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        return [
            self.child.to_representation(item.tag) if item is not None else None
            for item in iterable
        ]

    def to_internal_value(self, data):
        ret = super(TagShoppingListSerializer, self).to_internal_value(data=data)
        return set(ret)


class ShoppingAttributeSerializer(Serializer):
    def get_fields(self):
        return {
            field[0]: BooleanField(allow_null=True)
            for field in SHOPPING_BOOELAN_ATTRIBUTE_CHOICES
        }

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        ret = {field.name: field.state for field in iterable}
        return super(ShoppingAttributeSerializer, self).to_representation(ret)

    def to_internal_value(self, data):
        data = super(ShoppingAttributeSerializer, self).to_internal_value(data=data)
        return [{"name": name, "state": state} for name, state in data.items()]


class BaseLocationSerializer(ModelSerializer):
    id = ReadOnlyField(source="id_string")

    class Meta:
        model = BaseLocation
        fields = ["id", "name", "street", "postal_code", "city", "vegan"]
        read_only_fields = ["id_string"]


class PrivateBaseLocationListSerializer(BaseLocationSerializer):
    has_review_link = BooleanField()

    class Meta(BaseLocationSerializer.Meta):
        fields = BaseLocationSerializer.Meta.fields + ["has_review_link"]
        read_only_fields = fields


class PublicBaseDetailSerializer(BaseLocationSerializer):
    opening_hours = OpeningHoursSerializer(source="openinghours_set", required=False)
    images = ReadOnlyField(default=[])

    class Meta(BaseLocationSerializer.Meta):
        fields = BaseLocationSerializer.Meta.fields + [
            "created",
            "updated",
            "latitude",
            "longitude",
            "telephone",
            "website",
            "email",
            "comment",
            "comment_english",
            "review_link",
            "closed",
            "comment_opening_hours",
            "opening_hours",
            "tags",
            "attributes",
            "images",
        ]

        read_only_fields = BaseLocationSerializer.Meta.read_only_fields + [
            "created",
            "updated",
            "images",
        ]


class PublicNameMixin(Serializer):
    name = SerializerMethodField()

    @staticmethod
    def get_name(obj):
        return f"{obj.name} - GESCHLOSSEN / CLOSED" if obj.closed else obj.name


class PublicShoppingDetailSerializer(PublicNameMixin, PublicBaseDetailSerializer):
    tags = TagShoppingListSerializer(required=False)
    attributes = ShoppingAttributeSerializer(
        source="boolean_attributes", required=False
    )

    class Meta(PublicBaseDetailSerializer.Meta):
        pass


class LastEditorMixin(Serializer):
    last_editor = SerializerMethodField()

    @staticmethod
    def get_last_editor(obj):
        return (
            obj.last_editor.username if hasattr(obj.last_editor, "username") else None
        )


class PrivateShoppingDetailSerializer(LastEditorMixin, PublicBaseDetailSerializer):
    tags = TagShoppingListSerializer(required=False)
    attributes = ShoppingAttributeSerializer(
        source="boolean_attributes", required=False
    )

    class Meta(PublicBaseDetailSerializer.Meta):
        fields = PublicBaseDetailSerializer.Meta.fields + [
            "text_intern",
            "has_sticker",
            "is_submission",
            "submit_email",
            "last_editor",
        ]

        read_only_fields = PublicBaseDetailSerializer.Meta.read_only_fields + [
            "last_editor",
        ]

    def create(self, validated_data):
        boolean_attributes = validated_data.pop("boolean_attributes", [])
        tags = validated_data.pop("tags", [])
        opening_hours = validated_data.pop("openinghours_set", {})
        with transaction.atomic():
            base_location = BaseLocation.objects.create(
                type=LocationTypeChoices.SHOPPING, **validated_data
            )
            opening_hours = [
                OpeningHours(location=base_location, **opening_hour)
                for opening_hour in opening_hours
            ]
            OpeningHours.objects.bulk_create(opening_hours)
            boolean_attributes = [
                BooleanAttribute.objects.get_or_create(**boolean_attribute)[0]
                for boolean_attribute in boolean_attributes
            ]
            base_location.boolean_attributes.set(boolean_attributes)
            tags = [Tag.objects.get_or_create(tag=tag)[0] for tag in tags]
            base_location.tags.set(tags)
        return base_location

    def update(self, instance, validated_data):
        boolean_attributes = validated_data.pop("boolean_attributes", None)
        tags = validated_data.pop("tags", None)
        opening_hours = validated_data.pop("openinghours_set", None)
        with transaction.atomic():
            for (key, value) in validated_data.items():
                setattr(instance, key, value)
            instance.save()

            if opening_hours is not None:
                weekday_list = [
                    opening_hour["weekday"] for opening_hour in opening_hours
                ]
                # delete opening hours
                OpeningHours.objects.filter(location=instance).exclude(
                    weekday__in=weekday_list
                ).delete()
                # update or create opening hours
                for opening_hour in opening_hours:
                    defaults = dict(
                        opening=opening_hour["opening"], closing=opening_hour["closing"]
                    )
                    OpeningHours.objects.update_or_create(
                        defaults=defaults,
                        location=instance,
                        weekday=opening_hour["weekday"],
                    )

            if boolean_attributes is not None:
                boolean_attributes_new = [
                    BooleanAttribute.objects.get_or_create(**boolean_attribute)[0]
                    for boolean_attribute in boolean_attributes
                ]
                instance.boolean_attributes.set(boolean_attributes_new)

            if tags is not None:
                tags_new = [Tag.objects.get_or_create(tag=tag)[0] for tag in tags]
                instance.tags.set(tags_new)

        return instance
