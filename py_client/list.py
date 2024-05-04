import requests

endpoint = "http://localhost:8000/api/products/call/"
data = {
    "title": "product createlist"
}
response = requests.post(endpoint, json=data)
print(response.text)

response = requests.get(endpoint)
print(response.text)
