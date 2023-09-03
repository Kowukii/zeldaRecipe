from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from api.serializers.bank import BankCreateModelSerializer,BankListModelSerializer
from api import models

class FruitView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='水果')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class FishView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='鱼')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class MushroomView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='蘑菇')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class VegetableView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='蔬菜')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class MeatView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='肉类')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class CrabView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='螃蟹')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class NutView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='坚果')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class EnemyView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='敌人')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class RelishView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='佐料')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class SpecialView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='特殊')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class InsectView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='昆虫')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class BadView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Material.objects.filter(class_name='Bad')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer

class LastRecipe(ListAPIView, CreateAPIView, DestroyAPIView):
    # queryset = models.Material.objects.filter(class_name='Bad')

    def get_serializer_class(self):
        if self.request.method == "POST":
            return BankCreateModelSerializer
        return BankListModelSerializer