import requests
from logger import logger

API_URL = "https://dummyjson.com/carts"


def extract_orders():
    logger.info("Extracting orders from API")
    try:
        response = requests.get(API_URL, timeout=10)

        logger.info(f"Status Code: {response.status_code}")

        if response.status_code == 200:
            data = response.json()
            return data

        else:
            logger.error(f"API Error: {response.status_code}")
            return None

    except requests.exceptions.Timeout:
        logger.error("Request timed out")

    except requests.exceptions.ConnectionError:
        logger.error("Connection error occurred")

    except requests.exceptions.RequestException as e:
        logger.error(f"Unexpected error: {e}")

    return None


if __name__ == "__main__":
    orders = extract_orders()

    if orders:
        logger.info("Extraction successful")
        logger.info(f"Total carts fetched: {len(orders['carts'])}")

    else:
        logger.error("Extraction failed")




