# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from . import outputs

__all__ = [
    'GetVirtualMachineResult',
    'AwaitableGetVirtualMachineResult',
    'get_virtual_machine',
    'get_virtual_machine_output',
]

@pulumi.output_type
class GetVirtualMachineResult:
    """
    A virtual machine.
    """
    def __init__(__self__, allow_claim=None, applicable_schedule=None, artifact_deployment_status=None, artifacts=None, compute_id=None, compute_vm=None, created_by_user=None, created_by_user_id=None, created_date=None, custom_image_id=None, data_disk_parameters=None, disallow_public_ip_address=None, environment_id=None, expiration_date=None, fqdn=None, gallery_image_reference=None, id=None, is_authentication_with_ssh_key=None, lab_subnet_name=None, lab_virtual_network_id=None, last_known_power_state=None, location=None, name=None, network_interface=None, notes=None, os_type=None, owner_object_id=None, owner_user_principal_name=None, password=None, plan_id=None, provisioning_state=None, schedule_parameters=None, size=None, ssh_key=None, storage_type=None, tags=None, type=None, unique_identifier=None, user_name=None, virtual_machine_creation_source=None):
        if allow_claim and not isinstance(allow_claim, bool):
            raise TypeError("Expected argument 'allow_claim' to be a bool")
        pulumi.set(__self__, "allow_claim", allow_claim)
        if applicable_schedule and not isinstance(applicable_schedule, dict):
            raise TypeError("Expected argument 'applicable_schedule' to be a dict")
        pulumi.set(__self__, "applicable_schedule", applicable_schedule)
        if artifact_deployment_status and not isinstance(artifact_deployment_status, dict):
            raise TypeError("Expected argument 'artifact_deployment_status' to be a dict")
        pulumi.set(__self__, "artifact_deployment_status", artifact_deployment_status)
        if artifacts and not isinstance(artifacts, list):
            raise TypeError("Expected argument 'artifacts' to be a list")
        pulumi.set(__self__, "artifacts", artifacts)
        if compute_id and not isinstance(compute_id, str):
            raise TypeError("Expected argument 'compute_id' to be a str")
        pulumi.set(__self__, "compute_id", compute_id)
        if compute_vm and not isinstance(compute_vm, dict):
            raise TypeError("Expected argument 'compute_vm' to be a dict")
        pulumi.set(__self__, "compute_vm", compute_vm)
        if created_by_user and not isinstance(created_by_user, str):
            raise TypeError("Expected argument 'created_by_user' to be a str")
        pulumi.set(__self__, "created_by_user", created_by_user)
        if created_by_user_id and not isinstance(created_by_user_id, str):
            raise TypeError("Expected argument 'created_by_user_id' to be a str")
        pulumi.set(__self__, "created_by_user_id", created_by_user_id)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if custom_image_id and not isinstance(custom_image_id, str):
            raise TypeError("Expected argument 'custom_image_id' to be a str")
        pulumi.set(__self__, "custom_image_id", custom_image_id)
        if data_disk_parameters and not isinstance(data_disk_parameters, list):
            raise TypeError("Expected argument 'data_disk_parameters' to be a list")
        pulumi.set(__self__, "data_disk_parameters", data_disk_parameters)
        if disallow_public_ip_address and not isinstance(disallow_public_ip_address, bool):
            raise TypeError("Expected argument 'disallow_public_ip_address' to be a bool")
        pulumi.set(__self__, "disallow_public_ip_address", disallow_public_ip_address)
        if environment_id and not isinstance(environment_id, str):
            raise TypeError("Expected argument 'environment_id' to be a str")
        pulumi.set(__self__, "environment_id", environment_id)
        if expiration_date and not isinstance(expiration_date, str):
            raise TypeError("Expected argument 'expiration_date' to be a str")
        pulumi.set(__self__, "expiration_date", expiration_date)
        if fqdn and not isinstance(fqdn, str):
            raise TypeError("Expected argument 'fqdn' to be a str")
        pulumi.set(__self__, "fqdn", fqdn)
        if gallery_image_reference and not isinstance(gallery_image_reference, dict):
            raise TypeError("Expected argument 'gallery_image_reference' to be a dict")
        pulumi.set(__self__, "gallery_image_reference", gallery_image_reference)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_authentication_with_ssh_key and not isinstance(is_authentication_with_ssh_key, bool):
            raise TypeError("Expected argument 'is_authentication_with_ssh_key' to be a bool")
        pulumi.set(__self__, "is_authentication_with_ssh_key", is_authentication_with_ssh_key)
        if lab_subnet_name and not isinstance(lab_subnet_name, str):
            raise TypeError("Expected argument 'lab_subnet_name' to be a str")
        pulumi.set(__self__, "lab_subnet_name", lab_subnet_name)
        if lab_virtual_network_id and not isinstance(lab_virtual_network_id, str):
            raise TypeError("Expected argument 'lab_virtual_network_id' to be a str")
        pulumi.set(__self__, "lab_virtual_network_id", lab_virtual_network_id)
        if last_known_power_state and not isinstance(last_known_power_state, str):
            raise TypeError("Expected argument 'last_known_power_state' to be a str")
        pulumi.set(__self__, "last_known_power_state", last_known_power_state)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_interface and not isinstance(network_interface, dict):
            raise TypeError("Expected argument 'network_interface' to be a dict")
        pulumi.set(__self__, "network_interface", network_interface)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if owner_object_id and not isinstance(owner_object_id, str):
            raise TypeError("Expected argument 'owner_object_id' to be a str")
        pulumi.set(__self__, "owner_object_id", owner_object_id)
        if owner_user_principal_name and not isinstance(owner_user_principal_name, str):
            raise TypeError("Expected argument 'owner_user_principal_name' to be a str")
        pulumi.set(__self__, "owner_user_principal_name", owner_user_principal_name)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if plan_id and not isinstance(plan_id, str):
            raise TypeError("Expected argument 'plan_id' to be a str")
        pulumi.set(__self__, "plan_id", plan_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if schedule_parameters and not isinstance(schedule_parameters, list):
            raise TypeError("Expected argument 'schedule_parameters' to be a list")
        pulumi.set(__self__, "schedule_parameters", schedule_parameters)
        if size and not isinstance(size, str):
            raise TypeError("Expected argument 'size' to be a str")
        pulumi.set(__self__, "size", size)
        if ssh_key and not isinstance(ssh_key, str):
            raise TypeError("Expected argument 'ssh_key' to be a str")
        pulumi.set(__self__, "ssh_key", ssh_key)
        if storage_type and not isinstance(storage_type, str):
            raise TypeError("Expected argument 'storage_type' to be a str")
        pulumi.set(__self__, "storage_type", storage_type)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_identifier and not isinstance(unique_identifier, str):
            raise TypeError("Expected argument 'unique_identifier' to be a str")
        pulumi.set(__self__, "unique_identifier", unique_identifier)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)
        if virtual_machine_creation_source and not isinstance(virtual_machine_creation_source, str):
            raise TypeError("Expected argument 'virtual_machine_creation_source' to be a str")
        pulumi.set(__self__, "virtual_machine_creation_source", virtual_machine_creation_source)

    @property
    @pulumi.getter(name="allowClaim")
    def allow_claim(self) -> Optional[bool]:
        """
        Indicates whether another user can take ownership of the virtual machine
        """
        return pulumi.get(self, "allow_claim")

    @property
    @pulumi.getter(name="applicableSchedule")
    def applicable_schedule(self) -> 'outputs.ApplicableScheduleResponse':
        """
        The applicable schedule for the virtual machine.
        """
        return pulumi.get(self, "applicable_schedule")

    @property
    @pulumi.getter(name="artifactDeploymentStatus")
    def artifact_deployment_status(self) -> 'outputs.ArtifactDeploymentStatusPropertiesResponse':
        """
        The artifact deployment status for the virtual machine.
        """
        return pulumi.get(self, "artifact_deployment_status")

    @property
    @pulumi.getter
    def artifacts(self) -> Optional[Sequence['outputs.ArtifactInstallPropertiesResponse']]:
        """
        The artifacts to be installed on the virtual machine.
        """
        return pulumi.get(self, "artifacts")

    @property
    @pulumi.getter(name="computeId")
    def compute_id(self) -> str:
        """
        The resource identifier (Microsoft.Compute) of the virtual machine.
        """
        return pulumi.get(self, "compute_id")

    @property
    @pulumi.getter(name="computeVm")
    def compute_vm(self) -> 'outputs.ComputeVmPropertiesResponse':
        """
        The compute virtual machine properties.
        """
        return pulumi.get(self, "compute_vm")

    @property
    @pulumi.getter(name="createdByUser")
    def created_by_user(self) -> str:
        """
        The email address of creator of the virtual machine.
        """
        return pulumi.get(self, "created_by_user")

    @property
    @pulumi.getter(name="createdByUserId")
    def created_by_user_id(self) -> str:
        """
        The object identifier of the creator of the virtual machine.
        """
        return pulumi.get(self, "created_by_user_id")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[str]:
        """
        The creation date of the virtual machine.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="customImageId")
    def custom_image_id(self) -> Optional[str]:
        """
        The custom image identifier of the virtual machine.
        """
        return pulumi.get(self, "custom_image_id")

    @property
    @pulumi.getter(name="dataDiskParameters")
    def data_disk_parameters(self) -> Optional[Sequence['outputs.DataDiskPropertiesResponse']]:
        """
        New or existing data disks to attach to the virtual machine after creation
        """
        return pulumi.get(self, "data_disk_parameters")

    @property
    @pulumi.getter(name="disallowPublicIpAddress")
    def disallow_public_ip_address(self) -> Optional[bool]:
        """
        Indicates whether the virtual machine is to be created without a public IP address.
        """
        return pulumi.get(self, "disallow_public_ip_address")

    @property
    @pulumi.getter(name="environmentId")
    def environment_id(self) -> Optional[str]:
        """
        The resource ID of the environment that contains this virtual machine, if any.
        """
        return pulumi.get(self, "environment_id")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[str]:
        """
        The expiration date for VM.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        The fully-qualified domain name of the virtual machine.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter(name="galleryImageReference")
    def gallery_image_reference(self) -> Optional['outputs.GalleryImageReferenceResponse']:
        """
        The Microsoft Azure Marketplace image reference of the virtual machine.
        """
        return pulumi.get(self, "gallery_image_reference")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAuthenticationWithSshKey")
    def is_authentication_with_ssh_key(self) -> Optional[bool]:
        """
        Indicates whether this virtual machine uses an SSH key for authentication.
        """
        return pulumi.get(self, "is_authentication_with_ssh_key")

    @property
    @pulumi.getter(name="labSubnetName")
    def lab_subnet_name(self) -> Optional[str]:
        """
        The lab subnet name of the virtual machine.
        """
        return pulumi.get(self, "lab_subnet_name")

    @property
    @pulumi.getter(name="labVirtualNetworkId")
    def lab_virtual_network_id(self) -> Optional[str]:
        """
        The lab virtual network identifier of the virtual machine.
        """
        return pulumi.get(self, "lab_virtual_network_id")

    @property
    @pulumi.getter(name="lastKnownPowerState")
    def last_known_power_state(self) -> str:
        """
        Last known compute power state captured in DTL
        """
        return pulumi.get(self, "last_known_power_state")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkInterface")
    def network_interface(self) -> Optional['outputs.NetworkInterfacePropertiesResponse']:
        """
        The network interface properties.
        """
        return pulumi.get(self, "network_interface")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        """
        The notes of the virtual machine.
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        """
        The OS type of the virtual machine.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="ownerObjectId")
    def owner_object_id(self) -> Optional[str]:
        """
        The object identifier of the owner of the virtual machine.
        """
        return pulumi.get(self, "owner_object_id")

    @property
    @pulumi.getter(name="ownerUserPrincipalName")
    def owner_user_principal_name(self) -> Optional[str]:
        """
        The user principal name of the virtual machine owner.
        """
        return pulumi.get(self, "owner_user_principal_name")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        The password of the virtual machine administrator.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="planId")
    def plan_id(self) -> Optional[str]:
        """
        The id of the plan associated with the virtual machine image
        """
        return pulumi.get(self, "plan_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scheduleParameters")
    def schedule_parameters(self) -> Optional[Sequence['outputs.ScheduleCreationParameterResponse']]:
        """
        Virtual Machine schedules to be created
        """
        return pulumi.get(self, "schedule_parameters")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        The size of the virtual machine.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="sshKey")
    def ssh_key(self) -> Optional[str]:
        """
        The SSH key of the virtual machine administrator.
        """
        return pulumi.get(self, "ssh_key")

    @property
    @pulumi.getter(name="storageType")
    def storage_type(self) -> Optional[str]:
        """
        Storage type to use for virtual machine (i.e. Standard, Premium).
        """
        return pulumi.get(self, "storage_type")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> str:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> Optional[str]:
        """
        The user name of the virtual machine.
        """
        return pulumi.get(self, "user_name")

    @property
    @pulumi.getter(name="virtualMachineCreationSource")
    def virtual_machine_creation_source(self) -> str:
        """
        Tells source of creation of lab virtual machine. Output property only.
        """
        return pulumi.get(self, "virtual_machine_creation_source")


