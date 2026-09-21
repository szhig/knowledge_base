from datetime import datetime

from sqlalchemy import BigInteger, ForeignKey, Integer, String, DateTime
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, IDMixin, TimestampMixin


class ShareLink(Base, IDMixin, TimestampMixin):
    __tablename__ = "share_links"

    token: Mapped[str] = mapped_column(String(64), unique=True, nullable=False)
    note_id: Mapped[int | None] = mapped_column(
        BigInteger, ForeignKey("notes.id", ondelete="CASCADE"), nullable=True
    )
    space_id: Mapped[int | None] = mapped_column(
        BigInteger, ForeignKey("spaces.id", ondelete="CASCADE"), nullable=True
    )
    created_by: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id"), nullable=False
    )
    expires_at: Mapped[datetime | None] = mapped_column(DateTime, nullable=True)
    view_count: Mapped[int] = mapped_column(Integer, default=0, nullable=False)
