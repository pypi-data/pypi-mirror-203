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
from ._enums import *
from ._inputs import *

__all__ = ['RuleArgs', 'Rule']

@pulumi.input_type
class RuleArgs:
    def __init__(__self__, *,
                 actions: pulumi.Input[Sequence[pulumi.Input[Union['DeliveryRuleCacheExpirationActionArgs', 'DeliveryRuleCacheKeyQueryStringActionArgs', 'DeliveryRuleRequestHeaderActionArgs', 'DeliveryRuleResponseHeaderActionArgs', 'OriginGroupOverrideActionArgs', 'UrlRedirectActionArgs', 'UrlRewriteActionArgs', 'UrlSigningActionArgs']]]],
                 order: pulumi.Input[int],
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 rule_set_name: pulumi.Input[str],
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DeliveryRuleCookiesConditionArgs', 'DeliveryRuleHttpVersionConditionArgs', 'DeliveryRuleIsDeviceConditionArgs', 'DeliveryRulePostArgsConditionArgs', 'DeliveryRuleQueryStringConditionArgs', 'DeliveryRuleRemoteAddressConditionArgs', 'DeliveryRuleRequestBodyConditionArgs', 'DeliveryRuleRequestHeaderConditionArgs', 'DeliveryRuleRequestMethodConditionArgs', 'DeliveryRuleRequestSchemeConditionArgs', 'DeliveryRuleRequestUriConditionArgs', 'DeliveryRuleUrlFileExtensionConditionArgs', 'DeliveryRuleUrlFileNameConditionArgs', 'DeliveryRuleUrlPathConditionArgs']]]]] = None,
                 match_processing_behavior: Optional[pulumi.Input[Union[str, 'MatchProcessingBehavior']]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Rule resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DeliveryRuleCacheExpirationActionArgs', 'DeliveryRuleCacheKeyQueryStringActionArgs', 'DeliveryRuleRequestHeaderActionArgs', 'DeliveryRuleResponseHeaderActionArgs', 'OriginGroupOverrideActionArgs', 'UrlRedirectActionArgs', 'UrlRewriteActionArgs', 'UrlSigningActionArgs']]]] actions: A list of actions that are executed when all the conditions of a rule are satisfied.
        :param pulumi.Input[int] order: The order in which the rules are applied for the endpoint. Possible values {0,1,2,3,………}. A rule with a lesser order will be applied before a rule with a greater order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] rule_set_name: Name of the rule set under the profile.
        :param pulumi.Input[Sequence[pulumi.Input[Union['DeliveryRuleCookiesConditionArgs', 'DeliveryRuleHttpVersionConditionArgs', 'DeliveryRuleIsDeviceConditionArgs', 'DeliveryRulePostArgsConditionArgs', 'DeliveryRuleQueryStringConditionArgs', 'DeliveryRuleRemoteAddressConditionArgs', 'DeliveryRuleRequestBodyConditionArgs', 'DeliveryRuleRequestHeaderConditionArgs', 'DeliveryRuleRequestMethodConditionArgs', 'DeliveryRuleRequestSchemeConditionArgs', 'DeliveryRuleRequestUriConditionArgs', 'DeliveryRuleUrlFileExtensionConditionArgs', 'DeliveryRuleUrlFileNameConditionArgs', 'DeliveryRuleUrlPathConditionArgs']]]] conditions: A list of conditions that must be matched for the actions to be executed
        :param pulumi.Input[Union[str, 'MatchProcessingBehavior']] match_processing_behavior: If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue.
        :param pulumi.Input[str] rule_name: Name of the delivery rule which is unique within the endpoint.
        """
        pulumi.set(__self__, "actions", actions)
        pulumi.set(__self__, "order", order)
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "rule_set_name", rule_set_name)
        if conditions is not None:
            pulumi.set(__self__, "conditions", conditions)
        if match_processing_behavior is not None:
            pulumi.set(__self__, "match_processing_behavior", match_processing_behavior)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Input[Sequence[pulumi.Input[Union['DeliveryRuleCacheExpirationActionArgs', 'DeliveryRuleCacheKeyQueryStringActionArgs', 'DeliveryRuleRequestHeaderActionArgs', 'DeliveryRuleResponseHeaderActionArgs', 'OriginGroupOverrideActionArgs', 'UrlRedirectActionArgs', 'UrlRewriteActionArgs', 'UrlSigningActionArgs']]]]:
        """
        A list of actions that are executed when all the conditions of a rule are satisfied.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: pulumi.Input[Sequence[pulumi.Input[Union['DeliveryRuleCacheExpirationActionArgs', 'DeliveryRuleCacheKeyQueryStringActionArgs', 'DeliveryRuleRequestHeaderActionArgs', 'DeliveryRuleResponseHeaderActionArgs', 'OriginGroupOverrideActionArgs', 'UrlRedirectActionArgs', 'UrlRewriteActionArgs', 'UrlSigningActionArgs']]]]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter
    def order(self) -> pulumi.Input[int]:
        """
        The order in which the rules are applied for the endpoint. Possible values {0,1,2,3,………}. A rule with a lesser order will be applied before a rule with a greater order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.
        """
        return pulumi.get(self, "order")

    @order.setter
    def order(self, value: pulumi.Input[int]):
        pulumi.set(self, "order", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the CDN profile which is unique within the resource group.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

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
    @pulumi.getter(name="ruleSetName")
    def rule_set_name(self) -> pulumi.Input[str]:
        """
        Name of the rule set under the profile.
        """
        return pulumi.get(self, "rule_set_name")

    @rule_set_name.setter
    def rule_set_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "rule_set_name", value)

    @property
    @pulumi.getter
    def conditions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['DeliveryRuleCookiesConditionArgs', 'DeliveryRuleHttpVersionConditionArgs', 'DeliveryRuleIsDeviceConditionArgs', 'DeliveryRulePostArgsConditionArgs', 'DeliveryRuleQueryStringConditionArgs', 'DeliveryRuleRemoteAddressConditionArgs', 'DeliveryRuleRequestBodyConditionArgs', 'DeliveryRuleRequestHeaderConditionArgs', 'DeliveryRuleRequestMethodConditionArgs', 'DeliveryRuleRequestSchemeConditionArgs', 'DeliveryRuleRequestUriConditionArgs', 'DeliveryRuleUrlFileExtensionConditionArgs', 'DeliveryRuleUrlFileNameConditionArgs', 'DeliveryRuleUrlPathConditionArgs']]]]]:
        """
        A list of conditions that must be matched for the actions to be executed
        """
        return pulumi.get(self, "conditions")

    @conditions.setter
    def conditions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['DeliveryRuleCookiesConditionArgs', 'DeliveryRuleHttpVersionConditionArgs', 'DeliveryRuleIsDeviceConditionArgs', 'DeliveryRulePostArgsConditionArgs', 'DeliveryRuleQueryStringConditionArgs', 'DeliveryRuleRemoteAddressConditionArgs', 'DeliveryRuleRequestBodyConditionArgs', 'DeliveryRuleRequestHeaderConditionArgs', 'DeliveryRuleRequestMethodConditionArgs', 'DeliveryRuleRequestSchemeConditionArgs', 'DeliveryRuleRequestUriConditionArgs', 'DeliveryRuleUrlFileExtensionConditionArgs', 'DeliveryRuleUrlFileNameConditionArgs', 'DeliveryRuleUrlPathConditionArgs']]]]]):
        pulumi.set(self, "conditions", value)

    @property
    @pulumi.getter(name="matchProcessingBehavior")
    def match_processing_behavior(self) -> Optional[pulumi.Input[Union[str, 'MatchProcessingBehavior']]]:
        """
        If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue.
        """
        return pulumi.get(self, "match_processing_behavior")

    @match_processing_behavior.setter
    def match_processing_behavior(self, value: Optional[pulumi.Input[Union[str, 'MatchProcessingBehavior']]]):
        pulumi.set(self, "match_processing_behavior", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the delivery rule which is unique within the endpoint.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)


