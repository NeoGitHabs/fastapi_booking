from fastapi import Depends, HTTPException, APIRouter
from booking.db.models import Booking
from booking.db.schema import BookingSchema, BookingCreateSchema
from booking.db.database import SessionLocal
from typing import List
from sqlalchemy.orm import Session


booking_router = APIRouter(prefix='/booking', tags=['Booking'])

async def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@booking_router.post('/', response_model=dict)
async def booking_create(booking: BookingCreateSchema, db: Session = Depends(get_db)):
    db_booking = Booking(**booking.dict())
    db.add(db_booking)
    db.commit()
    db.refresh(db_booking)
    return {'message': 'успешно забронирован'}

@booking_router.get('/', response_model=List[BookingSchema])
async def booking_list(db: Session = Depends(get_db)):
    return db.query(Booking).all()

@booking_router.put('/{booking_id}/', response_model=dict)
async def booking_update(booking_id: int, booking: BookingCreateSchema, db: Session = Depends(get_db)):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    for key, value in booking.dict().items():
        setattr(db_booking, key, value)
    db.commit()
    db.refresh(db_booking)
    return {"message": "Updated"}

@booking_router.delete('/{booking_id}/', response_model=dict)
async def booking_delete(booking_id: int, db: Session = Depends(get_db)):
    db_booking = db.query(Booking).filter(Booking.id == booking_id).first()
    if not db_booking:
        raise HTTPException(status_code=404, detail="Booking not found")
    db.delete(db_booking)
    db.commit()
    return {"message": "Deleted"}