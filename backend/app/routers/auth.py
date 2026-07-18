from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas.user import UserCreate
from app.services.auth_service import register_user
from app.schemas.user import UserCreate, UserLogin
from app.services.auth_service import register_user, login_user

router = APIRouter(
    prefix="/auth",
    tags=["Authentication"]
)


@router.post("/register")
def register(user: UserCreate, db: Session = Depends(get_db)):
    return register_user(db, user)

@router.post("/login")
def login(user: UserLogin, db: Session = Depends(get_db)):

    token = login_user(
        db,
        user.username,
        user.password
    )

    if not token:
        return {
            "error": "Credenciales incorrectas"
        }

    return token