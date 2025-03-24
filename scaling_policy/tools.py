
from google.cloud import compute_v1
import os

class GCPInstanceTool:
    def __init__(self, project_id: str, zone: str):
        self.project_id = project_id
        self.zone = zone
        self.instance_template_client = compute_v1.InstanceTemplatesClient()
        self.instance_group_manager_client = compute_v1.InstanceGroupManagersClient()
        self.autoscaler_client = compute_v1.AutoscalersClient()
        self.instances_client = compute_v1.InstancesClient()

    def create_instance_template_from_existing_vm(
        self,
        template_name: str,
        source_vm_name: str,
        source_image: str = "projects/debian-cloud/global/images/family/debian-11",
    ):
        """
        Create an instance template from an existing VM.

        Args:
            template_name (str): Name of the instance template.
            source_vm_name (str): Name of the existing VM to use as a source.
            source_image (str): Source image for the boot disk (e.g., "projects/debian-cloud/global/images/family/debian-11").

        Returns:
            str: Name of the created instance template.
        """
        # Get the source VM
        source_vm = self.instances_client.get(
            project=self.project_id,
            zone=self.zone,
            instance=source_vm_name,
        )

        # Extract the machine type name from the URL
        machine_type_url = source_vm.machine_type
        machine_type_name = machine_type_url.split("/")[-1]

        # Define the disk configuration for the instance template
        disk = compute_v1.AttachedDisk(
            initialize_params=compute_v1.AttachedDiskInitializeParams(
                source_image=source_image
            ),
            auto_delete=True,
            boot=True,
        )

        # Define the instance template
        template = compute_v1.InstanceTemplate()
        template.name = template_name
        template.properties = compute_v1.InstanceProperties(
            machine_type=machine_type_name,  # Use the machine type name, not the URL
            disks=[disk],
            network_interfaces=[
                compute_v1.NetworkInterface(
                    name=source_vm.network_interfaces[0].name
                )
            ],
        )

        # Create the instance template
        operation = self.instance_template_client.insert(
            project=self.project_id,
            instance_template_resource=template,
        )
        return template_name

    def create_instance_group(
        self,
        group_name: str,
        template_name: str,
        base_instance_name: str,
        target_size: int = 1,
    ):
        """
        Create a managed instance group.

        Args:
            group_name (str): Name of the instance group.
            template_name (str): Name of the instance template.
            base_instance_name (str): Base name for instances in the group.
            target_size (int): Initial number of instances in the group.

        Returns:
            str: Name of the created instance group.
        """
        # Define the instance group manager
        instance_group_manager = compute_v1.InstanceGroupManager(
            name=group_name,
            base_instance_name=base_instance_name,
            instance_template=f"projects/{self.project_id}/global/instanceTemplates/{template_name}",
            target_size=target_size,
        )

        # Create the instance group
        operation = self.instance_group_manager_client.insert(
            project=self.project_id,
            zone=self.zone,
            instance_group_manager_resource=instance_group_manager,
        )
        return group_name

    def create_autoscaling_policy(
        self,
        instance_group_name: str,
        target_cpu_utilization: float = 0.7,
        min_instances: int = 1,
        max_instances: int = 5,
    ):
        """
        Create an autoscaling policy for a managed instance group.

        Args:
            instance_group_name (str): Name of the instance group.
            target_cpu_utilization (float): Target CPU utilization (e.g., 0.7 for 70%).
            min_instances (int): Minimum number of instances.
            max_instances (int): Maximum number of instances.

        Returns:
            str: Operation ID of the autoscaling policy creation process.
        """
        # Define the autoscaler
        autoscaler = compute_v1.Autoscaler(
            name=f"{instance_group_name}-autoscaler",
            target=f"projects/{self.project_id}/zones/{self.zone}/instanceGroupManagers/{instance_group_name}",
            autoscaling_policy=compute_v1.AutoscalingPolicy(
                cpu_utilization=compute_v1.AutoscalingPolicyCpuUtilization(
                    utilization_target=target_cpu_utilization
                ),
                min_num_replicas=min_instances,
                max_num_replicas=max_instances,
            ),
        )

        # Create the autoscaler
        operation = self.autoscaler_client.insert(
            project=self.project_id,
            zone=self.zone,
            autoscaler_resource=autoscaler,
        )

        # Wait for the operation to complete
        operation.result()

        return f"Autoscaling policy created. Operation ID: {operation.name}"