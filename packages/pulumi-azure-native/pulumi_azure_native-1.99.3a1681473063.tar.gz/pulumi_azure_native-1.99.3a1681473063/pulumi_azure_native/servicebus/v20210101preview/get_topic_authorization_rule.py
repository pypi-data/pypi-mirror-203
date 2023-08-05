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
    'GetTopicAuthorizationRuleResult',
    'AwaitableGetTopicAuthorizationRuleResult',
    'get_topic_authorization_rule',
    'get_topic_authorization_rule_output',
]

@pulumi.output_type
class GetTopicAuthorizationRuleResult:
    """
    Description of a namespace authorization rule.
    """
    def __init__(__self__, id=None, name=None, rights=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rights and not isinstance(rights, list):
            raise TypeError("Expected argument 'rights' to be a list")
        pulumi.set(__self__, "rights", rights)
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
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rights(self) -> Sequence[str]:
        """
        The rights associated with the rule.
        """
        return pulumi.get(self, "rights")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system meta data relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetTopicAuthorizationRuleResult(GetTopicAuthorizationRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTopicAuthorizationRuleResult(
            id=self.id,
            name=self.name,
            rights=self.rights,
            system_data=self.system_data,
            type=self.type)


def get_topic_authorization_rule(authorization_rule_name: Optional[str] = None,
                                 namespace_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 topic_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTopicAuthorizationRuleResult:
    """
    Returns the specified authorization rule.


    :param str authorization_rule_name: The authorization rule name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str topic_name: The topic name.
    """
    __args__ = dict()
    __args__['authorizationRuleName'] = authorization_rule_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['topicName'] = topic_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicebus/v20210101preview:getTopicAuthorizationRule', __args__, opts=opts, typ=GetTopicAuthorizationRuleResult).value

    return AwaitableGetTopicAuthorizationRuleResult(
        id=__ret__.id,
        name=__ret__.name,
        rights=__ret__.rights,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_topic_authorization_rule)
def get_topic_authorization_rule_output(authorization_rule_name: Optional[pulumi.Input[str]] = None,
                                        namespace_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        topic_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTopicAuthorizationRuleResult]:
    """
    Returns the specified authorization rule.


    :param str authorization_rule_name: The authorization rule name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    :param str topic_name: The topic name.
    """
    ...
