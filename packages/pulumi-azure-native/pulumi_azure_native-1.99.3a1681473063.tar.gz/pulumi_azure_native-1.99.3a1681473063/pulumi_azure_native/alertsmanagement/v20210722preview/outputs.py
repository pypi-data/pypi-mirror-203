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
    'PrometheusRuleGroupActionResponse',
    'PrometheusRuleResolveConfigurationResponse',
    'PrometheusRuleResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class PrometheusRuleGroupActionResponse(dict):
    """
    An alert action. Only relevant for alerts.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionGroupId":
            suggest = "action_group_id"
        elif key == "actionProperties":
            suggest = "action_properties"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrometheusRuleGroupActionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrometheusRuleGroupActionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrometheusRuleGroupActionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 action_group_id: Optional[str] = None,
                 action_properties: Optional[Mapping[str, str]] = None):
        """
        An alert action. Only relevant for alerts.
        :param str action_group_id: The resource id of the action group to use.
        :param Mapping[str, str] action_properties: The properties of an action group object.
        """
        if action_group_id is not None:
            pulumi.set(__self__, "action_group_id", action_group_id)
        if action_properties is not None:
            pulumi.set(__self__, "action_properties", action_properties)

    @property
    @pulumi.getter(name="actionGroupId")
    def action_group_id(self) -> Optional[str]:
        """
        The resource id of the action group to use.
        """
        return pulumi.get(self, "action_group_id")

    @property
    @pulumi.getter(name="actionProperties")
    def action_properties(self) -> Optional[Mapping[str, str]]:
        """
        The properties of an action group object.
        """
        return pulumi.get(self, "action_properties")


@pulumi.output_type
class PrometheusRuleResolveConfigurationResponse(dict):
    """
    Specifies the Prometheus alert rule configuration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "autoResolved":
            suggest = "auto_resolved"
        elif key == "timeToResolve":
            suggest = "time_to_resolve"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrometheusRuleResolveConfigurationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrometheusRuleResolveConfigurationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrometheusRuleResolveConfigurationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 auto_resolved: Optional[bool] = None,
                 time_to_resolve: Optional[str] = None):
        """
        Specifies the Prometheus alert rule configuration.
        :param bool auto_resolved: the flag that indicates whether or not to auto resolve a fired alert.
        :param str time_to_resolve: the duration a rule must evaluate as healthy before the fired alert is automatically resolved represented in ISO 8601 duration format. Should be between 1 and 15 minutes
        """
        if auto_resolved is not None:
            pulumi.set(__self__, "auto_resolved", auto_resolved)
        if time_to_resolve is not None:
            pulumi.set(__self__, "time_to_resolve", time_to_resolve)

    @property
    @pulumi.getter(name="autoResolved")
    def auto_resolved(self) -> Optional[bool]:
        """
        the flag that indicates whether or not to auto resolve a fired alert.
        """
        return pulumi.get(self, "auto_resolved")

    @property
    @pulumi.getter(name="timeToResolve")
    def time_to_resolve(self) -> Optional[str]:
        """
        the duration a rule must evaluate as healthy before the fired alert is automatically resolved represented in ISO 8601 duration format. Should be between 1 and 15 minutes
        """
        return pulumi.get(self, "time_to_resolve")


@pulumi.output_type
class PrometheusRuleResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "for":
            suggest = "for_"
        elif key == "resolveConfiguration":
            suggest = "resolve_configuration"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrometheusRuleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrometheusRuleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrometheusRuleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 expression: str,
                 actions: Optional[Sequence['outputs.PrometheusRuleGroupActionResponse']] = None,
                 alert: Optional[str] = None,
                 annotations: Optional[Mapping[str, str]] = None,
                 enabled: Optional[bool] = None,
                 for_: Optional[str] = None,
                 labels: Optional[Mapping[str, str]] = None,
                 record: Optional[str] = None,
                 resolve_configuration: Optional['outputs.PrometheusRuleResolveConfigurationResponse'] = None,
                 severity: Optional[int] = None):
        """
        :param str expression: the expression to run for the rule.
        :param Sequence['PrometheusRuleGroupActionResponse'] actions: The array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved. Only relevant for alerts.
        :param str alert: the name of the alert rule.
        :param Mapping[str, str] annotations: annotations for rule group. Only relevant for alerts.
        :param bool enabled: the flag that indicates whether the Prometheus rule is enabled.
        :param str for_: the amount of time alert must be active before firing. Only relevant for alerts.
        :param Mapping[str, str] labels: labels for rule group. Only relevant for alerts.
        :param str record: the name of the recording rule.
        :param 'PrometheusRuleResolveConfigurationResponse' resolve_configuration: defines the configuration for resolving fired alerts. Only relevant for alerts.
        :param int severity: the severity of the alerts fired by the rule. Only relevant for alerts.
        """
        pulumi.set(__self__, "expression", expression)
        if actions is not None:
            pulumi.set(__self__, "actions", actions)
        if alert is not None:
            pulumi.set(__self__, "alert", alert)
        if annotations is not None:
            pulumi.set(__self__, "annotations", annotations)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if for_ is not None:
            pulumi.set(__self__, "for_", for_)
        if labels is not None:
            pulumi.set(__self__, "labels", labels)
        if record is not None:
            pulumi.set(__self__, "record", record)
        if resolve_configuration is not None:
            pulumi.set(__self__, "resolve_configuration", resolve_configuration)
        if severity is not None:
            pulumi.set(__self__, "severity", severity)

    @property
    @pulumi.getter
    def expression(self) -> str:
        """
        the expression to run for the rule.
        """
        return pulumi.get(self, "expression")

    @property
    @pulumi.getter
    def actions(self) -> Optional[Sequence['outputs.PrometheusRuleGroupActionResponse']]:
        """
        The array of actions that are performed when the alert rule becomes active, and when an alert condition is resolved. Only relevant for alerts.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter
    def alert(self) -> Optional[str]:
        """
        the name of the alert rule.
        """
        return pulumi.get(self, "alert")

    @property
    @pulumi.getter
    def annotations(self) -> Optional[Mapping[str, str]]:
        """
        annotations for rule group. Only relevant for alerts.
        """
        return pulumi.get(self, "annotations")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        the flag that indicates whether the Prometheus rule is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="for")
    def for_(self) -> Optional[str]:
        """
        the amount of time alert must be active before firing. Only relevant for alerts.
        """
        return pulumi.get(self, "for_")

    @property
    @pulumi.getter
    def labels(self) -> Optional[Mapping[str, str]]:
        """
        labels for rule group. Only relevant for alerts.
        """
        return pulumi.get(self, "labels")

    @property
    @pulumi.getter
    def record(self) -> Optional[str]:
        """
        the name of the recording rule.
        """
        return pulumi.get(self, "record")

    @property
    @pulumi.getter(name="resolveConfiguration")
    def resolve_configuration(self) -> Optional['outputs.PrometheusRuleResolveConfigurationResponse']:
        """
        defines the configuration for resolving fired alerts. Only relevant for alerts.
        """
        return pulumi.get(self, "resolve_configuration")

    @property
    @pulumi.getter
    def severity(self) -> Optional[int]:
        """
        the severity of the alerts fired by the rule. Only relevant for alerts.
        """
        return pulumi.get(self, "severity")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


