from fastapi import FastAPI, Depends 
import schemas
import crud
from database import get_db
from sqlalchemy.orm import Session




app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to Products API"}



@app.get("/products", response_model=list[schemas.ProductResponse])
def get_products(
    db: Session = Depends(get_db)
):
    return crud.get_products(db)

@app.get("/products/{product_id}", response_model=schemas.ProductResponse)
def get_product(
    product_id: int,
    db: Session = Depends(get_db)
):
    return crud.get_product(
        db,
        product_id
    )

@app.post("/products", response_model=schemas.ProductResponse)
def create_product(
    product: schemas.ProductCreate,
    db: Session = Depends(get_db)
):
    return crud.create_product(db, product)


@app.put("/products/{product_id}", response_model=schemas.ProductResponse)
def update_product(
    product_id: int,
    product: schemas.ProductUpdate,
    db: Session = Depends(get_db)
):
    return crud.update_product(
        db,
        product_id,
        product
    )
    
    



@app.delete("/products/{product_id}")
def delete_product(
    product_id: int,
    db: Session = Depends(get_db)
):
     crud.delete_product(
        db,
        product_id
    )
     return {
         "message": "Product deleted successfully"
     }
