from app.schemas.detection_schema import DetectionCreate
from sqlalchemy.orm import Session
from app.repositories.detection_repository import create_detection
from app.repositories.incident_repository import create_incident
from app.core.logging import logger


def process_detection(db: Session, detection: DetectionCreate):
    logger.info(
        f"Detection received | camera={detection.camera_id} "
        f"type={detection.object_type} confidence={detection.confidence}"
    )

    db_detection = create_detection(db, detection)

    incident = create_incident(db, db_detection.id)

    logger.info(f"Incident created | id={incident.id} from detection={db_detection.id}")

    return {
        "detection_id": db_detection.id,
        "camera_id": db_detection.camera_id,
        "object_type": db_detection.object_type,
        "confidence": db_detection.confidence,
        "incident_id": incident.id,
        "status": incident.status,
    }
