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
    'GetCustomerSubscriptionResult',
    'AwaitableGetCustomerSubscriptionResult',
    'get_customer_subscription',
    'get_customer_subscription_output',
]

@pulumi.output_type
class GetCustomerSubscriptionResult:
    """
    Customer subscription.
    """
    def __init__(__self__, etag=None, id=None, name=None, tenant_id=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        The entity tag used for optimistic concurrency when modifying the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        Tenant Id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of Resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetCustomerSubscriptionResult(GetCustomerSubscriptionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomerSubscriptionResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            tenant_id=self.tenant_id,
            type=self.type)


def get_customer_subscription(customer_subscription_name: Optional[str] = None,
                              registration_name: Optional[str] = None,
                              resource_group: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomerSubscriptionResult:
    """
    Returns the specified product.


    :param str customer_subscription_name: Name of the product.
    :param str registration_name: Name of the Azure Stack registration.
    :param str resource_group: Name of the resource group.
    """
    __args__ = dict()
    __args__['customerSubscriptionName'] = customer_subscription_name
    __args__['registrationName'] = registration_name
    __args__['resourceGroup'] = resource_group
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestack/v20220601:getCustomerSubscription', __args__, opts=opts, typ=GetCustomerSubscriptionResult).value

    return AwaitableGetCustomerSubscriptionResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        tenant_id=__ret__.tenant_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_customer_subscription)
def get_customer_subscription_output(customer_subscription_name: Optional[pulumi.Input[str]] = None,
                                     registration_name: Optional[pulumi.Input[str]] = None,
                                     resource_group: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomerSubscriptionResult]:
    """
    Returns the specified product.


    :param str customer_subscription_name: Name of the product.
    :param str registration_name: Name of the Azure Stack registration.
    :param str resource_group: Name of the resource group.
    """
    ...
