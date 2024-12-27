from httpx import AsyncClient, HTTPStatusError, RequestError
import logging
from app.config import config
import asyncio

logger = logging.getLogger(__name__)

async def get_location(ip: str = None):
    max_retries = 3
    delay = 2
    for attempt in range(max_retries):
        try:
            logger.info(f"Attempt {attempt+1} to fetch location for IP: {ip or 'default'}")
            async with AsyncClient(timeout=10) as client:
                url = f"{config.LOCATION_API_URL}/{ip}" if ip else config.LOCATION_API_URL
                params = {"token": config.LOCATION_API_KEY}
                logger.debug(f"Requesting {url} with params {params}")
                
                response = await client.get(url, params=params)
                response.raise_for_status()
                data = response.json()

                if 'city' in data and 'country' in data:
                    logger.info(f"Location found for {ip or 'default'}: {data['city']}, {data['country']}")
                    return {"city": data["city"], "country": data["country"]}
                else:
                    logger.warning(f"Incomplete location data for {ip or 'default'}")
                    raise ValueError("Incomplete location data")
        except (HTTPStatusError, RequestError) as e:
            status_code = e.response.status_code if isinstance(e, HTTPStatusError) else "N/A"
            logger.warning(f"Error (status {status_code}): {str(e)}")
            if attempt < max_retries - 1:
                await asyncio.sleep(delay)
            else:
                logger.error(f"Failed to fetch location for IP {ip or 'default'} after {max_retries} attempts.")
                return {"error": f"Failed to fetch location: {str(e)}"}

