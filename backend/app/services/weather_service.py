import httpx
import logging
from app.config import config

logger = logging.getLogger(__name__)

async def get_weather(city: str):
    try:
        logger.info(f"Fetching weather for city: {city}")
        async with httpx.AsyncClient() as client:
            response = await client.get(config.WEATHER_API_URL, params={"q": city, "appid": config.WEATHER_API_KEY, "units": "metric"})
            response.raise_for_status()
            data = response.json()

            if 'main' in data and 'weather' in data:
                logger.info(f"Weather data retrieved for {city}")
                return {
                    "temperature": data["main"]["temp"],
                    "humidity": data["main"]["humidity"],
                    "description": data["weather"][0]["description"]
                }
            else:
                logger.warning(f"Weather data missing for {city}")
                raise Exception("Weather data missing from the response")
    except Exception as e:
        logger.error(f"Failed to fetch weather for {city}: {str(e)}")
        return {"error": f"Failed to fetch weather: {str(e)}"}
