from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from api.serializers.image import DataSerializer, ImageSerializer
# Create your bank here.
from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView
from api.serializers.recipe import *
from api.serializers.bank import BankCreateModelSerializer,BankListModelSerializer
from api import models
from django.db.models import Q
from django.forms.models import model_to_dict
# -*- coding=utf-8 -*-
def index(request):
    pass
    return HttpResponse('testDjango')

def get_info(request):
    info = UserModel.objects.all()
    return render(request, 'info_demo.html', {'info': info})

def brief(request, uid):
    print('uid:', uid)
    element = UserModel.objects.get(pk=uid)
    return render(request, 'brief.html', {'element': element})



# class ImageView(APIView):
#     def get(self, request):
#         picker_value = request.query_params.get('pickerValue')
#         image_url = get_image_by_picker(picker_value)
#
#         data = {
#             'errcode': 0,
#             'imageUrl': image_url
#         }
#
#         return Response(data)
class DataSubmitView(viewsets.ViewSet):

    def get_recipe(self, board):
        set = []
        fuzzy_set = []
        for i in range(4):
            if board[i] != -1:
                item_class = ClassOfIngredients.objects.get(class_id=board[i][0]+1).name_cn

                item_class_en = ClassOfIngredients.objects.get(class_id=board[i][0]+1).class_name
                set.append(Material.objects.filter(class_name=item_class)[board[i][1]].cn_name)

                if item_class_en.startswith("Cook"):
                    fuzzy_set.append(item_class_en)
                else:
                    print(item_class)
                    fuzzy_set.append(Material.objects.filter(class_name=item_class)[board[i][1]].cn_name)

        print("fuzzy", fuzzy_set)
        print("set:", set)
        # 构造查询条件
        q = Q()
        for ing in set:
            q &= Q(ingre1=ing) | Q(ingre2=ing) | Q(ingre3=ing) | Q(ingre4=ing)
        # 查询同时包含所有食材的菜谱
        recipes = Recipe.objects.filter(q)
        listrecipe = []
        for recipe in recipes:

            listrecipe.append(model_to_dict(recipe))

        q = Q()
        for ing in fuzzy_set:
            q &= Q(ingre1=ing) | Q(ingre2=ing) | Q(ingre3=ing) | Q(ingre4=ing)
        recipes = Recipe.objects.filter(q)
        for recipe in recipes:
            listrecipe.append(model_to_dict(recipe))
        try:
            print(listrecipe)
        except UnicodeEncodeError:
            pass
        return listrecipe

    def create(self, request):
        # print(request)
        serializer = DataSerializer(data=request.data)
        # print(serializer)
        if serializer.is_valid():
            # 接受并验证数据
            data = serializer.validated_data['data']
            print("data:", data)
            index = serializer.validated_data['index']
            print("index:", index)
            board = serializer.validated_data['board']
            print("pre_board:", board)
            # data传输当前选择的食材，index表示当前选中的食材位置，board表示当前维持的锅里的食材
            # 处理数据
            objClass = ClassOfIngredients.objects.get(class_id=data[0]+1)
            # data是一个数组，第一个数据data[0]表示当前食材类别，第二个数据data[1]表示食材类中偏移量
            # objClass是选择的食材类别表中的类别数据项
            obj = Material.objects.filter(class_name=objClass.name_cn)
            # obj是素材表中得到所有名字为对应类别的数据项
            print(len(obj))
            res = obj[data[1]]
            # res是按照偏移量选择所有数据项中对应的所选项
            print(res.cn_name)
            board[index] = data
            print("new_board", board)
            # 接下来根据board定义并返回食谱
            recipes = self.get_recipe(board)
            # dataList = [
            #     recipes,
            #     res.img_path,
            #     board,
            # ]
            serializer = ImageSerializer(data={'image_path': res.img_path, 'board': board,
                                               'recipes': recipes})

            if serializer.is_valid():
                return Response(serializer.data)
            # return JsonResponse(dataList, safe=False)
        else:
            print("serializer_error:", serializer.errors)
        return Response('valided_not')

class RecipeCheckView(ListAPIView, CreateAPIView, DestroyAPIView):
    queryset = models.Recipe.objects.all()

    def get_serializer_class(self):
        if self.request.method == "POST":
            return RecipeCreateModelSerializer
        return RecipeListModelSerializer