import requests

response = requests.get("http://127.0.0.1:8000/products")

assert response.status_code == 200

assert isinstance(response.json(), list)