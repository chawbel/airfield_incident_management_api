from sqlalchemy.orm import Mapped, mapped_column
from app.core.database import Base


class Detection(Base):
    __tablename__ = "detections"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    camera_id: Mapped[int] = mapped_column()
    object_type: Mapped[str] = mapped_column()
    confidence: Mapped[float] = mapped_column()
