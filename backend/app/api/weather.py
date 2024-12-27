from fastapi import APIRouter, HTTPException, Query
from app.services.location_service import get_location
from app.services.weather_service import get_weather
from app.utils.validators import validate_ip
import logging

logger = logging.getLogger(__name__)

router = APIRouter()

@router.get("/weather-by-ip")
async def weather_by_ip(ip: str = Query(..., description="The IP address to fetch weather for")):
    logger.info(f"Received request for weather by IP: {ip}")

    if not validate_ip(ip):
        logger.warning(f"Invalid IP format: {ip}")
        raise HTTPException(status_code=400, detail="Invalid IP address format")

    location = await get_location(ip)
    if "error" in location:
        logger.error(f"Error in fetching location for {ip}: {location['error']}")
        raise HTTPException(status_code=502, detail=location["error"])

    city = location.get("city", "Unknown")
    weather = await get_weather(city)
    if "error" in weather:
        logger.error(f"Error in fetching weather for {city}: {weather['error']}")
        raise HTTPException(status_code=502, detail=weather["error"])

    logger.info(f"Weather data for {city}: {weather}")
    return {
        "ip": ip,
        "location": location,
        "weather": weather
    }
