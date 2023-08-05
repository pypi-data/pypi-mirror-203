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
    'GetLinkedWorkspaceResult',
    'AwaitableGetLinkedWorkspaceResult',
    'get_linked_workspace',
    'get_linked_workspace_output',
]

@pulumi.output_type
class GetLinkedWorkspaceResult:
    """
    Linked workspace.
    """
    def __init__(__self__, id=None, name=None, properties=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if properties and not isinstance(properties, dict):
            raise TypeError("Expected argument 'properties' to be a dict")
        pulumi.set(__self__, "properties", properties)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ResourceId of the link of the linked workspace.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Friendly name of the linked workspace.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> 'outputs.LinkedWorkspacePropsResponse':
        """
        LinkedWorkspace specific properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type of linked workspace.
        """
        return pulumi.get(self, "type")


class AwaitableGetLinkedWorkspaceResult(GetLinkedWorkspaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetLinkedWorkspaceResult(
            id=self.id,
            name=self.name,
            properties=self.properties,
            type=self.type)


def get_linked_workspace(link_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         workspace_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetLinkedWorkspaceResult:
    """
    Get the detail of a linked workspace.


    :param str link_name: Friendly name of the linked workspace
    :param str resource_group_name: Name of the resource group in which workspace is located.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    __args__ = dict()
    __args__['linkName'] = link_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:machinelearningservices/v20200501preview:getLinkedWorkspace', __args__, opts=opts, typ=GetLinkedWorkspaceResult).value

    return AwaitableGetLinkedWorkspaceResult(
        id=__ret__.id,
        name=__ret__.name,
        properties=__ret__.properties,
        type=__ret__.type)


@_utilities.lift_output_func(get_linked_workspace)
def get_linked_workspace_output(link_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                workspace_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetLinkedWorkspaceResult]:
    """
    Get the detail of a linked workspace.


    :param str link_name: Friendly name of the linked workspace
    :param str resource_group_name: Name of the resource group in which workspace is located.
    :param str workspace_name: Name of Azure Machine Learning workspace.
    """
    ...
