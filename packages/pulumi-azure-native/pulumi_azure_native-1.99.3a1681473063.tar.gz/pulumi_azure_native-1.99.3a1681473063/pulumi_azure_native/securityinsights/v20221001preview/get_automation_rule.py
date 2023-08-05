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
    'GetAutomationRuleResult',
    'AwaitableGetAutomationRuleResult',
    'get_automation_rule',
    'get_automation_rule_output',
]

@pulumi.output_type
class GetAutomationRuleResult:
    def __init__(__self__, actions=None, created_by=None, created_time_utc=None, display_name=None, etag=None, id=None, last_modified_by=None, last_modified_time_utc=None, name=None, order=None, system_data=None, triggering_logic=None, type=None):
        if actions and not isinstance(actions, list):
            raise TypeError("Expected argument 'actions' to be a list")
        pulumi.set(__self__, "actions", actions)
        if created_by and not isinstance(created_by, dict):
            raise TypeError("Expected argument 'created_by' to be a dict")
        pulumi.set(__self__, "created_by", created_by)
        if created_time_utc and not isinstance(created_time_utc, str):
            raise TypeError("Expected argument 'created_time_utc' to be a str")
        pulumi.set(__self__, "created_time_utc", created_time_utc)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_by and not isinstance(last_modified_by, dict):
            raise TypeError("Expected argument 'last_modified_by' to be a dict")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_time_utc and not isinstance(last_modified_time_utc, str):
            raise TypeError("Expected argument 'last_modified_time_utc' to be a str")
        pulumi.set(__self__, "last_modified_time_utc", last_modified_time_utc)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if order and not isinstance(order, int):
            raise TypeError("Expected argument 'order' to be a int")
        pulumi.set(__self__, "order", order)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if triggering_logic and not isinstance(triggering_logic, dict):
            raise TypeError("Expected argument 'triggering_logic' to be a dict")
        pulumi.set(__self__, "triggering_logic", triggering_logic)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def actions(self) -> Sequence[Any]:
        """
        The actions to execute when the automation rule is triggered.
        """
        return pulumi.get(self, "actions")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> 'outputs.ClientInfoResponse':
        """
        Information on the client (user or application) that made some action
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdTimeUtc")
    def created_time_utc(self) -> str:
        """
        The time the automation rule was created.
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> str:
        """
        The display name of the automation rule.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> 'outputs.ClientInfoResponse':
        """
        Information on the client (user or application) that made some action
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTimeUtc")
    def last_modified_time_utc(self) -> str:
        """
        The last time the automation rule was updated.
        """
        return pulumi.get(self, "last_modified_time_utc")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def order(self) -> int:
        """
        The order of execution of the automation rule.
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="triggeringLogic")
    def triggering_logic(self) -> 'outputs.AutomationRuleTriggeringLogicResponse':
        """
        Describes automation rule triggering logic.
        """
        return pulumi.get(self, "triggering_logic")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAutomationRuleResult(GetAutomationRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAutomationRuleResult(
            actions=self.actions,
            created_by=self.created_by,
            created_time_utc=self.created_time_utc,
            display_name=self.display_name,
            etag=self.etag,
            id=self.id,
            last_modified_by=self.last_modified_by,
            last_modified_time_utc=self.last_modified_time_utc,
            name=self.name,
            order=self.order,
            system_data=self.system_data,
            triggering_logic=self.triggering_logic,
            type=self.type)


def get_automation_rule(automation_rule_id: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        workspace_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAutomationRuleResult:
    """
    Gets the automation rule.


    :param str automation_rule_id: Automation rule ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['automationRuleId'] = automation_rule_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20221001preview:getAutomationRule', __args__, opts=opts, typ=GetAutomationRuleResult).value

    return AwaitableGetAutomationRuleResult(
        actions=__ret__.actions,
        created_by=__ret__.created_by,
        created_time_utc=__ret__.created_time_utc,
        display_name=__ret__.display_name,
        etag=__ret__.etag,
        id=__ret__.id,
        last_modified_by=__ret__.last_modified_by,
        last_modified_time_utc=__ret__.last_modified_time_utc,
        name=__ret__.name,
        order=__ret__.order,
        system_data=__ret__.system_data,
        triggering_logic=__ret__.triggering_logic,
        type=__ret__.type)


@_utilities.lift_output_func(get_automation_rule)
def get_automation_rule_output(automation_rule_id: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               workspace_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAutomationRuleResult]:
    """
    Gets the automation rule.


    :param str automation_rule_id: Automation rule ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
