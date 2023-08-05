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
    'GetContainerGroupResult',
    'AwaitableGetContainerGroupResult',
    'get_container_group',
    'get_container_group_output',
]

warnings.warn("""Version 2017-08-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetContainerGroupResult:
    """
    A container group.
    """
    def __init__(__self__, containers=None, id=None, image_registry_credentials=None, ip_address=None, location=None, name=None, os_type=None, provisioning_state=None, restart_policy=None, state=None, tags=None, type=None, volumes=None):
        if containers and not isinstance(containers, list):
            raise TypeError("Expected argument 'containers' to be a list")
        pulumi.set(__self__, "containers", containers)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if image_registry_credentials and not isinstance(image_registry_credentials, list):
            raise TypeError("Expected argument 'image_registry_credentials' to be a list")
        pulumi.set(__self__, "image_registry_credentials", image_registry_credentials)
        if ip_address and not isinstance(ip_address, dict):
            raise TypeError("Expected argument 'ip_address' to be a dict")
        pulumi.set(__self__, "ip_address", ip_address)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if restart_policy and not isinstance(restart_policy, str):
            raise TypeError("Expected argument 'restart_policy' to be a str")
        pulumi.set(__self__, "restart_policy", restart_policy)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volumes and not isinstance(volumes, list):
            raise TypeError("Expected argument 'volumes' to be a list")
        pulumi.set(__self__, "volumes", volumes)

    @property
    @pulumi.getter
    def containers(self) -> Sequence['outputs.ContainerResponse']:
        """
        The containers within the container group.
        """
        return pulumi.get(self, "containers")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="imageRegistryCredentials")
    def image_registry_credentials(self) -> Optional[Sequence['outputs.ImageRegistryCredentialResponse']]:
        """
        The image registry credentials by which the container group is created from.
        """
        return pulumi.get(self, "image_registry_credentials")

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional['outputs.IpAddressResponse']:
        """
        The IP address type of the container group.
        """
        return pulumi.get(self, "ip_address")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        """
        The operating system type required by the containers in the container group.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the container group. This only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="restartPolicy")
    def restart_policy(self) -> Optional[str]:
        """
        Restart policy for all containers within the container group. Currently the only available option is `always`.
        """
        return pulumi.get(self, "restart_policy")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The current state of the container group. This is only valid for the response.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def volumes(self) -> Optional[Sequence['outputs.VolumeResponse']]:
        """
        The list of volumes that can be mounted by containers in this container group.
        """
        return pulumi.get(self, "volumes")


class AwaitableGetContainerGroupResult(GetContainerGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetContainerGroupResult(
            containers=self.containers,
            id=self.id,
            image_registry_credentials=self.image_registry_credentials,
            ip_address=self.ip_address,
            location=self.location,
            name=self.name,
            os_type=self.os_type,
            provisioning_state=self.provisioning_state,
            restart_policy=self.restart_policy,
            state=self.state,
            tags=self.tags,
            type=self.type,
            volumes=self.volumes)


def get_container_group(container_group_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetContainerGroupResult:
    """
    Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.


    :param str container_group_name: The name of the container group.
    :param str resource_group_name: The name of the resource group that contains the container group.
    """
    pulumi.log.warn("""get_container_group is deprecated: Version 2017-08-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['containerGroupName'] = container_group_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerinstance/v20170801preview:getContainerGroup', __args__, opts=opts, typ=GetContainerGroupResult).value

    return AwaitableGetContainerGroupResult(
        containers=__ret__.containers,
        id=__ret__.id,
        image_registry_credentials=__ret__.image_registry_credentials,
        ip_address=__ret__.ip_address,
        location=__ret__.location,
        name=__ret__.name,
        os_type=__ret__.os_type,
        provisioning_state=__ret__.provisioning_state,
        restart_policy=__ret__.restart_policy,
        state=__ret__.state,
        tags=__ret__.tags,
        type=__ret__.type,
        volumes=__ret__.volumes)


@_utilities.lift_output_func(get_container_group)
def get_container_group_output(container_group_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetContainerGroupResult]:
    """
    Gets the properties of the specified container group in the specified subscription and resource group. The operation returns the properties of each container group including containers, image registry credentials, restart policy, IP address type, OS type, state, and volumes.


    :param str container_group_name: The name of the container group.
    :param str resource_group_name: The name of the resource group that contains the container group.
    """
    pulumi.log.warn("""get_container_group is deprecated: Version 2017-08-01-preview will be removed in v2 of the provider.""")
    ...
