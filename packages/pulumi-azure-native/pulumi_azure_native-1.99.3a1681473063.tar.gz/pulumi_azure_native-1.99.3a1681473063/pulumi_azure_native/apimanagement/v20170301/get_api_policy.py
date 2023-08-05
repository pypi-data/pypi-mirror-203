# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetApiPolicyResult',
    'AwaitableGetApiPolicyResult',
    'get_api_policy',
    'get_api_policy_output',
]

@pulumi.output_type
class GetApiPolicyResult:
    """
    Policy Contract details.
    """
    def __init__(__self__, id=None, name=None, policy_content=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if policy_content and not isinstance(policy_content, str):
            raise TypeError("Expected argument 'policy_content' to be a str")
        pulumi.set(__self__, "policy_content", policy_content)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="policyContent")
    def policy_content(self) -> str:
        """
        Json escaped Xml Encoded contents of the Policy.
        """
        return pulumi.get(self, "policy_content")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetApiPolicyResult(GetApiPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiPolicyResult(
            id=self.id,
            name=self.name,
            policy_content=self.policy_content,
            type=self.type)


def get_api_policy(api_id: Optional[str] = None,
                   policy_id: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   service_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiPolicyResult:
    """
    Get the policy configuration at the API level.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str policy_id: The identifier of the Policy.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['policyId'] = policy_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20170301:getApiPolicy', __args__, opts=opts, typ=GetApiPolicyResult).value

    return AwaitableGetApiPolicyResult(
        id=__ret__.id,
        name=__ret__.name,
        policy_content=__ret__.policy_content,
        type=__ret__.type)


@_utilities.lift_output_func(get_api_policy)
def get_api_policy_output(api_id: Optional[pulumi.Input[str]] = None,
                          policy_id: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          service_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiPolicyResult]:
    """
    Get the policy configuration at the API level.


    :param str api_id: API revision identifier. Must be unique in the current API Management service instance. Non-current revision has ;rev=n as a suffix where n is the revision number.
    :param str policy_id: The identifier of the Policy.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...
