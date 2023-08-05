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
    'GetNamespaceAuthorizationRuleResult',
    'AwaitableGetNamespaceAuthorizationRuleResult',
    'get_namespace_authorization_rule',
    'get_namespace_authorization_rule_output',
]

warnings.warn("""Version 2016-03-01 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetNamespaceAuthorizationRuleResult:
    """
    Description of a Namespace AuthorizationRules.
    """
    def __init__(__self__, id=None, location=None, name=None, rights=None, sku=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if rights and not isinstance(rights, list):
            raise TypeError("Expected argument 'rights' to be a list")
        pulumi.set(__self__, "rights", rights)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
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
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def rights(self) -> Optional[Sequence[str]]:
        """
        The rights associated with the rule.
        """
        return pulumi.get(self, "rights")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The sku of the created namespace
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetNamespaceAuthorizationRuleResult(GetNamespaceAuthorizationRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceAuthorizationRuleResult(
            id=self.id,
            location=self.location,
            name=self.name,
            rights=self.rights,
            sku=self.sku,
            tags=self.tags,
            type=self.type)


def get_namespace_authorization_rule(authorization_rule_name: Optional[str] = None,
                                     namespace_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceAuthorizationRuleResult:
    """
    Gets an authorization rule for a namespace by name.


    :param str authorization_rule_name: Authorization rule name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_namespace_authorization_rule is deprecated: Version 2016-03-01 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['authorizationRuleName'] = authorization_rule_name
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:notificationhubs/v20160301:getNamespaceAuthorizationRule', __args__, opts=opts, typ=GetNamespaceAuthorizationRuleResult).value

    return AwaitableGetNamespaceAuthorizationRuleResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        rights=__ret__.rights,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_namespace_authorization_rule)
def get_namespace_authorization_rule_output(authorization_rule_name: Optional[pulumi.Input[str]] = None,
                                            namespace_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceAuthorizationRuleResult]:
    """
    Gets an authorization rule for a namespace by name.


    :param str authorization_rule_name: Authorization rule name.
    :param str namespace_name: The namespace name
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_namespace_authorization_rule is deprecated: Version 2016-03-01 will be removed in v2 of the provider.""")
    ...
