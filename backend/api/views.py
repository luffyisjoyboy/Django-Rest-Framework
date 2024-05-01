import json
from django.http import JsonResponse
from products.models import Product

def api_home(request, *args, **kwargs):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    print(model_data)
    print(type(model_data))
    if model_data:
        # we are trying to convert model instance (model data)
        # turn it into python dict
        # return json to my client
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
    return JsonResponse(data)