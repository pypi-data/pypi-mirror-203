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
from ._inputs import *

__all__ = ['RoutingIntentArgs', 'RoutingIntent']

@pulumi.input_type
class RoutingIntentArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_hub_name: pulumi.Input[str],
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 routing_intent_name: Optional[pulumi.Input[str]] = None,
                 routing_policies: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingPolicyArgs']]]] = None):
        """
        The set of arguments for constructing a RoutingIntent resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the RoutingIntent.
        :param pulumi.Input[str] virtual_hub_name: The name of the VirtualHub.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[str] routing_intent_name: The name of the per VirtualHub singleton Routing Intent resource.
        :param pulumi.Input[Sequence[pulumi.Input['RoutingPolicyArgs']]] routing_policies: List of routing policies.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_hub_name", virtual_hub_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if routing_intent_name is not None:
            pulumi.set(__self__, "routing_intent_name", routing_intent_name)
        if routing_policies is not None:
            pulumi.set(__self__, "routing_policies", routing_policies)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the RoutingIntent.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> pulumi.Input[str]:
        """
        The name of the VirtualHub.
        """
        return pulumi.get(self, "virtual_hub_name")

    @virtual_hub_name.setter
    def virtual_hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_hub_name", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="routingIntentName")
    def routing_intent_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the per VirtualHub singleton Routing Intent resource.
        """
        return pulumi.get(self, "routing_intent_name")

    @routing_intent_name.setter
    def routing_intent_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "routing_intent_name", value)

    @property
    @pulumi.getter(name="routingPolicies")
    def routing_policies(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RoutingPolicyArgs']]]]:
        """
        List of routing policies.
        """
        return pulumi.get(self, "routing_policies")

    @routing_policies.setter
    def routing_policies(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RoutingPolicyArgs']]]]):
        pulumi.set(self, "routing_policies", value)


class RoutingIntent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_intent_name: Optional[pulumi.Input[str]] = None,
                 routing_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingPolicyArgs']]]]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The routing intent child resource of a Virtual hub.
        API Version: 2022-01-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: The name of the resource that is unique within a resource group. This name can be used to access the resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the RoutingIntent.
        :param pulumi.Input[str] routing_intent_name: The name of the per VirtualHub singleton Routing Intent resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingPolicyArgs']]]] routing_policies: List of routing policies.
        :param pulumi.Input[str] virtual_hub_name: The name of the VirtualHub.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RoutingIntentArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The routing intent child resource of a Virtual hub.
        API Version: 2022-01-01.

        :param str resource_name: The name of the resource.
        :param RoutingIntentArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RoutingIntentArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 routing_intent_name: Optional[pulumi.Input[str]] = None,
                 routing_policies: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RoutingPolicyArgs']]]]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RoutingIntentArgs.__new__(RoutingIntentArgs)

            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["routing_intent_name"] = routing_intent_name
            __props__.__dict__["routing_policies"] = routing_policies
            if virtual_hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub_name'")
            __props__.__dict__["virtual_hub_name"] = virtual_hub_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20210501:RoutingIntent"), pulumi.Alias(type_="azure-native:network/v20210801:RoutingIntent"), pulumi.Alias(type_="azure-native:network/v20220101:RoutingIntent"), pulumi.Alias(type_="azure-native:network/v20220501:RoutingIntent"), pulumi.Alias(type_="azure-native:network/v20220701:RoutingIntent"), pulumi.Alias(type_="azure-native:network/v20220901:RoutingIntent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RoutingIntent, __self__).__init__(
            'azure-native:network:RoutingIntent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RoutingIntent':
        """
        Get an existing RoutingIntent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RoutingIntentArgs.__new__(RoutingIntentArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["routing_policies"] = None
        __props__.__dict__["type"] = None
        return RoutingIntent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the RoutingIntent resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="routingPolicies")
    def routing_policies(self) -> pulumi.Output[Optional[Sequence['outputs.RoutingPolicyResponse']]]:
        """
        List of routing policies.
        """
        return pulumi.get(self, "routing_policies")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

