
from agent import GCPAutoscalingAgent
from tasks import SetupAutoscalingTask


# Set up GCP credentials
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"

# Define agent and task
agent = GCPAutoscalingAgent(project_id="vcc-assignment-2-452011", zone="us-central1-a")
task = SetupAutoscalingTask(
    template_name="agent-instance-template",
    group_name="agent-instance-group",
    base_instance_name="agent-base-instance",
    source_vm_name="vm-by-agent",  # Replace with the name of your existing VM
    source_image="projects/debian-cloud/global/images/family/debian-11",
    target_cpu_utilization=0.7,  # 70% CPU utilization
    min_instances=1,
    max_instances=5,
)

# Execute the task
result = task.execute(agent)
print(result)