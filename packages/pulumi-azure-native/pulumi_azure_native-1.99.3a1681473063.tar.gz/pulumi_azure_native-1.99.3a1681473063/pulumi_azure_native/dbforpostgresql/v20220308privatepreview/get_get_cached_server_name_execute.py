# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *
from ._inputs import *

__all__ = [
    'GetGetCachedServerNameExecuteResult',
    'AwaitableGetGetCachedServerNameExecuteResult',
    'get_get_cached_server_name_execute',
    'get_get_cached_server_name_execute_output',
]

@pulumi.output_type
class GetGetCachedServerNameExecuteResult:
    """
    Represents a resource name of a cached server
    """
    def __init__(__self__, name=None):
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of available cached server
        """
        return pulumi.get(self, "name")


class AwaitableGetGetCachedServerNameExecuteResult(GetGetCachedServerNameExecuteResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGetCachedServerNameExecuteResult(
            name=self.name)


def get_get_cached_server_name_execute(location_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       sku: Optional[pulumi.InputType['Sku']] = None,
                                       storage: Optional[pulumi.InputType['Storage']] = None,
                                       version: Optional[Union[str, 'ServerVersion']] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGetCachedServerNameExecuteResult:
    """
    Get available cached server name for fast provisioning


    :param str location_name: The name of the location.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param pulumi.InputType['Sku'] sku: The SKU (pricing tier) of the server.
    :param pulumi.InputType['Storage'] storage: Storage properties of a server.
    :param Union[str, 'ServerVersion'] version: PostgreSQL Server version.
    """
    __args__ = dict()
    __args__['locationName'] = location_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sku'] = sku
    __args__['storage'] = storage
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:dbforpostgresql/v20220308privatepreview:getGetCachedServerNameExecute', __args__, opts=opts, typ=GetGetCachedServerNameExecuteResult).value

    return AwaitableGetGetCachedServerNameExecuteResult(
        name=__ret__.name)


@_utilities.lift_output_func(get_get_cached_server_name_execute)
def get_get_cached_server_name_execute_output(location_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              sku: Optional[pulumi.Input[pulumi.InputType['Sku']]] = None,
                                              storage: Optional[pulumi.Input[pulumi.InputType['Storage']]] = None,
                                              version: Optional[pulumi.Input[Union[str, 'ServerVersion']]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGetCachedServerNameExecuteResult]:
    """
    Get available cached server name for fast provisioning


    :param str location_name: The name of the location.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param pulumi.InputType['Sku'] sku: The SKU (pricing tier) of the server.
    :param pulumi.InputType['Storage'] storage: Storage properties of a server.
    :param Union[str, 'ServerVersion'] version: PostgreSQL Server version.
    """
    ...
