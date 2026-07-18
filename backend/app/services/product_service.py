from sqlalchemy.orm import Session

from app.models.product import Product
from app.schemas.product import ProductCreate


def create_product(db: Session, product: ProductCreate):

    db_product = Product(
        name=product.name,
        description=product.description,
        price=product.price,
        stock=product.stock,
    )

    db.add(db_product)
    db.commit()
    db.refresh(db_product)

    return db_product

def get_products(
    db: Session,
    page: int = 1,
    limit: int = 10,
    search: str | None = None,
):

    query = db.query(Product)

    if search:
        query = query.filter(
            Product.name.ilike(f"%{search}%")
        )

    return (
        query
        .offset((page - 1) * limit)
        .limit(limit)
        .all()
    )
    
def get_product(db: Session, product_id: int):
    return db.query(Product).filter(Product.id == product_id).first()

def update_product(db: Session, product_id: int, product: ProductCreate):

    db_product = db.query(Product).filter(Product.id == product_id).first()

    if db_product is None:
        return None

    db_product.name = product.name
    db_product.description = product.description
    db_product.price = product.price
    db_product.stock = product.stock

    db.commit()
    db.refresh(db_product)

    return db_product

def delete_product(db: Session, product_id: int):

    db_product = db.query(Product).filter(Product.id == product_id).first()

    if db_product is None:
        return None

    db.delete(db_product)
    db.commit()

    return db_product