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
    'GetMachinePoolResult',
    'AwaitableGetMachinePoolResult',
    'get_machine_pool',
    'get_machine_pool_output',
]

@pulumi.output_type
class GetMachinePoolResult:
    """
    MachinePool represents a MachinePool
    """
    def __init__(__self__, id=None, name=None, resources=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if resources and not isinstance(resources, str):
            raise TypeError("Expected argument 'resources' to be a str")
        pulumi.set(__self__, "resources", resources)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
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
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def resources(self) -> Optional[str]:
        return pulumi.get(self, "resources")

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


class AwaitableGetMachinePoolResult(GetMachinePoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetMachinePoolResult(
            id=self.id,
            name=self.name,
            resources=self.resources,
            system_data=self.system_data,
            type=self.type)


def get_machine_pool(child_resource_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     resource_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetMachinePoolResult:
    """
    The operation returns properties of a MachinePool.


    :param str child_resource_name: The name of the MachinePool resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the OpenShift cluster resource.
    """
    __args__ = dict()
    __args__['childResourceName'] = child_resource_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:redhatopenshift/v20220904:getMachinePool', __args__, opts=opts, typ=GetMachinePoolResult).value

    return AwaitableGetMachinePoolResult(
        id=__ret__.id,
        name=__ret__.name,
        resources=__ret__.resources,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_machine_pool)
def get_machine_pool_output(child_resource_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            resource_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetMachinePoolResult]:
    """
    The operation returns properties of a MachinePool.


    :param str child_resource_name: The name of the MachinePool resource.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: The name of the OpenShift cluster resource.
    """
    ...
