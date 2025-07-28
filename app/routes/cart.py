from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import schemas, models, database

router = APIRouter()

def get_db():
    db = database.SessionLocal()
    try:
        yield db
    finally:
         db.close()

@router.post("/cart/{user_id}", response_model=schemas.CartItemResponse)
def add_to_cart(user_id: str, item: schemas.CartItemCreate, db: Session = Depends(get_db)):
    db_item = models.CartItem(user_id=user_id, item_name=item.item_name, quantity=item.quantity)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/cart/{user_id}", response_model=list[schemas.CartItemResponse])
def get_cart_items(user_id: str, db: Session = Depends(get_db)):
    return db.query(models.CartItem).filter(models.CartItem.user_id == user_id).all()

@router.put("/cart/{item_id}", response_model=schemas.CartItemResponse)
def update_cart_item(item_id: int, item: schemas.CartItemUpdate, db: Session = Depends(get_db)):
    db_item = db.query(models.CartItem).filter(models.CartItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db_item.item_name = item.item_name
    db_item.quantity = item.quantity
    db.commit()
    db.refresh(db_item)
    return db_item

@router.delete("/cart/{item_id}")
def delete_cart_item(item_id: int, db: Session = Depends(get_db)):
    db_item = db.query(models.CartItem).filter(models.CartItem.id == item_id).first()
    if not db_item:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(db_item)
    db.commit()
    return {"message": "Item deleted"}
