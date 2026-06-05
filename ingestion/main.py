from validator import validate_config
from ingestion import extract_orders
from storage import save_data
from logger import logger


def main():

    try:

        logger.info(
            "Pipeline started"
        )

        validate_config()

        logger.info(
            "Configuration validated"
        )

        data = extract_orders()

        if not data:

            logger.error(
                "No data extracted"
            )

            return

        saved_file = save_data(data)

        if saved_file:

            logger.info(
                f"Pipeline completed "
                f"successfully. "
                f"File: {saved_file}"
            )

        else:

            logger.error(
                "Pipeline failed during storage"
            )

    except Exception as e:

        logger.exception(
            f"Pipeline failed: {e}"
        )


if __name__ == "__main__":
    main()