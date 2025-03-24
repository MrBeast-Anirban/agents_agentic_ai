
from crewai import Agent
from tools import GCPVMTool

class GCPVMAgent:
    def __init__(self, project_id: str, zone: str):
        # Initialize the CrewAI Agent with required fields
        self.agent = Agent(
            role="GCP VM Creator",
            goal="Create virtual machines on Google Cloud Platform",
            backstory="You are an AI agent specialized in creating and managing virtual machines on GCP. You have deep knowledge of GCP's Compute Engine and can efficiently provision VMs based on user requirements."
        )
        self.project_id = project_id
        self.zone = zone
        self.tool = GCPVMTool(project_id=self.project_id, zone=self.zone)

    def create_vm(self, instance_name: str, machine_type: str, source_image: str, network: str = "global/networks/default"):
        """
        Delegate the VM creation task to the tool.
        """
        return self.tool.create_vm(
            instance_name=instance_name,
            machine_type=machine_type,
            source_image=source_image,
            network=network
        )