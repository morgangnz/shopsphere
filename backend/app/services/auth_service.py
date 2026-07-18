from passlib.context import CryptContext
from sqlalchemy.orm import Session

from app.models.user import User
from app.schemas.user import UserCreate

from app.security import create_access_token

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


def register_user(db: Session, user: UserCreate):

    hashed_password = pwd_context.hash(user.password)

    db_user = User(
        username=user.username,
        email=user.email,
        password=hashed_password
    )

    db.add(db_user)
    db.commit()
    db.refresh(db_user)

    return db_user

def login_user(db: Session, username: str, password: str):

    user = db.query(User).filter(
        User.username == username
    ).first()

    if not user:
        return None

    if not pwd_context.verify(password, user.password):
        return None

    token = create_access_token(
        {"sub": user.username}
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }