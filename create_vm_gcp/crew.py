
from agent import GCPVMAgent
from tasks import CreateVMTask

# Set up GCP credentials
import os
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "service_account.json"
# Define agent and task
agent = GCPVMAgent(project_id="vcc-assignment-2-452011", zone="us-central1-a")
task = CreateVMTask(
    instance_name="vm-by-agent",
    machine_type="e2-medium",
    source_image="projects/debian-cloud/global/images/family/debian-11"
)

# Execute the task
result = task.execute(agent)
print(result)