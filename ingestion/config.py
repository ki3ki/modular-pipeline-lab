import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    ENVIRONMENTS = {
        "development": {
            "API_URL": "https://jsonplaceholder.typicode.com/posts",
            "TIMEOUT": 5,
            "RETRIES": 2
        },
        "testing": {
            "API_URL": "https://jsonplaceholder.typicode.com/comments",
            "TIMEOUT": 3,
            "RETRIES": 1
        },
        "production": {
            "API_URL": "https://jsonplaceholder.typicode.com/users",
            "TIMEOUT": 10,
            "RETRIES": 5
        }
    }

    CURRENT_ENV = os.getenv("ENVIRONMENT", "development")

    SETTINGS = ENVIRONMENTS.get(CURRENT_ENV)

    API_KEY = os.getenv("API_KEY")