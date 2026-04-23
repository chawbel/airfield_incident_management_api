from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from app.core.exceptions import BusinessException
from app.routers import detection_router, incident_router
from app.core.logging import logger

import time


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


@app.middleware("http")
async def log_requests(request: Request, call_next):
    start = time.time()

    logger.info(f"REQUEST START | {request.method} {request.url}")

    response = await call_next(request)

    duration = time.time() - start

    logger.info(
        f"RESQUEST END | {request.method} {request.url} "
        f"status={response.status_code} duration={duration:.3f}s"
    )

    return response
