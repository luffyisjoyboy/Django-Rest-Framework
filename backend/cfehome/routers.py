from rest_framework.routers import DefaultRouter

from products.viewsets import ProductViewSet, ProductGenericViewSet

# router = DefaultRouter()
# router.register('product-abc', ProductViewSet, basename='products')
# print(router.urls)
# urlpatterns = router.urls

router = DefaultRouter()
router.register('product-abc', ProductGenericViewSet, basename='products')
print(router.urls)
urlpatterns = router.urls
