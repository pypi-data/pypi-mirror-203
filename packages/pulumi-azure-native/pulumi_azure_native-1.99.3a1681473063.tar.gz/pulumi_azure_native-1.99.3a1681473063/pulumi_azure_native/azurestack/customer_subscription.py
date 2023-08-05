# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = ['CustomerSubscriptionArgs', 'CustomerSubscription']

@pulumi.input_type
class CustomerSubscriptionArgs:
    def __init__(__self__, *,
                 registration_name: pulumi.Input[str],
                 resource_group: pulumi.Input[str],
                 customer_subscription_name: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a CustomerSubscription resource.
        :param pulumi.Input[str] registration_name: Name of the Azure Stack registration.
        :param pulumi.Input[str] resource_group: Name of the resource group.
        :param pulumi.Input[str] customer_subscription_name: Name of the product.
        :param pulumi.Input[str] tenant_id: Tenant Id.
        """
        pulumi.set(__self__, "registration_name", registration_name)
        pulumi.set(__self__, "resource_group", resource_group)
        if customer_subscription_name is not None:
            pulumi.set(__self__, "customer_subscription_name", customer_subscription_name)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="registrationName")
    def registration_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Stack registration.
        """
        return pulumi.get(self, "registration_name")

    @registration_name.setter
    def registration_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "registration_name", value)

    @property
    @pulumi.getter(name="resourceGroup")
    def resource_group(self) -> pulumi.Input[str]:
        """
        Name of the resource group.
        """
        return pulumi.get(self, "resource_group")

    @resource_group.setter
    def resource_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group", value)

    @property
    @pulumi.getter(name="customerSubscriptionName")
    def customer_subscription_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the product.
        """
        return pulumi.get(self, "customer_subscription_name")

    @customer_subscription_name.setter
    def customer_subscription_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "customer_subscription_name", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        Tenant Id.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


class CustomerSubscription(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_subscription_name: Optional[pulumi.Input[str]] = None,
                 registration_name: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Customer subscription.
        API Version: 2017-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] customer_subscription_name: Name of the product.
        :param pulumi.Input[str] registration_name: Name of the Azure Stack registration.
        :param pulumi.Input[str] resource_group: Name of the resource group.
        :param pulumi.Input[str] tenant_id: Tenant Id.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CustomerSubscriptionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Customer subscription.
        API Version: 2017-06-01.

        :param str resource_name: The name of the resource.
        :param CustomerSubscriptionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CustomerSubscriptionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 customer_subscription_name: Optional[pulumi.Input[str]] = None,
                 registration_name: Optional[pulumi.Input[str]] = None,
                 resource_group: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CustomerSubscriptionArgs.__new__(CustomerSubscriptionArgs)

            __props__.__dict__["customer_subscription_name"] = customer_subscription_name
            if registration_name is None and not opts.urn:
                raise TypeError("Missing required property 'registration_name'")
            __props__.__dict__["registration_name"] = registration_name
            if resource_group is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group'")
            __props__.__dict__["resource_group"] = resource_group
            __props__.__dict__["tenant_id"] = tenant_id
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:azurestack/v20170601:CustomerSubscription"), pulumi.Alias(type_="azure-native:azurestack/v20200601preview:CustomerSubscription"), pulumi.Alias(type_="azure-native:azurestack/v20220601:CustomerSubscription")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(CustomerSubscription, __self__).__init__(
            'azure-native:azurestack:CustomerSubscription',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'CustomerSubscription':
        """
        Get an existing CustomerSubscription resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CustomerSubscriptionArgs.__new__(CustomerSubscriptionArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return CustomerSubscription(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        The entity tag used for optimistic concurrency when modifying the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        Tenant Id.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of Resource.
        """
        return pulumi.get(self, "type")

