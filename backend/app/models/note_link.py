from sqlalchemy import BigInteger, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, IDMixin


class NoteLink(Base, IDMixin):
    __tablename__ = "note_links"
    __table_args__ = (
        UniqueConstraint("source_note_id", "target_note_id", name="uq_note_link"),
    )

    source_note_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("notes.id", ondelete="CASCADE"), nullable=False
    )
    target_note_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("notes.id", ondelete="CASCADE"), nullable=False
    )
    link_text: Mapped[str] = mapped_column(String(200), nullable=False)
