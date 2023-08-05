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

__all__ = ['ScheduledQueryRuleArgs', 'ScheduledQueryRule']

@pulumi.input_type
class ScheduledQueryRuleArgs:
    def __init__(__self__, *,
                 criteria: pulumi.Input['ScheduledQueryRuleCriteriaArgs'],
                 enabled: pulumi.Input[bool],
                 resource_group_name: pulumi.Input[str],
                 scopes: pulumi.Input[Sequence[pulumi.Input[str]]],
                 actions: Optional[pulumi.Input['ActionsArgs']] = None,
                 auto_mitigate: Optional[pulumi.Input[bool]] = None,
                 check_workspace_alerts_storage_configured: Optional[pulumi.Input[bool]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 evaluation_frequency: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mute_actions_duration: Optional[pulumi.Input[str]] = None,
                 override_query_time_range: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 severity: Optional[pulumi.Input[float]] = None,
                 skip_query_validation: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 window_size: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ScheduledQueryRule resource.
        :param pulumi.Input['ScheduledQueryRuleCriteriaArgs'] criteria: The rule criteria that defines the conditions of the scheduled query rule.
        :param pulumi.Input[bool] enabled: The flag which indicates whether this scheduled query rule is enabled. Value should be true or false
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The list of resource id's that this scheduled query rule is scoped to.
        :param pulumi.Input['ActionsArgs'] actions: Actions to invoke when the alert fires.
        :param pulumi.Input[bool] auto_mitigate: The flag that indicates whether the alert should be automatically resolved or not. The default is true. Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[bool] check_workspace_alerts_storage_configured: The flag which indicates whether this scheduled query rule should be stored in the customer's storage. The default is false. Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[str] description: The description of the scheduled query rule.
        :param pulumi.Input[str] display_name: The display name of the alert rule
        :param pulumi.Input[str] evaluation_frequency: How often the scheduled query rule is evaluated represented in ISO 8601 duration format. Relevant and required only for rules of the kind LogAlert.
        :param pulumi.Input[Union[str, 'Kind']] kind: Indicates the type of scheduled query rule. The default is LogAlert.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] mute_actions_duration: Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired. Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[str] override_query_time_range: If specified then overrides the query time range (default is WindowSize*NumberOfEvaluationPeriods). Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[str] rule_name: The name of the rule.
        :param pulumi.Input[float] severity: Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and required only for rules of the kind LogAlert.
        :param pulumi.Input[bool] skip_query_validation: The flag which indicates whether the provided query should be validated or not. The default is false. Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_resource_types: List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria. Relevant only for rules of the kind LogAlert
        :param pulumi.Input[str] window_size: The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size). Relevant and required only for rules of the kind LogAlert.
        """
        pulumi.set(__self__, "criteria", criteria)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "scopes", scopes)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if auto_mitigate is not None:
            pulumi.set(__self__, "auto_mitigate", auto_mitigate)
        if check_workspace_alerts_storage_configured is not None:
            pulumi.set(__self__, "check_workspace_alerts_storage_configured", check_workspace_alerts_storage_configured)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if evaluation_frequency is not None:
            pulumi.set(__self__, "evaluation_frequency", evaluation_frequency)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if mute_actions_duration is not None:
            pulumi.set(__self__, "mute_actions_duration", mute_actions_duration)
        if override_query_time_range is not None:
            pulumi.set(__self__, "override_query_time_range", override_query_time_range)
        if rule_name is not None:
            pulumi.set(__self__, "rule_name", rule_name)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)
        if skip_query_validation is not None:
            pulumi.set(__self__, "skip_query_validation", skip_query_validation)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if target_resource_types is not None:
            pulumi.set(__self__, "target_resource_types", target_resource_types)
        if window_size is not None:
            pulumi.set(__self__, "window_size", window_size)

    @property
    @pulumi.getter
    def criteria(self) -> pulumi.Input['ScheduledQueryRuleCriteriaArgs']:
        """
        The rule criteria that defines the conditions of the scheduled query rule.
        """
        return pulumi.get(self, "criteria")

    @criteria.setter
    def criteria(self, value: pulumi.Input['ScheduledQueryRuleCriteriaArgs']):
        pulumi.set(self, "criteria", value)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[bool]:
        """
        The flag which indicates whether this scheduled query rule is enabled. Value should be true or false
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[bool]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The list of resource id's that this scheduled query rule is scoped to.
        """
        return pulumi.get(self, "scopes")

    @scopes.setter
    def scopes(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "scopes", value)

    @property
    @pulumi.getter
    def actions(self) -> Optional[pulumi.Input['ActionsArgs']]:
        """
        Actions to invoke when the alert fires.
        """
        return pulumi.get(self, "actions")

    @actions.setter
    def actions(self, value: Optional[pulumi.Input['ActionsArgs']]):
        pulumi.set(self, "actions", value)

    @property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag that indicates whether the alert should be automatically resolved or not. The default is true. Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "auto_mitigate")

    @auto_mitigate.setter
    def auto_mitigate(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_mitigate", value)

    @property
    @pulumi.getter(name="checkWorkspaceAlertsStorageConfigured")
    def check_workspace_alerts_storage_configured(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag which indicates whether this scheduled query rule should be stored in the customer's storage. The default is false. Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "check_workspace_alerts_storage_configured")

    @check_workspace_alerts_storage_configured.setter
    def check_workspace_alerts_storage_configured(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "check_workspace_alerts_storage_configured", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The description of the scheduled query rule.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the alert rule
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> Optional[pulumi.Input[str]]:
        """
        How often the scheduled query rule is evaluated represented in ISO 8601 duration format. Relevant and required only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "evaluation_frequency")

    @evaluation_frequency.setter
    def evaluation_frequency(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "evaluation_frequency", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[Union[str, 'Kind']]]:
        """
        Indicates the type of scheduled query rule. The default is LogAlert.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[Union[str, 'Kind']]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="muteActionsDuration")
    def mute_actions_duration(self) -> Optional[pulumi.Input[str]]:
        """
        Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired. Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "mute_actions_duration")

    @mute_actions_duration.setter
    def mute_actions_duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mute_actions_duration", value)

    @property
    @pulumi.getter(name="overrideQueryTimeRange")
    def override_query_time_range(self) -> Optional[pulumi.Input[str]]:
        """
        If specified then overrides the query time range (default is WindowSize*NumberOfEvaluationPeriods). Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "override_query_time_range")

    @override_query_time_range.setter
    def override_query_time_range(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "override_query_time_range", value)

    @property
    @pulumi.getter(name="ruleName")
    def rule_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the rule.
        """
        return pulumi.get(self, "rule_name")

    @rule_name.setter
    def rule_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "rule_name", value)

    @property
    @pulumi.getter
    def severity(self) -> Optional[pulumi.Input[float]]:
        """
        Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and required only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "severity")

    @severity.setter
    def severity(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "severity", value)

    @property
    @pulumi.getter(name="skipQueryValidation")
    def skip_query_validation(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag which indicates whether the provided query should be validated or not. The default is false. Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "skip_query_validation")

    @skip_query_validation.setter
    def skip_query_validation(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "skip_query_validation", value)

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

    @property
    @pulumi.getter(name="targetResourceTypes")
    def target_resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria. Relevant only for rules of the kind LogAlert
        """
        return pulumi.get(self, "target_resource_types")

    @target_resource_types.setter
    def target_resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "target_resource_types", value)

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> Optional[pulumi.Input[str]]:
        """
        The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size). Relevant and required only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "window_size")

    @window_size.setter
    def window_size(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "window_size", value)


class ScheduledQueryRule(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[pulumi.InputType['ActionsArgs']]] = None,
                 auto_mitigate: Optional[pulumi.Input[bool]] = None,
                 check_workspace_alerts_storage_configured: Optional[pulumi.Input[bool]] = None,
                 criteria: Optional[pulumi.Input[pulumi.InputType['ScheduledQueryRuleCriteriaArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 evaluation_frequency: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mute_actions_duration: Optional[pulumi.Input[str]] = None,
                 override_query_time_range: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 severity: Optional[pulumi.Input[float]] = None,
                 skip_query_validation: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 window_size: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The scheduled query rule resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ActionsArgs']] actions: Actions to invoke when the alert fires.
        :param pulumi.Input[bool] auto_mitigate: The flag that indicates whether the alert should be automatically resolved or not. The default is true. Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[bool] check_workspace_alerts_storage_configured: The flag which indicates whether this scheduled query rule should be stored in the customer's storage. The default is false. Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[pulumi.InputType['ScheduledQueryRuleCriteriaArgs']] criteria: The rule criteria that defines the conditions of the scheduled query rule.
        :param pulumi.Input[str] description: The description of the scheduled query rule.
        :param pulumi.Input[str] display_name: The display name of the alert rule
        :param pulumi.Input[bool] enabled: The flag which indicates whether this scheduled query rule is enabled. Value should be true or false
        :param pulumi.Input[str] evaluation_frequency: How often the scheduled query rule is evaluated represented in ISO 8601 duration format. Relevant and required only for rules of the kind LogAlert.
        :param pulumi.Input[Union[str, 'Kind']] kind: Indicates the type of scheduled query rule. The default is LogAlert.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] mute_actions_duration: Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired. Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[str] override_query_time_range: If specified then overrides the query time range (default is WindowSize*NumberOfEvaluationPeriods). Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] rule_name: The name of the rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] scopes: The list of resource id's that this scheduled query rule is scoped to.
        :param pulumi.Input[float] severity: Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and required only for rules of the kind LogAlert.
        :param pulumi.Input[bool] skip_query_validation: The flag which indicates whether the provided query should be validated or not. The default is false. Relevant only for rules of the kind LogAlert.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] target_resource_types: List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria. Relevant only for rules of the kind LogAlert
        :param pulumi.Input[str] window_size: The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size). Relevant and required only for rules of the kind LogAlert.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduledQueryRuleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The scheduled query rule resource.

        :param str resource_name: The name of the resource.
        :param ScheduledQueryRuleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduledQueryRuleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 actions: Optional[pulumi.Input[pulumi.InputType['ActionsArgs']]] = None,
                 auto_mitigate: Optional[pulumi.Input[bool]] = None,
                 check_workspace_alerts_storage_configured: Optional[pulumi.Input[bool]] = None,
                 criteria: Optional[pulumi.Input[pulumi.InputType['ScheduledQueryRuleCriteriaArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[bool]] = None,
                 evaluation_frequency: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[Union[str, 'Kind']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 mute_actions_duration: Optional[pulumi.Input[str]] = None,
                 override_query_time_range: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 rule_name: Optional[pulumi.Input[str]] = None,
                 scopes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 severity: Optional[pulumi.Input[float]] = None,
                 skip_query_validation: Optional[pulumi.Input[bool]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 target_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 window_size: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduledQueryRuleArgs.__new__(ScheduledQueryRuleArgs)

            __props__.__dict__["actions"] = actions
            __props__.__dict__["auto_mitigate"] = auto_mitigate
            __props__.__dict__["check_workspace_alerts_storage_configured"] = check_workspace_alerts_storage_configured
            if criteria is None and not opts.urn:
                raise TypeError("Missing required property 'criteria'")
            __props__.__dict__["criteria"] = criteria
            __props__.__dict__["description"] = description
            __props__.__dict__["display_name"] = display_name
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["evaluation_frequency"] = evaluation_frequency
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["mute_actions_duration"] = mute_actions_duration
            __props__.__dict__["override_query_time_range"] = override_query_time_range
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["rule_name"] = rule_name
            if scopes is None and not opts.urn:
                raise TypeError("Missing required property 'scopes'")
            __props__.__dict__["scopes"] = scopes
            __props__.__dict__["severity"] = severity
            __props__.__dict__["skip_query_validation"] = skip_query_validation
            __props__.__dict__["tags"] = tags
            __props__.__dict__["target_resource_types"] = target_resource_types
            __props__.__dict__["window_size"] = window_size
            __props__.__dict__["created_with_api_version"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["is_legacy_log_analytics_rule"] = None
            __props__.__dict__["is_workspace_alerts_storage_configured"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:insights:ScheduledQueryRule"), pulumi.Alias(type_="azure-native:insights/v20180416:ScheduledQueryRule"), pulumi.Alias(type_="azure-native:insights/v20200501preview:ScheduledQueryRule"), pulumi.Alias(type_="azure-native:insights/v20210201preview:ScheduledQueryRule"), pulumi.Alias(type_="azure-native:insights/v20220615:ScheduledQueryRule"), pulumi.Alias(type_="azure-native:insights/v20220801preview:ScheduledQueryRule")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScheduledQueryRule, __self__).__init__(
            'azure-native:insights/v20210801:ScheduledQueryRule',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScheduledQueryRule':
        """
        Get an existing ScheduledQueryRule resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduledQueryRuleArgs.__new__(ScheduledQueryRuleArgs)

        __props__.__dict__["actions"] = None
        __props__.__dict__["auto_mitigate"] = None
        __props__.__dict__["check_workspace_alerts_storage_configured"] = None
        __props__.__dict__["created_with_api_version"] = None
        __props__.__dict__["criteria"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["evaluation_frequency"] = None
        __props__.__dict__["is_legacy_log_analytics_rule"] = None
        __props__.__dict__["is_workspace_alerts_storage_configured"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["mute_actions_duration"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["override_query_time_range"] = None
        __props__.__dict__["scopes"] = None
        __props__.__dict__["severity"] = None
        __props__.__dict__["skip_query_validation"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["target_resource_types"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["window_size"] = None
        return ScheduledQueryRule(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def actions(self) -> pulumi.Output[Optional['outputs.ActionsResponse']]:
        """
        Actions to invoke when the alert fires.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="autoMitigate")
    def auto_mitigate(self) -> pulumi.Output[Optional[bool]]:
        """
        The flag that indicates whether the alert should be automatically resolved or not. The default is true. Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "auto_mitigate")

    @property
    @pulumi.getter(name="checkWorkspaceAlertsStorageConfigured")
    def check_workspace_alerts_storage_configured(self) -> pulumi.Output[Optional[bool]]:
        """
        The flag which indicates whether this scheduled query rule should be stored in the customer's storage. The default is false. Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "check_workspace_alerts_storage_configured")

    @property
    @pulumi.getter(name="createdWithApiVersion")
    def created_with_api_version(self) -> pulumi.Output[str]:
        """
        The api-version used when creating this alert rule
        """
        return pulumi.get(self, "created_with_api_version")

    @property
    @pulumi.getter
    def criteria(self) -> pulumi.Output['outputs.ScheduledQueryRuleCriteriaResponse']:
        """
        The rule criteria that defines the conditions of the scheduled query rule.
        """
        return pulumi.get(self, "criteria")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        The description of the scheduled query rule.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The display name of the alert rule
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Output[bool]:
        """
        The flag which indicates whether this scheduled query rule is enabled. Value should be true or false
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        The etag field is *not* required. If it is provided in the response body, it must also be provided as a header per the normal etag convention.  Entity tags are used for comparing two or more entities from the same requested resource. HTTP/1.1 uses entity tags in the etag (section 14.19), If-Match (section 14.24), If-None-Match (section 14.26), and If-Range (section 14.27) header fields. 
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="evaluationFrequency")
    def evaluation_frequency(self) -> pulumi.Output[Optional[str]]:
        """
        How often the scheduled query rule is evaluated represented in ISO 8601 duration format. Relevant and required only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "evaluation_frequency")

    @property
    @pulumi.getter(name="isLegacyLogAnalyticsRule")
    def is_legacy_log_analytics_rule(self) -> pulumi.Output[bool]:
        """
        True if alert rule is legacy Log Analytic rule
        """
        return pulumi.get(self, "is_legacy_log_analytics_rule")

    @property
    @pulumi.getter(name="isWorkspaceAlertsStorageConfigured")
    def is_workspace_alerts_storage_configured(self) -> pulumi.Output[bool]:
        """
        The flag which indicates whether this scheduled query rule has been configured to be stored in the customer's storage. The default is false.
        """
        return pulumi.get(self, "is_workspace_alerts_storage_configured")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Indicates the type of scheduled query rule. The default is LogAlert.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="muteActionsDuration")
    def mute_actions_duration(self) -> pulumi.Output[Optional[str]]:
        """
        Mute actions for the chosen period of time (in ISO 8601 duration format) after the alert is fired. Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "mute_actions_duration")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="overrideQueryTimeRange")
    def override_query_time_range(self) -> pulumi.Output[Optional[str]]:
        """
        If specified then overrides the query time range (default is WindowSize*NumberOfEvaluationPeriods). Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "override_query_time_range")

    @property
    @pulumi.getter
    def scopes(self) -> pulumi.Output[Sequence[str]]:
        """
        The list of resource id's that this scheduled query rule is scoped to.
        """
        return pulumi.get(self, "scopes")

    @property
    @pulumi.getter
    def severity(self) -> pulumi.Output[Optional[float]]:
        """
        Severity of the alert. Should be an integer between [0-4]. Value of 0 is severest. Relevant and required only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "severity")

    @property
    @pulumi.getter(name="skipQueryValidation")
    def skip_query_validation(self) -> pulumi.Output[Optional[bool]]:
        """
        The flag which indicates whether the provided query should be validated or not. The default is false. Relevant only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "skip_query_validation")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        SystemData of ScheduledQueryRule.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="targetResourceTypes")
    def target_resource_types(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of resource type of the target resource(s) on which the alert is created/updated. For example if the scope is a resource group and targetResourceTypes is Microsoft.Compute/virtualMachines, then a different alert will be fired for each virtual machine in the resource group which meet the alert criteria. Relevant only for rules of the kind LogAlert
        """
        return pulumi.get(self, "target_resource_types")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="windowSize")
    def window_size(self) -> pulumi.Output[Optional[str]]:
        """
        The period of time (in ISO 8601 duration format) on which the Alert query will be executed (bin size). Relevant and required only for rules of the kind LogAlert.
        """
        return pulumi.get(self, "window_size")

