from fastapi import FastAPI
from app.database import Base, engine
from app.models.product import Product
from app.routers import products
from app.models.user import User
from app.routers import auth

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ShopSphere API",
    description="Backend de la tienda online ShopSphere",
    version="1.0.0"
)

app.include_router(products.router)
app.include_router(auth.router)


@app.get("/")
def home():
    return {
        "message": "Bienvenido a ShopSphere API"
    }


@app.get("/health")
def health():
    return {
        "status": "ok"
    }