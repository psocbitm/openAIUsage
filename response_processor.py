from logger_config import logger
from config import Config

class ResponseProcessor:
    @staticmethod
    def process(data):
        if not data:
            logger.error("No data received from the API.")
            return

        try:
            # Validate 'data' list
            data_entries = data.get("data", [])
            if not data_entries:
                logger.error("The 'data' list in the response is empty.")
                return

            # Parse the first entry
            first_data_entry = data_entries[0]
            results = first_data_entry.get("results", [])

            if not results:
                logger.error("No results found in the response.")
                return

            # Parse amount value
            amount_value = results[0].get("amount", {}).get("value")

            if amount_value is None:
                logger.error("Amount value is missing in the response.")
                return

            # Check against the threshold
            if amount_value < Config.THRESHOLD:
                logger.warning(f"Alert: Amount value {amount_value} is below the threshold of {Config.THRESHOLD}!")
            else:
                logger.info(f"Amount value {amount_value} is above the threshold.")

        except (IndexError, KeyError, TypeError) as e:
            logger.error(f"A parsing error occurred: {e}")
        except Exception as e:
            logger.error(f"An unexpected error occurred while processing the response: {e}")
