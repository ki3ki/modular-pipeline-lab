from config import Config


def validate_config():

    errors = []

    if not Config.SETTINGS:
        errors.append(
            f"Invalid environment '{Config.CURRENT_ENV}'. "
            "Use development/testing/production."
        )

    if not Config.API_KEY:
        errors.append(
            "Missing API_KEY in .env file."
        )

    if Config.SETTINGS:

        if not Config.SETTINGS["API_URL"]:
            errors.append(
                "API_URL is missing."
            )

        if Config.SETTINGS["TIMEOUT"] <= 0:
            errors.append(
                "TIMEOUT must be greater than 0."
            )

        if Config.SETTINGS["RETRIES"] < 0:
            errors.append(
                "RETRIES cannot be negative."
            )

    if errors:
        raise ValueError("\n".join(errors))