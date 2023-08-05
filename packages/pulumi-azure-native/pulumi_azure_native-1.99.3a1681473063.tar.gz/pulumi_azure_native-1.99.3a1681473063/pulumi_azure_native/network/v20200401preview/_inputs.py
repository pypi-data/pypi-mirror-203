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
    'InboundEndpointIPConfigurationArgs',
    'SubResourceArgs',
    'TargetDnsServerArgs',
]

@pulumi.input_type
class InboundEndpointIPConfigurationArgs:
    def __init__(__self__, *,
                 private_ip_address: Optional[pulumi.Input[str]] = None,
                 private_ip_allocation_method: Optional[pulumi.Input[Union[str, 'IpAllocationMethod']]] = None,
                 subnet: Optional[pulumi.Input['SubResourceArgs']] = None):
        """
        IP configuration.
        :param pulumi.Input[str] private_ip_address: Private IP address of the IP configuration.
        :param pulumi.Input[Union[str, 'IpAllocationMethod']] private_ip_allocation_method: Private IP address allocation method.
        :param pulumi.Input['SubResourceArgs'] subnet: The reference to the subnet bound to the IP configuration.
        """
        if private_ip_address is not None:
            pulumi.set(__self__, "private_ip_address", private_ip_address)
        if private_ip_allocation_method is None:
            private_ip_allocation_method = 'Dynamic'
        if private_ip_allocation_method is not None:
            pulumi.set(__self__, "private_ip_allocation_method", private_ip_allocation_method)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter(name="privateIpAddress")
    def private_ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        Private IP address of the IP configuration.
        """
        return pulumi.get(self, "private_ip_address")

    @private_ip_address.setter
    def private_ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_ip_address", value)

    @property
    @pulumi.getter(name="privateIpAllocationMethod")
    def private_ip_allocation_method(self) -> Optional[pulumi.Input[Union[str, 'IpAllocationMethod']]]:
        """
        Private IP address allocation method.
        """
        return pulumi.get(self, "private_ip_allocation_method")

    @private_ip_allocation_method.setter
    def private_ip_allocation_method(self, value: Optional[pulumi.Input[Union[str, 'IpAllocationMethod']]]):
        pulumi.set(self, "private_ip_allocation_method", value)

    @property
    @pulumi.getter
    def subnet(self) -> Optional[pulumi.Input['SubResourceArgs']]:
        """
        The reference to the subnet bound to the IP configuration.
        """
        return pulumi.get(self, "subnet")

    @subnet.setter
    def subnet(self, value: Optional[pulumi.Input['SubResourceArgs']]):
        pulumi.set(self, "subnet", value)


@pulumi.input_type
class SubResourceArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Reference to another ARM resource.
        :param pulumi.Input[str] id: Resource ID.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

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


@pulumi.input_type
class TargetDnsServerArgs:
    def __init__(__self__, *,
                 ip_address: Optional[pulumi.Input[str]] = None,
                 port: Optional[pulumi.Input[int]] = None):
        """
        Describes a server to forward the DNS queries to.
        :param pulumi.Input[str] ip_address: DNS server IP address.
        :param pulumi.Input[int] port: DNS server port.
        """
        if ip_address is not None:
            pulumi.set(__self__, "ip_address", ip_address)
        if port is None:
            port = 53
        if port is not None:
            pulumi.set(__self__, "port", port)

    @property
    @pulumi.getter(name="ipAddress")
    def ip_address(self) -> Optional[pulumi.Input[str]]:
        """
        DNS server IP address.
        """
        return pulumi.get(self, "ip_address")

    @ip_address.setter
    def ip_address(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "ip_address", value)

    @property
    @pulumi.getter
    def port(self) -> Optional[pulumi.Input[int]]:
        """
        DNS server port.
        """
        return pulumi.get(self, "port")

    @port.setter
    def port(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "port", value)