class Rule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['DeliveryRuleCacheExpirationActionArgs'], pulumi.InputType['DeliveryRuleCacheKeyQueryStringActionArgs'], pulumi.InputType['DeliveryRuleRequestHeaderActionArgs'], pulumi.InputType['DeliveryRuleResponseHeaderActionArgs'], pulumi.InputType['OriginGroupOverrideActionArgs'], pulumi.InputType['UrlRedirectActionArgs'], pulumi.InputType['UrlRewriteActionArgs'], pulumi.InputType['UrlSigningActionArgs']]]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['DeliveryRuleCookiesConditionArgs'], pulumi.InputType['DeliveryRuleHttpVersionConditionArgs'], pulumi.InputType['DeliveryRuleIsDeviceConditionArgs'], pulumi.InputType['DeliveryRulePostArgsConditionArgs'], pulumi.InputType['DeliveryRuleQueryStringConditionArgs'], pulumi.InputType['DeliveryRuleRemoteAddressConditionArgs'], pulumi.InputType['DeliveryRuleRequestBodyConditionArgs'], pulumi.InputType['DeliveryRuleRequestHeaderConditionArgs'], pulumi.InputType['DeliveryRuleRequestMethodConditionArgs'], pulumi.InputType['DeliveryRuleRequestSchemeConditionArgs'], pulumi.InputType['DeliveryRuleRequestUriConditionArgs'], pulumi.InputType['DeliveryRuleUrlFileExtensionConditionArgs'], pulumi.InputType['DeliveryRuleUrlFileNameConditionArgs'], pulumi.InputType['DeliveryRuleUrlPathConditionArgs']]]]]] = None,
                 match_processing_behavior: Optional[pulumi.Input[Union[str, 'MatchProcessingBehavior']]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 rule_set_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Friendly Rules name mapping to the any Rules or secret related information.
        API Version: 2020-09-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['DeliveryRuleCacheExpirationActionArgs'], pulumi.InputType['DeliveryRuleCacheKeyQueryStringActionArgs'], pulumi.InputType['DeliveryRuleRequestHeaderActionArgs'], pulumi.InputType['DeliveryRuleResponseHeaderActionArgs'], pulumi.InputType['OriginGroupOverrideActionArgs'], pulumi.InputType['UrlRedirectActionArgs'], pulumi.InputType['UrlRewriteActionArgs'], pulumi.InputType['UrlSigningActionArgs']]]]] actions: A list of actions that are executed when all the conditions of a rule are satisfied.
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['DeliveryRuleCookiesConditionArgs'], pulumi.InputType['DeliveryRuleHttpVersionConditionArgs'], pulumi.InputType['DeliveryRuleIsDeviceConditionArgs'], pulumi.InputType['DeliveryRulePostArgsConditionArgs'], pulumi.InputType['DeliveryRuleQueryStringConditionArgs'], pulumi.InputType['DeliveryRuleRemoteAddressConditionArgs'], pulumi.InputType['DeliveryRuleRequestBodyConditionArgs'], pulumi.InputType['DeliveryRuleRequestHeaderConditionArgs'], pulumi.InputType['DeliveryRuleRequestMethodConditionArgs'], pulumi.InputType['DeliveryRuleRequestSchemeConditionArgs'], pulumi.InputType['DeliveryRuleRequestUriConditionArgs'], pulumi.InputType['DeliveryRuleUrlFileExtensionConditionArgs'], pulumi.InputType['DeliveryRuleUrlFileNameConditionArgs'], pulumi.InputType['DeliveryRuleUrlPathConditionArgs']]]]] conditions: A list of conditions that must be matched for the actions to be executed
        :param pulumi.Input[Union[str, 'MatchProcessingBehavior']] match_processing_behavior: If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue.
        :param pulumi.Input[int] order: The order in which the rules are applied for the endpoint. Possible values {0,1,2,3,………}. A rule with a lesser order will be applied before a rule with a greater order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[str] rule_name: Name of the delivery rule which is unique within the endpoint.
        :param pulumi.Input[str] rule_set_name: Name of the rule set under the profile.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Friendly Rules name mapping to the any Rules or secret related information.
        API Version: 2020-09-01.

        :param str resource_name: The name of the resource.
        :param RuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['DeliveryRuleCacheExpirationActionArgs'], pulumi.InputType['DeliveryRuleCacheKeyQueryStringActionArgs'], pulumi.InputType['DeliveryRuleRequestHeaderActionArgs'], pulumi.InputType['DeliveryRuleResponseHeaderActionArgs'], pulumi.InputType['OriginGroupOverrideActionArgs'], pulumi.InputType['UrlRedirectActionArgs'], pulumi.InputType['UrlRewriteActionArgs'], pulumi.InputType['UrlSigningActionArgs']]]]]] = None,
                 conditions: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['DeliveryRuleCookiesConditionArgs'], pulumi.InputType['DeliveryRuleHttpVersionConditionArgs'], pulumi.InputType['DeliveryRuleIsDeviceConditionArgs'], pulumi.InputType['DeliveryRulePostArgsConditionArgs'], pulumi.InputType['DeliveryRuleQueryStringConditionArgs'], pulumi.InputType['DeliveryRuleRemoteAddressConditionArgs'], pulumi.InputType['DeliveryRuleRequestBodyConditionArgs'], pulumi.InputType['DeliveryRuleRequestHeaderConditionArgs'], pulumi.InputType['DeliveryRuleRequestMethodConditionArgs'], pulumi.InputType['DeliveryRuleRequestSchemeConditionArgs'], pulumi.InputType['DeliveryRuleRequestUriConditionArgs'], pulumi.InputType['DeliveryRuleUrlFileExtensionConditionArgs'], pulumi.InputType['DeliveryRuleUrlFileNameConditionArgs'], pulumi.InputType['DeliveryRuleUrlPathConditionArgs']]]]]] = None,
                 match_processing_behavior: Optional[pulumi.Input[Union[str, 'MatchProcessingBehavior']]] = None,
                 order: Optional[pulumi.Input[int]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 rule_set_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RuleArgs.__new__(RuleArgs)

            if actions is None and not opts.urn:
                raise TypeError("Missing required property 'actions'")
            __props__.__dict__["actions"] = actions
            __props__.__dict__["conditions"] = conditions
            __props__.__dict__["match_processing_behavior"] = match_processing_behavior
            if order is None and not opts.urn:
                raise TypeError("Missing required property 'order'")
            __props__.__dict__["order"] = order
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rule_name"] = rule_name
            if rule_set_name is None and not opts.urn:
                raise TypeError("Missing required property 'rule_set_name'")
            __props__.__dict__["rule_set_name"] = rule_set_name
            __props__.__dict__["deployment_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn/v20200901:Rule"), pulumi.Alias(type_="azure-native:cdn/v20210601:Rule"), pulumi.Alias(type_="azure-native:cdn/v20220501preview:Rule"), pulumi.Alias(type_="azure-native:cdn/v20221101preview:Rule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Rule, __self__).__init__(
            'azure-native:cdn:Rule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Rule':
        """
        Get an existing Rule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RuleArgs.__new__(RuleArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["conditions"] = None
        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["match_processing_behavior"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["order"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Rule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Sequence[Any]]:
        """
        A list of actions that are executed when all the conditions of a rule are satisfied.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def conditions(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        A list of conditions that must be matched for the actions to be executed
        """
        return pulumi.get(self, "conditions")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="matchProcessingBehavior")
    def match_processing_behavior(self) -> pulumi.Output[Optional[str]]:
        """
        If this rule is a match should the rules engine continue running the remaining rules or stop. If not present, defaults to Continue.
        """
        return pulumi.get(self, "match_processing_behavior")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def order(self) -> pulumi.Output[int]:
        """
        The order in which the rules are applied for the endpoint. Possible values {0,1,2,3,………}. A rule with a lesser order will be applied before a rule with a greater order. Rule with order 0 is a special rule. It does not require any condition and actions listed in it will always be applied.
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

