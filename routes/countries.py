from fastapi.responses import ORJSONResponse

from fastapi import APIRouter

from celery_service.tasks.fetch_countries import fetch_countries_data

api_router = APIRouter()


@api_router.post("/country")
async def save_countries_data() -> ORJSONResponse:
    """
    Save countries data in Database

    Returns:
        ORJSONResponse: A dict with celery task id
    """
    task_result = fetch_countries_data.delay()

    return ORJSONResponse(
        status_code=200,
        content={"task_id": task_result.id}
    )
