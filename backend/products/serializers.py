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
    discount = serializers.SerializerMethodField(read_only=True)
    edit_url = serializers.SerializerMethodField(read_only=True)
    url = serializers.HyperlinkedIdentityField(
        view_name='product-detail', lookup_field='pk'
    )
    title = serializers.CharField(validators = [validate_title_no_hello, unique_product_title])
    owner = UserPublicSerializer(source='user', read_only=True)
    related_products = ProductInlineSerializer(source='user.product_set.all', read_only=True, many=True)
   #  name = serializers.CharField(source='title', read_only=True)
   #  email = serializers.EmailField(source='user.email', write_only=True)
    class Meta:
        model = Product
        fields = [
            "owner", "pk", "url", "edit_url" , "title", "content", "price", "sale_price", "discount", "related_products"
        ]
    
    def validate_title(self, value):
        request = self.context.get("request")
        user = request.user
        qs = Product.objects.filter(user=user, title__iexact=value)
        if qs.exists():
            raise serializers.ValidationError(f"{value} is already a product name")
        return value
    
    # def create(self, validated_data):
    #     # email = validated_data.pop("email")
    #     obj = super().create(validated_data)
    #     print(obj)
    #     return obj

    # def update(self, instance, validated_data):
    #     email = validated_data.pop('email')
    #     return super().update(instance, validated_data)

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
    