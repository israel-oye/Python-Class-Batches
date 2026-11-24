import os

from dotenv import load_dotenv

load_dotenv()

SECRET_KEY = os.getenv("SECRET", os.urandom(32))
SQLALCHEMY_DATABASE_URI = os.getenv("DB_URI", "sqlite:///db.sqlite")
MAIL_FROM = os.getenv("MAIL_FROM")
MAIL_PASSWORD = os.getenv("MAIL_PASSWORD", 'password')