from django import forms

from .models import Product

class ProductFomr(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['title', 'sale_price']