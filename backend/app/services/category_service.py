from sqlalchemy.orm import Session
from app.models.category import Category


def get_categories(db: Session):
    return db.query(Category).all()


def create_category(db: Session, name: str):

    category = Category(name=name)

    db.add(category)
    db.commit()
    db.refresh(category)

    return category