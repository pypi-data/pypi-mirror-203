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
    'GetArcAddonResult',
    'AwaitableGetArcAddonResult',
    'get_arc_addon',
    'get_arc_addon_output',
]

@pulumi.output_type
class GetArcAddonResult:
    """
    Arc Addon.
    """
    def __init__(__self__, custom_locations_object_id=None, host_platform=None, host_platform_type=None, id=None, kind=None, name=None, provisioning_state=None, resource_group_name=None, resource_location=None, resource_name=None, subscription_id=None, system_data=None, type=None, version=None):
        if custom_locations_object_id and not isinstance(custom_locations_object_id, str):
            raise TypeError("Expected argument 'custom_locations_object_id' to be a str")
        pulumi.set(__self__, "custom_locations_object_id", custom_locations_object_id)
        if host_platform and not isinstance(host_platform, str):
            raise TypeError("Expected argument 'host_platform' to be a str")
        pulumi.set(__self__, "host_platform", host_platform)
        if host_platform_type and not isinstance(host_platform_type, str):
            raise TypeError("Expected argument 'host_platform_type' to be a str")
        pulumi.set(__self__, "host_platform_type", host_platform_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_group_name and not isinstance(resource_group_name, str):
            raise TypeError("Expected argument 'resource_group_name' to be a str")
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if resource_location and not isinstance(resource_location, str):
            raise TypeError("Expected argument 'resource_location' to be a str")
        pulumi.set(__self__, "resource_location", resource_location)
        if resource_name and not isinstance(resource_name, str):
            raise TypeError("Expected argument 'resource_name' to be a str")
        pulumi.set(__self__, "resource_name", resource_name)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
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
    @pulumi.getter(name="customLocationsObjectId")
    def custom_locations_object_id(self) -> str:
        """
        Arc Custom Locations ObjectId
        """
        return pulumi.get(self, "custom_locations_object_id")

    @property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> str:
        """
        Host OS supported by the Arc addon.
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
    @pulumi.getter
    def kind(self) -> str:
        """
        Addon type.
        Expected value is 'ArcForKubernetes'.
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
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> str:
        """
        Arc resource group name
        """
        return pulumi.get(self, "resource_group_name")

    @property
    @pulumi.getter(name="resourceLocation")
    def resource_location(self) -> str:
        """
        Arc resource location
        """
        return pulumi.get(self, "resource_location")

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> str:
        """
        Arc resource Name
        """
        return pulumi.get(self, "resource_name")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> str:
        """
        Arc resource subscription Id
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of Addon
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
        Arc resource version
        """
        return pulumi.get(self, "version")


class AwaitableGetArcAddonResult(GetArcAddonResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetArcAddonResult(
            custom_locations_object_id=self.custom_locations_object_id,
            host_platform=self.host_platform,
            host_platform_type=self.host_platform_type,
            id=self.id,
            kind=self.kind,
            name=self.name,
            provisioning_state=self.provisioning_state,
            resource_group_name=self.resource_group_name,
            resource_location=self.resource_location,
            resource_name=self.resource_name,
            subscription_id=self.subscription_id,
            system_data=self.system_data,
            type=self.type,
            version=self.version)


def get_arc_addon(addon_name: Optional[str] = None,
                  device_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  role_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetArcAddonResult:
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
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20230101preview:getArcAddon', __args__, opts=opts, typ=GetArcAddonResult).value

    return AwaitableGetArcAddonResult(
        custom_locations_object_id=__ret__.custom_locations_object_id,
        host_platform=__ret__.host_platform,
        host_platform_type=__ret__.host_platform_type,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        resource_group_name=__ret__.resource_group_name,
        resource_location=__ret__.resource_location,
        resource_name=__ret__.resource_name,
        subscription_id=__ret__.subscription_id,
        system_data=__ret__.system_data,
        type=__ret__.type,
        version=__ret__.version)


@_utilities.lift_output_func(get_arc_addon)
def get_arc_addon_output(addon_name: Optional[pulumi.Input[str]] = None,
                         device_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         role_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetArcAddonResult]:
    """
    Gets a specific addon by name.


    :param str addon_name: The addon name.
    :param str device_name: The device name.
    :param str resource_group_name: The resource group name.
    :param str role_name: The role name.
    """
    ...
