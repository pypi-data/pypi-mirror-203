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
    'ListSubscriptionSecretsResult',
    'AwaitableListSubscriptionSecretsResult',
    'list_subscription_secrets',
    'list_subscription_secrets_output',
]

@pulumi.output_type
class ListSubscriptionSecretsResult:
    """
    Subscription keys.
    """
    def __init__(__self__, primary_key=None, secondary_key=None):
        if primary_key and not isinstance(primary_key, str):
            raise TypeError("Expected argument 'primary_key' to be a str")
        pulumi.set(__self__, "primary_key", primary_key)
        if secondary_key and not isinstance(secondary_key, str):
            raise TypeError("Expected argument 'secondary_key' to be a str")
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> Optional[str]:
        """
        Subscription primary key.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> Optional[str]:
        """
        Subscription secondary key.
        """
        return pulumi.get(self, "secondary_key")


class AwaitableListSubscriptionSecretsResult(ListSubscriptionSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListSubscriptionSecretsResult(
            primary_key=self.primary_key,
            secondary_key=self.secondary_key)


def list_subscription_secrets(resource_group_name: Optional[str] = None,
                              service_name: Optional[str] = None,
                              sid: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListSubscriptionSecretsResult:
    """
    Gets the specified Subscription keys.


    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    :param str sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    __args__['sid'] = sid
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20210101preview:listSubscriptionSecrets', __args__, opts=opts, typ=ListSubscriptionSecretsResult).value

    return AwaitableListSubscriptionSecretsResult(
        primary_key=__ret__.primary_key,
        secondary_key=__ret__.secondary_key)


@_utilities.lift_output_func(list_subscription_secrets)
def list_subscription_secrets_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                     service_name: Optional[pulumi.Input[str]] = None,
                                     sid: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListSubscriptionSecretsResult]:
    """
    Gets the specified Subscription keys.


    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    :param str sid: Subscription entity Identifier. The entity represents the association between a user and a product in API Management.
    """
    ...
