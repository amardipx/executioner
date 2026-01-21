from sqlalchemy import String, Integer
from sqlalchemy.orm import Mapped, mapped_column
from app.db.pool import Base


class User(Base):
    __tablename__ = "users"

    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(50), unique=True, index=True)
    password_hash: Mapped[str] = mapped_column(String(255))
    rating: Mapped[int] = mapped_column(Integer, default=1200)
