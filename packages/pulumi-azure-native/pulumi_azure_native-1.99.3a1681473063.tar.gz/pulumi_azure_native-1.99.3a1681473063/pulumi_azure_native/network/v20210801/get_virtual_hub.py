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

__all__ = [
    'GetVirtualHubResult',
    'AwaitableGetVirtualHubResult',
    'get_virtual_hub',
    'get_virtual_hub_output',
]

@pulumi.output_type
class GetVirtualHubResult:
    """
    VirtualHub Resource.
    """
    def __init__(__self__, address_prefix=None, allow_branch_to_branch_traffic=None, azure_firewall=None, bgp_connections=None, etag=None, express_route_gateway=None, hub_routing_preference=None, id=None, ip_configurations=None, kind=None, location=None, name=None, p2_s_vpn_gateway=None, preferred_routing_gateway=None, provisioning_state=None, route_table=None, routing_state=None, security_partner_provider=None, security_provider_name=None, sku=None, tags=None, type=None, virtual_hub_route_table_v2s=None, virtual_router_asn=None, virtual_router_ips=None, virtual_wan=None, vpn_gateway=None):
        if address_prefix and not isinstance(address_prefix, str):
            raise TypeError("Expected argument 'address_prefix' to be a str")
        pulumi.set(__self__, "address_prefix", address_prefix)
        if allow_branch_to_branch_traffic and not isinstance(allow_branch_to_branch_traffic, bool):
            raise TypeError("Expected argument 'allow_branch_to_branch_traffic' to be a bool")
        pulumi.set(__self__, "allow_branch_to_branch_traffic", allow_branch_to_branch_traffic)
        if azure_firewall and not isinstance(azure_firewall, dict):
            raise TypeError("Expected argument 'azure_firewall' to be a dict")
        pulumi.set(__self__, "azure_firewall", azure_firewall)
        if bgp_connections and not isinstance(bgp_connections, list):
            raise TypeError("Expected argument 'bgp_connections' to be a list")
        pulumi.set(__self__, "bgp_connections", bgp_connections)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if express_route_gateway and not isinstance(express_route_gateway, dict):
            raise TypeError("Expected argument 'express_route_gateway' to be a dict")
        pulumi.set(__self__, "express_route_gateway", express_route_gateway)
        if hub_routing_preference and not isinstance(hub_routing_preference, str):
            raise TypeError("Expected argument 'hub_routing_preference' to be a str")
        pulumi.set(__self__, "hub_routing_preference", hub_routing_preference)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if ip_configurations and not isinstance(ip_configurations, list):
            raise TypeError("Expected argument 'ip_configurations' to be a list")
        pulumi.set(__self__, "ip_configurations", ip_configurations)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if p2_s_vpn_gateway and not isinstance(p2_s_vpn_gateway, dict):
            raise TypeError("Expected argument 'p2_s_vpn_gateway' to be a dict")
        pulumi.set(__self__, "p2_s_vpn_gateway", p2_s_vpn_gateway)
        if preferred_routing_gateway and not isinstance(preferred_routing_gateway, str):
            raise TypeError("Expected argument 'preferred_routing_gateway' to be a str")
        pulumi.set(__self__, "preferred_routing_gateway", preferred_routing_gateway)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if route_table and not isinstance(route_table, dict):
            raise TypeError("Expected argument 'route_table' to be a dict")
        pulumi.set(__self__, "route_table", route_table)
        if routing_state and not isinstance(routing_state, str):
            raise TypeError("Expected argument 'routing_state' to be a str")
        pulumi.set(__self__, "routing_state", routing_state)
        if security_partner_provider and not isinstance(security_partner_provider, dict):
            raise TypeError("Expected argument 'security_partner_provider' to be a dict")
        pulumi.set(__self__, "security_partner_provider", security_partner_provider)
        if security_provider_name and not isinstance(security_provider_name, str):
            raise TypeError("Expected argument 'security_provider_name' to be a str")
        pulumi.set(__self__, "security_provider_name", security_provider_name)
        if sku and not isinstance(sku, str):
            raise TypeError("Expected argument 'sku' to be a str")
        pulumi.set(__self__, "sku", sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if virtual_hub_route_table_v2s and not isinstance(virtual_hub_route_table_v2s, list):
            raise TypeError("Expected argument 'virtual_hub_route_table_v2s' to be a list")
        pulumi.set(__self__, "virtual_hub_route_table_v2s", virtual_hub_route_table_v2s)
        if virtual_router_asn and not isinstance(virtual_router_asn, float):
            raise TypeError("Expected argument 'virtual_router_asn' to be a float")
        pulumi.set(__self__, "virtual_router_asn", virtual_router_asn)
        if virtual_router_ips and not isinstance(virtual_router_ips, list):
            raise TypeError("Expected argument 'virtual_router_ips' to be a list")
        pulumi.set(__self__, "virtual_router_ips", virtual_router_ips)
        if virtual_wan and not isinstance(virtual_wan, dict):
            raise TypeError("Expected argument 'virtual_wan' to be a dict")
        pulumi.set(__self__, "virtual_wan", virtual_wan)
        if vpn_gateway and not isinstance(vpn_gateway, dict):
            raise TypeError("Expected argument 'vpn_gateway' to be a dict")
        pulumi.set(__self__, "vpn_gateway", vpn_gateway)

    @property
    @pulumi.getter(name="addressPrefix")
    def address_prefix(self) -> Optional[str]:
        """
        Address-prefix for this VirtualHub.
        """
        return pulumi.get(self, "address_prefix")

    @property
    @pulumi.getter(name="allowBranchToBranchTraffic")
    def allow_branch_to_branch_traffic(self) -> Optional[bool]:
        """
        Flag to control transit for VirtualRouter hub.
        """
        return pulumi.get(self, "allow_branch_to_branch_traffic")

    @property
    @pulumi.getter(name="azureFirewall")
    def azure_firewall(self) -> Optional['outputs.SubResourceResponse']:
        """
        The azureFirewall associated with this VirtualHub.
        """
        return pulumi.get(self, "azure_firewall")

    @property
    @pulumi.getter(name="bgpConnections")
    def bgp_connections(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to Bgp Connections.
        """
        return pulumi.get(self, "bgp_connections")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="expressRouteGateway")
    def express_route_gateway(self) -> Optional['outputs.SubResourceResponse']:
        """
        The expressRouteGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "express_route_gateway")

    @property
    @pulumi.getter(name="hubRoutingPreference")
    def hub_routing_preference(self) -> Optional[str]:
        """
        The hubRoutingPreference of this VirtualHub.
        """
        return pulumi.get(self, "hub_routing_preference")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="ipConfigurations")
    def ip_configurations(self) -> Sequence['outputs.SubResourceResponse']:
        """
        List of references to IpConfigurations.
        """
        return pulumi.get(self, "ip_configurations")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of service virtual hub. This is metadata used for the Azure portal experience for Route Server.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="p2SVpnGateway")
    def p2_s_vpn_gateway(self) -> Optional['outputs.SubResourceResponse']:
        """
        The P2SVpnGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "p2_s_vpn_gateway")

    @property
    @pulumi.getter(name="preferredRoutingGateway")
    def preferred_routing_gateway(self) -> Optional[str]:
        """
        The preferred gateway to route on-prem traffic
        """
        return pulumi.get(self, "preferred_routing_gateway")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the virtual hub resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="routeTable")
    def route_table(self) -> Optional['outputs.VirtualHubRouteTableResponse']:
        """
        The routeTable associated with this virtual hub.
        """
        return pulumi.get(self, "route_table")

    @property
    @pulumi.getter(name="routingState")
    def routing_state(self) -> str:
        """
        The routing state.
        """
        return pulumi.get(self, "routing_state")

    @property
    @pulumi.getter(name="securityPartnerProvider")
    def security_partner_provider(self) -> Optional['outputs.SubResourceResponse']:
        """
        The securityPartnerProvider associated with this VirtualHub.
        """
        return pulumi.get(self, "security_partner_provider")

    @property
    @pulumi.getter(name="securityProviderName")
    def security_provider_name(self) -> Optional[str]:
        """
        The Security Provider name.
        """
        return pulumi.get(self, "security_provider_name")

    @property
    @pulumi.getter
    def sku(self) -> Optional[str]:
        """
        The sku of this VirtualHub.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="virtualHubRouteTableV2s")
    def virtual_hub_route_table_v2s(self) -> Optional[Sequence['outputs.VirtualHubRouteTableV2Response']]:
        """
        List of all virtual hub route table v2s associated with this VirtualHub.
        """
        return pulumi.get(self, "virtual_hub_route_table_v2s")

    @property
    @pulumi.getter(name="virtualRouterAsn")
    def virtual_router_asn(self) -> Optional[float]:
        """
        VirtualRouter ASN.
        """
        return pulumi.get(self, "virtual_router_asn")

    @property
    @pulumi.getter(name="virtualRouterIps")
    def virtual_router_ips(self) -> Optional[Sequence[str]]:
        """
        VirtualRouter IPs.
        """
        return pulumi.get(self, "virtual_router_ips")

    @property
    @pulumi.getter(name="virtualWan")
    def virtual_wan(self) -> Optional['outputs.SubResourceResponse']:
        """
        The VirtualWAN to which the VirtualHub belongs.
        """
        return pulumi.get(self, "virtual_wan")

    @property
    @pulumi.getter(name="vpnGateway")
    def vpn_gateway(self) -> Optional['outputs.SubResourceResponse']:
        """
        The VpnGateway associated with this VirtualHub.
        """
        return pulumi.get(self, "vpn_gateway")


