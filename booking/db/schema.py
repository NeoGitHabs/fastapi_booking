from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional
from .models import ROLE_CHOICES, STATUS_CHOICES, TYPE_CHOICE, STATUS_BOOK_CHOICES


class UserProfileLoginSchema(BaseModel):
    username: str
    password: str

    class Config:
        from_attributes = True

class UserProfileSchema(BaseModel):
    id: int
    first_name: str
    lastname: str
    username: str
    email: EmailStr
    age: Optional[int] = None
    phone_number: Optional[str] = None
    password: str
    role: ROLE_CHOICES
    created_date: datetime

    class Config:
        from_attributes = True

# -------------------------------------------------------------------

class CountrySchema(BaseModel):
    id: int
    country_name: str

    class Config:
        from_attributes = True

# -------------------------------------------------------------------

class HotelCreateSchema(BaseModel):
    id: int
    hotel_name: str
    hotel_address: str
    hotel_description: str
    hotel_stars: int
    owner_id: Optional[int] = None
    country_id: Optional[int] = None

class HotelSchema(HotelCreateSchema):
    id: int

    class Config:
        from_attributes = True

# -------------------------------------------------------------------

class RoomSchema(BaseModel):
    id: int

    class Config:
        from_attributes = True

class RoomCreateSchema(BaseModel):
    hotel_id: int
    room_description: str
    room_status: STATUS_CHOICES
    room_type: TYPE_CHOICE

    class Config:
        from_attributes = True

# -------------------------------------------------------------------

class BookingSchema(BaseModel):
    id: int
    user_id: int
    hotel_id: int
    room_id: int
    created_date: datetime
    status_book: STATUS_BOOK_CHOICES

    class Config:
        from_attributes = True

class BookingCreateSchema(BaseModel):
    user_id: int
    hotel_id: int
    room_id: int
    status_book: STATUS_BOOK_CHOICES

    class Config:
        from_attributes = True

# -------------------------------------------------------------------

class ReviewCreateSchema(BaseModel):
    author_id: int
    product_id: int
    comment: str
    stars: int

    class Config:
        from_attributes = True

class ReviewGetSchema(BaseModel):
    id: int
    author_id: int
    product_id: int
    comment: str
    stars: int
    created_date: datetime

    class Config:
        from_attributes = True