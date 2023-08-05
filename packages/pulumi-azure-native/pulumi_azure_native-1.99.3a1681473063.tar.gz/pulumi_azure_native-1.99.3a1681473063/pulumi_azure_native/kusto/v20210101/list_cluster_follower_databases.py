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
    'ListClusterFollowerDatabasesResult',
    'AwaitableListClusterFollowerDatabasesResult',
    'list_cluster_follower_databases',
    'list_cluster_follower_databases_output',
]

@pulumi.output_type
class ListClusterFollowerDatabasesResult:
    """
    The list Kusto database principals operation response.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.FollowerDatabaseDefinitionResponse']]:
        """
        The list of follower database result.
        """
        return pulumi.get(self, "value")


class AwaitableListClusterFollowerDatabasesResult(ListClusterFollowerDatabasesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListClusterFollowerDatabasesResult(
            value=self.value)


def list_cluster_follower_databases(cluster_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListClusterFollowerDatabasesResult:
    """
    Returns a list of databases that are owned by this cluster and were followed by another cluster.


    :param str cluster_name: The name of the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kusto/v20210101:listClusterFollowerDatabases', __args__, opts=opts, typ=ListClusterFollowerDatabasesResult).value

    return AwaitableListClusterFollowerDatabasesResult(
        value=__ret__.value)


@_utilities.lift_output_func(list_cluster_follower_databases)
def list_cluster_follower_databases_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListClusterFollowerDatabasesResult]:
    """
    Returns a list of databases that are owned by this cluster and were followed by another cluster.


    :param str cluster_name: The name of the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
