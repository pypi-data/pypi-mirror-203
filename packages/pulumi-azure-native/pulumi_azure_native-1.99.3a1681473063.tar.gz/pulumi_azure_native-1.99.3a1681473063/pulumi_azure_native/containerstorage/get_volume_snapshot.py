# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetVolumeSnapshotResult',
    'AwaitableGetVolumeSnapshotResult',
    'get_volume_snapshot',
    'get_volume_snapshot_output',
]

@pulumi.output_type
class GetVolumeSnapshotResult:
    """
    Concrete proxy resource types can be created by aliasing this type using a specific property type.
    """
    def __init__(__self__, id=None, mount_options=None, name=None, provisioning_state=None, reclaim_policy=None, source=None, system_data=None, type=None, volume_mode=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if mount_options and not isinstance(mount_options, list):
            raise TypeError("Expected argument 'mount_options' to be a list")
        pulumi.set(__self__, "mount_options", mount_options)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if reclaim_policy and not isinstance(reclaim_policy, str):
            raise TypeError("Expected argument 'reclaim_policy' to be a str")
        pulumi.set(__self__, "reclaim_policy", reclaim_policy)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volume_mode and not isinstance(volume_mode, str):
            raise TypeError("Expected argument 'volume_mode' to be a str")
        pulumi.set(__self__, "volume_mode", volume_mode)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="mountOptions")
    def mount_options(self) -> Sequence[str]:
        """
        List of string mount options
        """
        return pulumi.get(self, "mount_options")

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
        The status of the last operation.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="reclaimPolicy")
    def reclaim_policy(self) -> str:
        """
        Reclaim Policy, Delete or Retain
        """
        return pulumi.get(self, "reclaim_policy")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        Reference to the source volume
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeMode")
    def volume_mode(self) -> str:
        """
        Indicates how the volumes created from the snapshot should be attached
        """
        return pulumi.get(self, "volume_mode")


class AwaitableGetVolumeSnapshotResult(GetVolumeSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeSnapshotResult(
            id=self.id,
            mount_options=self.mount_options,
            name=self.name,
            provisioning_state=self.provisioning_state,
            reclaim_policy=self.reclaim_policy,
            source=self.source,
            system_data=self.system_data,
            type=self.type,
            volume_mode=self.volume_mode)


def get_volume_snapshot(pool_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        volume_snapshot_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeSnapshotResult:
    """
    Get a VolumeSnapshot
    API Version: 2023-03-01-preview.


    :param str pool_name: Pool Object
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str volume_snapshot_name: Volume Snapshot Resource
    """
    __args__ = dict()
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['volumeSnapshotName'] = volume_snapshot_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerstorage:getVolumeSnapshot', __args__, opts=opts, typ=GetVolumeSnapshotResult).value

    return AwaitableGetVolumeSnapshotResult(
        id=__ret__.id,
        mount_options=__ret__.mount_options,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        reclaim_policy=__ret__.reclaim_policy,
        source=__ret__.source,
        system_data=__ret__.system_data,
        type=__ret__.type,
        volume_mode=__ret__.volume_mode)


@_utilities.lift_output_func(get_volume_snapshot)
def get_volume_snapshot_output(pool_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               volume_snapshot_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeSnapshotResult]:
    """
    Get a VolumeSnapshot
    API Version: 2023-03-01-preview.


    :param str pool_name: Pool Object
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str volume_snapshot_name: Volume Snapshot Resource
    """
    ...
