from django.db import models, transaction
from rest_framework.fields import (
    BooleanField,
    ChoiceField,
    DictField,
    IntegerField,
    ReadOnlyField,
    SerializerMethodField,
    TimeField,
)
from rest_framework.serializers import ListSerializer, ModelSerializer, Serializer

from bvdata.data.models import (
    GASTRO_BOOLEAN_ATTRIBUTE_CHOICES,
    GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES,
    GASTRO_TAG_CHOICES,
    SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES,
    SHOPPING_TAG_CHOICES,
    BaseLocation,
    BooleanAttribute,
    OpeningHours,
    PositiveIntegerAttribute,
    Tag,
)

__all__ = (
    "TagListSerializer",
    "OpeningHoursSerializer",
    "ShoppingAttributeSerializer",
    "LocationListSerializer",
    "ShoppingDetailSerializer",
    "GastroDetailSerializer",
    "GastroAttributeSerializer",
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


class TagListSerializer(ListSerializer):
    def __init__(self, tags, *args, **kwargs):
        child = ChoiceField(choices=tags)
        super(TagListSerializer, self).__init__(
            required=False, child=child, *args, **kwargs
        )

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        return [
            self.child.to_representation(item.tag) if item is not None else None
            for item in iterable
        ]

    def to_internal_value(self, data):
        ret = super(TagListSerializer, self).to_internal_value(data=data)
        return set(ret)


class ShoppingAttributeSerializer(Serializer):
    def get_fields(self):
        return {
            field[0]: BooleanField(allow_null=True)
            for field in SHOPPING_BOOLEAN_ATTRIBUTE_CHOICES
        }

    def to_representation(self, data):
        iterable = data.all() if isinstance(data, models.Manager) else data
        ret = {field.name: field.state for field in iterable}
        return super(ShoppingAttributeSerializer, self).to_representation(ret)

    def to_internal_value(self, data):
        data = super(ShoppingAttributeSerializer, self).to_internal_value(data=data)
        return [{"name": name, "state": state} for name, state in data.items()]


class GastroAttributeSerializer(Serializer):
    def get_fields(self):
        return {
            **{
                field[0]: BooleanField(allow_null=True)
                for field in GASTRO_BOOLEAN_ATTRIBUTE_CHOICES
            },
            **{
                field[0]: IntegerField(min_value=0, default=0)
                for field in GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES
            },
        }

    def to_representation(self, data: BaseLocation):
        boolean_attributes = (
            data.boolean_attributes.all()
            if isinstance(data.boolean_attributes, models.Manager)
            else data.boolean_attributes
        )
        positive_integer_attributes = (
            data.positive_integer_attributes.all()
            if isinstance(data.positive_integer_attributes, models.Manager)
            else data.positive_integer_attributes
        )
        ret = {
            field.name: field.state
            for field in [*boolean_attributes, *positive_integer_attributes]
        }
        return super(GastroAttributeSerializer, self).to_representation(ret)

    @staticmethod
    def _get_attrs(attrs):
        return [{"name": name, "state": state} for name, state in attrs.items()]

    def to_internal_value(self, data):
        data = super(GastroAttributeSerializer, self).to_internal_value(data=data)
        return {
            "boolean_attributes": self._get_attrs(
                {
                    boolean_key: data[boolean_key]
                    for boolean_key in dict(GASTRO_BOOLEAN_ATTRIBUTE_CHOICES)
                }
            ),
            "positive_integer_attributes": self._get_attrs(
                {
                    p_integer_key: data[p_integer_key]
                    for p_integer_key in dict(GASTRO_POSITIVE_INTEGER_ATTRIBUTE_CHOICES)
                }
            ),
        }


class BaseLocationSerializer(ModelSerializer):
    id = ReadOnlyField(source="id_string")

    class Meta:
        model = BaseLocation
        fields = ["id", "name", "street", "postal_code", "city", "vegan"]
        read_only_fields = ["id_string"]


class LocationListSerializer(BaseLocationSerializer):
    has_review_link = BooleanField()
    image_count = IntegerField()

    class Meta(BaseLocationSerializer.Meta):
        fields = BaseLocationSerializer.Meta.fields + ["has_review_link", "image_count"]
        read_only_fields = fields


class ShoppingTagsAttributesSerializerMixin(Serializer):
    tags = TagListSerializer(tags=SHOPPING_TAG_CHOICES)
    attributes = ShoppingAttributeSerializer(
        source="boolean_attributes", required=False
    )


class GastroTagsAttributesSerializerMixin(Serializer):
    tags = TagListSerializer(tags=GASTRO_TAG_CHOICES)
    attributes = GastroAttributeSerializer(source="*", required=False)


class LastEditorMixin(Serializer):
    last_editor = SerializerMethodField()

    @staticmethod
    def get_last_editor(obj):
        return (
            obj.last_editor.username if hasattr(obj.last_editor, "username") else None
        )


class BaseDetailSerializer(LastEditorMixin, BaseLocationSerializer):
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
            "comment_opening_hours",
            "comment_public_transport",
            "closed",
            "opening_hours",
            "tags",
            "attributes",
            "images",
            "text_intern",
            "has_sticker",
            "is_submission",
            "submit_email",
            "last_editor",
            "review",
        ]

        read_only_fields = BaseLocationSerializer.Meta.read_only_fields + [
            "created",
            "updated",
            "images",
            "last_editor",
        ]

    @transaction.atomic
    def create(self, validated_data):
        tags = validated_data.pop("tags", [])
        opening_hours = validated_data.pop("openinghours_set", {})
        instance = BaseLocation.objects.create(**validated_data)
        opening_hours = [
            OpeningHours(location=instance, **opening_hour)
            for opening_hour in opening_hours
        ]
        OpeningHours.objects.bulk_create(opening_hours)
        tags = [Tag.objects.get_or_create(tag=tag)[0] for tag in tags]
        instance.tags.set(tags)

        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        tags = validated_data.pop("tags", None)
        opening_hours = validated_data.pop("openinghours_set", None)
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()

        if opening_hours is not None:
            weekday_list = [opening_hour["weekday"] for opening_hour in opening_hours]
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

        if tags is not None:
            tags_new = [Tag.objects.get_or_create(tag=tag)[0] for tag in tags]
            instance.tags.set(tags_new)

        return instance


