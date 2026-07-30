from api import product_api
import logging


def test_get_product_by_id():

    response = product_api.get_product_by_id(1)

   

    logging.info(f"Response status code: {response.status_code}")
    logging.info(f"Response data: {response.json()}")

    assert response.status_code == 200

    product = response.json()

    assert product["ProductID"] == 1

    product_fields = [
        "ProductID",
        "ProductName",
        "Category",
        "Brand",
        "Price",
        "Stock",
        "Status"
    ]

    for field in product_fields:
        assert field in product, f"Missing field: {field}"

    logging.info("Product Details:")
    for key, value in product.items():
        logging.info(f"{key}: {value}")



  