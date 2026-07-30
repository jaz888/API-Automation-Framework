from api import product_api
import logging

def test_create_product():
    product = {
        "ProductName": "Samsung Galaxy S21",
        "Category": "Mobile",
        "Brand": "Samsung",
        "Price": 800,
        "Stock": 20,
        "Status": "Available"
    
    }

    logging.info("========== Starting Create Product Test ==========")

    response = product_api.create_product(product)

    response_data = response.json()

    logging.info(f"Response status code: {response.status_code}")
    assert response.status_code == 201

    for key, value in product.items():
        assert response_data[key] == value

    required_fields = [
        "ProductID",
        "ProductName",
        "Category",
        "Brand",
        "Price",
        "Stock",
        "Status"
    ]
    for field in required_fields:
        assert field in response_data, f"Missing field: {field}"

    logging.info(f"Created product details: {response_data}")

        

    





