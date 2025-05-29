import os
import urllib.request as request
import zipfile

from src.winequalitymlops import logger
from src.winequalitymlops.entity.config_entity import DataIngestionConfig


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config

    def download_data(self):
        """
        Downloads the dataset from the specified URL if it does not already exist.
        """
        if not os.path.exists(self.config.local_data_file):
            filename, headers = request.urlretrieve(
                url=self.config.source_URL, filename=self.config.local_data_file
            )
            logger.info(f"Downloaded file: {filename} with headers: {headers}")
        else:
            logger.info(f"File already exists: {self.config.local_data_file}")

    def extract_zip_file(self):
        """
        Extracts the downloaded zip file to the specified directory if it does not already exist.
        """
        if not os.path.exists(self.config.unzip_dir):
            os.makedirs(self.config.unzip_dir, exist_ok=True)
        else:
            logger.info(f"Directory already exists: {self.config.unzip_dir}")

        with zipfile.ZipFile(self.config.local_data_file, "r") as zip_ref:
            zip_ref.extractall(self.config.unzip_dir)
        logger.info(f"Extracted files to: {self.config.unzip_dir}")
