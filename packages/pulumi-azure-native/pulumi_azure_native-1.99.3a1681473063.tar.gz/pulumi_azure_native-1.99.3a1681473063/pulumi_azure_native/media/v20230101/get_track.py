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
    'GetTrackResult',
    'AwaitableGetTrackResult',
    'get_track',
    'get_track_output',
]

@pulumi.output_type
class GetTrackResult:
    """
    An Asset Track resource.
    """
    def __init__(__self__, id=None, name=None, provisioning_state=None, track=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if track and not isinstance(track, dict):
            raise TypeError("Expected argument 'track' to be a dict")
        pulumi.set(__self__, "track", track)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the asset track.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def track(self) -> Optional[Any]:
        """
        Detailed information about a track in the asset.
        """
        return pulumi.get(self, "track")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetTrackResult(GetTrackResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTrackResult(
            id=self.id,
            name=self.name,
            provisioning_state=self.provisioning_state,
            track=self.track,
            type=self.type)


def get_track(account_name: Optional[str] = None,
              asset_name: Optional[str] = None,
              resource_group_name: Optional[str] = None,
              track_name: Optional[str] = None,
              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTrackResult:
    """
    Get the details of a Track in the Asset


    :param str account_name: The Media Services account name.
    :param str asset_name: The Asset name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    :param str track_name: The Asset Track name.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['assetName'] = asset_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['trackName'] = track_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20230101:getTrack', __args__, opts=opts, typ=GetTrackResult).value

    return AwaitableGetTrackResult(
        id=__ret__.id,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        track=__ret__.track,
        type=__ret__.type)


@_utilities.lift_output_func(get_track)
def get_track_output(account_name: Optional[pulumi.Input[str]] = None,
                     asset_name: Optional[pulumi.Input[str]] = None,
                     resource_group_name: Optional[pulumi.Input[str]] = None,
                     track_name: Optional[pulumi.Input[str]] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTrackResult]:
    """
    Get the details of a Track in the Asset


    :param str account_name: The Media Services account name.
    :param str asset_name: The Asset name.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    :param str track_name: The Asset Track name.
    """
    ...
