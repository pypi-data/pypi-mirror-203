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
    'ListDnsForwardingRulesetByVirtualNetworkResult',
    'AwaitableListDnsForwardingRulesetByVirtualNetworkResult',
    'list_dns_forwarding_ruleset_by_virtual_network',
    'list_dns_forwarding_ruleset_by_virtual_network_output',
]

@pulumi.output_type
class ListDnsForwardingRulesetByVirtualNetworkResult:
    """
    The response to an enumeration operation on Virtual Network DNS Forwarding Ruleset.
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
    def next_link(self) -> str:
        """
        The continuation token for the next page of results.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.VirtualNetworkDnsForwardingRulesetResponse']]:
        """
        Enumeration of the Virtual Network DNS Forwarding Ruleset.
        """
        return pulumi.get(self, "value")


class AwaitableListDnsForwardingRulesetByVirtualNetworkResult(ListDnsForwardingRulesetByVirtualNetworkResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListDnsForwardingRulesetByVirtualNetworkResult(
            next_link=self.next_link,
            value=self.value)


def list_dns_forwarding_ruleset_by_virtual_network(resource_group_name: Optional[str] = None,
                                                   top: Optional[int] = None,
                                                   virtual_network_name: Optional[str] = None,
                                                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListDnsForwardingRulesetByVirtualNetworkResult:
    """
    Lists DNS forwarding ruleset resource IDs attached to a virtual network.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param int top: The maximum number of results to return. If not specified, returns up to 100 results.
    :param str virtual_network_name: The name of the virtual network.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['top'] = top
    __args__['virtualNetworkName'] = virtual_network_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20200401preview:listDnsForwardingRulesetByVirtualNetwork', __args__, opts=opts, typ=ListDnsForwardingRulesetByVirtualNetworkResult).value

    return AwaitableListDnsForwardingRulesetByVirtualNetworkResult(
        next_link=__ret__.next_link,
        value=__ret__.value)


@_utilities.lift_output_func(list_dns_forwarding_ruleset_by_virtual_network)
def list_dns_forwarding_ruleset_by_virtual_network_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                          top: Optional[pulumi.Input[Optional[int]]] = None,
                                                          virtual_network_name: Optional[pulumi.Input[str]] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListDnsForwardingRulesetByVirtualNetworkResult]:
    """
    Lists DNS forwarding ruleset resource IDs attached to a virtual network.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param int top: The maximum number of results to return. If not specified, returns up to 100 results.
    :param str virtual_network_name: The name of the virtual network.
    """
    ...
