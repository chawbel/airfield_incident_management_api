from sqlalchemy.orm import Session
from app.models.detection_model import Detection
from app.schemas.detection_schema import DetectionCreate


def create_detection(db: Session, detection: DetectionCreate):
    db_detection = Detection(
        camera_id=detection.camera_id,
        object_type=detection.object_type,
        confidence=detection.confidence,
    )

    db.add(db_detection)
    db.commit()
    db.refresh(db_detection)

    return db_detection
