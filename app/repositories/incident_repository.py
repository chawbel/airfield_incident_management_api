from app.models.incident_model import Incident
from sqlalchemy.orm import Session


def create_incident(db: Session, detection_id: int) -> Incident:
    incident = Incident(detection_id=detection_id)

    db.add(incident)
    db.commit()
    db.refresh(incident)

    return incident


def get_incident(db: Session, incident_id: int) -> Incident | None:
    return db.get(Incident, incident_id)


def update_incident(db: Session, incident: Incident) -> Incident:
    db.commit()
    db.refresh(incident)
    return incident
