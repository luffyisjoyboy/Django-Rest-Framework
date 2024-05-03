import json
from django.forms.models import model_to_dict

# from django.http import JsonResponse, HttpResponse

from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["GET"])
def api_home(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
      # data = model_to_dict(instance, fields=['id', 'title', 'sale_price'])
      data = ProductSerializer(instance).data
    return Response(data)
