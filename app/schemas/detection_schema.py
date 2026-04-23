from pydantic import BaseModel
from app.models.enums import IncidentStatus


class DetectionCreate(BaseModel):
    camera_id: int
    object_type: str
    confidence: float


class DetectionResponse(BaseModel):
    detection_id: int
    camera_id: int
    object_type: str
    confidence: float
    incident_id: int
    status: IncidentStatus
