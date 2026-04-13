from fastapi import FastAPI
from app.routers import detection_router

app = FastAPI(title="Airfield Incident Management API")
app.include_router(detection_router.router)
