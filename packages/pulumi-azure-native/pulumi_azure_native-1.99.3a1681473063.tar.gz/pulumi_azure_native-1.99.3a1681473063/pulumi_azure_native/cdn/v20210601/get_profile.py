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
    'GetProfileResult',
    'AwaitableGetProfileResult',
    'get_profile',
    'get_profile_output',
]

@pulumi.output_type
class GetProfileResult:
    """
    A profile is a logical grouping of endpoints that share the same settings.
    """
    def __init__(__self__, front_door_id=None, id=None, kind=None, location=None, name=None, origin_response_timeout_seconds=None, provisioning_state=None, resource_state=None, sku=None, system_data=None, tags=None, type=None):
        if front_door_id and not isinstance(front_door_id, str):
            raise TypeError("Expected argument 'front_door_id' to be a str")
        pulumi.set(__self__, "front_door_id", front_door_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if origin_response_timeout_seconds and not isinstance(origin_response_timeout_seconds, int):
            raise TypeError("Expected argument 'origin_response_timeout_seconds' to be a int")
        pulumi.set(__self__, "origin_response_timeout_seconds", origin_response_timeout_seconds)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="frontDoorId")
    def front_door_id(self) -> str:
        """
        The Id of the frontdoor.
        """
        return pulumi.get(self, "front_door_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of the profile. Used by portal to differentiate traditional CDN profile and new AFD profile.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originResponseTimeoutSeconds")
    def origin_response_timeout_seconds(self) -> Optional[int]:
        """
        Send and receive timeout on forwarding request to the origin. When timeout is reached, the request fails and returns.
        """
        return pulumi.get(self, "origin_response_timeout_seconds")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning status of the profile.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        Resource status of the profile.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        The pricing tier (defines Azure Front Door Standard or Premium or a CDN provider, feature list and rate) of the profile.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetProfileResult(GetProfileResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetProfileResult(
            front_door_id=self.front_door_id,
            id=self.id,
            kind=self.kind,
            location=self.location,
            name=self.name,
            origin_response_timeout_seconds=self.origin_response_timeout_seconds,
            provisioning_state=self.provisioning_state,
            resource_state=self.resource_state,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_profile(profile_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetProfileResult:
    """
    Gets an Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group.


    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cdn/v20210601:getProfile', __args__, opts=opts, typ=GetProfileResult).value

    return AwaitableGetProfileResult(
        front_door_id=__ret__.front_door_id,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        origin_response_timeout_seconds=__ret__.origin_response_timeout_seconds,
        provisioning_state=__ret__.provisioning_state,
        resource_state=__ret__.resource_state,
        sku=__ret__.sku,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_profile)
def get_profile_output(profile_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetProfileResult]:
    """
    Gets an Azure Front Door Standard or Azure Front Door Premium or CDN profile with the specified profile name under the specified subscription and resource group.


    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium or CDN profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
