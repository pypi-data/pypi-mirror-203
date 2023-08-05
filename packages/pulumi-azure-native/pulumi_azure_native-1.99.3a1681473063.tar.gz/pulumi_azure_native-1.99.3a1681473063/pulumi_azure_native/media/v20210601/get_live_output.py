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
    'GetLiveOutputResult',
    'AwaitableGetLiveOutputResult',
    'get_live_output',
    'get_live_output_output',
]

@pulumi.output_type
class GetLiveOutputResult:
    """
    The Live Output.
    """
    def __init__(__self__, archive_window_length=None, asset_name=None, created=None, description=None, hls=None, id=None, last_modified=None, manifest_name=None, name=None, output_snap_time=None, provisioning_state=None, resource_state=None, system_data=None, type=None):
        if archive_window_length and not isinstance(archive_window_length, str):
            raise TypeError("Expected argument 'archive_window_length' to be a str")
        pulumi.set(__self__, "archive_window_length", archive_window_length)
        if asset_name and not isinstance(asset_name, str):
            raise TypeError("Expected argument 'asset_name' to be a str")
        pulumi.set(__self__, "asset_name", asset_name)
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if hls and not isinstance(hls, dict):
            raise TypeError("Expected argument 'hls' to be a dict")
        pulumi.set(__self__, "hls", hls)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified and not isinstance(last_modified, str):
            raise TypeError("Expected argument 'last_modified' to be a str")
        pulumi.set(__self__, "last_modified", last_modified)
        if manifest_name and not isinstance(manifest_name, str):
            raise TypeError("Expected argument 'manifest_name' to be a str")
        pulumi.set(__self__, "manifest_name", manifest_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if output_snap_time and not isinstance(output_snap_time, float):
            raise TypeError("Expected argument 'output_snap_time' to be a float")
        pulumi.set(__self__, "output_snap_time", output_snap_time)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if resource_state and not isinstance(resource_state, str):
            raise TypeError("Expected argument 'resource_state' to be a str")
        pulumi.set(__self__, "resource_state", resource_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="archiveWindowLength")
    def archive_window_length(self) -> str:
        """
        ISO 8601 time between 1 minute to 25 hours to indicate the maximum content length that can be archived in the asset for this live output. This also sets the maximum content length for the rewind window. For example, use PT1H30M to indicate 1 hour and 30 minutes of archive window.
        """
        return pulumi.get(self, "archive_window_length")

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> str:
        """
        The asset that the live output will write to.
        """
        return pulumi.get(self, "asset_name")

    @property
    @pulumi.getter
    def created(self) -> str:
        """
        The creation time the live output.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the live output.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def hls(self) -> Optional['outputs.HlsResponse']:
        """
        HTTP Live Streaming (HLS) packing setting for the live output.
        """
        return pulumi.get(self, "hls")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> str:
        """
        The time the live output was last modified.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter(name="manifestName")
    def manifest_name(self) -> Optional[str]:
        """
        The manifest file name. If not provided, the service will generate one automatically.
        """
        return pulumi.get(self, "manifest_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="outputSnapTime")
    def output_snap_time(self) -> Optional[float]:
        """
        The initial timestamp that the live output will start at, any content before this value will not be archived.
        """
        return pulumi.get(self, "output_snap_time")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the live output.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> str:
        """
        The resource state of the live output.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetLiveOutputResult(GetLiveOutputResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLiveOutputResult(
            archive_window_length=self.archive_window_length,
            asset_name=self.asset_name,
            created=self.created,
            description=self.description,
            hls=self.hls,
            id=self.id,
            last_modified=self.last_modified,
            manifest_name=self.manifest_name,
            name=self.name,
            output_snap_time=self.output_snap_time,
            provisioning_state=self.provisioning_state,
            resource_state=self.resource_state,
            system_data=self.system_data,
            type=self.type)


def get_live_output(account_name: Optional[str] = None,
                    live_event_name: Optional[str] = None,
                    live_output_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLiveOutputResult:
    """
    Gets a live output.


    :param str account_name: The Media Services account name.
    :param str live_event_name: The name of the live event, maximum length is 32.
    :param str live_output_name: The name of the live output.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['liveEventName'] = live_event_name
    __args__['liveOutputName'] = live_output_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:media/v20210601:getLiveOutput', __args__, opts=opts, typ=GetLiveOutputResult).value

    return AwaitableGetLiveOutputResult(
        archive_window_length=__ret__.archive_window_length,
        asset_name=__ret__.asset_name,
        created=__ret__.created,
        description=__ret__.description,
        hls=__ret__.hls,
        id=__ret__.id,
        last_modified=__ret__.last_modified,
        manifest_name=__ret__.manifest_name,
        name=__ret__.name,
        output_snap_time=__ret__.output_snap_time,
        provisioning_state=__ret__.provisioning_state,
        resource_state=__ret__.resource_state,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_live_output)
def get_live_output_output(account_name: Optional[pulumi.Input[str]] = None,
                           live_event_name: Optional[pulumi.Input[str]] = None,
                           live_output_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLiveOutputResult]:
    """
    Gets a live output.


    :param str account_name: The Media Services account name.
    :param str live_event_name: The name of the live event, maximum length is 32.
    :param str live_output_name: The name of the live output.
    :param str resource_group_name: The name of the resource group within the Azure subscription.
    """
    ...
