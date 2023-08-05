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

__all__ = ['AFDOriginArgs', 'AFDOrigin']

@pulumi.input_type
class AFDOriginArgs:
    def __init__(__self__, *,
                 host_name: pulumi.Input[str],
                 origin_group_name: pulumi.Input[str],
                 profile_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 azure_origin: Optional[pulumi.Input['ResourceReferenceArgs']] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'EnabledState']]] = None,
                 http_port: Optional[pulumi.Input[int]] = None,
                 https_port: Optional[pulumi.Input[int]] = None,
                 origin_host_header: Optional[pulumi.Input[str]] = None,
                 origin_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 shared_private_link_resource: Optional[pulumi.Input['SharedPrivateLinkResourcePropertiesArgs']] = None,
                 weight: Optional[pulumi.Input[int]] = None):
        """
        The set of arguments for constructing a AFDOrigin resource.
        :param pulumi.Input[str] host_name: The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        :param pulumi.Input[str] origin_group_name: Name of the origin group which is unique within the profile.
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input['ResourceReferenceArgs'] azure_origin: Resource reference to the Azure origin resource.
        :param pulumi.Input[Union[str, 'EnabledState']] enabled_state: Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool.
        :param pulumi.Input[int] http_port: The value of the HTTP port. Must be between 1 and 65535.
        :param pulumi.Input[int] https_port: The value of the HTTPS port. Must be between 1 and 65535.
        :param pulumi.Input[str] origin_host_header: The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        :param pulumi.Input[str] origin_name: Name of the origin that is unique within the profile.
        :param pulumi.Input[int] priority: Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        :param pulumi.Input['SharedPrivateLinkResourcePropertiesArgs'] shared_private_link_resource: The properties of the private link resource for private origin.
        :param pulumi.Input[int] weight: Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        pulumi.set(__self__, "host_name", host_name)
        pulumi.set(__self__, "origin_group_name", origin_group_name)
        pulumi.set(__self__, "profile_name", profile_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if azure_origin is not None:
            pulumi.set(__self__, "azure_origin", azure_origin)
        if enabled_state is not None:
            pulumi.set(__self__, "enabled_state", enabled_state)
        if http_port is not None:
            pulumi.set(__self__, "http_port", http_port)
        if https_port is not None:
            pulumi.set(__self__, "https_port", https_port)
        if origin_host_header is not None:
            pulumi.set(__self__, "origin_host_header", origin_host_header)
        if origin_name is not None:
            pulumi.set(__self__, "origin_name", origin_name)
        if priority is not None:
            pulumi.set(__self__, "priority", priority)
        if shared_private_link_resource is not None:
            pulumi.set(__self__, "shared_private_link_resource", shared_private_link_resource)
        if weight is not None:
            pulumi.set(__self__, "weight", weight)

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Input[str]:
        """
        The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        """
        return pulumi.get(self, "host_name")

    @host_name.setter
    def host_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "host_name", value)

    @property
    @pulumi.getter(name="originGroupName")
    def origin_group_name(self) -> pulumi.Input[str]:
        """
        Name of the origin group which is unique within the profile.
        """
        return pulumi.get(self, "origin_group_name")

    @origin_group_name.setter
    def origin_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "origin_group_name", value)

    @property
    @pulumi.getter(name="profileName")
    def profile_name(self) -> pulumi.Input[str]:
        """
        Name of the CDN profile which is unique within the resource group.
        """
        return pulumi.get(self, "profile_name")

    @profile_name.setter
    def profile_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "profile_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="azureOrigin")
    def azure_origin(self) -> Optional[pulumi.Input['ResourceReferenceArgs']]:
        """
        Resource reference to the Azure origin resource.
        """
        return pulumi.get(self, "azure_origin")

    @azure_origin.setter
    def azure_origin(self, value: Optional[pulumi.Input['ResourceReferenceArgs']]):
        pulumi.set(self, "azure_origin", value)

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[pulumi.Input[Union[str, 'EnabledState']]]:
        """
        Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool.
        """
        return pulumi.get(self, "enabled_state")

    @enabled_state.setter
    def enabled_state(self, value: Optional[pulumi.Input[Union[str, 'EnabledState']]]):
        pulumi.set(self, "enabled_state", value)

    @property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> Optional[pulumi.Input[int]]:
        """
        The value of the HTTP port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "http_port")

    @http_port.setter
    def http_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "http_port", value)

    @property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> Optional[pulumi.Input[int]]:
        """
        The value of the HTTPS port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "https_port")

    @https_port.setter
    def https_port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "https_port", value)

    @property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> Optional[pulumi.Input[str]]:
        """
        The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        """
        return pulumi.get(self, "origin_host_header")

    @origin_host_header.setter
    def origin_host_header(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_host_header", value)

    @property
    @pulumi.getter(name="originName")
    def origin_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the origin that is unique within the profile.
        """
        return pulumi.get(self, "origin_name")

    @origin_name.setter
    def origin_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "origin_name", value)

    @property
    @pulumi.getter
    def priority(self) -> Optional[pulumi.Input[int]]:
        """
        Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        """
        return pulumi.get(self, "priority")

    @priority.setter
    def priority(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "priority", value)

    @property
    @pulumi.getter(name="sharedPrivateLinkResource")
    def shared_private_link_resource(self) -> Optional[pulumi.Input['SharedPrivateLinkResourcePropertiesArgs']]:
        """
        The properties of the private link resource for private origin.
        """
        return pulumi.get(self, "shared_private_link_resource")

    @shared_private_link_resource.setter
    def shared_private_link_resource(self, value: Optional[pulumi.Input['SharedPrivateLinkResourcePropertiesArgs']]):
        pulumi.set(self, "shared_private_link_resource", value)

    @property
    @pulumi.getter
    def weight(self) -> Optional[pulumi.Input[int]]:
        """
        Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        return pulumi.get(self, "weight")

    @weight.setter
    def weight(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "weight", value)


class AFDOrigin(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_origin: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'EnabledState']]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 http_port: Optional[pulumi.Input[int]] = None,
                 https_port: Optional[pulumi.Input[int]] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 origin_host_header: Optional[pulumi.Input[str]] = None,
                 origin_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shared_private_link_resource: Optional[pulumi.Input[pulumi.InputType['SharedPrivateLinkResourcePropertiesArgs']]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        """
        CDN origin is the source of the content being delivered via CDN. When the edge nodes represented by an endpoint do not have the requested content cached, they attempt to fetch it from one or more of the configured origins.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['ResourceReferenceArgs']] azure_origin: Resource reference to the Azure origin resource.
        :param pulumi.Input[Union[str, 'EnabledState']] enabled_state: Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool.
        :param pulumi.Input[str] host_name: The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        :param pulumi.Input[int] http_port: The value of the HTTP port. Must be between 1 and 65535.
        :param pulumi.Input[int] https_port: The value of the HTTPS port. Must be between 1 and 65535.
        :param pulumi.Input[str] origin_group_name: Name of the origin group which is unique within the profile.
        :param pulumi.Input[str] origin_host_header: The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        :param pulumi.Input[str] origin_name: Name of the origin that is unique within the profile.
        :param pulumi.Input[int] priority: Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        :param pulumi.Input[str] profile_name: Name of the CDN profile which is unique within the resource group.
        :param pulumi.Input[str] resource_group_name: Name of the Resource group within the Azure subscription.
        :param pulumi.Input[pulumi.InputType['SharedPrivateLinkResourcePropertiesArgs']] shared_private_link_resource: The properties of the private link resource for private origin.
        :param pulumi.Input[int] weight: Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AFDOriginArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        CDN origin is the source of the content being delivered via CDN. When the edge nodes represented by an endpoint do not have the requested content cached, they attempt to fetch it from one or more of the configured origins.

        :param str resource_name: The name of the resource.
        :param AFDOriginArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AFDOriginArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 azure_origin: Optional[pulumi.Input[pulumi.InputType['ResourceReferenceArgs']]] = None,
                 enabled_state: Optional[pulumi.Input[Union[str, 'EnabledState']]] = None,
                 host_name: Optional[pulumi.Input[str]] = None,
                 http_port: Optional[pulumi.Input[int]] = None,
                 https_port: Optional[pulumi.Input[int]] = None,
                 origin_group_name: Optional[pulumi.Input[str]] = None,
                 origin_host_header: Optional[pulumi.Input[str]] = None,
                 origin_name: Optional[pulumi.Input[str]] = None,
                 priority: Optional[pulumi.Input[int]] = None,
                 profile_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 shared_private_link_resource: Optional[pulumi.Input[pulumi.InputType['SharedPrivateLinkResourcePropertiesArgs']]] = None,
                 weight: Optional[pulumi.Input[int]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AFDOriginArgs.__new__(AFDOriginArgs)

            __props__.__dict__["azure_origin"] = azure_origin
            __props__.__dict__["enabled_state"] = enabled_state
            if host_name is None and not opts.urn:
                raise TypeError("Missing required property 'host_name'")
            __props__.__dict__["host_name"] = host_name
            __props__.__dict__["http_port"] = http_port
            __props__.__dict__["https_port"] = https_port
            if origin_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'origin_group_name'")
            __props__.__dict__["origin_group_name"] = origin_group_name
            __props__.__dict__["origin_host_header"] = origin_host_header
            __props__.__dict__["origin_name"] = origin_name
            __props__.__dict__["priority"] = priority
            if profile_name is None and not opts.urn:
                raise TypeError("Missing required property 'profile_name'")
            __props__.__dict__["profile_name"] = profile_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["shared_private_link_resource"] = shared_private_link_resource
            __props__.__dict__["weight"] = weight
            __props__.__dict__["deployment_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:cdn:AFDOrigin"), pulumi.Alias(type_="azure-native:cdn/v20210601:AFDOrigin"), pulumi.Alias(type_="azure-native:cdn/v20220501preview:AFDOrigin"), pulumi.Alias(type_="azure-native:cdn/v20221101preview:AFDOrigin")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AFDOrigin, __self__).__init__(
            'azure-native:cdn/v20200901:AFDOrigin',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AFDOrigin':
        """
        Get an existing AFDOrigin resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AFDOriginArgs.__new__(AFDOriginArgs)

        __props__.__dict__["azure_origin"] = None
        __props__.__dict__["deployment_status"] = None
        __props__.__dict__["enabled_state"] = None
        __props__.__dict__["host_name"] = None
        __props__.__dict__["http_port"] = None
        __props__.__dict__["https_port"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["origin_host_header"] = None
        __props__.__dict__["priority"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["shared_private_link_resource"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["weight"] = None
        return AFDOrigin(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureOrigin")
    def azure_origin(self) -> pulumi.Output[Optional['outputs.ResourceReferenceResponse']]:
        """
        Resource reference to the Azure origin resource.
        """
        return pulumi.get(self, "azure_origin")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> pulumi.Output[str]:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> pulumi.Output[Optional[str]]:
        """
        Whether to enable health probes to be made against backends defined under backendPools. Health probes can only be disabled if there is a single enabled backend in single enabled backend pool.
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> pulumi.Output[str]:
        """
        The address of the origin. Domain names, IPv4 addresses, and IPv6 addresses are supported.This should be unique across all origins in an endpoint.
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter(name="httpPort")
    def http_port(self) -> pulumi.Output[Optional[int]]:
        """
        The value of the HTTP port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "http_port")

    @property
    @pulumi.getter(name="httpsPort")
    def https_port(self) -> pulumi.Output[Optional[int]]:
        """
        The value of the HTTPS port. Must be between 1 and 65535.
        """
        return pulumi.get(self, "https_port")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="originHostHeader")
    def origin_host_header(self) -> pulumi.Output[Optional[str]]:
        """
        The host header value sent to the origin with each request. If you leave this blank, the request hostname determines this value. Azure CDN origins, such as Web Apps, Blob Storage, and Cloud Services require this host header value to match the origin hostname by default. This overrides the host header defined at Endpoint
        """
        return pulumi.get(self, "origin_host_header")

    @property
    @pulumi.getter
    def priority(self) -> pulumi.Output[Optional[int]]:
        """
        Priority of origin in given origin group for load balancing. Higher priorities will not be used for load balancing if any lower priority origin is healthy.Must be between 1 and 5
        """
        return pulumi.get(self, "priority")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sharedPrivateLinkResource")
    def shared_private_link_resource(self) -> pulumi.Output[Optional['outputs.SharedPrivateLinkResourcePropertiesResponse']]:
        """
        The properties of the private link resource for private origin.
        """
        return pulumi.get(self, "shared_private_link_resource")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def weight(self) -> pulumi.Output[Optional[int]]:
        """
        Weight of the origin in given origin group for load balancing. Must be between 1 and 1000
        """
        return pulumi.get(self, "weight")

