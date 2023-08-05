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

__all__ = ['ApplicationGatewayArgs', 'ApplicationGateway']

@pulumi.input_type
class ApplicationGatewayArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendAddressPoolArgs']]]] = None,
                 backend_http_settings_collection: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendHttpSettingsArgs']]]] = None,
                 frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendIPConfigurationArgs']]]] = None,
                 frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendPortArgs']]]] = None,
                 gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayIPConfigurationArgs']]]] = None,
                 http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayHttpListenerArgs']]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 probes: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayProbeArgs']]]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayRequestRoutingRuleArgs']]]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input['ApplicationGatewaySkuArgs']] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewaySslCertificateArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 url_path_maps: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayUrlPathMapArgs']]]] = None):
        """
        The set of arguments for constructing a ApplicationGateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] application_gateway_name: The name of the application gateway.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendAddressPoolArgs']]] backend_address_pools: Backend address pool of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendHttpSettingsArgs']]] backend_http_settings_collection: Backend http settings of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendIPConfigurationArgs']]] frontend_ip_configurations: Frontend IP addresses of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendPortArgs']]] frontend_ports: Frontend ports of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayIPConfigurationArgs']]] gateway_ip_configurations: Gets or sets subnets of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayHttpListenerArgs']]] http_listeners: Http listeners of the application gateway resource.
        :param pulumi.Input[str] id: Resource Identifier.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayProbeArgs']]] probes: Probes of the application gateway resource.
        :param pulumi.Input[str] provisioning_state: Provisioning state of the application gateway resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayRequestRoutingRuleArgs']]] request_routing_rules: Request routing rules of the application gateway resource.
        :param pulumi.Input[str] resource_guid: Resource GUID property of the application gateway resource.
        :param pulumi.Input['ApplicationGatewaySkuArgs'] sku: SKU of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewaySslCertificateArgs']]] ssl_certificates: SSL certificates of the application gateway resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayUrlPathMapArgs']]] url_path_maps: URL path map of the application gateway resource.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if application_gateway_name is not None:
            pulumi.set(__self__, "application_gateway_name", application_gateway_name)
        if backend_address_pools is not None:
            pulumi.set(__self__, "backend_address_pools", backend_address_pools)
        if backend_http_settings_collection is not None:
            pulumi.set(__self__, "backend_http_settings_collection", backend_http_settings_collection)
        if frontend_ip_configurations is not None:
            pulumi.set(__self__, "frontend_ip_configurations", frontend_ip_configurations)
        if frontend_ports is not None:
            pulumi.set(__self__, "frontend_ports", frontend_ports)
        if gateway_ip_configurations is not None:
            pulumi.set(__self__, "gateway_ip_configurations", gateway_ip_configurations)
        if http_listeners is not None:
            pulumi.set(__self__, "http_listeners", http_listeners)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if probes is not None:
            pulumi.set(__self__, "probes", probes)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if request_routing_rules is not None:
            pulumi.set(__self__, "request_routing_rules", request_routing_rules)
        if resource_guid is not None:
            pulumi.set(__self__, "resource_guid", resource_guid)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if ssl_certificates is not None:
            pulumi.set(__self__, "ssl_certificates", ssl_certificates)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if url_path_maps is not None:
            pulumi.set(__self__, "url_path_maps", url_path_maps)

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
    @pulumi.getter(name="applicationGatewayName")
    def application_gateway_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the application gateway.
        """
        return pulumi.get(self, "application_gateway_name")

    @application_gateway_name.setter
    def application_gateway_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_gateway_name", value)

    @property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendAddressPoolArgs']]]]:
        """
        Backend address pool of the application gateway resource.
        """
        return pulumi.get(self, "backend_address_pools")

    @backend_address_pools.setter
    def backend_address_pools(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendAddressPoolArgs']]]]):
        pulumi.set(self, "backend_address_pools", value)

    @property
    @pulumi.getter(name="backendHttpSettingsCollection")
    def backend_http_settings_collection(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendHttpSettingsArgs']]]]:
        """
        Backend http settings of the application gateway resource.
        """
        return pulumi.get(self, "backend_http_settings_collection")

    @backend_http_settings_collection.setter
    def backend_http_settings_collection(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayBackendHttpSettingsArgs']]]]):
        pulumi.set(self, "backend_http_settings_collection", value)

    @property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendIPConfigurationArgs']]]]:
        """
        Frontend IP addresses of the application gateway resource.
        """
        return pulumi.get(self, "frontend_ip_configurations")

    @frontend_ip_configurations.setter
    def frontend_ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendIPConfigurationArgs']]]]):
        pulumi.set(self, "frontend_ip_configurations", value)

    @property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendPortArgs']]]]:
        """
        Frontend ports of the application gateway resource.
        """
        return pulumi.get(self, "frontend_ports")

    @frontend_ports.setter
    def frontend_ports(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayFrontendPortArgs']]]]):
        pulumi.set(self, "frontend_ports", value)

    @property
    @pulumi.getter(name="gatewayIPConfigurations")
    def gateway_ip_configurations(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayIPConfigurationArgs']]]]:
        """
        Gets or sets subnets of application gateway resource
        """
        return pulumi.get(self, "gateway_ip_configurations")

    @gateway_ip_configurations.setter
    def gateway_ip_configurations(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayIPConfigurationArgs']]]]):
        pulumi.set(self, "gateway_ip_configurations", value)

    @property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayHttpListenerArgs']]]]:
        """
        Http listeners of the application gateway resource.
        """
        return pulumi.get(self, "http_listeners")

    @http_listeners.setter
    def http_listeners(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayHttpListenerArgs']]]]):
        pulumi.set(self, "http_listeners", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Identifier.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def probes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayProbeArgs']]]]:
        """
        Probes of the application gateway resource.
        """
        return pulumi.get(self, "probes")

    @probes.setter
    def probes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayProbeArgs']]]]):
        pulumi.set(self, "probes", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        Provisioning state of the application gateway resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayRequestRoutingRuleArgs']]]]:
        """
        Request routing rules of the application gateway resource.
        """
        return pulumi.get(self, "request_routing_rules")

    @request_routing_rules.setter
    def request_routing_rules(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayRequestRoutingRuleArgs']]]]):
        pulumi.set(self, "request_routing_rules", value)

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> Optional[pulumi.Input[str]]:
        """
        Resource GUID property of the application gateway resource.
        """
        return pulumi.get(self, "resource_guid")

    @resource_guid.setter
    def resource_guid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_guid", value)

    @property
    @pulumi.getter
    def sku(self) -> Optional[pulumi.Input['ApplicationGatewaySkuArgs']]:
        """
        SKU of the application gateway resource.
        """
        return pulumi.get(self, "sku")

    @sku.setter
    def sku(self, value: Optional[pulumi.Input['ApplicationGatewaySkuArgs']]):
        pulumi.set(self, "sku", value)

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewaySslCertificateArgs']]]]:
        """
        SSL certificates of the application gateway resource.
        """
        return pulumi.get(self, "ssl_certificates")

    @ssl_certificates.setter
    def ssl_certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewaySslCertificateArgs']]]]):
        pulumi.set(self, "ssl_certificates", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="urlPathMaps")
    def url_path_maps(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayUrlPathMapArgs']]]]:
        """
        URL path map of the application gateway resource.
        """
        return pulumi.get(self, "url_path_maps")

    @url_path_maps.setter
    def url_path_maps(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['ApplicationGatewayUrlPathMapArgs']]]]):
        pulumi.set(self, "url_path_maps", value)


warnings.warn("""Version 2015-06-15 will be removed in v2 of the provider.""", DeprecationWarning)


class ApplicationGateway(pulumi.CustomResource):
    warnings.warn("""Version 2015-06-15 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]]] = None,
                 backend_http_settings_collection: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingsArgs']]]]] = None,
                 frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIPConfigurationArgs']]]]] = None,
                 frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]]] = None,
                 gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayIPConfigurationArgs']]]]] = None,
                 http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 probes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 url_path_maps: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]]] = None,
                 __props__=None):
        """
        Application gateway resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] application_gateway_name: The name of the application gateway.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]] backend_address_pools: Backend address pool of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingsArgs']]]] backend_http_settings_collection: Backend http settings of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIPConfigurationArgs']]]] frontend_ip_configurations: Frontend IP addresses of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]] frontend_ports: Frontend ports of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayIPConfigurationArgs']]]] gateway_ip_configurations: Gets or sets subnets of application gateway resource
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]] http_listeners: Http listeners of the application gateway resource.
        :param pulumi.Input[str] id: Resource Identifier.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]] probes: Probes of the application gateway resource.
        :param pulumi.Input[str] provisioning_state: Provisioning state of the application gateway resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]] request_routing_rules: Request routing rules of the application gateway resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_guid: Resource GUID property of the application gateway resource.
        :param pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']] sku: SKU of the application gateway resource.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]] ssl_certificates: SSL certificates of the application gateway resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]] url_path_maps: URL path map of the application gateway resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApplicationGatewayArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Application gateway resource

        :param str resource_name: The name of the resource.
        :param ApplicationGatewayArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApplicationGatewayArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 application_gateway_name: Optional[pulumi.Input[str]] = None,
                 backend_address_pools: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendAddressPoolArgs']]]]] = None,
                 backend_http_settings_collection: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayBackendHttpSettingsArgs']]]]] = None,
                 frontend_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendIPConfigurationArgs']]]]] = None,
                 frontend_ports: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayFrontendPortArgs']]]]] = None,
                 gateway_ip_configurations: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayIPConfigurationArgs']]]]] = None,
                 http_listeners: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayHttpListenerArgs']]]]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 probes: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayProbeArgs']]]]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 request_routing_rules: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayRequestRoutingRuleArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_guid: Optional[pulumi.Input[str]] = None,
                 sku: Optional[pulumi.Input[pulumi.InputType['ApplicationGatewaySkuArgs']]] = None,
                 ssl_certificates: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewaySslCertificateArgs']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 url_path_maps: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['ApplicationGatewayUrlPathMapArgs']]]]] = None,
                 __props__=None):
        pulumi.log.warn("""ApplicationGateway is deprecated: Version 2015-06-15 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApplicationGatewayArgs.__new__(ApplicationGatewayArgs)

            __props__.__dict__["application_gateway_name"] = application_gateway_name
            __props__.__dict__["backend_address_pools"] = backend_address_pools
            __props__.__dict__["backend_http_settings_collection"] = backend_http_settings_collection
            __props__.__dict__["frontend_ip_configurations"] = frontend_ip_configurations
            __props__.__dict__["frontend_ports"] = frontend_ports
            __props__.__dict__["gateway_ip_configurations"] = gateway_ip_configurations
            __props__.__dict__["http_listeners"] = http_listeners
            __props__.__dict__["id"] = id
            __props__.__dict__["location"] = location
            __props__.__dict__["probes"] = probes
            __props__.__dict__["provisioning_state"] = provisioning_state
            __props__.__dict__["request_routing_rules"] = request_routing_rules
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_guid"] = resource_guid
            __props__.__dict__["sku"] = sku
            __props__.__dict__["ssl_certificates"] = ssl_certificates
            __props__.__dict__["tags"] = tags
            __props__.__dict__["url_path_maps"] = url_path_maps
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["operational_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20150501preview:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20160330:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20160601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20160901:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20161201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20170301:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20170601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20170801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20170901:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20171001:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20171101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180401:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180701:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20180801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20181001:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20181101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20181201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190401:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190701:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20190901:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20191101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20191201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200301:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200401:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200501:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200601:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200701:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20200801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20201101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20210201:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20210301:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20210501:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20210801:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20220101:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20220501:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20220701:ApplicationGateway"), pulumi.Alias(type_="azure-native:network/v20220901:ApplicationGateway")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApplicationGateway, __self__).__init__(
            'azure-native:network/v20150615:ApplicationGateway',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApplicationGateway':
        """
        Get an existing ApplicationGateway resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApplicationGatewayArgs.__new__(ApplicationGatewayArgs)

        __props__.__dict__["backend_address_pools"] = None
        __props__.__dict__["backend_http_settings_collection"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["frontend_ip_configurations"] = None
        __props__.__dict__["frontend_ports"] = None
        __props__.__dict__["gateway_ip_configurations"] = None
        __props__.__dict__["http_listeners"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["operational_state"] = None
        __props__.__dict__["probes"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["request_routing_rules"] = None
        __props__.__dict__["resource_guid"] = None
        __props__.__dict__["sku"] = None
        __props__.__dict__["ssl_certificates"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["url_path_maps"] = None
        return ApplicationGateway(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="backendAddressPools")
    def backend_address_pools(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayBackendAddressPoolResponse']]]:
        """
        Backend address pool of the application gateway resource.
        """
        return pulumi.get(self, "backend_address_pools")

    @property
    @pulumi.getter(name="backendHttpSettingsCollection")
    def backend_http_settings_collection(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayBackendHttpSettingsResponse']]]:
        """
        Backend http settings of the application gateway resource.
        """
        return pulumi.get(self, "backend_http_settings_collection")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="frontendIPConfigurations")
    def frontend_ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayFrontendIPConfigurationResponse']]]:
        """
        Frontend IP addresses of the application gateway resource.
        """
        return pulumi.get(self, "frontend_ip_configurations")

    @property
    @pulumi.getter(name="frontendPorts")
    def frontend_ports(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayFrontendPortResponse']]]:
        """
        Frontend ports of the application gateway resource.
        """
        return pulumi.get(self, "frontend_ports")

    @property
    @pulumi.getter(name="gatewayIPConfigurations")
    def gateway_ip_configurations(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayIPConfigurationResponse']]]:
        """
        Gets or sets subnets of application gateway resource
        """
        return pulumi.get(self, "gateway_ip_configurations")

    @property
    @pulumi.getter(name="httpListeners")
    def http_listeners(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayHttpListenerResponse']]]:
        """
        Http listeners of the application gateway resource.
        """
        return pulumi.get(self, "http_listeners")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="operationalState")
    def operational_state(self) -> pulumi.Output[str]:
        """
        Operational state of the application gateway resource. Possible values are: 'Stopped', 'Started', 'Running', and 'Stopping'.
        """
        return pulumi.get(self, "operational_state")

    @property
    @pulumi.getter
    def probes(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayProbeResponse']]]:
        """
        Probes of the application gateway resource.
        """
        return pulumi.get(self, "probes")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Provisioning state of the application gateway resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="requestRoutingRules")
    def request_routing_rules(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayRequestRoutingRuleResponse']]]:
        """
        Request routing rules of the application gateway resource.
        """
        return pulumi.get(self, "request_routing_rules")

    @property
    @pulumi.getter(name="resourceGuid")
    def resource_guid(self) -> pulumi.Output[Optional[str]]:
        """
        Resource GUID property of the application gateway resource.
        """
        return pulumi.get(self, "resource_guid")

    @property
    @pulumi.getter
    def sku(self) -> pulumi.Output[Optional['outputs.ApplicationGatewaySkuResponse']]:
        """
        SKU of the application gateway resource.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="sslCertificates")
    def ssl_certificates(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewaySslCertificateResponse']]]:
        """
        SSL certificates of the application gateway resource.
        """
        return pulumi.get(self, "ssl_certificates")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="urlPathMaps")
    def url_path_maps(self) -> pulumi.Output[Optional[Sequence['outputs.ApplicationGatewayUrlPathMapResponse']]]:
        """
        URL path map of the application gateway resource.
        """
        return pulumi.get(self, "url_path_maps")

