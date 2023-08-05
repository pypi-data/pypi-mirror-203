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
from ._enums import *
from ._inputs import *

__all__ = ['NamespaceNetworkRuleSetArgs', 'NamespaceNetworkRuleSet']

@pulumi.input_type
class NamespaceNetworkRuleSetArgs:
    def __init__(__self__, *,
                 namespace_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 default_action: Optional[pulumi.Input[Union[str, 'DefaultAction']]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input['NWRuleSetIpRulesArgs']]]] = None,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input['NWRuleSetVirtualNetworkRulesArgs']]]] = None):
        """
        The set of arguments for constructing a NamespaceNetworkRuleSet resource.
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Union[str, 'DefaultAction']] default_action: Default Action for Network Rule Set
        :param pulumi.Input[Sequence[pulumi.Input['NWRuleSetIpRulesArgs']]] ip_rules: List of IpRules
        :param pulumi.Input[Sequence[pulumi.Input['NWRuleSetVirtualNetworkRulesArgs']]] virtual_network_rules: List VirtualNetwork Rules
        """
        pulumi.set(__self__, "namespace_name", namespace_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if default_action is not None:
            pulumi.set(__self__, "default_action", default_action)
        if ip_rules is not None:
            pulumi.set(__self__, "ip_rules", ip_rules)
        if virtual_network_rules is not None:
            pulumi.set(__self__, "virtual_network_rules", virtual_network_rules)

    @property
    @pulumi.getter(name="namespaceName")
    def namespace_name(self) -> pulumi.Input[str]:
        """
        The namespace name
        """
        return pulumi.get(self, "namespace_name")

    @namespace_name.setter
    def namespace_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "namespace_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> Optional[pulumi.Input[Union[str, 'DefaultAction']]]:
        """
        Default Action for Network Rule Set
        """
        return pulumi.get(self, "default_action")

    @default_action.setter
    def default_action(self, value: Optional[pulumi.Input[Union[str, 'DefaultAction']]]):
        pulumi.set(self, "default_action", value)

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NWRuleSetIpRulesArgs']]]]:
        """
        List of IpRules
        """
        return pulumi.get(self, "ip_rules")

    @ip_rules.setter
    def ip_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NWRuleSetIpRulesArgs']]]]):
        pulumi.set(self, "ip_rules", value)

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['NWRuleSetVirtualNetworkRulesArgs']]]]:
        """
        List VirtualNetwork Rules
        """
        return pulumi.get(self, "virtual_network_rules")

    @virtual_network_rules.setter
    def virtual_network_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['NWRuleSetVirtualNetworkRulesArgs']]]]):
        pulumi.set(self, "virtual_network_rules", value)


class NamespaceNetworkRuleSet(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_action: Optional[pulumi.Input[Union[str, 'DefaultAction']]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NWRuleSetIpRulesArgs']]]]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NWRuleSetVirtualNetworkRulesArgs']]]]] = None,
                 __props__=None):
        """
        Description of NetworkRuleSet resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Union[str, 'DefaultAction']] default_action: Default Action for Network Rule Set
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NWRuleSetIpRulesArgs']]]] ip_rules: List of IpRules
        :param pulumi.Input[str] namespace_name: The namespace name
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NWRuleSetVirtualNetworkRulesArgs']]]] virtual_network_rules: List VirtualNetwork Rules
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: NamespaceNetworkRuleSetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Description of NetworkRuleSet resource.

        :param str resource_name: The name of the resource.
        :param NamespaceNetworkRuleSetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(NamespaceNetworkRuleSetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_action: Optional[pulumi.Input[Union[str, 'DefaultAction']]] = None,
                 ip_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NWRuleSetIpRulesArgs']]]]] = None,
                 namespace_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 virtual_network_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['NWRuleSetVirtualNetworkRulesArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = NamespaceNetworkRuleSetArgs.__new__(NamespaceNetworkRuleSetArgs)

            __props__.__dict__["default_action"] = default_action
            __props__.__dict__["ip_rules"] = ip_rules
            if namespace_name is None and not opts.urn:
                raise TypeError("Missing required property 'namespace_name'")
            __props__.__dict__["namespace_name"] = namespace_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["virtual_network_rules"] = virtual_network_rules
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:servicebus:NamespaceNetworkRuleSet"), pulumi.Alias(type_="azure-native:servicebus/v20170401:NamespaceNetworkRuleSet"), pulumi.Alias(type_="azure-native:servicebus/v20210101preview:NamespaceNetworkRuleSet"), pulumi.Alias(type_="azure-native:servicebus/v20210601preview:NamespaceNetworkRuleSet"), pulumi.Alias(type_="azure-native:servicebus/v20211101:NamespaceNetworkRuleSet"), pulumi.Alias(type_="azure-native:servicebus/v20220101preview:NamespaceNetworkRuleSet"), pulumi.Alias(type_="azure-native:servicebus/v20221001preview:NamespaceNetworkRuleSet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(NamespaceNetworkRuleSet, __self__).__init__(
            'azure-native:servicebus/v20180101preview:NamespaceNetworkRuleSet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'NamespaceNetworkRuleSet':
        """
        Get an existing NamespaceNetworkRuleSet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = NamespaceNetworkRuleSetArgs.__new__(NamespaceNetworkRuleSetArgs)

        __props__.__dict__["default_action"] = None
        __props__.__dict__["ip_rules"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_network_rules"] = None
        return NamespaceNetworkRuleSet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultAction")
    def default_action(self) -> pulumi.Output[Optional[str]]:
        """
        Default Action for Network Rule Set
        """
        return pulumi.get(self, "default_action")

    @property
    @pulumi.getter(name="ipRules")
    def ip_rules(self) -> pulumi.Output[Optional[Sequence['outputs.NWRuleSetIpRulesResponse']]]:
        """
        List of IpRules
        """
        return pulumi.get(self, "ip_rules")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualNetworkRules")
    def virtual_network_rules(self) -> pulumi.Output[Optional[Sequence['outputs.NWRuleSetVirtualNetworkRulesResponse']]]:
        """
        List VirtualNetwork Rules
        """
        return pulumi.get(self, "virtual_network_rules")

