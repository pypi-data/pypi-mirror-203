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
    'ListDatabasePrincipalsResult',
    'AwaitableListDatabasePrincipalsResult',
    'list_database_principals',
    'list_database_principals_output',
]

@pulumi.output_type
class ListDatabasePrincipalsResult:
    """
    The list Kusto database principals operation response.
    """
    def __init__(__self__, value=None):
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.DatabasePrincipalResponse']]:
        """
        The list of Kusto database principals.
        """
        return pulumi.get(self, "value")


class AwaitableListDatabasePrincipalsResult(ListDatabasePrincipalsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDatabasePrincipalsResult(
            value=self.value)


def list_database_principals(cluster_name: Optional[str] = None,
                             database_name: Optional[str] = None,
                             resource_group_name: Optional[str] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDatabasePrincipalsResult:
    """
    Returns a list of database principals of the given Kusto cluster and database.


    :param str cluster_name: The name of the Kusto cluster.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kusto/v20190515:listDatabasePrincipals', __args__, opts=opts, typ=ListDatabasePrincipalsResult).value

    return AwaitableListDatabasePrincipalsResult(
        value=__ret__.value)


@_utilities.lift_output_func(list_database_principals)
def list_database_principals_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                    database_name: Optional[pulumi.Input[str]] = None,
                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDatabasePrincipalsResult]:
    """
    Returns a list of database principals of the given Kusto cluster and database.


    :param str cluster_name: The name of the Kusto cluster.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
