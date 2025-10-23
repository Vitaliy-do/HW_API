from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Product, Review
from django.http import Http404

from .serializers import ReviewSerializer, ProductListSerializer, ProductDetailsSerializer

# Реализован обработчик использующий метод запроса GET,
# который запрашивает все продукты
@api_view(['GET'])
def products_list_view(request):
    prod = Product.objects.all()
    ser = ProductListSerializer(prod, many=True)
    return Response(ser.data)

# Реализован обработчик, который подготавливает ответ
# по конкретному id продукта
class ProductDetailsView(APIView):
    def get(self, request, product_id):
        try:
            prod = Product.objects(pk=product_id)
            ser = ProductDetailsSerializer(prod, many=False)
            return Response(ser.data)
        except Product.DoesNotExist:
            raise Http404('Нет такого товара')

