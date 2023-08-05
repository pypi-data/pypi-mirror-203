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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    """
    Single Event Hubs Cluster resource in List or Get operations.
    """
    def __init__(__self__, created_at=None, id=None, location=None, metric_id=None, name=None, sku=None, status=None, system_data=None, tags=None, type=None, updated_at=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if metric_id and not isinstance(metric_id, str):
            raise TypeError("Expected argument 'metric_id' to be a str")
        pulumi.set(__self__, "metric_id", metric_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The UTC time when the Event Hubs Cluster was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> str:
        """
        The metric ID of the cluster resource. Provided by the service and not modifiable by the user.
        """
        return pulumi.get(self, "metric_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.ClusterSkuResponse']:
        """
        Properties of the cluster SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the Cluster resource
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
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

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> str:
        """
        The UTC time when the Event Hubs Cluster was last updated.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            created_at=self.created_at,
            id=self.id,
            location=self.location,
            metric_id=self.metric_id,
            name=self.name,
            sku=self.sku,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            updated_at=self.updated_at)


def get_cluster(cluster_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Gets the resource description of the specified Event Hubs Cluster.


    :param str cluster_name: The name of the Event Hubs Cluster.
    :param str resource_group_name: Name of the resource group within the azure subscription.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:eventhub/v20210601preview:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        created_at=__ret__.created_at,
        id=__ret__.id,
        location=__ret__.location,
        metric_id=__ret__.metric_id,
        name=__ret__.name,
        sku=__ret__.sku,
        status=__ret__.status,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        updated_at=__ret__.updated_at)


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(cluster_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Gets the resource description of the specified Event Hubs Cluster.


    :param str cluster_name: The name of the Event Hubs Cluster.
    :param str resource_group_name: Name of the resource group within the azure subscription.
    """
    ...
