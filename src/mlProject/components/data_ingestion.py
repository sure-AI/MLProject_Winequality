import os
import urllib.request
import zipfile
from mlProject import logger
from mlProject.utils.common import get_size
from pathlib import Path
from mlProject.entity.config_entity import (DataIngestionConfig)


class DataIngestion:
    def __init__(self, config: DataIngestionConfig):
        self.config = config


    def download_file(self):
        try:
            # Check if the file already exists
            if not os.path.exists(self.config.local_data_file):
                # Attempt to download the file
                filename, headers = urllib.request.urlretrieve(
                    url=self.config.source_URL,
                    filename=self.config.local_data_file
                )
                logger.info(f"{filename} downloaded successfully! Info: \n{headers}")
            else:
                # Log that the file already exists and display its size
                file_size = get_size(Path(self.config.local_data_file))
                logger.info(f"File already exists with size: {file_size}")

        except Exception as e:
            # Handle exceptions (e.g., HTTP errors, file errors)
            print(f"An error occurred during file download: {str(e)}")
            logger.error(f"Error during download: {str(e)}")
            raise



    def extract_zip_file(self):
        """
        zip_file_path: str
        Extracts the zip file into the data directory
        Function returns None
        """
       
        unzip_path = self.config.unzip_dir

        os.makedirs(unzip_path, exist_ok=True)


        with zipfile.ZipFile(self.config.local_data_file, 'r') as zip_ref:
            zip_ref.extractall(unzip_path)

  
  