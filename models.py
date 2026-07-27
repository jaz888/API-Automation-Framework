from sqlalchemy import Column, Integer, String, DECIMAL
from database import Base


class Product(Base):
    __tablename__ = "products"


    ProductID = Column(Integer, primary_key=True, index=True)


    ProductName = Column(String(100), nullable=False)
    Category = Column(String(50), nullable=False)
    Brand = Column(String(50), nullable=False)
    Price = Column(DECIMAL(10, 2), nullable=False)
    Stock = Column(Integer, nullable=False)
    Status = Column(String(20), nullable=False)