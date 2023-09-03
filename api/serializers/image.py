import uuid
import datetime
from rest_framework.serializers import ModelSerializer, Serializer, ListSerializer
from rest_framework import serializers
from rest_framework import exceptions
from rest_framework.utils.serializer_helpers import (
    BindingDict, BoundField, JSONBoundField, NestedBoundField,
    ReturnDict, ReturnList
)
from api import models


# serializers.py

from rest_framework import serializers

class DataSerializer(serializers.Serializer):
    data = serializers.ListField(child=serializers.IntegerField())

class ImageSerializer(serializers.Serializer):
    image_paths = serializers.CharField()