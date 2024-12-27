# Weather API Service

A FastAPI backend service for fetching weather data by IP address. Features include caching, rate-limiting, and modular architecture.

---

## Features
- Fetch weather details (temperature, humidity, description) for an IP address.
- Caching with Redis for faster responses.
- Rate limiting to prevent excessive requests.
- Error handling and logging.
- Modular, scalable codebase.

---

## Prerequisites
- Python 3.9+
- Redis
- Docker & Docker Compose (optional).

---

#### Setup Instructions

# Step 1: Clone the Repository

Clone the Repository
git clone <repository-url>
cd FastAPI_backendAPI/backend

# Step 2: Configure Environment Variables

Create a .env file in the backend directory with:
LOCATION_API_KEY=your_location_api_key
WEATHER_API_KEY=your_weather_api_key
REDIS_HOST=localhost
REDIS_PORT=6379

# Step 3: Install Dependencies

- Using Docker
    docker-compose up --build
    Access the app at: http://localhost:8000

- Without Docker

    pip install -r requirements.txt
    redis-server
    uvicorn app.main:app --host 0.0.0.0 --port 8000

###  API Endpoints

# 1. Root
- URL: /
- Method: GET
- Response: { "message": "Welcome to Weather API" }

# 2. Health Check

- URL: /health
- Method: GET
- Response: { "status": "ok" }

# 3. Weather by IP

- URL: /api/v1/weather-by-ip
- Method: GET
- Query: ip (optional; defaults to client IP).
- Response :
    {
        "ip": "123.123.123.123",
        "location": {
            "city": "Pune",
            "country": "India"
        },
        "weather": {
            "temperature": 30.5,
            "humidity": 60,
            "description": "clear sky"
        }
    }

# Testing

pytest tests/


# Project Structure

backend/
├── app/
│   ├── api/
│   │   └── weather.py          # API endpoints
│   ├── config.py               # Configuration settings
│   ├── main.py                 # Application entry point
│   ├── services/
│   │   ├── location_service.py # Handles geolocation API interactions
│   │   └── weather_service.py  # Handles weather API interactions
│   ├── utils/
│   │   ├── cache.py            # Redis caching logic
│   │   ├── rate_limiter.py     # Rate limiting logic
│   │   └── validators.py       # Input validation utilities
├── Dockerfile                  # Docker configuration
├── docker-compose.yml          # Docker Compose configuration
├── requirements.txt            # Python dependencies
└── tests/
    └── test_weather_api.py     # Unit tests for the API


### Deployment

## Using Docker
- docker-compose up --build

## Manual Deployment
- Set up Redis and Python dependencies, configure .env, and run:

- uvicorn app.main:app --host 0.0.0.0 --port 8000

## Monitoring & Logs
 - Use /health to check service status.
 - Logs are generated for debugging and analytics.

## Example Usage 

- Try these sample requests:
- http://127.0.0.1:8000/api/v1/weather-by-ip?ip=49.204.20.38
- Replace ip with any valid IP address for testing.

```bash