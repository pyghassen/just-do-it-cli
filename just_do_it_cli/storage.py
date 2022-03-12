"""The storage module contains the JsonStorage class."""
import json
from typing import Dict


class JsonStorage:
    """JSON storage class."""

    def __init__(self, file_path: str) -> None:
        """
        Json Storage constructor.

        Args:
        ----
            file_path (str): A string that contains the storage file path
                within the OS.
        """
        self.file_path = file_path

    def read(self) -> Dict:
        """
        Read the storage file content and return it as a dictionary.

        Returns
        -------
            A dictionary contains all the boards data with its tasks data too.
        """
        with open(self.file_path) as storage_file:
            return json.load(storage_file)

    def write(self, data: Dict) -> None:
        """
        Get a dictionary and save to the storage file.

        Args:
        ----
            data (dict): A dictionary contains all the boards data with its
                tasks data too.
        """
        with open(self.file_path, 'w') as storage_file:
            json.dump(data, storage_file, indent=4)
