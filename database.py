from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
import json
import json

Base = declarative_base()

# Load database configuration
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

# Create all tables
Base.metadata.create_all(bind=engine)

# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()