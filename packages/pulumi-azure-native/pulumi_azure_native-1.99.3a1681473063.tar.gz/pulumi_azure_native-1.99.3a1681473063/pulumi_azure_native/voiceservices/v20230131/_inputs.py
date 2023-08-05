# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'PrimaryRegionPropertiesArgs',
    'ServiceRegionPropertiesArgs',
]

@pulumi.input_type
class PrimaryRegionPropertiesArgs:
    def __init__(__self__, *,
                 operator_addresses: pulumi.Input[Sequence[pulumi.Input[str]]],
                 allowed_media_source_address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 allowed_signaling_source_address_prefixes: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 esrp_addresses: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The configuration used in this region as primary, and other regions as backup.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] operator_addresses: IP address to use to contact the operator network from this region
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_media_source_address_prefixes: The allowed source IP address or CIDR ranges for media
        :param pulumi.Input[Sequence[pulumi.Input[str]]] allowed_signaling_source_address_prefixes: The allowed source IP address or CIDR ranges for signaling
        :param pulumi.Input[Sequence[pulumi.Input[str]]] esrp_addresses: IP address to use to contact the ESRP from this region
        """
        pulumi.set(__self__, "operator_addresses", operator_addresses)
        if allowed_media_source_address_prefixes is not None:
            pulumi.set(__self__, "allowed_media_source_address_prefixes", allowed_media_source_address_prefixes)
        if allowed_signaling_source_address_prefixes is not None:
            pulumi.set(__self__, "allowed_signaling_source_address_prefixes", allowed_signaling_source_address_prefixes)
        if esrp_addresses is not None:
            pulumi.set(__self__, "esrp_addresses", esrp_addresses)

    @property
    @pulumi.getter(name="operatorAddresses")
    def operator_addresses(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        IP address to use to contact the operator network from this region
        """
        return pulumi.get(self, "operator_addresses")

    @operator_addresses.setter
    def operator_addresses(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "operator_addresses", value)

    @property
    @pulumi.getter(name="allowedMediaSourceAddressPrefixes")
    def allowed_media_source_address_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The allowed source IP address or CIDR ranges for media
        """
        return pulumi.get(self, "allowed_media_source_address_prefixes")

    @allowed_media_source_address_prefixes.setter
    def allowed_media_source_address_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_media_source_address_prefixes", value)

    @property
    @pulumi.getter(name="allowedSignalingSourceAddressPrefixes")
    def allowed_signaling_source_address_prefixes(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The allowed source IP address or CIDR ranges for signaling
        """
        return pulumi.get(self, "allowed_signaling_source_address_prefixes")

    @allowed_signaling_source_address_prefixes.setter
    def allowed_signaling_source_address_prefixes(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "allowed_signaling_source_address_prefixes", value)

    @property
    @pulumi.getter(name="esrpAddresses")
    def esrp_addresses(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        IP address to use to contact the ESRP from this region
        """
        return pulumi.get(self, "esrp_addresses")

    @esrp_addresses.setter
    def esrp_addresses(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "esrp_addresses", value)


@pulumi.input_type
class ServiceRegionPropertiesArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 primary_region_properties: pulumi.Input['PrimaryRegionPropertiesArgs']):
        """
        The service region configuration needed for Teams Callings.
        :param pulumi.Input[str] name: The name of the region in which the resources needed for Teams Calling will be deployed.
        :param pulumi.Input['PrimaryRegionPropertiesArgs'] primary_region_properties: The configuration used in this region as primary, and other regions as backup.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "primary_region_properties", primary_region_properties)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The name of the region in which the resources needed for Teams Calling will be deployed.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="primaryRegionProperties")
    def primary_region_properties(self) -> pulumi.Input['PrimaryRegionPropertiesArgs']:
        """
        The configuration used in this region as primary, and other regions as backup.
        """
        return pulumi.get(self, "primary_region_properties")

    @primary_region_properties.setter
    def primary_region_properties(self, value: pulumi.Input['PrimaryRegionPropertiesArgs']):
        pulumi.set(self, "primary_region_properties", value)


