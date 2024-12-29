from config import Config
from logger_config import logger
from api_handler import APIHandler
from response_processor import ResponseProcessor

if __name__ == "__main__":
    headers = {
        "Authorization": f"Bearer {Config.AUTH_TOKEN}",
        "Content-Type": "application/json"
    }

    params = {
        "start_time": Config.START_TIME,
        "limit": Config.LIMIT
    }

    logger.info("Starting API request...")
    api_data = APIHandler.fetch_data(Config.API_URL, headers, params)

    if api_data:
        logger.info(f"Data received from API: {api_data}")
    
    logger.info("Processing API response...")
    ResponseProcessor.process(api_data)
    logger.info("Script execution completed.")