import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "product createlist"
}

response = requests.get(endpoint)
print(response.json())
