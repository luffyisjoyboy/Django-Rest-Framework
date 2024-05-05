from django.urls import path
from . import views

urlpatterns = [
    path('', views.product_list_create_api_view),
    path('<int:pk>/', views.ProductDetailAPIView.as_view())
]
