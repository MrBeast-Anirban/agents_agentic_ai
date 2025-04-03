import json
import os
from datetime import datetime

class DataStorageTools:
    _storage_file = 'data_storage.json'

    @classmethod
    def _initialize_storage_file(cls):
        """Initialize the JSON storage file if it doesn't exist"""
        if not os.path.exists(cls._storage_file):
            with open(cls._storage_file, 'w') as f:
                json.dump([], f)

    @classmethod
    def _read_data(cls) -> list:
        """Read existing data from the JSON file"""
        cls._initialize_storage_file()
        with open(cls._storage_file, 'r') as f:
            return json.load(f)

    @classmethod
    def _write_data(cls, data: list):
        """Write data to the JSON file"""
        with open(cls._storage_file, 'w') as f:
            json.dump(data, f, indent=2)

    @classmethod
    def store_data(cls, data: dict) -> str:
        """Store input data in JSON format"""
        try:
            data['timestamp'] = datetime.now().isoformat()
            existing_data = cls._read_data()
            existing_data.append(data)
            cls._write_data(existing_data)
            return f"Data stored successfully in {cls._storage_file}"
        except Exception as e:
            return f"Error storing data: {str(e)}"

    @classmethod
    def search_data(cls, criteria: dict) -> list:
        """Search data based on criteria"""
        try:
            existing_data = cls._read_data()
            return [item for item in existing_data 
                   if all(item.get(k) == v for k, v in criteria.items())]
        except Exception as e:
            return [f"Error searching data: {str(e)}"]

    @classmethod
    def clear_all_data(cls) -> str:
        """Clear all data from the storage file"""
        try:
            cls._write_data([])  # Write empty list to file
            return "All data has been cleared from storage"
        except Exception as e:
            return f"Error clearing data: {str(e)}"