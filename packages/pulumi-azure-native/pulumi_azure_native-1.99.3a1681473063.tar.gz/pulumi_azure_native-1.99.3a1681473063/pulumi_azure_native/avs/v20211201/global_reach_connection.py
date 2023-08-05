# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['GlobalReachConnectionArgs', 'GlobalReachConnection']

@pulumi.input_type
class GlobalReachConnectionArgs:
    def __init__(__self__, *,
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 express_route_id: Optional[pulumi.Input[str]] = None,
                 global_reach_connection_name: Optional[pulumi.Input[str]] = None,
                 peer_express_route_circuit: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a GlobalReachConnection resource.
        :param pulumi.Input[str] private_cloud_name: The name of the private cloud.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] authorization_key: Authorization key from the peer express route used for the global reach connection
        :param pulumi.Input[str] express_route_id: The ID of the Private Cloud's ExpressRoute Circuit that is participating in the global reach connection
        :param pulumi.Input[str] global_reach_connection_name: Name of the global reach connection in the private cloud
        :param pulumi.Input[str] peer_express_route_circuit: Identifier of the ExpressRoute Circuit to peer with in the global reach connection
        """
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if authorization_key is not None:
            pulumi.set(__self__, "authorization_key", authorization_key)
        if express_route_id is not None:
            pulumi.set(__self__, "express_route_id", express_route_id)
        if global_reach_connection_name is not None:
            pulumi.set(__self__, "global_reach_connection_name", global_reach_connection_name)
        if peer_express_route_circuit is not None:
            pulumi.set(__self__, "peer_express_route_circuit", peer_express_route_circuit)

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[str]:
        """
        The name of the private cloud.
        """
        return pulumi.get(self, "private_cloud_name")

    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_cloud_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> Optional[pulumi.Input[str]]:
        """
        Authorization key from the peer express route used for the global reach connection
        """
        return pulumi.get(self, "authorization_key")

    @authorization_key.setter
    def authorization_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authorization_key", value)

    @property
    @pulumi.getter(name="expressRouteId")
    def express_route_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Private Cloud's ExpressRoute Circuit that is participating in the global reach connection
        """
        return pulumi.get(self, "express_route_id")

    @express_route_id.setter
    def express_route_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "express_route_id", value)

    @property
    @pulumi.getter(name="globalReachConnectionName")
    def global_reach_connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the global reach connection in the private cloud
        """
        return pulumi.get(self, "global_reach_connection_name")

    @global_reach_connection_name.setter
    def global_reach_connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "global_reach_connection_name", value)

    @property
    @pulumi.getter(name="peerExpressRouteCircuit")
    def peer_express_route_circuit(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the ExpressRoute Circuit to peer with in the global reach connection
        """
        return pulumi.get(self, "peer_express_route_circuit")

    @peer_express_route_circuit.setter
    def peer_express_route_circuit(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peer_express_route_circuit", value)


class GlobalReachConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 express_route_id: Optional[pulumi.Input[str]] = None,
                 global_reach_connection_name: Optional[pulumi.Input[str]] = None,
                 peer_express_route_circuit: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A global reach connection resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authorization_key: Authorization key from the peer express route used for the global reach connection
        :param pulumi.Input[str] express_route_id: The ID of the Private Cloud's ExpressRoute Circuit that is participating in the global reach connection
        :param pulumi.Input[str] global_reach_connection_name: Name of the global reach connection in the private cloud
        :param pulumi.Input[str] peer_express_route_circuit: Identifier of the ExpressRoute Circuit to peer with in the global reach connection
        :param pulumi.Input[str] private_cloud_name: The name of the private cloud.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: GlobalReachConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A global reach connection resource

        :param str resource_name: The name of the resource.
        :param GlobalReachConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(GlobalReachConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authorization_key: Optional[pulumi.Input[str]] = None,
                 express_route_id: Optional[pulumi.Input[str]] = None,
                 global_reach_connection_name: Optional[pulumi.Input[str]] = None,
                 peer_express_route_circuit: Optional[pulumi.Input[str]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = GlobalReachConnectionArgs.__new__(GlobalReachConnectionArgs)

            __props__.__dict__["authorization_key"] = authorization_key
            __props__.__dict__["express_route_id"] = express_route_id
            __props__.__dict__["global_reach_connection_name"] = global_reach_connection_name
            __props__.__dict__["peer_express_route_circuit"] = peer_express_route_circuit
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["address_prefix"] = None
            __props__.__dict__["circuit_connection_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs:GlobalReachConnection"), pulumi.Alias(type_="azure-native:avs/v20200717preview:GlobalReachConnection"), pulumi.Alias(type_="azure-native:avs/v20210101preview:GlobalReachConnection"), pulumi.Alias(type_="azure-native:avs/v20210601:GlobalReachConnection"), pulumi.Alias(type_="azure-native:avs/v20220501:GlobalReachConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(GlobalReachConnection, __self__).__init__(
            'azure-native:avs/v20211201:GlobalReachConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'GlobalReachConnection':
        """
        Get an existing GlobalReachConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = GlobalReachConnectionArgs.__new__(GlobalReachConnectionArgs)

        __props__.__dict__["address_prefix"] = None
        __props__.__dict__["authorization_key"] = None
        __props__.__dict__["circuit_connection_status"] = None
        __props__.__dict__["express_route_id"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["peer_express_route_circuit"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return GlobalReachConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> pulumi.Output[str]:
        """
        The network used for global reach carved out from the original network block provided for the private cloud
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter(name="authorizationKey")
    def authorization_key(self) -> pulumi.Output[Optional[str]]:
        """
        Authorization key from the peer express route used for the global reach connection
        """
        return pulumi.get(self, "authorization_key")

    @property
    @pulumi.getter(name="circuitConnectionStatus")
    def circuit_connection_status(self) -> pulumi.Output[str]:
        """
        The connection status of the global reach connection
        """
        return pulumi.get(self, "circuit_connection_status")

    @property
    @pulumi.getter(name="expressRouteId")
    def express_route_id(self) -> pulumi.Output[Optional[str]]:
        """
        The ID of the Private Cloud's ExpressRoute Circuit that is participating in the global reach connection
        """
        return pulumi.get(self, "express_route_id")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="peerExpressRouteCircuit")
    def peer_express_route_circuit(self) -> pulumi.Output[Optional[str]]:
        """
        Identifier of the ExpressRoute Circuit to peer with in the global reach connection
        """
        return pulumi.get(self, "peer_express_route_circuit")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The state of the  ExpressRoute Circuit Authorization provisioning
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

