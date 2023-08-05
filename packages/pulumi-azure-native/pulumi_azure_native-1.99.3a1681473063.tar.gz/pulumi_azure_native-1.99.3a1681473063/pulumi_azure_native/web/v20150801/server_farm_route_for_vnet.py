# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ServerFarmRouteForVnetArgs', 'ServerFarmRouteForVnet']

@pulumi.input_type
class ServerFarmRouteForVnetArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 vnet_name: pulumi.Input[str],
                 end_address: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 route_type: Optional[pulumi.Input[str]] = None,
                 start_address: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerFarmRouteForVnet resource.
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[str] vnet_name: Name of virtual network
        :param pulumi.Input[str] end_address: The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] route_name: Name of the virtual network route
        :param pulumi.Input[str] route_type: The type of route this is:
                           DEFAULT - By default, every web app has routes to the local address ranges specified by RFC1918
                           INHERITED - Routes inherited from the real Virtual Network routes
                           STATIC - Static route set on the web app only
                           
                           These values will be used for syncing a Web App's routes with those from a Virtual Network. This operation will clear all DEFAULT and INHERITED routes and replace them
                           with new INHERITED routes.
        :param pulumi.Input[str] start_address: The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "vnet_name", vnet_name)
        if end_address is not None:
            pulumi.set(__self__, "end_address", end_address)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if route_name is not None:
            pulumi.set(__self__, "route_name", route_name)
        if route_type is not None:
            pulumi.set(__self__, "route_type", route_type)
        if start_address is not None:
            pulumi.set(__self__, "start_address", start_address)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of resource group
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="vnetName")
    def vnet_name(self) -> pulumi.Input[str]:
        """
        Name of virtual network
        """
        return pulumi.get(self, "vnet_name")

    @vnet_name.setter
    def vnet_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "vnet_name", value)

    @property
    @pulumi.getter(name="endAddress")
    def end_address(self) -> Optional[pulumi.Input[str]]:
        """
        The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.
        """
        return pulumi.get(self, "end_address")

    @end_address.setter
    def end_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "end_address", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="routeName")
    def route_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the virtual network route
        """
        return pulumi.get(self, "route_name")

    @route_name.setter
    def route_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_name", value)

    @property
    @pulumi.getter(name="routeType")
    def route_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of route this is:
                    DEFAULT - By default, every web app has routes to the local address ranges specified by RFC1918
                    INHERITED - Routes inherited from the real Virtual Network routes
                    STATIC - Static route set on the web app only
                    
                    These values will be used for syncing a Web App's routes with those from a Virtual Network. This operation will clear all DEFAULT and INHERITED routes and replace them
                    with new INHERITED routes.
        """
        return pulumi.get(self, "route_type")

    @route_type.setter
    def route_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "route_type", value)

    @property
    @pulumi.getter(name="startAddress")
    def start_address(self) -> Optional[pulumi.Input[str]]:
        """
        The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.
        """
        return pulumi.get(self, "start_address")

    @start_address.setter
    def start_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "start_address", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)


warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)


class ServerFarmRouteForVnet(pulumi.CustomResource):
    warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_address: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 route_type: Optional[pulumi.Input[str]] = None,
                 start_address: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vnet_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        VnetRoute contract used to pass routing information for a vnet.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] end_address: The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] resource_group_name: Name of resource group
        :param pulumi.Input[str] route_name: Name of the virtual network route
        :param pulumi.Input[str] route_type: The type of route this is:
                           DEFAULT - By default, every web app has routes to the local address ranges specified by RFC1918
                           INHERITED - Routes inherited from the real Virtual Network routes
                           STATIC - Static route set on the web app only
                           
                           These values will be used for syncing a Web App's routes with those from a Virtual Network. This operation will clear all DEFAULT and INHERITED routes and replace them
                           with new INHERITED routes.
        :param pulumi.Input[str] start_address: The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] type: Resource type
        :param pulumi.Input[str] vnet_name: Name of virtual network
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerFarmRouteForVnetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        VnetRoute contract used to pass routing information for a vnet.

        :param str resource_name: The name of the resource.
        :param ServerFarmRouteForVnetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerFarmRouteForVnetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 end_address: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 route_name: Optional[pulumi.Input[str]] = None,
                 route_type: Optional[pulumi.Input[str]] = None,
                 start_address: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 vnet_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ServerFarmRouteForVnet is deprecated: Version 2015-08-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerFarmRouteForVnetArgs.__new__(ServerFarmRouteForVnetArgs)

            __props__.__dict__["end_address"] = end_address
            __props__.__dict__["id"] = id
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            if name is None and not opts.urn:
                raise TypeError("Missing required property 'name'")
            __props__.__dict__["name"] = name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["route_name"] = route_name
            __props__.__dict__["route_type"] = route_type
            __props__.__dict__["start_address"] = start_address
            __props__.__dict__["tags"] = tags
            __props__.__dict__["type"] = type
            if vnet_name is None and not opts.urn:
                raise TypeError("Missing required property 'vnet_name'")
            __props__.__dict__["vnet_name"] = vnet_name
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20160901:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20180201:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20190801:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20200601:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20200901:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20201001:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20201201:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20210101:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20210115:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20210201:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20210301:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20220301:ServerFarmRouteForVnet"), pulumi.Alias(type_="azure-native:web/v20220901:ServerFarmRouteForVnet")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerFarmRouteForVnet, __self__).__init__(
            'azure-native:web/v20150801:ServerFarmRouteForVnet',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerFarmRouteForVnet':
        """
        Get an existing ServerFarmRouteForVnet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerFarmRouteForVnetArgs.__new__(ServerFarmRouteForVnetArgs)

        __props__.__dict__["end_address"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["route_type"] = None
        __props__.__dict__["start_address"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ServerFarmRouteForVnet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="endAddress")
    def end_address(self) -> pulumi.Output[Optional[str]]:
        """
        The ending address for this route. If the start address is specified in CIDR notation, this must be omitted.
        """
        return pulumi.get(self, "end_address")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="routeType")
    def route_type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of route this is:
                    DEFAULT - By default, every web app has routes to the local address ranges specified by RFC1918
                    INHERITED - Routes inherited from the real Virtual Network routes
                    STATIC - Static route set on the web app only
                    
                    These values will be used for syncing a Web App's routes with those from a Virtual Network. This operation will clear all DEFAULT and INHERITED routes and replace them
                    with new INHERITED routes.
        """
        return pulumi.get(self, "route_type")

    @property
    @pulumi.getter(name="startAddress")
    def start_address(self) -> pulumi.Output[Optional[str]]:
        """
        The starting address for this route. This may also include a CIDR notation, in which case the end address must not be specified.
        """
        return pulumi.get(self, "start_address")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

