import requests
from api import product_api


BASE_URL = "http://127.0.0.1:8000"


def test_create_product():

    product = {
        "ProductName": "iPhone 16",
        "Category": "Mobile",
        "Brand": "Apple",
        "Price": 1500,
        "Stock": 12,
        "Status": "Available"
    }

    response = product_api.create_product(product)

    assert response.status_code == 200

    created_product = response.json()

   

    assert created_product["ProductName"] == product["ProductName"]
    assert created_product["Category"] == product["Category"]
    assert created_product["Brand"] == product["Brand"]
    assert created_product["Price"] == product["Price"]
    assert created_product["Stock"] == product["Stock"]
    assert created_product["Status"] == product["Status"]

    assert created_product["ProductID"]> 0

    product_id = created_product["ProductID"]

    response = requests.delete(f"{BASE_URL}/products/{product_id}")

    assert response.status_code == 200

    data = response.json()

    assert data["message"] == "Product deleted successfully"

    response = requests.get(f"{BASE_URL}/products/{product_id}")

    assert response.status_code == 404



