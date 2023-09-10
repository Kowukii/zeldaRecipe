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


class RecipeListSerializer(ListSerializer):

    @property
    def data(self):
        ret = super(ListSerializer, self).data
        total_count = models.Recipe.objects.all().count()
        # today_count = models.ListOfAll.objects.filter(create_date=datetime.datetime.today()).count()

        info = {
            "total_count": total_count,
            # "today_count": today_count,
            "data": ret
        }
        return ReturnDict(info, serializer=self)


class RecipeListModelSerializer(ModelSerializer):

    class Meta:
        list_serializer_class = RecipeListSerializer
        model = models.Recipe
        fields = ["dish_id", "name_cn", "dish_info", "ingre1", "ingre2", "ingre3", "ingre4", "img_path"]

class RecipeCreateModelSerializer(ModelSerializer):
# area = serializer.CharField(source="get_area_display")
    class Meta:
        model = models.Recipe
        exclude = ['dish_id']
    def validate(self, data):
        name = data.get('name_cn')
        return data


