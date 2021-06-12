import json
from typing import Dict


class JsonStorage:
    def __init__(self, file_path: str) -> None:
        self.file_path = file_path

    def read(self) -> Dict:
        with open(self.file_path) as storage_file:
            return json.load(storage_file)

    def write(self, data: Dict) -> None:
        with open(self.file_path, 'w') as storage_file:
            json.dump(data, storage_file, indent=4)
