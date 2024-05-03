from rest_framework.decorators import api_view
from rest_framework.response import Response

from products.models import Product
from products.serializers import ProductSerializer

@api_view(["POST"])
def api_home(request, *args, **kwargs):
   """
    DRF API View
   """
   serializer = ProductSerializer(data=request.data)
   print(serializer)
   if serializer.is_valid(raise_exception=True):
      serializer.save()
      data = serializer.data
      return Response(data)
   return Response({"invalid":"not good data"}, status=400)
