import requests
from ultralytics import YOLO

API_URL = "http://127.0.0.1:8000/detection/"

model = YOLO("yolov8n.pt")


def mapp_class_to_airport_object(cls_name: str) -> str | None:
    mapping = {
        "bird": "bird",
        "car": "vehicle",
        "truck": "vehicle",
        "bus": "vehicle",
        "bottle": "debris",
    }
    return mapping.get(cls_name)


def run_detection(image_path: str):
    results = model(image_path)

    for r in results:
        for box in r.boxes:
            cls_id = int(box.cls[0])
            cls_name = model.names[cls_id]
            confidence = float(box.conf[0])

            print(f"YOLO detected: {cls_name} ({confidence:.2f})")

            mapped = mapp_class_to_airport_object(cls_name)

            if mapped is None:
                continue

            yield {
                "object_type": mapped,
                "confidence": confidence,
            }


def send_to_backend(detection: dict):
    payload = {
        "camera_id": 1,
        "object_type": detection["object_type"],
        "confidence": detection["confidence"],
    }

    try:
        response = requests.post(API_URL, json=payload, timeout=5)

        print("STATUS:", response.status_code)
        print("RESPONSE:", response.json())

    except requests.exceptions.RequestException as e:
        print("ERROR sending to backend: ", e)


if __name__ == "__main__":
    image_path = "test2.jpeg"

    for detection in run_detection(image_path):
        print("DETECTED:", detection)
        send_to_backend(detection)
