import requests
import time

from logger import logger
from config import Config


def extract_orders():

    api_url = Config.SETTINGS["API_URL"]
    timeout = Config.SETTINGS["TIMEOUT"]
    max_retries = Config.SETTINGS["RETRIES"]

    logger.info(
        f"Extracting orders from {api_url}"
    )

    for attempt in range(max_retries):

        try:

            logger.info(
                f"Attempt {attempt + 1}/{max_retries}"
            )

            response = requests.get(
                api_url,
                timeout=timeout
            )

            logger.info(
                f"Status Code: {response.status_code}"
            )

            if response.status_code == 200:

                data = response.json()

                logger.info(
                    f"Successfully fetched "
                    f"{len(data['carts'])} carts"
                )

                return data

            elif response.status_code == 404:

                logger.error(
                    "API endpoint not found (404)"
                )

            elif response.status_code == 401:

                logger.error(
                    "Unauthorized access (401)"
                )

            elif response.status_code >= 500:

                logger.error(
                    f"Server error ({response.status_code})"
                )

            else:

                logger.error(
                    f"Unexpected status code "
                    f"{response.status_code}"
                )

        except requests.exceptions.Timeout:

            logger.error(
                f"Timeout on attempt {attempt + 1}"
            )

        except requests.exceptions.ConnectionError:

            logger.error(
                f"Connection error on attempt "
                f"{attempt + 1}"
            )

        except requests.exceptions.RequestException as e:

            logger.error(
                f"Request error: {e}"
            )

        if attempt < max_retries - 1:

            wait_time = 2 ** attempt

            logger.warning(
                f"Retrying in {wait_time} seconds..."
            )

            time.sleep(wait_time)

    logger.error(
        "All retry attempts failed"
    )

    return None