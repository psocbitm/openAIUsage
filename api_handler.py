import requests
from logger_config import logger

class APIHandler:
    @staticmethod
    def fetch_data(api_url, headers, params):
        try:
            response = requests.get(api_url, headers=headers, params=params)
            response.raise_for_status()  # Raise exception for HTTP errors
            return response.json()
        except requests.RequestException as e:
            logger.error(f"HTTP Request failed: {e}")
            return None
