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

__all__ = ['RouteMapArgs', 'RouteMap']

@pulumi.input_type
class RouteMapArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 virtual_hub_name: pulumi.Input[str],
                 associated_inbound_connections: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 associated_outbound_connections: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 route_map_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input['RouteMapRuleArgs']]]] = None):
        """
        The set of arguments for constructing a RouteMap resource.
        :param pulumi.Input[str] resource_group_name: The resource group name of the RouteMap's resource group.
        :param pulumi.Input[str] virtual_hub_name: The name of the VirtualHub containing the RouteMap.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_inbound_connections: List of connections which have this RoutMap associated for inbound traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_outbound_connections: List of connections which have this RoutMap associated for outbound traffic.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] route_map_name: The name of the RouteMap.
        :param pulumi.Input[Sequence[pulumi.Input['RouteMapRuleArgs']]] rules: List of RouteMap rules to be applied.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "virtual_hub_name", virtual_hub_name)
        if associated_inbound_connections is not None:
            pulumi.set(__self__, "associated_inbound_connections", associated_inbound_connections)
        if associated_outbound_connections is not None:
            pulumi.set(__self__, "associated_outbound_connections", associated_outbound_connections)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if route_map_name is not None:
            pulumi.set(__self__, "route_map_name", route_map_name)
        if rules is not None:
            pulumi.set(__self__, "rules", rules)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name of the RouteMap's resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="virtualHubName")
    def virtual_hub_name(self) -> pulumi.Input[str]:
        """
        The name of the VirtualHub containing the RouteMap.
        """
        return pulumi.get(self, "virtual_hub_name")

    @virtual_hub_name.setter
    def virtual_hub_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_hub_name", value)

    @property
    @pulumi.getter(name="associatedInboundConnections")
    def associated_inbound_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of connections which have this RoutMap associated for inbound traffic.
        """
        return pulumi.get(self, "associated_inbound_connections")

    @associated_inbound_connections.setter
    def associated_inbound_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "associated_inbound_connections", value)

    @property
    @pulumi.getter(name="associatedOutboundConnections")
    def associated_outbound_connections(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        List of connections which have this RoutMap associated for outbound traffic.
        """
        return pulumi.get(self, "associated_outbound_connections")

    @associated_outbound_connections.setter
    def associated_outbound_connections(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "associated_outbound_connections", value)

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
    @pulumi.getter(name="routeMapName")
    def route_map_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the RouteMap.
        """
        return pulumi.get(self, "route_map_name")

    @route_map_name.setter
    def route_map_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_map_name", value)

    @property
    @pulumi.getter
    def rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['RouteMapRuleArgs']]]]:
        """
        List of RouteMap rules to be applied.
        """
        return pulumi.get(self, "rules")

    @rules.setter
    def rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['RouteMapRuleArgs']]]]):
        pulumi.set(self, "rules", value)


class RouteMap(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_inbound_connections: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 associated_outbound_connections: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_map_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteMapRuleArgs']]]]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The RouteMap child resource of a Virtual hub.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_inbound_connections: List of connections which have this RoutMap associated for inbound traffic.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] associated_outbound_connections: List of connections which have this RoutMap associated for outbound traffic.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] resource_group_name: The resource group name of the RouteMap's resource group.
        :param pulumi.Input[str] route_map_name: The name of the RouteMap.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteMapRuleArgs']]]] rules: List of RouteMap rules to be applied.
        :param pulumi.Input[str] virtual_hub_name: The name of the VirtualHub containing the RouteMap.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: RouteMapArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The RouteMap child resource of a Virtual hub.

        :param str resource_name: The name of the resource.
        :param RouteMapArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(RouteMapArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 associated_inbound_connections: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 associated_outbound_connections: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_map_name: Optional[pulumi.Input[str]] = None,
                 rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['RouteMapRuleArgs']]]]] = None,
                 virtual_hub_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = RouteMapArgs.__new__(RouteMapArgs)

            __props__.__dict__["associated_inbound_connections"] = associated_inbound_connections
            __props__.__dict__["associated_outbound_connections"] = associated_outbound_connections
            __props__.__dict__["id"] = id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["route_map_name"] = route_map_name
            __props__.__dict__["rules"] = rules
            if virtual_hub_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_hub_name'")
            __props__.__dict__["virtual_hub_name"] = virtual_hub_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network/v20220501:RouteMap"), pulumi.Alias(type_="azure-native:network/v20220901:RouteMap")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(RouteMap, __self__).__init__(
            'azure-native:network/v20220701:RouteMap',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'RouteMap':
        """
        Get an existing RouteMap resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = RouteMapArgs.__new__(RouteMapArgs)

        __props__.__dict__["associated_inbound_connections"] = None
        __props__.__dict__["associated_outbound_connections"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rules"] = None
        __props__.__dict__["type"] = None
        return RouteMap(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="associatedInboundConnections")
    def associated_inbound_connections(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of connections which have this RoutMap associated for inbound traffic.
        """
        return pulumi.get(self, "associated_inbound_connections")

    @property
    @pulumi.getter(name="associatedOutboundConnections")
    def associated_outbound_connections(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        List of connections which have this RoutMap associated for outbound traffic.
        """
        return pulumi.get(self, "associated_outbound_connections")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the RouteMap resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def rules(self) -> pulumi.Output[Optional[Sequence['outputs.RouteMapRuleResponse']]]:
        """
        List of RouteMap rules to be applied.
        """
        return pulumi.get(self, "rules")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

