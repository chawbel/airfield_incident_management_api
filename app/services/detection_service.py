from app.schemas.detection_schema import DetectionCreate
from sqlalchemy.orm import Session
from app.repositories.detection_repository import create_detection
from app.repositories.incident_repository import create_incident


def process_detection(db: Session, detection: DetectionCreate):
    db_detection = create_detection(db, detection)

    incident = create_incident(db, db_detection.id)

    return {
        "detection_id": db_detection.id,
        "camera_id": db_detection.camera_id,
        "object_type": db_detection.object_type,
        "confidence": db_detection.confidence,
        "incident_id": incident.id,
        "status": incident.status,
    }
