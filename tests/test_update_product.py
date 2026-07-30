from api import product_api
import logging



def test_update_product():

    product = {
        "ProductName": "iPhone 15",
        "Category": "Mobile",
        "Brand": "Apple",
        "Price": 1200,
        "Stock": 10,
        "Status": "Available"
    }
    logging.info("========== Starting Update Product Test ==========")

    product_id =  product_api.create_product(product).json()["ProductID"]


    response = product_api.update_product(product_id , product)

    logging.info(f"Response status code: {response.status_code}")

    assert response.status_code == 200

    updated_product = response.json()

    for key, value in product.items():
     assert updated_product[key] == value

    


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
        assert field in updated_product, f"Missing field: {field}"

        logging.info(f"updated product details: {updated_product}")


        

    
        
        



