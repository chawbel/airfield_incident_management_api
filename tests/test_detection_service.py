from app.models.enums import IncidentStatus
from app.services.detection_service import process_detection
from app.schemas.detection_schema import DetectionCreate


def test_detection_create_incident(db):
    detection = DetectionCreate(camera_id=1, object_type="vehicle", confidence=0.95)

    result = process_detection(db, detection)

    assert "incident_id" in result
    assert result["status"] == IncidentStatus.OPEN
