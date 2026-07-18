from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.order import OrderCreate
from app.services.order_service import (
    get_orders,
    create_order
)
from app.dependencies import get_current_user

router = APIRouter(
    prefix="/orders",
    tags=["Orders"]
)


@router.get("/")
def read_orders(
    db: Session = Depends(get_db)
):
    return get_orders(db)


@router.post("/")
def create(
    order: OrderCreate,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user)
):
    return create_order(
        db,
        user_id=1,  # Lo mejoraremos después
        total=order.total
    )