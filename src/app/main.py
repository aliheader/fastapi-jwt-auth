import uvicorn
from fastapi import FastAPI
from app.core.config import settings
from app.api import api_router


app = FastAPI(
    title=settings.PROJECT_NAME,
    docs_url="/docs",
    openapi_url=f"/openapi.json",
)


@api_router.get("/health", include_in_schema=True)
def healthcheck():
    """Check if API is up and running."""
    return {"status": "ok"}


app.include_router(api_router, prefix=settings.PREFIX)


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080, reload=True, workers=4)
