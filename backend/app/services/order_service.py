from sqlalchemy.orm import Session

from app.models.order import Order


def get_orders(db: Session):
    return db.query(Order).all()


def create_order(db: Session, user_id: int, total: float):

    order = Order(
        user_id=user_id,
        total=total
    )

    db.add(order)
    db.commit()
    db.refresh(order)

    return order