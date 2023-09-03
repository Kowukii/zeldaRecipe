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


class BankListSerializer(ListSerializer):

    @property
    def data(self):
        ret = super(ListSerializer, self).data
        total_count = models.Material.objects.all().count()
        # today_count = models.ListOfAll.objects.filter(create_date=datetime.datetime.today()).count()

        info = {
            "total_count": total_count,
            # "today_count": today_count,
            "data": ret
        }
        return ReturnDict(info, serializer=self)


class BankListModelSerializer(ModelSerializer):

    class Meta:
        list_serializer_class = BankListSerializer
        model = models.Material
        fields = ["id", "cn_name", "DyeColor", "info", "img_path"]

class BankCreateModelSerializer(ModelSerializer):
# area = serializer.CharField(source="get_area_display")
    class Meta:
        model = models.Material
        exclude = ['id', 'cn_name']
    def validate(self, data):
        name = data.get('cn_name')
        return data


