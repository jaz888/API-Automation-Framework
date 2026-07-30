import logging

from api import product_api


def test_get_all_products():
    logging.info("========== Starting GET All Products Test ==========")

    # Send request
    response = product_api.get_products()

    logging.info(f"Status Code: {response.status_code}")

    # Verify response
    assert response.status_code == 200

    # Convert JSON response
    data = response.json()

    logging.info(f"Total Products Returned: {len(data)}")

    # Validate response type
    assert isinstance(data, list)

    # Validate data exists
    assert len(data) > 0

    # Validate first product
    first_product = data[0]

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
        assert field in first_product, f"Missing field: {field}"

    logging.info("First Product Details")

    for key, value in first_product.items():
        logging.info(f"{key}: {value}")

    logging.info("========== GET All Products Test Passed ==========")