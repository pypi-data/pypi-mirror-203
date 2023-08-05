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
    'GetManagedClusterSnapshotResult',
    'AwaitableGetManagedClusterSnapshotResult',
    'get_managed_cluster_snapshot',
    'get_managed_cluster_snapshot_output',
]

@pulumi.output_type
class GetManagedClusterSnapshotResult:
    """
    A managed cluster snapshot resource.
    """
    def __init__(__self__, creation_data=None, id=None, location=None, managed_cluster_properties_read_only=None, name=None, snapshot_type=None, system_data=None, tags=None, type=None):
        if creation_data and not isinstance(creation_data, dict):
            raise TypeError("Expected argument 'creation_data' to be a dict")
        pulumi.set(__self__, "creation_data", creation_data)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_cluster_properties_read_only and not isinstance(managed_cluster_properties_read_only, dict):
            raise TypeError("Expected argument 'managed_cluster_properties_read_only' to be a dict")
        pulumi.set(__self__, "managed_cluster_properties_read_only", managed_cluster_properties_read_only)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if snapshot_type and not isinstance(snapshot_type, str):
            raise TypeError("Expected argument 'snapshot_type' to be a str")
        pulumi.set(__self__, "snapshot_type", snapshot_type)
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
    @pulumi.getter(name="creationData")
    def creation_data(self) -> Optional['outputs.CreationDataResponse']:
        """
        CreationData to be used to specify the source resource ID to create this snapshot.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedClusterPropertiesReadOnly")
    def managed_cluster_properties_read_only(self) -> 'outputs.ManagedClusterPropertiesForSnapshotResponse':
        """
        What the properties will be showed when getting managed cluster snapshot. Those properties are read-only.
        """
        return pulumi.get(self, "managed_cluster_properties_read_only")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="snapshotType")
    def snapshot_type(self) -> Optional[str]:
        """
        The type of a snapshot. The default is NodePool.
        """
        return pulumi.get(self, "snapshot_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
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
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedClusterSnapshotResult(GetManagedClusterSnapshotResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedClusterSnapshotResult(
            creation_data=self.creation_data,
            id=self.id,
            location=self.location,
            managed_cluster_properties_read_only=self.managed_cluster_properties_read_only,
            name=self.name,
            snapshot_type=self.snapshot_type,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_managed_cluster_snapshot(resource_group_name: Optional[str] = None,
                                 resource_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedClusterSnapshotResult:
    """
    A managed cluster snapshot resource.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20220902preview:getManagedClusterSnapshot', __args__, opts=opts, typ=GetManagedClusterSnapshotResult).value

    return AwaitableGetManagedClusterSnapshotResult(
        creation_data=__ret__.creation_data,
        id=__ret__.id,
        location=__ret__.location,
        managed_cluster_properties_read_only=__ret__.managed_cluster_properties_read_only,
        name=__ret__.name,
        snapshot_type=__ret__.snapshot_type,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_managed_cluster_snapshot)
def get_managed_cluster_snapshot_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                        resource_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedClusterSnapshotResult]:
    """
    A managed cluster snapshot resource.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the managed cluster resource.
    """
    ...
