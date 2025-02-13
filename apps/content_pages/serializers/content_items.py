from rest_framework import serializers

from apps.content_pages.models import Link, OrderedImage, OrderedVideo, Preamble, Quote, Text, Title
from apps.core.serializers import RoleSerializer


class ExtendedPersonSerializer(serializers.Serializer):
    id = serializers.SlugRelatedField(
        source="person",
        slug_field="id",
        read_only=True,
    )
    first_name = serializers.SlugRelatedField(
        source="person",
        slug_field="first_name",
        read_only=True,
    )
    last_name = serializers.SlugRelatedField(
        source="person",
        slug_field="last_name",
        read_only=True,
    )
    middle_name = serializers.SlugRelatedField(
        source="person",
        slug_field="middle_name",
        read_only=True,
    )
    city = serializers.SlugRelatedField(
        source="person",
        slug_field="city",
        read_only=True,
    )
    email = serializers.SlugRelatedField(
        source="person",
        slug_field="email",
        read_only=True,
    )
    image = serializers.ImageField(
        source="person.image",
        read_only=True,
    )
    roles = RoleSerializer(many=True)


class LinkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Link
        fields = (
            "title",
            "description",
            "url",
        )


class PreambleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Preamble
        fields = ("preamble",)


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ("quote",)


class TextSerializer(serializers.ModelSerializer):
    class Meta:
        model = Text
        fields = ("text",)


class TitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Title
        fields = ("title",)


class OrderedImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedImage
        fields = (
            "title",
            "image",
        )


class OrderedVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderedVideo
        fields = (
            "title",
            "url",
        )
