import os
from dotenv import load_dotenv

load_dotenv()


class Config:

    ENVIRONMENTS = {

        "development": {
            "API_URL": "https://dummyjson.com/carts",
            "TIMEOUT": 5,
            "RETRIES": 2,
            "OUTPUT_FORMAT": "json"
        },

        "testing": {
            "API_URL": "https://dummyjson.com/carts",
            "TIMEOUT": 3,
            "RETRIES": 1,
            "OUTPUT_FORMAT": "json"
        },

        "production": {
            "API_URL": "https://dummyjson.com/carts",
            "TIMEOUT": 10,
            "RETRIES": 5,
            "OUTPUT_FORMAT": "json"
        }
    }

    CURRENT_ENV = os.getenv(
        "ENVIRONMENT",
        "development"
    )

    SETTINGS = ENVIRONMENTS.get(
        CURRENT_ENV
    )

    API_KEY = os.getenv(
        "API_KEY"
    )