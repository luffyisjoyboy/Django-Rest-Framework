from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'


class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        return super().perform_update(serializer)

product_update_api_view = ProductUpdateAPIView.as_view()

class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'pk'

    def perform_destroy(self, instance):
        print(instance)
        super().perform_destroy(instance)

product_delete_api_view = ProductDeleteAPIView.as_view()

class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content', None)
        if content is None:
            content = title
        serializer.save(title=title, content=content)

product_create_view = ProductCreateAPIView.as_view()

class ProductListAPIView(generics.ListAPIView):
    """
        Returns all list of json objects of Product
    """
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_view = ProductListAPIView.as_view()


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_list_create_api_view = ProductListCreateAPIView.as_view()

# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404

# @api_view(["GET", "POST"])
# def product_alt_view(request, pk=None, *args, **kwargs):
#     method = request.method

#     if method == "GET":
#         # depends on params passed
#         # get data for given id -> detail view
#         if pk is not None:
#             obj = get_object_or_404(Product, id=pk)
#             data = ProductSerializer(obj, many=False).data
#             return Response(data)
#             # qs = Product.objects.filter(id=pk)
#             # if not qs.exist():
#             #     raise Http404

#         # get all list of data -> list view
#         qs = Product.objects.all()
#         data = ProductSerializer(qs, many=True).data
#         return Response(data)
    
#     if method == "POST":
#         # create a new instance
#         serializer = ProductSerializer(data=request.data)
#         if serializer.is_valid(raise_exception=True):
#             # serializer.save()
#             title = serializer.validated_data.get('title')
#             content = serializer.validated_data.get('content', None)
#             if content is None:
#                 content = title
#             serializer.save(title=title, content=content)
#             return Response(serializer.data)
#         return Response({"invalid":"not good data"}, status=400)
