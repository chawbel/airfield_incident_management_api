from fastapi import APIRouter
from app.schemas.detection_schema import DetectionCreate
from app.services.detection_service import process_detection


router = APIRouter(prefix="/detection", tags=["Detections"])


@router.post("/")
def create_detection(detection: DetectionCreate):
    result = process_detection(detection)
    return result
