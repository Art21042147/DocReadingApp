from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column

from backend.db.base import Base


class User(Base):
    username: Mapped[str] = mapped_column(unique=True, nullable=False)
    password: Mapped[str] = mapped_column(nullable=False)

    book: Mapped[list["Book"]] = relationship("Book", back_populates="user")

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, username={self.username})"


class Book(Base):
    title: Mapped[str] = mapped_column(unique=True, nullable=False)
    file_path: Mapped[str] = mapped_column(unique=True, nullable=False)

    user_id: Mapped[int] = mapped_column(ForeignKey("user.id"), nullable=False)

    user: Mapped["User"] = relationship("User", back_populates="book")

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id}, title={self.title})"
