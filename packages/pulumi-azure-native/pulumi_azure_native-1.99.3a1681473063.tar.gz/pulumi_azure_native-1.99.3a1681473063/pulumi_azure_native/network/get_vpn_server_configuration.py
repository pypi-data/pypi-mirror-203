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

__all__ = [
    'GetVpnServerConfigurationResult',
    'AwaitableGetVpnServerConfigurationResult',
    'get_vpn_server_configuration',
    'get_vpn_server_configuration_output',
]

@pulumi.output_type
class GetVpnServerConfigurationResult:
    """
    VpnServerConfiguration Resource.
    """
    def __init__(__self__, aad_authentication_parameters=None, etag=None, id=None, location=None, name=None, p2_s_vpn_gateways=None, provisioning_state=None, radius_client_root_certificates=None, radius_server_address=None, radius_server_root_certificates=None, radius_server_secret=None, radius_servers=None, tags=None, type=None, vpn_authentication_types=None, vpn_client_ipsec_policies=None, vpn_client_revoked_certificates=None, vpn_client_root_certificates=None, vpn_protocols=None):
        if aad_authentication_parameters and not isinstance(aad_authentication_parameters, dict):
            raise TypeError("Expected argument 'aad_authentication_parameters' to be a dict")
        pulumi.set(__self__, "aad_authentication_parameters", aad_authentication_parameters)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if p2_s_vpn_gateways and not isinstance(p2_s_vpn_gateways, list):
            raise TypeError("Expected argument 'p2_s_vpn_gateways' to be a list")
        pulumi.set(__self__, "p2_s_vpn_gateways", p2_s_vpn_gateways)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if radius_client_root_certificates and not isinstance(radius_client_root_certificates, list):
            raise TypeError("Expected argument 'radius_client_root_certificates' to be a list")
        pulumi.set(__self__, "radius_client_root_certificates", radius_client_root_certificates)
        if radius_server_address and not isinstance(radius_server_address, str):
            raise TypeError("Expected argument 'radius_server_address' to be a str")
        pulumi.set(__self__, "radius_server_address", radius_server_address)
        if radius_server_root_certificates and not isinstance(radius_server_root_certificates, list):
            raise TypeError("Expected argument 'radius_server_root_certificates' to be a list")
        pulumi.set(__self__, "radius_server_root_certificates", radius_server_root_certificates)
        if radius_server_secret and not isinstance(radius_server_secret, str):
            raise TypeError("Expected argument 'radius_server_secret' to be a str")
        pulumi.set(__self__, "radius_server_secret", radius_server_secret)
        if radius_servers and not isinstance(radius_servers, list):
            raise TypeError("Expected argument 'radius_servers' to be a list")
        pulumi.set(__self__, "radius_servers", radius_servers)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if vpn_authentication_types and not isinstance(vpn_authentication_types, list):
            raise TypeError("Expected argument 'vpn_authentication_types' to be a list")
        pulumi.set(__self__, "vpn_authentication_types", vpn_authentication_types)
        if vpn_client_ipsec_policies and not isinstance(vpn_client_ipsec_policies, list):
            raise TypeError("Expected argument 'vpn_client_ipsec_policies' to be a list")
        pulumi.set(__self__, "vpn_client_ipsec_policies", vpn_client_ipsec_policies)
        if vpn_client_revoked_certificates and not isinstance(vpn_client_revoked_certificates, list):
            raise TypeError("Expected argument 'vpn_client_revoked_certificates' to be a list")
        pulumi.set(__self__, "vpn_client_revoked_certificates", vpn_client_revoked_certificates)
        if vpn_client_root_certificates and not isinstance(vpn_client_root_certificates, list):
            raise TypeError("Expected argument 'vpn_client_root_certificates' to be a list")
        pulumi.set(__self__, "vpn_client_root_certificates", vpn_client_root_certificates)
        if vpn_protocols and not isinstance(vpn_protocols, list):
            raise TypeError("Expected argument 'vpn_protocols' to be a list")
        pulumi.set(__self__, "vpn_protocols", vpn_protocols)

    @property
    @pulumi.getter(name="aadAuthenticationParameters")
    def aad_authentication_parameters(self) -> Optional['outputs.AadAuthenticationParametersResponse']:
        """
        The set of aad vpn authentication parameters.
        """
        return pulumi.get(self, "aad_authentication_parameters")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
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
    @pulumi.getter(name="p2SVpnGateways")
    def p2_s_vpn_gateways(self) -> Sequence['outputs.P2SVpnGatewayResponse']:
        """
        List of references to P2SVpnGateways.
        """
        return pulumi.get(self, "p2_s_vpn_gateways")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the VpnServerConfiguration resource. Possible values are: 'Updating', 'Deleting', and 'Failed'.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="radiusClientRootCertificates")
    def radius_client_root_certificates(self) -> Optional[Sequence['outputs.VpnServerConfigRadiusClientRootCertificateResponse']]:
        """
        Radius client root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "radius_client_root_certificates")

    @property
    @pulumi.getter(name="radiusServerAddress")
    def radius_server_address(self) -> Optional[str]:
        """
        The radius server address property of the VpnServerConfiguration resource for point to site client connection.
        """
        return pulumi.get(self, "radius_server_address")

    @property
    @pulumi.getter(name="radiusServerRootCertificates")
    def radius_server_root_certificates(self) -> Optional[Sequence['outputs.VpnServerConfigRadiusServerRootCertificateResponse']]:
        """
        Radius Server root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "radius_server_root_certificates")

    @property
    @pulumi.getter(name="radiusServerSecret")
    def radius_server_secret(self) -> Optional[str]:
        """
        The radius secret property of the VpnServerConfiguration resource for point to site client connection.
        """
        return pulumi.get(self, "radius_server_secret")

    @property
    @pulumi.getter(name="radiusServers")
    def radius_servers(self) -> Optional[Sequence['outputs.RadiusServerResponse']]:
        """
        Multiple Radius Server configuration for VpnServerConfiguration.
        """
        return pulumi.get(self, "radius_servers")

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
    @pulumi.getter(name="vpnAuthenticationTypes")
    def vpn_authentication_types(self) -> Optional[Sequence[str]]:
        """
        VPN authentication types for the VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_authentication_types")

    @property
    @pulumi.getter(name="vpnClientIpsecPolicies")
    def vpn_client_ipsec_policies(self) -> Optional[Sequence['outputs.IpsecPolicyResponse']]:
        """
        VpnClientIpsecPolicies for VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_ipsec_policies")

    @property
    @pulumi.getter(name="vpnClientRevokedCertificates")
    def vpn_client_revoked_certificates(self) -> Optional[Sequence['outputs.VpnServerConfigVpnClientRevokedCertificateResponse']]:
        """
        VPN client revoked certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_revoked_certificates")

    @property
    @pulumi.getter(name="vpnClientRootCertificates")
    def vpn_client_root_certificates(self) -> Optional[Sequence['outputs.VpnServerConfigVpnClientRootCertificateResponse']]:
        """
        VPN client root certificate of VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_client_root_certificates")

    @property
    @pulumi.getter(name="vpnProtocols")
    def vpn_protocols(self) -> Optional[Sequence[str]]:
        """
        VPN protocols for the VpnServerConfiguration.
        """
        return pulumi.get(self, "vpn_protocols")


