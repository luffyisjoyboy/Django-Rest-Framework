import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    # request -> HTTP Request -> Django
    # request.body
    print(request.GET) # url query parameters
    print(type(request.GET))
    print(request.POST)
    body = request.body
    data = {}
    try: 
        data = json.loads(body) # converts byte string Json data --> Python Dict
    except:
        pass
    print(data.keys())
    print(type(request.headers))
    print(request.headers)
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    return JsonResponse(data)