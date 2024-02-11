import requests

res = requests.get("http://127.0.0.1:8080/api/storages")
print(res.json())
