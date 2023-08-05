# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetSharedKeysResult',
    'AwaitableGetSharedKeysResult',
    'get_shared_keys',
    'get_shared_keys_output',
]

@pulumi.output_type
class GetSharedKeysResult:
    """
    The shared keys for a workspace.
    """
    def __init__(__self__, primary_shared_key=None, secondary_shared_key=None):
        if primary_shared_key and not isinstance(primary_shared_key, str):
            raise TypeError("Expected argument 'primary_shared_key' to be a str")
        pulumi.set(__self__, "primary_shared_key", primary_shared_key)
        if secondary_shared_key and not isinstance(secondary_shared_key, str):
            raise TypeError("Expected argument 'secondary_shared_key' to be a str")
        pulumi.set(__self__, "secondary_shared_key", secondary_shared_key)

    @property
    @pulumi.getter(name="primarySharedKey")
    def primary_shared_key(self) -> Optional[str]:
        """
        The primary shared key of a workspace.
        """
        return pulumi.get(self, "primary_shared_key")

    @property
    @pulumi.getter(name="secondarySharedKey")
    def secondary_shared_key(self) -> Optional[str]:
        """
        The secondary shared key of a workspace.
        """
        return pulumi.get(self, "secondary_shared_key")


class AwaitableGetSharedKeysResult(GetSharedKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSharedKeysResult(
            primary_shared_key=self.primary_shared_key,
            secondary_shared_key=self.secondary_shared_key)


def get_shared_keys(resource_group_name: Optional[str] = None,
                    workspace_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSharedKeysResult:
    """
    Gets the shared keys for a workspace.
    API Version: 2020-08-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:operationalinsights:getSharedKeys', __args__, opts=opts, typ=GetSharedKeysResult).value

    return AwaitableGetSharedKeysResult(
        primary_shared_key=__ret__.primary_shared_key,
        secondary_shared_key=__ret__.secondary_shared_key)


@_utilities.lift_output_func(get_shared_keys)
def get_shared_keys_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                           workspace_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSharedKeysResult]:
    """
    Gets the shared keys for a workspace.
    API Version: 2020-08-01.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
