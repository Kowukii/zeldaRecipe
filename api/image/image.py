from rest_framework.generics import ListAPIView, CreateAPIView, DestroyAPIView

from api.serializers.bank import BankCreateModelSerializer,BankListModelSerializer
from api import models
from rest_framework import serializers
from rest_framework.views import APIView
from rest_framework.response import Response
from api import models
class ImageSerializer(serializers.Serializer):
  picker_values = serializers.ListField()
  image_src = serializers.CharField()

class ImageView(APIView):
    http_method_names = ['get', 'post']

    def get(self, request):
        picker_values = request.GET.get('pickerValues')
        image_src = get_image_src_from_db(picker_values)
        return Response({
            'image_src': image_src
        })
    def post(self, request):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
          picker_values = serializer.validated_data['picker_values']
          #print(picker_values)
          image_src = get_image_src_from_db(picker_values)

          serializer.save(image_src=image_src)
          return Response(serializer.data)
        else:
          return Response(serializer.errors)

def get_image_src_from_db(picker_values):
    try:
        image = models.Material.objects.get(cn_name=picker_values)
        return image.img_path
    except models.Material.DoesNotExist:
        return None

# serializers.py


# views.py

from rest_framework import viewsets
