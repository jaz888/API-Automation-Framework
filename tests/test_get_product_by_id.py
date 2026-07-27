import requests

BASE_URL = "http://127.0.0.1:8000"


def test_get_product_by_id():

    response = requests.get(f"{BASE_URL}/products")

    assert response.status_code == 200

    products = response.json()

    assert len(products) > 0

    product_id = products[0]["ProductID"]

    response = requests.get(
        f"{BASE_URL}/products/{product_id}"
    )

    assert response.status_code == 200

    product = response.json()

    assert product["ProductID"] == product_id
    assert "ProductName" in product
    assert "Category" in product
    assert "Brand" in product
    assert "Price" in product
    assert "Stock" in product