class AwaitableGetVirtualMachineResult(GetVirtualMachineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualMachineResult(
            allow_claim=self.allow_claim,
            applicable_schedule=self.applicable_schedule,
            artifact_deployment_status=self.artifact_deployment_status,
            artifacts=self.artifacts,
            compute_id=self.compute_id,
            compute_vm=self.compute_vm,
            created_by_user=self.created_by_user,
            created_by_user_id=self.created_by_user_id,
            created_date=self.created_date,
            custom_image_id=self.custom_image_id,
            data_disk_parameters=self.data_disk_parameters,
            disallow_public_ip_address=self.disallow_public_ip_address,
            environment_id=self.environment_id,
            expiration_date=self.expiration_date,
            fqdn=self.fqdn,
            gallery_image_reference=self.gallery_image_reference,
            id=self.id,
            is_authentication_with_ssh_key=self.is_authentication_with_ssh_key,
            lab_subnet_name=self.lab_subnet_name,
            lab_virtual_network_id=self.lab_virtual_network_id,
            last_known_power_state=self.last_known_power_state,
            location=self.location,
            name=self.name,
            network_interface=self.network_interface,
            notes=self.notes,
            os_type=self.os_type,
            owner_object_id=self.owner_object_id,
            owner_user_principal_name=self.owner_user_principal_name,
            password=self.password,
            plan_id=self.plan_id,
            provisioning_state=self.provisioning_state,
            schedule_parameters=self.schedule_parameters,
            size=self.size,
            ssh_key=self.ssh_key,
            storage_type=self.storage_type,
            tags=self.tags,
            type=self.type,
            unique_identifier=self.unique_identifier,
            user_name=self.user_name,
            virtual_machine_creation_source=self.virtual_machine_creation_source)


def get_virtual_machine(expand: Optional[str] = None,
                        lab_name: Optional[str] = None,
                        name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualMachineResult:
    """
    Get virtual machine.


    :param str expand: Specify the $expand query. Example: 'properties($expand=artifacts,computeVm,networkInterface,applicableSchedule)'
    :param str lab_name: The name of the lab.
    :param str name: The name of the virtual machine.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['expand'] = expand
    __args__['labName'] = lab_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devtestlab/v20180915:getVirtualMachine', __args__, opts=opts, typ=GetVirtualMachineResult).value

    return AwaitableGetVirtualMachineResult(
        allow_claim=__ret__.allow_claim,
        applicable_schedule=__ret__.applicable_schedule,
        artifact_deployment_status=__ret__.artifact_deployment_status,
        artifacts=__ret__.artifacts,
        compute_id=__ret__.compute_id,
        compute_vm=__ret__.compute_vm,
        created_by_user=__ret__.created_by_user,
        created_by_user_id=__ret__.created_by_user_id,
        created_date=__ret__.created_date,
        custom_image_id=__ret__.custom_image_id,
        data_disk_parameters=__ret__.data_disk_parameters,
        disallow_public_ip_address=__ret__.disallow_public_ip_address,
        environment_id=__ret__.environment_id,
        expiration_date=__ret__.expiration_date,
        fqdn=__ret__.fqdn,
        gallery_image_reference=__ret__.gallery_image_reference,
        id=__ret__.id,
        is_authentication_with_ssh_key=__ret__.is_authentication_with_ssh_key,
        lab_subnet_name=__ret__.lab_subnet_name,
        lab_virtual_network_id=__ret__.lab_virtual_network_id,
        last_known_power_state=__ret__.last_known_power_state,
        location=__ret__.location,
        name=__ret__.name,
        network_interface=__ret__.network_interface,
        notes=__ret__.notes,
        os_type=__ret__.os_type,
        owner_object_id=__ret__.owner_object_id,
        owner_user_principal_name=__ret__.owner_user_principal_name,
        password=__ret__.password,
        plan_id=__ret__.plan_id,
        provisioning_state=__ret__.provisioning_state,
        schedule_parameters=__ret__.schedule_parameters,
        size=__ret__.size,
        ssh_key=__ret__.ssh_key,
        storage_type=__ret__.storage_type,
        tags=__ret__.tags,
        type=__ret__.type,
        unique_identifier=__ret__.unique_identifier,
        user_name=__ret__.user_name,
        virtual_machine_creation_source=__ret__.virtual_machine_creation_source)


@_utilities.lift_output_func(get_virtual_machine)
def get_virtual_machine_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                               lab_name: Optional[pulumi.Input[str]] = None,
                               name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualMachineResult]:
    """
    Get virtual machine.


    :param str expand: Specify the $expand query. Example: 'properties($expand=artifacts,computeVm,networkInterface,applicableSchedule)'
    :param str lab_name: The name of the lab.
    :param str name: The name of the virtual machine.
    :param str resource_group_name: The name of the resource group.
    """
    ...
