import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://localhost:8000/api"

# When sending json in parameters output would be in data key and content type is application/json
response = requests.get(endpoint, json={"query":"Hello world!"})

# prints json: raw text response
print(response.text)
print(response.status_code)
print(response.json()['message'])

# When sending json in parameters output would be in form key and content type is application/x-www-form-urlencoded
# response = requests.get(endpoint, data={"query":"Hello world!"})


# HTTP Request -> HTML
# REST API HTTP Request -> json
# Javascript object Notation
# Typically what you want to send is what you expect it to be recieved like sending a json you would be expecting a json as well mostly
# converts json to dict
# print(response.json())
