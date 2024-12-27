import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    LOCATION_API_URL = "https://ipinfo.io"
    LOCATION_API_KEY = os.getenv("LOCATION_API_KEY")
    WEATHER_API_URL = "https://api.openweathermap.org/data/2.5/weather"
    WEATHER_API_KEY = os.getenv("WEATHER_API_KEY")
    CACHE_EXPIRATION = 600  
    RATE_LIMIT = 5

config = Config()
