

from pydantic import BaseModel

class UserCreate(BaseModel):
    username: str
    email: str

class ProductCreate(BaseModel):
    name: str
    price: float

class CartItemCreate(BaseModel):
    user_id: int
    product_id: int
    quantity: int
