# tasks.py
from crewai import Task

class CreateVMTask:
    def __init__(self, instance_name: str, machine_type: str, source_image: str, network: str = "global/networks/default"):
        # Define the task description
        description = f"Create a VM instance named '{instance_name}' with machine type '{machine_type}' and source image '{source_image}'."
        
        # Initialize the Task with required fields
        self.task = Task(
            description=description
        )
        self.instance_name = instance_name
        self.machine_type = machine_type
        self.source_image = source_image
        self.network = network

    def execute(self, agent):
        """
        Execute the task using the provided agent.
        """
        return agent.create_vm(
            instance_name=self.instance_name,
            machine_type=self.machine_type,
            source_image=self.source_image,
            network=self.network
        )