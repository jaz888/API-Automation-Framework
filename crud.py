from sqlalchemy.orm import Session
from fastapi import HTTPException

import models
import schemas


def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(
    ProductName=product.ProductName,
    Category=product.Category,
    Brand=product.Brand,
    Price=product.Price,
    Stock=product.Stock,
    Status=product.Status
)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product


def get_products(db: Session):
    return db.query(models.Product).all()


def get_product(db: Session, product_id: int):
    product = db.query(models.Product).filter(
        models.Product.ProductID == product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code=404,
            detail="Product not found."
        )

    return product



def update_product(
    db: Session,
    product_id: int,
    product: schemas.ProductUpdate
):
    db_product = db.query(models.Product).filter(
    models.Product.ProductID == product_id
).first()
    
    if db_product is None:

     raise HTTPException(
        status_code=404,
        detail="Product not found."
    )
    db_product.ProductName = product.ProductName
    db_product.Category = product.Category
    db_product.Brand = product.Brand
    db_product.Price = product.Price
    db_product.Stock = product.Stock
    db_product.Status = product.Status

    db.commit()
    db.refresh(db_product)
    return db_product


def delete_product(db:Session,product_id :int):
    db_product = db.query(models.Product).filter(
    models.Product.ProductID == product_id
).first()

    if db_product is None:
     raise HTTPException(
        status_code=404,
        detail="Product not found."
    )
    db.delete(db_product)
    db.commit()

