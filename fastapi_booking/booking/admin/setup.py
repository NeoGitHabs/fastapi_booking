from fastapi import FastAPI
from sqladmin import Admin
from booking.db.database import engine
from booking.admin.views import (UserProfileAdmin, CountryAdmin, HotelAdmin, RoomAdmin, BookingAdmin, ReviewAdmin)


def setup_admin(app: FastAPI):
    admin = Admin(app, engine)
    admin.add_view(UserProfileAdmin)
    admin.add_view(CountryAdmin)
    admin.add_view(HotelAdmin)
    admin.add_view(RoomAdmin)
    admin.add_view(BookingAdmin)
    admin.add_view(ReviewAdmin)