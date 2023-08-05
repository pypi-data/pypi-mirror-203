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
    'GetAdminRuleResult',
    'AwaitableGetAdminRuleResult',
    'get_admin_rule',
    'get_admin_rule_output',
]

@pulumi.output_type
class GetAdminRuleResult:
    """
    Network admin rule.
    """
    def __init__(__self__, access=None, description=None, destination_port_ranges=None, destinations=None, direction=None, etag=None, id=None, kind=None, name=None, priority=None, protocol=None, provisioning_state=None, source_port_ranges=None, sources=None, system_data=None, type=None):
        if access and not isinstance(access, str):
            raise TypeError("Expected argument 'access' to be a str")
        pulumi.set(__self__, "access", access)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if destination_port_ranges and not isinstance(destination_port_ranges, list):
            raise TypeError("Expected argument 'destination_port_ranges' to be a list")
        pulumi.set(__self__, "destination_port_ranges", destination_port_ranges)
        if destinations and not isinstance(destinations, list):
            raise TypeError("Expected argument 'destinations' to be a list")
        pulumi.set(__self__, "destinations", destinations)
        if direction and not isinstance(direction, str):
            raise TypeError("Expected argument 'direction' to be a str")
        pulumi.set(__self__, "direction", direction)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if priority and not isinstance(priority, int):
            raise TypeError("Expected argument 'priority' to be a int")
        pulumi.set(__self__, "priority", priority)
        if protocol and not isinstance(protocol, str):
            raise TypeError("Expected argument 'protocol' to be a str")
        pulumi.set(__self__, "protocol", protocol)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source_port_ranges and not isinstance(source_port_ranges, list):
            raise TypeError("Expected argument 'source_port_ranges' to be a list")
        pulumi.set(__self__, "source_port_ranges", source_port_ranges)
        if sources and not isinstance(sources, list):
            raise TypeError("Expected argument 'sources' to be a list")
        pulumi.set(__self__, "sources", sources)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def access(self) -> str:
        """
        Indicates the access allowed for this particular rule
        """
        return pulumi.get(self, "access")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        A description for this rule. Restricted to 140 chars.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="destinationPortRanges")
    def destination_port_ranges(self) -> Optional[Sequence[str]]:
        """
        The destination port ranges.
        """
        return pulumi.get(self, "destination_port_ranges")

    @property
    @pulumi.getter
    def destinations(self) -> Optional[Sequence['outputs.AddressPrefixItemResponse']]:
        """
        The destination address prefixes. CIDR or destination IP ranges.
        """
        return pulumi.get(self, "destinations")

    @property
    @pulumi.getter
    def direction(self) -> str:
        """
        Indicates if the traffic matched against the rule in inbound or outbound.
        """
        return pulumi.get(self, "direction")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Whether the rule is custom or default.
        Expected value is 'Custom'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def priority(self) -> int:
        """
        The priority of the rule. The value can be between 1 and 4096. The priority number must be unique for each rule in the collection. The lower the priority number, the higher the priority of the rule.
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter
    def protocol(self) -> str:
        """
        Network protocol this rule applies to.
        """
        return pulumi.get(self, "protocol")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sourcePortRanges")
    def source_port_ranges(self) -> Optional[Sequence[str]]:
        """
        The source port ranges.
        """
        return pulumi.get(self, "source_port_ranges")

    @property
    @pulumi.getter
    def sources(self) -> Optional[Sequence['outputs.AddressPrefixItemResponse']]:
        """
        The CIDR or source IP ranges.
        """
        return pulumi.get(self, "sources")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetAdminRuleResult(GetAdminRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAdminRuleResult(
            access=self.access,
            description=self.description,
            destination_port_ranges=self.destination_port_ranges,
            destinations=self.destinations,
            direction=self.direction,
            etag=self.etag,
            id=self.id,
            kind=self.kind,
            name=self.name,
            priority=self.priority,
            protocol=self.protocol,
            provisioning_state=self.provisioning_state,
            source_port_ranges=self.source_port_ranges,
            sources=self.sources,
            system_data=self.system_data,
            type=self.type)


def get_admin_rule(configuration_name: Optional[str] = None,
                   network_manager_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   rule_collection_name: Optional[str] = None,
                   rule_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAdminRuleResult:
    """
    Gets a network manager security configuration admin rule.


    :param str configuration_name: The name of the network manager Security Configuration.
    :param str network_manager_name: The name of the network manager.
    :param str resource_group_name: The name of the resource group.
    :param str rule_collection_name: The name of the network manager security Configuration rule collection.
    :param str rule_name: The name of the rule.
    """
    __args__ = dict()
    __args__['configurationName'] = configuration_name
    __args__['networkManagerName'] = network_manager_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['ruleCollectionName'] = rule_collection_name
    __args__['ruleName'] = rule_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20220901:getAdminRule', __args__, opts=opts, typ=GetAdminRuleResult).value

    return AwaitableGetAdminRuleResult(
        access=__ret__.access,
        description=__ret__.description,
        destination_port_ranges=__ret__.destination_port_ranges,
        destinations=__ret__.destinations,
        direction=__ret__.direction,
        etag=__ret__.etag,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        priority=__ret__.priority,
        protocol=__ret__.protocol,
        provisioning_state=__ret__.provisioning_state,
        source_port_ranges=__ret__.source_port_ranges,
        sources=__ret__.sources,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_admin_rule)
def get_admin_rule_output(configuration_name: Optional[pulumi.Input[str]] = None,
                          network_manager_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          rule_collection_name: Optional[pulumi.Input[str]] = None,
                          rule_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAdminRuleResult]:
    """
    Gets a network manager security configuration admin rule.


    :param str configuration_name: The name of the network manager Security Configuration.
    :param str network_manager_name: The name of the network manager.
    :param str resource_group_name: The name of the resource group.
    :param str rule_collection_name: The name of the network manager security Configuration rule collection.
    :param str rule_name: The name of the rule.
    """
    ...
