from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas.category import CategoryCreate
from app.services.category_service import (
    get_categories,
    create_category
)
from app.dependencies import require_admin

router = APIRouter(
    prefix="/categories",
    tags=["Categories"]
)


@router.get("/")
def read_categories(
    db: Session = Depends(get_db)
):
    return get_categories(db)


@router.post("/")
def create(
    category: CategoryCreate,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    return create_category(db, category.name)