class ShoppingDetailSerializer(
    ShoppingTagsAttributesSerializerMixin, BaseDetailSerializer
):
    class Meta(BaseDetailSerializer.Meta):
        pass

    @transaction.atomic
    def create(self, validated_data):
        boolean_attributes = validated_data.pop("boolean_attributes", None)
        instance = super(ShoppingDetailSerializer, self).create(
            validated_data=validated_data
        )
        if boolean_attributes:
            boolean_attributes = [
                BooleanAttribute.objects.get_or_create(**boolean_attribute)[0]
                for boolean_attribute in boolean_attributes
            ]
            instance.boolean_attributes.set(boolean_attributes)
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        boolean_attributes = validated_data.pop("boolean_attributes", None)
        instance = super(ShoppingDetailSerializer, self).update(
            instance=instance, validated_data=validated_data
        )
        if boolean_attributes is not None:
            boolean_attributes_new = [
                BooleanAttribute.objects.get_or_create(**boolean_attribute)[0]
                for boolean_attribute in boolean_attributes
            ]
            instance.boolean_attributes.set(boolean_attributes_new)

        return instance


class GastroDetailSerializer(GastroTagsAttributesSerializerMixin, BaseDetailSerializer):
    class Meta(BaseDetailSerializer.Meta):
        pass

    @transaction.atomic
    def create(self, validated_data):
        boolean_attributes = validated_data.pop("boolean_attributes", None)
        positive_integer_attributes = validated_data.pop(
            "positive_integer_attributes", None
        )
        instance = super(GastroDetailSerializer, self).create(
            validated_data=validated_data
        )
        if boolean_attributes:
            boolean_attributes = [
                BooleanAttribute.objects.get_or_create(**boolean_attribute)[0]
                for boolean_attribute in boolean_attributes
            ]
            instance.boolean_attributes.set(boolean_attributes)
        if positive_integer_attributes:
            positive_integer_attributes = [
                PositiveIntegerAttribute.objects.get_or_create(
                    **positive_integer_attribute
                )[0]
                for positive_integer_attribute in positive_integer_attributes
            ]
            instance.positive_integer_attributes.set(positive_integer_attributes)
        return instance

    @transaction.atomic
    def update(self, instance, validated_data):
        boolean_attributes = validated_data.pop("boolean_attributes", None)
        positive_integer_attributes = validated_data.pop(
            "positive_integer_attributes", None
        )
        instance = super(GastroDetailSerializer, self).update(
            instance=instance, validated_data=validated_data
        )
        if boolean_attributes is not None:
            boolean_attributes_new = [
                BooleanAttribute.objects.get_or_create(**boolean_attribute)[0]
                for boolean_attribute in boolean_attributes
            ]
            instance.boolean_attributes.set(boolean_attributes_new)
        if positive_integer_attributes:
            positive_integer_attributes = [
                PositiveIntegerAttribute.objects.get_or_create(
                    **positive_integer_attribute
                )[0]
                for positive_integer_attribute in positive_integer_attributes
            ]
            instance.positive_integer_attributes.set(positive_integer_attributes)
        return instance
