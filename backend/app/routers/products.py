from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.product import ProductCreate
from app.dependencies import require_admin

from app.services.product_service import (
    create_product as create_product_service,
    get_products,
    get_product,
    update_product,
    delete_product
)

router = APIRouter(
    prefix="/products",
    tags=["Products"]
)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED
)
def create_product(
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return create_product_service(db, product)


@router.get("/")
def read_products(
    db: Session = Depends(get_db)
):
    return get_products(db)


@router.get("/{product_id}")
def read_product(
    product_id: int,
    db: Session = Depends(get_db)
):

    product = get_product(db, product_id)

    if product is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return product


@router.put("/{product_id}")
def update_product_endpoint(
    product_id: int,
    product: ProductCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):

    updated = update_product(db, product_id, product)

    if updated is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return updated


@router.delete(
    "/{product_id}",
    status_code=status.HTTP_204_NO_CONTENT
)
def delete_product_endpoint(
    product_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):

    deleted = delete_product(db, product_id)

    if deleted is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Producto no encontrado"
        )

    return