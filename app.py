import sentry_sdk
from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from config import SENTRY_DSN
from helpers.metadata import tags_metadata
from routes.countries import api_router

sentry_sdk.init(
    dsn=SENTRY_DSN,
    traces_sample_rate=0.5,
)

app = FastAPI(
    title="Pika Assignment",
    version="1.0.0",
    openapi_url="/openapi.json",
    docs_url="/docs/swagger",
    redoc_url="/docs/redoc",
    openapi_tags=tags_metadata,
)


@app.get("/ping", tags=["Health"])
async def health() -> ORJSONResponse:
    """
    Health Check
    """
    return ORJSONResponse(status_code=200, content={"message": "pong"})


app.include_router(api_router, prefix="/api/v1", tags=["Countries"])
