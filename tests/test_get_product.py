import requests

BASE_URL = "http://127.0.0.1:8000"

def test_get_all_products():
    response = requests.get(f"{BASE_URL}/products")

    assert response.status_code == 200

    data = response.json()

    assert isinstance(data, list)

    assert len(data) > 0

    first_product = data[0]

    assert "ProductID" in first_product
    assert "ProductName" in first_product
    assert "Category" in first_product
    assert "Brand" in first_product
    assert "Price" in first_product
    assert "Stock" in first_product
    assert "Status" in first_product


    