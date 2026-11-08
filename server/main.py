"""Vercel looks for a module-level FastAPI `app`. The API lives in app/main.py."""
from app.main import app

__all__ = ["app"]
