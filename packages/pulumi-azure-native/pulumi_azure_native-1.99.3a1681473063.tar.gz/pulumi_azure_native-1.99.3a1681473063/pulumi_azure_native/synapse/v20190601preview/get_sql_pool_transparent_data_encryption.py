# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetSqlPoolTransparentDataEncryptionResult',
    'AwaitableGetSqlPoolTransparentDataEncryptionResult',
    'get_sql_pool_transparent_data_encryption',
    'get_sql_pool_transparent_data_encryption_output',
]

warnings.warn("""Version 2019-06-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetSqlPoolTransparentDataEncryptionResult:
    """
    Represents a Sql pool transparent data encryption configuration.
    """
    def __init__(__self__, id=None, location=None, name=None, status=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
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
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        The status of the database transparent data encryption.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetSqlPoolTransparentDataEncryptionResult(GetSqlPoolTransparentDataEncryptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlPoolTransparentDataEncryptionResult(
            id=self.id,
            location=self.location,
            name=self.name,
            status=self.status,
            type=self.type)


def get_sql_pool_transparent_data_encryption(resource_group_name: Optional[str] = None,
                                             sql_pool_name: Optional[str] = None,
                                             transparent_data_encryption_name: Optional[str] = None,
                                             workspace_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlPoolTransparentDataEncryptionResult:
    """
    Get a SQL pool's transparent data encryption configuration.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sql_pool_name: SQL pool name
    :param str transparent_data_encryption_name: The name of the transparent data encryption configuration.
    :param str workspace_name: The name of the workspace
    """
    pulumi.log.warn("""get_sql_pool_transparent_data_encryption is deprecated: Version 2019-06-01-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sqlPoolName'] = sql_pool_name
    __args__['transparentDataEncryptionName'] = transparent_data_encryption_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:synapse/v20190601preview:getSqlPoolTransparentDataEncryption', __args__, opts=opts, typ=GetSqlPoolTransparentDataEncryptionResult).value

    return AwaitableGetSqlPoolTransparentDataEncryptionResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        status=__ret__.status,
        type=__ret__.type)


@_utilities.lift_output_func(get_sql_pool_transparent_data_encryption)
def get_sql_pool_transparent_data_encryption_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    sql_pool_name: Optional[pulumi.Input[str]] = None,
                                                    transparent_data_encryption_name: Optional[pulumi.Input[str]] = None,
                                                    workspace_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlPoolTransparentDataEncryptionResult]:
    """
    Get a SQL pool's transparent data encryption configuration.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str sql_pool_name: SQL pool name
    :param str transparent_data_encryption_name: The name of the transparent data encryption configuration.
    :param str workspace_name: The name of the workspace
    """
    pulumi.log.warn("""get_sql_pool_transparent_data_encryption is deprecated: Version 2019-06-01-preview will be removed in v2 of the provider.""")
    ...
