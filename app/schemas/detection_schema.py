from pydantic import BaseModel


class DetectionCreate(BaseModel):
    camera_id: int
    object_type: str
    confidence: float
