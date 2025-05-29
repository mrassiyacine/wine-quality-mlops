import os

import pandas as pd

from src.winequalitymlops import logger
from src.winequalitymlops.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        """
        Validates that all columns in the data match the schema.

        Returns:
            bool: True if all columns are valid, False otherwise.
        """
        try:
            logger.info("Validating all columns against the schema...")

            data = pd.read_csv(self.config.unzip_data)
            data_cols = set(data.columns)
            schema_cols = set(self.config.all_schema.keys())

            extra_cols = data_cols - schema_cols
            missing_cols = schema_cols - data_cols

            messages = []
            if extra_cols:
                for col in extra_cols:
                    logger.error(f"Column '{col}' is not in the schema.")
                    messages.append(f"Column '{col}' is not in the schema.")
            if missing_cols:
                for col in missing_cols:
                    logger.error(f"Schema column '{col}' is missing in the data.")
                    messages.append(f"Schema column '{col}' is missing in the data.")

            if messages:
                with open(self.config.STATUS_FILE, "w") as f:
                    for msg in messages:
                        f.write(msg + "\n")
                return False

            return True
        except Exception as e:
            logger.exception(f"An error occurred during column validation: {e}")
            with open(self.config.STATUS_FILE, "w") as f:
                f.write(f"Exception: {e}\n")
            return False
