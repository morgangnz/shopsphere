from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import ProductCreate
from app.models.product import Product

from app.services.product_service import (
    create_product as create_product_service,
    get_products,
    get_product,
    update_product,
    delete_product
)

from app.dependencies import get_current_user

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)

@router.post("/")
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user: str = Depends(get_current_user)
):
    return create_product_service(db, product)
    
@router.get("/")
def read_products(db: Session = Depends(get_db)):
    return get_products(db)

@router.get("/{product_id}")
def read_product(product_id: int, db: Session = Depends(get_db)):

    product = get_product(db, product_id)

    if product is None:
        return {
            "error": "Producto no encontrado"
        }

    return product

@router.put("/{product_id}")
def update(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db)
):

    updated = update_product(db, product_id, product)

    if updated is None:
        return {
            "error": "Producto no encontrado"
        }

    return updated

@router.delete("/{product_id}")
def delete(product_id: int, db: Session = Depends(get_db)):

    deleted = delete_product(db, product_id)

    if deleted is None:
        return {
            "error": "Producto no encontrado"
        }

    return {
        "message": "Producto eliminado correctamente"
    }