from crewai import Task
from typing import Dict

def data_storage_task(agent, data: Dict[str, any]):
    return Task(
        description=f"Store the following data in JSON format: {data}",
        agent=agent,
        expected_output="Confirmation message that data was successfully stored",
        async_execution=False,
        tools=['store_data']
    )

def data_validation_task(agent, data: Dict[str, any]):
    return Task(
        description=f"Validate the structure and content of the following data: {data}",
        agent=agent,
        expected_output="Validation result message",
        async_execution=False,
        tools=['validate_data']
    )

def data_retrieval_task(agent, search_criteria: Dict[str, any]):
    return Task(
        description=f"Retrieve data matching the criteria: {search_criteria}",
        agent=agent,
        expected_output="List of matching data entries or 'No matches found' message",
        async_execution=False,
        tools=['search_data']
    )

def full_data_processing_task(agent, data: Dict[str, any]):
    return Task(
        description=f"""Process the following data through the complete pipeline:
        1. Validate the data structure
        2. Store the validated data
        3. Return confirmation and the stored data""",
        agent=agent,
        expected_output="Processing confirmation and the stored data",
        async_execution=False,
        tools=['validate_data', 'store_data', 'search_data']
    )