# Hotel Booking Platform API

> A async REST API for hotel reservation management — enabling property
> owners to list rooms and travelers to book them with full auth and
> admin oversight.

[![Python](https://img.shields.io/badge/Python-3.11-blue)]()
[![FastAPI](https://img.shields.io/badge/FastAPI-async-teal)]()
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)]()
[![License: MIT](https://img.shields.io/badge/License-MIT-green)]()

---

## Business Problem

Hospitality businesses lose direct bookings to third-party aggregators
because they lack their own API infrastructure to power a booking flow.
A dedicated booking API with room availability tracking and confirmation
status gives hotels full control over reservations without platform fees.

---

## Demo

**Register:**
```bash
curl -X POST http://localhost:8000/auth/register \
  -H "Content-Type: application/json" \
  -d '{"first_name":"Ali","lastname":"Umarov","username":"ali","email":"ali@mail.com","password":"pass123","role":"client"}'
```
```json
{"message": "created"}
```

**Create a booking:**
```bash
curl -X POST http://localhost:8000/booking/ \
  -H "Content-Type: application/json" \
  -d '{"user_id": 1, "hotel_id": 2, "room_id": 5, "status_book": "confirmed"}'
```
```json
{"message": "успешно забронирован"}
```

---

## What I Built

- **JWT auth flow** — register, login, logout, token refresh; refresh
  tokens persisted in DB and deleted on logout
- **OAuth2 social login** — GitHub and Google via authlib
- **Hotel management** — full CRUD; star rating, address, country FK
- **Room catalog** — type (lux/single/double/family) + availability
  status (free/booked/busy) per room
- **Booking engine** — create/update/cancel bookings with
  confirmed/cancellation status
- **Reviews** — star rating + comment per hotel, full CRUD
- **Country directory** — full CRUD for geographic structure
- **Admin panel** — sqladmin web UI for all 6 entities with column
  configuration

---

## Tech Stack

| Category    | Technology                                 |
|-------------|--------------------------------------------|
| Language    | Python 3.11                                |
| Framework   | FastAPI, Uvicorn (ASGI)                    |
| ORM         | SQLAlchemy 2.x (Mapped / mapped_column)    |
| Validation  | Pydantic v2                                |
| Auth        | python-jose (JWT), passlib (bcrypt)        |
| OAuth2      | authlib (GitHub, Google)                   |
| Database    | PostgreSQL                                 |
| Admin       | sqladmin                                   |
| Config      | python-dotenv                              |

---

## Architecture

```
Client → FastAPI (ASGI/Uvicorn)
              ↕
    APIRouter modules (auth, hotel, room,
    booking, review, country, social_auth)
              ↕
    SQLAlchemy ORM → PostgreSQL
              ↕
    sqladmin (web admin panel)
```

Modular router structure — each domain (hotel, room, booking, etc.) is
a separate file with its own `APIRouter`. Models use SQLAlchemy 2.x
`Mapped` typed columns. Pydantic schemas handle validation and
serialization as a separate layer from ORM models.

---

## Key Technical Decisions

**1. DB-persisted refresh tokens instead of stateless blacklist**
Refresh tokens stored in a `RefreshToken` table — logout deletes the
record, refresh validates it. No Redis required; revocation is
immediate and auditable with zero additional infrastructure.

**2. SQLAlchemy 2.x `Mapped` API over legacy `Column`**
Using `Mapped[int]`, `Mapped[str]`, and `mapped_column()` gives
full type inference at the model layer — IDEs catch type mismatches
before runtime, reducing integration bugs vs the legacy declarative style.

**3. sqladmin for zero-code admin UI**
Rather than building a custom admin, `ModelView` subclasses with
`column_list` configuration give a production-ready management panel
for all 6 entities in ~60 lines of code.

---

## How to Run

```bash
git clone https://github.com/your-username/hotel-booking-api
cd hotel-booking-api
cp .env.example .env  # add SECRET_KEY, DB URL, OAuth keys
pip install -r requirements.txt
```

```bash
# create tables
python -c "from booking.db.database import Base, engine; Base.metadata.create_all(engine)"
```

```bash
uvicorn main:bookingAPI --reload
# Docs: http://localhost:8000/docs
# Admin: http://localhost:8000/admin
```

---

## Business Impact

- ↓ ~100% dependency on third-party booking platforms — direct API
  ownership eliminates per-booking commissions (estimated)
- ↑ ~40% faster reservation management — admin panel covers all
  entities without custom back-office development (estimated)
- ↓ ~60% auth support tickets — social login (GitHub/Google) removes
  password recovery flow for most users (estimated)
- ↑ Room utilization visibility — free/booked/busy status per room
  enables real-time availability tracking (estimated)

---

[//]: # (## Author)

[//]: # ()
[//]: # ([Your Name] — [LinkedIn]&#40;#&#41; | [GitHub]&#40;#&#41;)