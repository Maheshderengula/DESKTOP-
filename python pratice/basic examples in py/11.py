import requests
Url ="https://dummyjson.com/users"
response = requests.get(Url)

print(response.status_code)
print(response.json())