class AwaitableGetVirtualHubResult(GetVirtualHubResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualHubResult(
            address_prefix=self.address_prefix,
            allow_branch_to_branch_traffic=self.allow_branch_to_branch_traffic,
            azure_firewall=self.azure_firewall,
            bgp_connections=self.bgp_connections,
            etag=self.etag,
            express_route_gateway=self.express_route_gateway,
            hub_routing_preference=self.hub_routing_preference,
            id=self.id,
            ip_configurations=self.ip_configurations,
            kind=self.kind,
            location=self.location,
            name=self.name,
            p2_s_vpn_gateway=self.p2_s_vpn_gateway,
            preferred_routing_gateway=self.preferred_routing_gateway,
            provisioning_state=self.provisioning_state,
            route_table=self.route_table,
            routing_state=self.routing_state,
            security_partner_provider=self.security_partner_provider,
            security_provider_name=self.security_provider_name,
            sku=self.sku,
            tags=self.tags,
            type=self.type,
            virtual_hub_route_table_v2s=self.virtual_hub_route_table_v2s,
            virtual_router_asn=self.virtual_router_asn,
            virtual_router_ips=self.virtual_router_ips,
            virtual_wan=self.virtual_wan,
            vpn_gateway=self.vpn_gateway)


def get_virtual_hub(resource_group_name: Optional[str] = None,
                    virtual_hub_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualHubResult:
    """
    Retrieves the details of a VirtualHub.


    :param str resource_group_name: The resource group name of the VirtualHub.
    :param str virtual_hub_name: The name of the VirtualHub.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualHubName'] = virtual_hub_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20210801:getVirtualHub', __args__, opts=opts, typ=GetVirtualHubResult).value

    return AwaitableGetVirtualHubResult(
        address_prefix=__ret__.address_prefix,
        allow_branch_to_branch_traffic=__ret__.allow_branch_to_branch_traffic,
        azure_firewall=__ret__.azure_firewall,
        bgp_connections=__ret__.bgp_connections,
        etag=__ret__.etag,
        express_route_gateway=__ret__.express_route_gateway,
        hub_routing_preference=__ret__.hub_routing_preference,
        id=__ret__.id,
        ip_configurations=__ret__.ip_configurations,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        p2_s_vpn_gateway=__ret__.p2_s_vpn_gateway,
        preferred_routing_gateway=__ret__.preferred_routing_gateway,
        provisioning_state=__ret__.provisioning_state,
        route_table=__ret__.route_table,
        routing_state=__ret__.routing_state,
        security_partner_provider=__ret__.security_partner_provider,
        security_provider_name=__ret__.security_provider_name,
        sku=__ret__.sku,
        tags=__ret__.tags,
        type=__ret__.type,
        virtual_hub_route_table_v2s=__ret__.virtual_hub_route_table_v2s,
        virtual_router_asn=__ret__.virtual_router_asn,
        virtual_router_ips=__ret__.virtual_router_ips,
        virtual_wan=__ret__.virtual_wan,
        vpn_gateway=__ret__.vpn_gateway)


@_utilities.lift_output_func(get_virtual_hub)
def get_virtual_hub_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                           virtual_hub_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualHubResult]:
    """
    Retrieves the details of a VirtualHub.


    :param str resource_group_name: The resource group name of the VirtualHub.
    :param str virtual_hub_name: The name of the VirtualHub.
    """
    ...
