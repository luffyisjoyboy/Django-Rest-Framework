import requests

endpoint = "http://localhost:8000/api/"
response = requests.post(endpoint, params={"abc": 123}, json={"content":"Hello world!"})
print(response.text)
