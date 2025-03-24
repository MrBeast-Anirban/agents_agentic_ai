
from crewai import Task

class SetupAutoscalingTask:
    def __init__(
        self,
        template_name: str,
        group_name: str,
        base_instance_name: str,
        source_vm_name: str,
        source_image: str = "projects/debian-cloud/global/images/family/debian-11",
        target_cpu_utilization: float = 0.7,
        min_instances: int = 1,
        max_instances: int = 5,
    ):
        # Define the task description
        description = f"Set up an autoscaling policy for instance group '{group_name}' with CPU utilization threshold {target_cpu_utilization * 100}%, min instances {min_instances}, and max instances {max_instances}."

        # Initialize the Task with required fields
        self.task = Task(
            description=description
        )
        self.template_name = template_name
        self.group_name = group_name
        self.base_instance_name = base_instance_name
        self.source_vm_name = source_vm_name
        self.source_image = source_image
        self.target_cpu_utilization = target_cpu_utilization
        self.min_instances = min_instances
        self.max_instances = max_instances

    def execute(self, agent):
        """
        Execute the task using the provided agent.
        """
        # Step 1: Create instance template from existing VM
        agent.create_instance_template_from_existing_vm(
            template_name=self.template_name,
            source_vm_name=self.source_vm_name,
            source_image=self.source_image,
        )

        # Step 2: Create instance group
        agent.create_instance_group(
            group_name=self.group_name,
            template_name=self.template_name,
            base_instance_name=self.base_instance_name,
        )

        # Step 3: Set up autoscaling policy
        result = agent.create_autoscaling_policy(
            instance_group_name=self.group_name,
            target_cpu_utilization=self.target_cpu_utilization,
            min_instances=self.min_instances,
            max_instances=self.max_instances,
        )
        return result