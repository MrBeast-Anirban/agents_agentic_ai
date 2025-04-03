from crewai import Agent
from typing import Dict, Any
import json
import os
from datetime import datetime
from tools import DataStorageTools

from crewai import Agent

class DataStorageAgent(Agent):
    def __init__(self):
        super().__init__(
            role='Data Storage Specialist',
            goal='Store data in JSON format',
            backstory="""Specialized in data storage operations""",
            verbose=True,
            allow_delegation=False
        )
        # Disable LLM since we don't need it for basic storage
        self.llm = False

    def store_data(self, data):
        """Custom method to store data"""
        from tools import DataStorageTools
        return DataStorageTools.store_data(data)

    def search_data(self, criteria):
        """Custom method to search data"""
        from tools import DataStorageTools
        return DataStorageTools.search_data(criteria)

    def clear_data(self):
        """Clear all stored data"""
        from tools import DataStorageTools
        return DataStorageTools.clear_all_data()