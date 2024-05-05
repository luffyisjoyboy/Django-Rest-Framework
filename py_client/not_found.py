import requests

endpoint = "http://localhost:8000/api/products/19843ur84ut58u/"
response = requests.get(endpoint)
print(response.text)
