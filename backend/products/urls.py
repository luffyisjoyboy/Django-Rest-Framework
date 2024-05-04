from django.urls import path
from .views import ProductDetailAPIView, product_create_view, product_list_view, product_list_create_apiview

urlpatterns = [
    path('', product_create_view),
    path('all/', product_list_view),
    path('call/', product_list_create_apiview),
    path('<int:pk>/', ProductDetailAPIView.as_view())
]
