from pydantic import BaseModel


class OrderCreate(BaseModel):
    total: float


class OrderResponse(OrderCreate):
    id: int
    user_id: int
    status: str

    class Config:
        from_attributes = True