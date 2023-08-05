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
    'GetIotDpsResourcePrivateEndpointConnectionResult',
    'AwaitableGetIotDpsResourcePrivateEndpointConnectionResult',
    'get_iot_dps_resource_private_endpoint_connection',
    'get_iot_dps_resource_private_endpoint_connection_output',
]

@pulumi.output_type
class GetIotDpsResourcePrivateEndpointConnectionResult:
    """
    The private endpoint connection of a provisioning service
    """
    def __init__(__self__, id=None, name=None, properties=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.PrivateEndpointConnectionPropertiesResponse':
        """
        The properties of a private endpoint connection
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIotDpsResourcePrivateEndpointConnectionResult(GetIotDpsResourcePrivateEndpointConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIotDpsResourcePrivateEndpointConnectionResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            system_data=self.system_data,
            type=self.type)


def get_iot_dps_resource_private_endpoint_connection(private_endpoint_connection_name: Optional[str] = None,
                                                     resource_group_name: Optional[str] = None,
                                                     resource_name: Optional[str] = None,
                                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIotDpsResourcePrivateEndpointConnectionResult:
    """
    Get private endpoint connection properties


    :param str private_endpoint_connection_name: The name of the private endpoint connection
    :param str resource_group_name: The name of the resource group that contains the provisioning service.
    :param str resource_name: The name of the provisioning service.
    """
    __args__ = dict()
    __args__['privateEndpointConnectionName'] = private_endpoint_connection_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devices/v20220205:getIotDpsResourcePrivateEndpointConnection', __args__, opts=opts, typ=GetIotDpsResourcePrivateEndpointConnectionResult).value

    return AwaitableGetIotDpsResourcePrivateEndpointConnectionResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_iot_dps_resource_private_endpoint_connection)
def get_iot_dps_resource_private_endpoint_connection_output(private_endpoint_connection_name: Optional[pulumi.Input[str]] = None,
                                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                                            resource_name: Optional[pulumi.Input[str]] = None,
                                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIotDpsResourcePrivateEndpointConnectionResult]:
    """
    Get private endpoint connection properties


    :param str private_endpoint_connection_name: The name of the private endpoint connection
    :param str resource_group_name: The name of the resource group that contains the provisioning service.
    :param str resource_name: The name of the provisioning service.
    """
    ...
