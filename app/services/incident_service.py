from datetime import datetime, timezone
from sqlalchemy.orm import Session
from app.repositories.incident_repository import get_incident, update_incident
from app.models.enums import IncidentStatus
from app.core.exceptions import BusinessException


VALID_TRANSITIONS = {
    IncidentStatus.OPEN: IncidentStatus.INVESTIGATING,
    IncidentStatus.INVESTIGATING: IncidentStatus.RESOLVED,
}


def update_incident_status(db: Session, incident_id: int, new_status: IncidentStatus):
    incident = get_incident(db, incident_id)

    if not incident:
        raise BusinessException("Incident not found")

    current_status = incident.status

    if current_status == IncidentStatus.RESOLVED:
        raise BusinessException("Incident already resolved")

    if VALID_TRANSITIONS.get(current_status) != new_status:
        raise BusinessException(
            f"Invalid transition from {current_status} to {new_status}"
        )

    incident.status = new_status

    if new_status == IncidentStatus.RESOLVED:
        incident.resolved_at = datetime.now(timezone.utc)

    return update_incident(db, incident)
