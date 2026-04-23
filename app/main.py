from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import BusinessException
from app.routers import detection_router, incident_router


app = FastAPI(title="Airfield Incident Management API")

app.include_router(detection_router.router)
app.include_router(incident_router.router)


@app.exception_handler(BusinessException)
def business_exception_handler(request: Request, exc: BusinessException):
    return JSONResponse(
        status_code=400,
        content={
            "error": "BUSINESS_RULE_VIOLATION",
            "message": exc.message,
        },
    )
