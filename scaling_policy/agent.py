
from crewai import Agent
from tools import GCPInstanceTool

class GCPAutoscalingAgent:
    def __init__(self, project_id: str, zone: str):
        # Initialize the CrewAI Agent with required fields
        self.agent = Agent(
            role="GCP Autoscaling Manager",
            goal="Set up autoscaling policies for virtual machines on Google Cloud Platform",
            backstory="You are an AI agent specialized in managing autoscaling policies for GCP Compute Engine. You ensure that VM instances scale efficiently based on workload demands."
        )
        self.project_id = project_id
        self.zone = zone
        self.tool = GCPInstanceTool(project_id=self.project_id, zone=self.zone)

    def create_instance_template_from_existing_vm(self, template_name: str, source_vm_name: str, source_image: str):
        """
        Delegate the instance template creation task to the tool.
        """
        return self.tool.create_instance_template_from_existing_vm(
            template_name=template_name,
            source_vm_name=source_vm_name,
            source_image=source_image,
        )

    def create_instance_group(self, group_name: str, template_name: str, base_instance_name: str, **kwargs):
        """
        Delegate the instance group creation task to the tool.
        """
        return self.tool.create_instance_group(
            group_name=group_name,
            template_name=template_name,
            base_instance_name=base_instance_name,
            **kwargs
        )

    def create_autoscaling_policy(self, instance_group_name: str, **kwargs):
        """
        Delegate the autoscaling setup task to the tool.
        """
        return self.tool.create_autoscaling_policy(
            instance_group_name=instance_group_name,
            **kwargs
        )