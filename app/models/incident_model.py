from datetime import datetime
from sqlalchemy.sql import func
from typing import Optional
from sqlalchemy import ForeignKey, Enum as SAEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.core.database import Base
from app.models.enums import IncidentStatus


class Incident(Base):
    __tablename__ = "incidents"

    id: Mapped[int] = mapped_column(primary_key=True)

    detection_id: Mapped[int] = mapped_column(
        ForeignKey("detections.id"),
    )

    status: Mapped[IncidentStatus] = mapped_column(
        SAEnum(IncidentStatus),
        default=IncidentStatus.OPEN
    )

    priority: Mapped[str] = mapped_column(default="MEDIUM")

    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    resolved_at: Mapped[Optional[datetime]] = mapped_column()

    detection = relationship("Detection")
