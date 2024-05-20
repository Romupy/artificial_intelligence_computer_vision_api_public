from rest_framework import serializers
from .models import Text


class TextSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Text
        fields = ['image']


class OcrResultSerializer(serializers.Serializer):
    count = serializers.IntegerField()
    locations = serializers.ListField(child=serializers.DictField())