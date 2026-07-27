import requests

BASE_URL = "http://127.0.0.1:8000"


def test_update_product():

    # Create product
    product = {
        "ProductName": "iPhone 16",
        "Category": "Mobile",
        "Brand": "Apple",
        "Price": 1500,
        "Stock": 12,
        "Status": "Available"
    }

    response = requests.post(
        f"{BASE_URL}/products",
        json=product
    )

    assert response.status_code == 200

    created_product = response.json()

    product_id = created_product["ProductID"]

    # Updated data
    updated_product = {
        "ProductName": "iPhone 17",
        "Category": "Mobile",
        "Brand": "Apple",
        "Price": 1800,
        "Stock": 25,
        "Status": "Available"
    }

    # Update product
    response = requests.put(
        f"{BASE_URL}/products/{product_id}",
        json=updated_product
    )

    assert response.status_code == 200

    updated_response = response.json()

    # Verify PUT response
    assert updated_response["ProductName"] == updated_product["ProductName"]
    assert updated_response["Category"] == updated_product["Category"]
    assert updated_response["Brand"] == updated_product["Brand"]
    assert updated_response["Price"] == updated_product["Price"]
    assert updated_response["Stock"] == updated_product["Stock"]
    assert updated_response["Status"] == updated_product["Status"]

    # Verify data from GET request
    response = requests.get(
        f"{BASE_URL}/products/{product_id}"
    )

    assert response.status_code == 200

    retrieved_product = response.json()

    assert retrieved_product["ProductName"] == updated_product["ProductName"]
    assert retrieved_product["Category"] == updated_product["Category"]
    assert retrieved_product["Brand"] == updated_product["Brand"]
    assert retrieved_product["Price"] == updated_product["Price"]
    assert retrieved_product["Stock"] == updated_product["Stock"]
    assert retrieved_product["Status"] == updated_product["Status"]

    # Cleanup
    response = requests.delete(
        f"{BASE_URL}/products/{product_id}"
    )

    assert response.status_code == 200

    # Verify product is deleted
    response = requests.get(
        f"{BASE_URL}/products/{product_id}"
    )

    assert response.status_code == 404