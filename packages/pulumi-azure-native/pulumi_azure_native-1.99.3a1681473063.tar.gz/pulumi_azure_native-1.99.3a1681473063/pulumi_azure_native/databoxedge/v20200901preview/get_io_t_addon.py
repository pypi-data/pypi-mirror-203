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
    'GetIoTAddonResult',
    'AwaitableGetIoTAddonResult',
    'get_io_t_addon',
    'get_io_t_addon_output',
]

@pulumi.output_type
class GetIoTAddonResult:
    """
    IoT Addon.
    """
    def __init__(__self__, host_platform=None, host_platform_type=None, id=None, io_t_device_details=None, io_t_edge_device_details=None, kind=None, name=None, provisioning_state=None, system_data=None, type=None, version=None):
        if host_platform and not isinstance(host_platform, str):
            raise TypeError("Expected argument 'host_platform' to be a str")
        pulumi.set(__self__, "host_platform", host_platform)
        if host_platform_type and not isinstance(host_platform_type, str):
            raise TypeError("Expected argument 'host_platform_type' to be a str")
        pulumi.set(__self__, "host_platform_type", host_platform_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if io_t_device_details and not isinstance(io_t_device_details, dict):
            raise TypeError("Expected argument 'io_t_device_details' to be a dict")
        pulumi.set(__self__, "io_t_device_details", io_t_device_details)
        if io_t_edge_device_details and not isinstance(io_t_edge_device_details, dict):
            raise TypeError("Expected argument 'io_t_edge_device_details' to be a dict")
        pulumi.set(__self__, "io_t_edge_device_details", io_t_edge_device_details)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> str:
        """
        Host OS supported by the IoT addon.
        """
        return pulumi.get(self, "host_platform")

    @property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> str:
        """
        Platform where the runtime is hosted.
        """
        return pulumi.get(self, "host_platform_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> 'outputs.IoTDeviceInfoResponse':
        """
        IoT device metadata to which appliance needs to be connected.
        """
        return pulumi.get(self, "io_t_device_details")

    @property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> 'outputs.IoTDeviceInfoResponse':
        """
        IoT edge device to which the IoT Addon needs to be configured.
        """
        return pulumi.get(self, "io_t_edge_device_details")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Addon type.
        Expected value is 'IotEdge'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Addon Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Addon type
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Version of IoT running on the appliance.
        """
        return pulumi.get(self, "version")


class AwaitableGetIoTAddonResult(GetIoTAddonResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIoTAddonResult(
            host_platform=self.host_platform,
            host_platform_type=self.host_platform_type,
            id=self.id,
            io_t_device_details=self.io_t_device_details,
            io_t_edge_device_details=self.io_t_edge_device_details,
            kind=self.kind,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type,
            version=self.version)


def get_io_t_addon(addon_name: Optional[str] = None,
                   device_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   role_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIoTAddonResult:
    """
    Gets a specific addon by name.


    :param str addon_name: The addon name.
    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str role_name: The role name.
    """
    __args__ = dict()
    __args__['addonName'] = addon_name
    __args__['deviceName'] = device_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['roleName'] = role_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20200901preview:getIoTAddon', __args__, opts=opts, typ=GetIoTAddonResult).value

    return AwaitableGetIoTAddonResult(
        host_platform=__ret__.host_platform,
        host_platform_type=__ret__.host_platform_type,
        id=__ret__.id,
        io_t_device_details=__ret__.io_t_device_details,
        io_t_edge_device_details=__ret__.io_t_edge_device_details,
        kind=__ret__.kind,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        type=__ret__.type,
        version=__ret__.version)


@_utilities.lift_output_func(get_io_t_addon)
def get_io_t_addon_output(addon_name: Optional[pulumi.Input[str]] = None,
                          device_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          role_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIoTAddonResult]:
    """
    Gets a specific addon by name.


    :param str addon_name: The addon name.
    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str role_name: The role name.
    """
    ...
