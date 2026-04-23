from pydantic import BaseModel
from app.models.enums import IncidentStatus
from datetime import datetime


class IncidentResponse(BaseModel):
    id: int
    detection_id: int
    status: IncidentStatus
    created_at: datetime
    resolved_at: datetime | None

    class Config:
        from_attributes = True
