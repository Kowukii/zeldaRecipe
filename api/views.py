from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import *
from api.serializers.image import DataSerializer, ImageSerializer
# Create your bank here.


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
    def create(self, request):
        serializer = DataSerializer(data=request.data)
        print(serializer)
        if serializer.is_valid():
            data = serializer.validated_data['data']
            # 处理数据
            objClass = ClassOfIngredients.objects.get(class_id=data[0]+1)
            obj = Material.objects.filter(class_name=objClass.name_cn)
            res = obj[data[1]+1]
            serializer = ImageSerializer(data={'image_paths': res.img_path})
            print(res.img_path)
            print(serializer)
            if serializer.is_valid():
                return Response(serializer.data)
        else:
            print("serializer_error:", serializer.errors)
        return Response('valided_not')