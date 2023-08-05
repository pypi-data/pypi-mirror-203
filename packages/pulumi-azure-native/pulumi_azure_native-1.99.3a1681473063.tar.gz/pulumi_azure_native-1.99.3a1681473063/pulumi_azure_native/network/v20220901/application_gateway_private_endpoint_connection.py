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
from ._inputs import *

__all__ = ['ApplicationGatewayPrivateEndpointConnectionArgs', 'ApplicationGatewayPrivateEndpointConnection']

@pulumi.input_type
class ApplicationGatewayPrivateEndpointConnectionArgs:
    def __init__(__self__, *,
                 application_gateway_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 connection_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']] = None):
        """
        The set of arguments for constructing a ApplicationGatewayPrivateEndpointConnection resource.
        :param pulumi.Input[str] application_gateway_name: The name of the application gateway.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] connection_name: The name of the application gateway private endpoint connection.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Name of the private endpoint connection on an application gateway.
        :param pulumi.Input['PrivateLinkServiceConnectionStateArgs'] private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        """
        pulumi.set(__self__, "application_gateway_name", application_gateway_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if connection_name is not None:
            pulumi.set(__self__, "connection_name", connection_name)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

    @property
    @pulumi.getter(name="applicationGatewayName")
    def application_gateway_name(self) -> pulumi.Input[str]:
        """
        The name of the application gateway.
        """
        return pulumi.get(self, "application_gateway_name")

    @application_gateway_name.setter
    def application_gateway_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_gateway_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="connectionName")
    def connection_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the application gateway private endpoint connection.
        """
        return pulumi.get(self, "connection_name")

    @connection_name.setter
    def connection_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "connection_name", value)

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
        Name of the private endpoint connection on an application gateway.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']]:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input['PrivateLinkServiceConnectionStateArgs']]):
        pulumi.set(self, "private_link_service_connection_state", value)


class ApplicationGatewayPrivateEndpointConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Private Endpoint connection on an application gateway.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_gateway_name: The name of the application gateway.
        :param pulumi.Input[str] connection_name: The name of the application gateway private endpoint connection.
        :param pulumi.Input[str] id: Resource ID.
        :param pulumi.Input[str] name: Name of the private endpoint connection on an application gateway.
        :param pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']] private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationGatewayPrivateEndpointConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Private Endpoint connection on an application gateway.

        :param str resource_name: The name of the resource.
        :param ApplicationGatewayPrivateEndpointConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationGatewayPrivateEndpointConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 connection_name: Optional[pulumi.Input[str]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 private_link_service_connection_state: Optional[pulumi.Input[pulumi.InputType['PrivateLinkServiceConnectionStateArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationGatewayPrivateEndpointConnectionArgs.__new__(ApplicationGatewayPrivateEndpointConnectionArgs)

            if application_gateway_name is None and not opts.urn:
                raise TypeError("Missing required property 'application_gateway_name'")
            __props__.__dict__["application_gateway_name"] = application_gateway_name
            __props__.__dict__["connection_name"] = connection_name
            __props__.__dict__["id"] = id
            __props__.__dict__["name"] = name
            __props__.__dict__["private_link_service_connection_state"] = private_link_service_connection_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["link_identifier"] = None
            __props__.__dict__["private_endpoint"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20200501:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20200601:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20200701:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20200801:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20201101:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20210201:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20210301:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20210501:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20210801:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20220101:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20220501:ApplicationGatewayPrivateEndpointConnection"), pulumi.Alias(type_="azure-native:network/v20220701:ApplicationGatewayPrivateEndpointConnection")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApplicationGatewayPrivateEndpointConnection, __self__).__init__(
            'azure-native:network/v20220901:ApplicationGatewayPrivateEndpointConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationGatewayPrivateEndpointConnection':
        """
        Get an existing ApplicationGatewayPrivateEndpointConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationGatewayPrivateEndpointConnectionArgs.__new__(ApplicationGatewayPrivateEndpointConnectionArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["link_identifier"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_endpoint"] = None
        __props__.__dict__["private_link_service_connection_state"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["type"] = None
        return ApplicationGatewayPrivateEndpointConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="linkIdentifier")
    def link_identifier(self) -> pulumi.Output[str]:
        """
        The consumer link id.
        """
        return pulumi.get(self, "link_identifier")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Name of the private endpoint connection on an application gateway.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> pulumi.Output['outputs.PrivateEndpointResponse']:
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> pulumi.Output[Optional['outputs.PrivateLinkServiceConnectionStateResponse']]:
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the application gateway private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Type of the resource.
        """
        return pulumi.get(self, "type")

