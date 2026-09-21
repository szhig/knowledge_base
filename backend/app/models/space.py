import enum

from sqlalchemy import BigInteger, Enum, ForeignKey, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from app.models.base import Base, IDMixin, TimestampMixin


class SpaceVisibility(str, enum.Enum):
    PRIVATE = "private"
    SHARED = "shared"
    PUBLIC = "public"


class SpaceRole(str, enum.Enum):
    OWNER = "owner"
    EDITOR = "editor"
    VIEWER = "viewer"


class Space(Base, IDMixin, TimestampMixin):
    __tablename__ = "spaces"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str | None] = mapped_column(Text, nullable=True)
    owner_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id"), nullable=False
    )
    visibility: Mapped[SpaceVisibility] = mapped_column(
        Enum(SpaceVisibility), default=SpaceVisibility.PRIVATE, nullable=False
    )


class SpaceMember(Base, IDMixin):
    __tablename__ = "space_members"

    space_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("spaces.id", ondelete="CASCADE"), nullable=False
    )
    user_id: Mapped[int] = mapped_column(
        BigInteger, ForeignKey("users.id", ondelete="CASCADE"), nullable=False
    )
    role: Mapped[SpaceRole] = mapped_column(
        Enum(SpaceRole), default=SpaceRole.VIEWER, nullable=False
    )
