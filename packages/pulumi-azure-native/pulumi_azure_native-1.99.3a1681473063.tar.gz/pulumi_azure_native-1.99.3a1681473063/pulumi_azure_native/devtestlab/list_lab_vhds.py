# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'ListLabVhdsResult',
    'AwaitableListLabVhdsResult',
    'list_lab_vhds',
    'list_lab_vhds_output',
]

@pulumi.output_type
class ListLabVhdsResult:
    """
    The response of a list operation.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        Link for next set of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.LabVhdResponse']]:
        """
        Results of the list operation.
        """
        return pulumi.get(self, "value")


class AwaitableListLabVhdsResult(ListLabVhdsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListLabVhdsResult(
            next_link=self.next_link,
            value=self.value)


def list_lab_vhds(name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListLabVhdsResult:
    """
    List disk images available for custom image creation.
    API Version: 2018-09-15.


    :param str name: The name of the lab.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devtestlab:listLabVhds', __args__, opts=opts, typ=ListLabVhdsResult).value

    return AwaitableListLabVhdsResult(
        next_link=__ret__.next_link,
        value=__ret__.value)


@_utilities.lift_output_func(list_lab_vhds)
def list_lab_vhds_output(name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListLabVhdsResult]:
    """
    List disk images available for custom image creation.
    API Version: 2018-09-15.


    :param str name: The name of the lab.
    :param str resource_group_name: The name of the resource group.
    """
    ...
