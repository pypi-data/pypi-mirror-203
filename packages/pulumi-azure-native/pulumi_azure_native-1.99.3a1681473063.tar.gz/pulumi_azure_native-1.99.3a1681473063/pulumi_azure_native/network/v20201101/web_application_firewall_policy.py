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

__all__ = ['WebApplicationFirewallPolicyArgs', 'WebApplicationFirewallPolicy']

@pulumi.input_type
class WebApplicationFirewallPolicyArgs:
    def __init__(__self__, *,
                 managed_rules: pulumi.Input['ManagedRulesDefinitionArgs'],
                 resource_group_name: pulumi.Input[str],
                 custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input['WebApplicationFirewallCustomRuleArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_settings: Optional[pulumi.Input['PolicySettingsArgs']] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a WebApplicationFirewallPolicy resource.
        :param pulumi.Input['ManagedRulesDefinitionArgs'] managed_rules: Describes the managedRules structure.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Sequence[pulumi.Input['WebApplicationFirewallCustomRuleArgs']]] custom_rules: The custom rules inside the policy.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] policy_name: The name of the policy.
        :param pulumi.Input['PolicySettingsArgs'] policy_settings: The PolicySettings for policy.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "managed_rules", managed_rules)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if custom_rules is not None:
            pulumi.set(__self__, "custom_rules", custom_rules)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if policy_name is not None:
            pulumi.set(__self__, "policy_name", policy_name)
        if policy_settings is not None:
            pulumi.set(__self__, "policy_settings", policy_settings)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> pulumi.Input['ManagedRulesDefinitionArgs']:
        """
        Describes the managedRules structure.
        """
        return pulumi.get(self, "managed_rules")

    @managed_rules.setter
    def managed_rules(self, value: pulumi.Input['ManagedRulesDefinitionArgs']):
        pulumi.set(self, "managed_rules", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['WebApplicationFirewallCustomRuleArgs']]]]:
        """
        The custom rules inside the policy.
        """
        return pulumi.get(self, "custom_rules")

    @custom_rules.setter
    def custom_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['WebApplicationFirewallCustomRuleArgs']]]]):
        pulumi.set(self, "custom_rules", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="policyName")
    def policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the policy.
        """
        return pulumi.get(self, "policy_name")

    @policy_name.setter
    def policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_name", value)

    @property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> Optional[pulumi.Input['PolicySettingsArgs']]:
        """
        The PolicySettings for policy.
        """
        return pulumi.get(self, "policy_settings")

    @policy_settings.setter
    def policy_settings(self, value: Optional[pulumi.Input['PolicySettingsArgs']]):
        pulumi.set(self, "policy_settings", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class WebApplicationFirewallPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebApplicationFirewallCustomRuleArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_rules: Optional[pulumi.Input[pulumi.InputType['ManagedRulesDefinitionArgs']]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_settings: Optional[pulumi.Input[pulumi.InputType['PolicySettingsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Defines web application firewall policy.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebApplicationFirewallCustomRuleArgs']]]] custom_rules: The custom rules inside the policy.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[pulumi.InputType['ManagedRulesDefinitionArgs']] managed_rules: Describes the managedRules structure.
        :param pulumi.Input[str] policy_name: The name of the policy.
        :param pulumi.Input[pulumi.InputType['PolicySettingsArgs']] policy_settings: The PolicySettings for policy.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WebApplicationFirewallPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines web application firewall policy.

        :param str resource_name: The name of the resource.
        :param WebApplicationFirewallPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WebApplicationFirewallPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 custom_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['WebApplicationFirewallCustomRuleArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 managed_rules: Optional[pulumi.Input[pulumi.InputType['ManagedRulesDefinitionArgs']]] = None,
                 policy_name: Optional[pulumi.Input[str]] = None,
                 policy_settings: Optional[pulumi.Input[pulumi.InputType['PolicySettingsArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WebApplicationFirewallPolicyArgs.__new__(WebApplicationFirewallPolicyArgs)

            __props__.__dict__["custom_rules"] = custom_rules
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            if managed_rules is None and not opts.urn:
                raise TypeError("Missing required property 'managed_rules'")
            __props__.__dict__["managed_rules"] = managed_rules
            __props__.__dict__["policy_name"] = policy_name
            __props__.__dict__["policy_settings"] = policy_settings
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["application_gateways"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["http_listeners"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["path_based_rules"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20181201:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190201:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190401:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190601:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190701:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190801:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20190901:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20191101:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20191201:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200301:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200401:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200501:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200601:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200701:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20200801:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20210201:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20210301:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20210501:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20210801:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20220101:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20220501:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20220701:WebApplicationFirewallPolicy"), pulumi.Alias(type_="azure-native:network/v20220901:WebApplicationFirewallPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WebApplicationFirewallPolicy, __self__).__init__(
            'azure-native:network/v20201101:WebApplicationFirewallPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WebApplicationFirewallPolicy':
        """
        Get an existing WebApplicationFirewallPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WebApplicationFirewallPolicyArgs.__new__(WebApplicationFirewallPolicyArgs)

        __props__.__dict__["application_gateways"] = None
        __props__.__dict__["custom_rules"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["http_listeners"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["managed_rules"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["path_based_rules"] = None
        __props__.__dict__["policy_settings"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return WebApplicationFirewallPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="applicationGateways")
    def application_gateways(self) -> pulumi.Output[Sequence['outputs.ApplicationGatewayResponse']]:
        """
        A collection of references to application gateways.
        """
        return pulumi.get(self, "application_gateways")

    @property
    @pulumi.getter(name="customRules")
    def custom_rules(self) -> pulumi.Output[Optional[Sequence['outputs.WebApplicationFirewallCustomRuleResponse']]]:
        """
        The custom rules inside the policy.
        """
        return pulumi.get(self, "custom_rules")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        A collection of references to application gateway http listeners.
        """
        return pulumi.get(self, "http_listeners")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedRules")
    def managed_rules(self) -> pulumi.Output['outputs.ManagedRulesDefinitionResponse']:
        """
        Describes the managedRules structure.
        """
        return pulumi.get(self, "managed_rules")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="pathBasedRules")
    def path_based_rules(self) -> pulumi.Output[Sequence['outputs.SubResourceResponse']]:
        """
        A collection of references to application gateway path rules.
        """
        return pulumi.get(self, "path_based_rules")

    @property
    @pulumi.getter(name="policySettings")
    def policy_settings(self) -> pulumi.Output[Optional['outputs.PolicySettingsResponse']]:
        """
        The PolicySettings for policy.
        """
        return pulumi.get(self, "policy_settings")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the web application firewall policy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        Resource status of the policy.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

