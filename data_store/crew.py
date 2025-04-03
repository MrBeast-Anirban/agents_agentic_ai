from crewai import Crew
from agents import DataStorageAgent

class DataStorageCrew:
    def __init__(self):
        self.storage_agent = DataStorageAgent()

    def store_data(self, data: dict):
        """Store data using the agent"""
        return self.storage_agent.store_data(data)

    def search_data(self, criteria: dict):
        """Search data using the agent"""
        return self.storage_agent.search_data(criteria)

    def clear_storage(self):
        """Clear all stored data"""
        return self.storage_agent.clear_data()