# TO-DOAPP

An AI Productivity Platform featuring Projects, Tasks, Habits, and Streaks.

## Project Structure

- **Backend**: FastAPI with SQLAlchemy, Alembic for migrations, and JWT Authentication.
- **Mobile**: Flutter application for iOS and Android.

## Backend Setup

1. `cd backend`
2. Create virtual environment and install dependencies: `python -m venv venv` and `pip install -r requirements.txt`
3. Set up the environment variables: Copy `.env.example` to `.env`.
4. Run migrations: `alembic upgrade head`
5. Run the server: `uvicorn app.main:app --reload`

## Mobile Setup

1. `cd mobile`
2. Run `flutter pub get`
3. Run the app: `flutter run`

## Docker Setup

You can run the entire backend stack (API + PostgreSQL) using Docker Compose:

```bash
docker-compose up --build
```
