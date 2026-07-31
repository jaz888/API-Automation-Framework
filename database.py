from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import json
import os


Base = declarative_base()

DATABASE_URL = os.getenv("DATABASE_URL")

if DATABASE_URL is None:
    with open("config/config.json", "r") as file:
        config = json.load(file)

    DATABASE_URL = config["DATABASE_URL"]


# Create database engine
engine = create_engine(DATABASE_URL)

# Create session factory
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

import models
# Create all tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

import models

print("========== TABLES REGISTERED ==========")
print(Base.metadata.tables.keys())

Base.metadata.create_all(bind=engine)

print("========== TABLE CREATION COMPLETE ==========")