import logging
from fastapi import FastAPI
from app.api.weather import router as weather_router
from fastapi import Request

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
logger = logging.getLogger(__name__)

app = FastAPI()

app.include_router(weather_router, prefix="/api/v1")

@app.get("/")
def root():
    logger.info("Root endpoint hit")
    return {"message": "Welcome to Weather API"}

@app.get("/health")
def health_check():
    logger.info("Health check endpoint hit")
    return {"status": "ok"}

@app.middleware("http")
async def log_requests(request: Request, call_next):
    logger.info(f"Request URL: {request.url}")
    response = await call_next(request)
    logger.info(f"Response Status: {response.status_code}")
    return response

@app.on_event("startup")
async def startup_event():
    logger.info("Application startup")
    routes = [route.path for route in app.routes]
    logger.info(f"Registered routes: {routes}")
