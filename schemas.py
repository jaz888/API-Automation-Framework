from pydantic import BaseModel


class ProductCreate(BaseModel):
    ProductName: str
    Category: str
    Brand: str
    Price: float
    Stock: int
    Status: str


class ProductUpdate(ProductCreate):
    pass


class ProductResponse(ProductCreate):
    ProductID: int

    class Config:
        from_attributes = True