import pytest
from app.services.incident_service import update_incident_status
from app.services.detection_service import process_detection
from app.schemas.detection_schema import DetectionCreate
from app.models.enums import IncidentStatus
from app.core.exceptions import BusinessException


def create_incident_via_detection(db):
    detection = DetectionCreate(camera_id=1, object_type="bird", confidence=0.0)
    result = process_detection(db, detection)
    return result["incident_id"]


def test_valid_transition_open_to_investigation(db):
    incident_id = create_incident_via_detection(db)

    incident = update_incident_status(db, incident_id, IncidentStatus.INVESTIGATING)

    assert incident.status == IncidentStatus.INVESTIGATING


def test_valid_transition_to_resolved(db):
    incident_id = create_incident_via_detection(db)

    update_incident_status(db, incident_id, IncidentStatus.INVESTIGATING)
    incident = update_incident_status(db, incident_id, IncidentStatus.RESOLVED)

    assert incident.status == IncidentStatus.RESOLVED
    assert incident.resolved_at is not None


def test_invalid_transition_skip_state(db):
    incident_id = create_incident_via_detection(db)

    update_incident_status(db, incident_id, IncidentStatus.INVESTIGATING)
    update_incident_status(db, incident_id, IncidentStatus.RESOLVED)

    with pytest.raises(BusinessException):
        update_incident_status(db, incident_id, IncidentStatus.INVESTIGATING)


def test_invalid_same_state_transition(db):
    incident_id = create_incident_via_detection(db)

    with pytest.raises(BusinessException):
        update_incident_status(db, incident_id, IncidentStatus.OPEN)
