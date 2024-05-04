from rest_framework import generics

from .models import Product
from .serializers import ProductSerializer

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    # lookup_field = 'pk'

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

product_list_create_apiview = ProductListCreateAPIView.as_view()