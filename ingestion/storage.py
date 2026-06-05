import json
import os

from datetime import datetime
from logger import logger

os.makedirs("data", exist_ok=True)


def save_data(data):

    try:

        timestamp = datetime.now().strftime(
            "%Y%m%d_%H%M%S"
        )

        final_file = (
            f"data/carts_{timestamp}.json"
        )

        temp_file = (
            f"{final_file}.tmp"
        )

        payload = {

            "metadata": {

                "extraction_time":
                    datetime.now().isoformat(),

                "record_count":
                    len(data["carts"])
            },

            "data": data["carts"]
        }

        with open(
            temp_file,
            "w",
            encoding="utf-8"
        ) as file:

            json.dump(
                payload,
                file,
                indent=4
            )

        os.replace(
            temp_file,
            final_file
        )

        logger.info(
            f"Data saved successfully: "
            f"{final_file}"
        )

        return final_file

    except IOError as e:

        logger.error(
            f"Storage failed: {e}"
        )

        return None