import requests
data = {
    'title': 'QWERTY',
    'price': 1000
}
endpoint = "http://localhost:8000/api/products/1/update/"
response = requests.put(endpoint, json=data)
print(response.json())
