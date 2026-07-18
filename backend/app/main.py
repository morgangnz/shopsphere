from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.database import Base, engine

from app.models.product import Product
from app.models.user import User
from app.models.category import Category

from app.routers import products
from app.routers import auth
from app.routers import categories
from app.models.order import Order
from app.routers import orders

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="ShopSphere API",
    description="Backend de la tienda online ShopSphere",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(products.router)
app.include_router(auth.router)
app.include_router(categories.router)
app.include_router(orders.router)


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