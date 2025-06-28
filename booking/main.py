from fastapi import FastAPI
import uvicorn
from booking.api import country, auth,social_auth,  booking, hotel, review, room
from booking.admin.setup import setup_admin
from starlette.middleware.sessions import SessionMiddleware
from booking.db.config import SECRET_KEY


bookingAPI = FastAPI()

bookingAPI.include_router(country.country_router)
bookingAPI.include_router(hotel.hotel_router)
bookingAPI.include_router(auth.auth_router)
bookingAPI.include_router(review.review_router)
bookingAPI.include_router(room.room_router)
bookingAPI.include_router(booking.booking_router)
bookingAPI.include_router(social_auth.social_router)
bookingAPI.add_middleware(SessionMiddleware, secret_key=SECRET_KEY)
setup_admin(bookingAPI)

if __name__ == '__main__':
    uvicorn.run(bookingAPI, host='127.0.0.1', port=8000)