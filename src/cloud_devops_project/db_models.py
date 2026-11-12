from datetime import datetime, timezone

from sqlalchemy import DateTime, Enum, Integer, String
from sqlalchemy.orm import Mapped, mapped_column

from .database import Base
from .models import TaskStatus


class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(
	Integer,
	primary_key=True,
	index=True,
    )

    title: Mapped[str] = mapped_column(
	String(100),
	nullable=False,
    )

    description: Mapped[str] = mapped_column(
	String(500),
	default="",
    )

    status: Mapped[str] = mapped_column(
	Enum(TaskStatus, name="task_status"),
	default=TaskStatus.TODO,
	nullable=False,
    )

    created_at: Mapped[datetime] = mapped_column(
	DateTime(timezone=True),
	default=lambda: datetime.now(timezone.utc),
    )
