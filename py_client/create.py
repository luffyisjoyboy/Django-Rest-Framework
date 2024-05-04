import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "product p3"
}
response = requests.post(endpoint, json=data)
print(response.text)
