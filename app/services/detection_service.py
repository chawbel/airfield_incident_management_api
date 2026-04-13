from app.schemas.detection_schema import DetectionCreate


def process_detection(detection: DetectionCreate):
    return {
        "camera_id": detection.camera_id,
        "object_type": detection.object_type,
        "confidence": detection.confidence,
        "incident_created": True,
    }
