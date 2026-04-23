from app.models.enums import IncidentStatus
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.core.dependencies import get_db
from app.services.incident_service import update_incident_status
from app.schemas.incident_schema import IncidentResponse


router = APIRouter(prefix="/incidents", tags=["Incidents"])


@router.patch("/{incident_id}/status")
def update_status(
    incident_id: int, status: IncidentStatus, db: Session = Depends(get_db)
):
    try:
        incident = update_incident_status(db, incident_id, status)
        return IncidentResponse.model_validate(incident)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
