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
    'GetEdgeModuleResult',
    'AwaitableGetEdgeModuleResult',
    'get_edge_module',
    'get_edge_module_output',
]

@pulumi.output_type
class GetEdgeModuleResult:
    """
    The representation of an edge module.
    """
    def __init__(__self__, edge_module_id=None, id=None, name=None, system_data=None, type=None):
        if edge_module_id and not isinstance(edge_module_id, str):
            raise TypeError("Expected argument 'edge_module_id' to be a str")
        pulumi.set(__self__, "edge_module_id", edge_module_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="edgeModuleId")
    def edge_module_id(self) -> str:
        """
        Internal ID generated for the instance of the Video Analyzer edge module.
        """
        return pulumi.get(self, "edge_module_id")

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


class AwaitableGetEdgeModuleResult(GetEdgeModuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEdgeModuleResult(
            edge_module_id=self.edge_module_id,
            id=self.id,
            name=self.name,
            system_data=self.system_data,
            type=self.type)


def get_edge_module(account_name: Optional[str] = None,
                    edge_module_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEdgeModuleResult:
    """
    Retrieves a specific existing edge module resource in the given Video Analyzer account.


    :param str account_name: The Azure Video Analyzer account name.
    :param str edge_module_name: The name of the edge module to retrieve.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['edgeModuleName'] = edge_module_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:videoanalyzer/v20210501preview:getEdgeModule', __args__, opts=opts, typ=GetEdgeModuleResult).value

    return AwaitableGetEdgeModuleResult(
        edge_module_id=__ret__.edge_module_id,
        id=__ret__.id,
        name=__ret__.name,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_edge_module)
def get_edge_module_output(account_name: Optional[pulumi.Input[str]] = None,
                           edge_module_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEdgeModuleResult]:
    """
    Retrieves a specific existing edge module resource in the given Video Analyzer account.


    :param str account_name: The Azure Video Analyzer account name.
    :param str edge_module_name: The name of the edge module to retrieve.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
