from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product

from .validators import validate_title_no_hello, unique_product_title

from api.serializers import UserPublicSerializer

class ProductInlineSerializer(serializers.Serializer):
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk', read_only=True
    )
    title = serializers.CharField(read_only=True)

class ProductSerializer(serializers.ModelSerializer):
    # loss_making = serializers.SerializerMethodField(read_only=True)
    # we want to rename get_discount to discount
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk'
    )
    title = serializers.CharField(validators = [validate_title_no_hello, unique_product_title])
    owner = UserPublicSerializer(source='user', read_only=True)
   
   #  name = serializers.CharField(source='title', read_only=True)
   #  email = serializers.EmailField(source='user.email', write_only=True)
    class Meta:
        model = Product
        fields = [
            "owner", "pk", "url", "edit_url" , "title", "content", "price", "sale_price",
        ]
    
    def validate_title(self, value):
        request = self.context.get("request")
        user = request.user
        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value
    
    def get_edit_url(self, obj):
        # return f"api/products/{obj.pk}/"
        request = self.context.get('request')  # we are using this instead of self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs = {"pk":obj.pk}, request=request)