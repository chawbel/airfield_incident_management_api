from fastapi import APIRouter, Depends
from app.schemas.detection_schema import DetectionCreate
from app.services.detection_service import process_detection
from sqlalchemy.orm import Session
from app.core.dependencies import get_db


router = APIRouter(prefix="/detection", tags=["Detections"])


@router.post("/")
def create_detection(detection: DetectionCreate, db: Session = Depends(get_db)):
    return process_detection(db, detection)
