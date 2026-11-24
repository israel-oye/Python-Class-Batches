from datetime import datetime, timezone

# from hashlib import sha256
from uuid import UUID, uuid4

from flask_login import UserMixin
from sqlalchemy import Boolean, DateTime, Integer, String
from sqlalchemy import Uuid as SAEUuid
from sqlalchemy import func
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.security import check_password_hash, generate_password_hash

from db import db


class User(UserMixin, db.Model):
    uuid: Mapped[UUID] = mapped_column(SAEUuid, primary_key=True, default=uuid4)
    # username = Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    first_name = mapped_column(String(50), nullable=False)
    last_name = mapped_column(String(50), nullable=True)
    email: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(255))
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False)
    verified_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)
    created_at: Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(tz=timezone.utc))
    updated_at = mapped_column(
        DateTime,
        default=lambda: datetime.now(tz=timezone.utc),
        onupdate=lambda: datetime.now(tz=timezone.utc),
    )

    def __init__(
        self,
        first_name: str, 
        last_name: str, 
        email: str
        ):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        super().__init__()

    def set_password(self, plain_pwd: str):
        self.password = generate_password_hash(plain_pwd)

    def check_password(self, plain_txt: str):
        return check_password_hash(self.password, plain_txt)

    def get_id(self):
        return str(self.uuid)
