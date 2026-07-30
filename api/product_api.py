from api.base_api import get, post, put, delete


def get_products():
    return get("/products")


def get_product_by_id(product_id):
    return get(f"/products/{product_id}")



def create_product(product):
    return post("/products", product)


def update_product(product_id, product):
    return put(
        f"/products/{product_id}",
        product
    )


def delete_product(product_id):
    return delete(f"/products/{product_id}")