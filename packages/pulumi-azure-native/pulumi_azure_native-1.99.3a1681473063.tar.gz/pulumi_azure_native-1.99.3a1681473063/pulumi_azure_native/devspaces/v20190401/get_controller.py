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
    'GetControllerResult',
    'AwaitableGetControllerResult',
    'get_controller',
    'get_controller_output',
]

@pulumi.output_type
class GetControllerResult:
    def __init__(__self__, data_plane_fqdn=None, host_suffix=None, id=None, location=None, name=None, provisioning_state=None, sku=None, tags=None, target_container_host_api_server_fqdn=None, target_container_host_resource_id=None, type=None):
        if data_plane_fqdn and not isinstance(data_plane_fqdn, str):
            raise TypeError("Expected argument 'data_plane_fqdn' to be a str")
        pulumi.set(__self__, "data_plane_fqdn", data_plane_fqdn)
        if host_suffix and not isinstance(host_suffix, str):
            raise TypeError("Expected argument 'host_suffix' to be a str")
        pulumi.set(__self__, "host_suffix", host_suffix)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if target_container_host_api_server_fqdn and not isinstance(target_container_host_api_server_fqdn, str):
            raise TypeError("Expected argument 'target_container_host_api_server_fqdn' to be a str")
        pulumi.set(__self__, "target_container_host_api_server_fqdn", target_container_host_api_server_fqdn)
        if target_container_host_resource_id and not isinstance(target_container_host_resource_id, str):
            raise TypeError("Expected argument 'target_container_host_resource_id' to be a str")
        pulumi.set(__self__, "target_container_host_resource_id", target_container_host_resource_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataPlaneFqdn")
    def data_plane_fqdn(self) -> str:
        """
        DNS name for accessing DataPlane services
        """
        return pulumi.get(self, "data_plane_fqdn")

    @property
    @pulumi.getter(name="hostSuffix")
    def host_suffix(self) -> str:
        """
        DNS suffix for public endpoints running in the Azure Dev Spaces Controller.
        """
        return pulumi.get(self, "host_suffix")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Region where the Azure resource is located.
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the Azure Dev Spaces Controller.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        Model representing SKU for Azure Dev Spaces Controller.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Tags for the Azure resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetContainerHostApiServerFqdn")
    def target_container_host_api_server_fqdn(self) -> str:
        """
        DNS of the target container host's API server
        """
        return pulumi.get(self, "target_container_host_api_server_fqdn")

    @property
    @pulumi.getter(name="targetContainerHostResourceId")
    def target_container_host_resource_id(self) -> str:
        """
        Resource ID of the target container host
        """
        return pulumi.get(self, "target_container_host_resource_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetControllerResult(GetControllerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetControllerResult(
            data_plane_fqdn=self.data_plane_fqdn,
            host_suffix=self.host_suffix,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            tags=self.tags,
            target_container_host_api_server_fqdn=self.target_container_host_api_server_fqdn,
            target_container_host_resource_id=self.target_container_host_resource_id,
            type=self.type)


def get_controller(name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetControllerResult:
    """
    Gets the properties for an Azure Dev Spaces Controller.


    :param str name: Name of the resource.
    :param str resource_group_name: Resource group to which the resource belongs.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devspaces/v20190401:getController', __args__, opts=opts, typ=GetControllerResult).value

    return AwaitableGetControllerResult(
        data_plane_fqdn=__ret__.data_plane_fqdn,
        host_suffix=__ret__.host_suffix,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        tags=__ret__.tags,
        target_container_host_api_server_fqdn=__ret__.target_container_host_api_server_fqdn,
        target_container_host_resource_id=__ret__.target_container_host_resource_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_controller)
def get_controller_output(name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetControllerResult]:
    """
    Gets the properties for an Azure Dev Spaces Controller.


    :param str name: Name of the resource.
    :param str resource_group_name: Resource group to which the resource belongs.
    """
    ...