class AwaitableGetVpnServerConfigurationResult(GetVpnServerConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVpnServerConfigurationResult(
            aad_authentication_parameters=self.aad_authentication_parameters,
            etag=self.etag,
            id=self.id,
            location=self.location,
            name=self.name,
            p2_s_vpn_gateways=self.p2_s_vpn_gateways,
            provisioning_state=self.provisioning_state,
            radius_client_root_certificates=self.radius_client_root_certificates,
            radius_server_address=self.radius_server_address,
            radius_server_root_certificates=self.radius_server_root_certificates,
            radius_server_secret=self.radius_server_secret,
            radius_servers=self.radius_servers,
            tags=self.tags,
            type=self.type,
            vpn_authentication_types=self.vpn_authentication_types,
            vpn_client_ipsec_policies=self.vpn_client_ipsec_policies,
            vpn_client_revoked_certificates=self.vpn_client_revoked_certificates,
            vpn_client_root_certificates=self.vpn_client_root_certificates,
            vpn_protocols=self.vpn_protocols)


def get_vpn_server_configuration(resource_group_name: Optional[str] = None,
                                 vpn_server_configuration_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVpnServerConfigurationResult:
    """
    Retrieves the details of a VpnServerConfiguration.
    API Version: 2020-11-01.


    :param str resource_group_name: The resource group name of the VpnServerConfiguration.
    :param str vpn_server_configuration_name: The name of the VpnServerConfiguration being retrieved.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['vpnServerConfigurationName'] = vpn_server_configuration_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network:getVpnServerConfiguration', __args__, opts=opts, typ=GetVpnServerConfigurationResult).value

    return AwaitableGetVpnServerConfigurationResult(
        aad_authentication_parameters=__ret__.aad_authentication_parameters,
        etag=__ret__.etag,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        p2_s_vpn_gateways=__ret__.p2_s_vpn_gateways,
        provisioning_state=__ret__.provisioning_state,
        radius_client_root_certificates=__ret__.radius_client_root_certificates,
        radius_server_address=__ret__.radius_server_address,
        radius_server_root_certificates=__ret__.radius_server_root_certificates,
        radius_server_secret=__ret__.radius_server_secret,
        radius_servers=__ret__.radius_servers,
        tags=__ret__.tags,
        type=__ret__.type,
        vpn_authentication_types=__ret__.vpn_authentication_types,
        vpn_client_ipsec_policies=__ret__.vpn_client_ipsec_policies,
        vpn_client_revoked_certificates=__ret__.vpn_client_revoked_certificates,
        vpn_client_root_certificates=__ret__.vpn_client_root_certificates,
        vpn_protocols=__ret__.vpn_protocols)


@_utilities.lift_output_func(get_vpn_server_configuration)
def get_vpn_server_configuration_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                        vpn_server_configuration_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVpnServerConfigurationResult]:
    """
    Retrieves the details of a VpnServerConfiguration.
    API Version: 2020-11-01.


    :param str resource_group_name: The resource group name of the VpnServerConfiguration.
    :param str vpn_server_configuration_name: The name of the VpnServerConfiguration being retrieved.
    """
    ...
