from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

class ProductSerializer(serializers.ModelSerializer):
    # loss_making = serializers.SerializerMethodField(read_only=True)
    # we want to rename get_discount to discount
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk'
    )
    class Meta:
        model = Product
        fields = [
            "pk", "url", "edit_url" , "title", "content", "price", "sale_price", "discount"
        ]
    
    def get_edit_url(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get('request')  # we are using this instead of self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs = {"pk":obj.pk}, request=request)

    def get_discount(self, obj):
        # return ""
        if not hasattr(obj, 'id'):
            return None
        if not isinstance(obj, Product):
            return None
        return obj.get_discount()
    