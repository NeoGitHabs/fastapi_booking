from sqladmin import ModelView
from booking.db.models import (UserProfile, Country, Hotel, Room, Booking, Review, RefreshToken)


class UserProfileAdmin(ModelView, model=UserProfile):
    column_list = [
        UserProfile.id,
        UserProfile.first_name,
        UserProfile.lastname,
        UserProfile.username,
        UserProfile.email,
        UserProfile.role,
        UserProfile.phone_number,
        UserProfile.created_date
    ]

class CountryAdmin(ModelView, model=Country):
    column_list = [
        Country.id,
        Country.country_name,
        Country.user_id
    ]

class HotelAdmin(ModelView, model=Hotel):
    column_list = [
        Hotel.id,
        Hotel.hotel_name,
        Hotel.hotel_address,
        Hotel.hotel_stars,
        Hotel.owner_id,
        Hotel.country_id
    ]

class RoomAdmin(ModelView, model=Room):
    column_list = [
        Room.id,
        Room.hotel_id,
        Room.room_type,
        Room.room_status
    ]

class BookingAdmin(ModelView, model=Booking):
    column_list = [
        Booking.id,
        Booking.user_id,
        Booking.hotel_id,
        Booking.room_id,
        Booking.created_date,
        Booking.status_book
    ]

class ReviewAdmin(ModelView, model=Review):
    column_list = [
        Review.id,
        Review.author_id,
        Review.hotel_id,
        Review.rating,
        Review.comment,
        Review.created_date
    ]