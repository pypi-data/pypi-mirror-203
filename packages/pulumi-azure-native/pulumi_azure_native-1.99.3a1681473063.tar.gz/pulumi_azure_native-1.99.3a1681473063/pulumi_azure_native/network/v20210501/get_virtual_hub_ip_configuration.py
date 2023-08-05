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
    'GetVirtualHubIpConfigurationResult',
    'AwaitableGetVirtualHubIpConfigurationResult',
    'get_virtual_hub_ip_configuration',
    'get_virtual_hub_ip_configuration_output',
]

@pulumi.output_type
class GetVirtualHubIpConfigurationResult:
    """
    IpConfigurations.
    """
    def __init__(__self__, etag=None, id=None, name=None, private_ip_address=None, private_ip_allocation_method=None, provisioning_state=None, public_ip_address=None, subnet=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_ip_address and not isinstance(private_ip_address, str):
            raise TypeError("Expected argument 'private_ip_address' to be a str")
        pulumi.set(__self__, "private_ip_address", private_ip_address)
        if private_ip_allocation_method and not isinstance(private_ip_allocation_method, str):
            raise TypeError("Expected argument 'private_ip_allocation_method' to be a str")
        pulumi.set(__self__, "private_ip_allocation_method", private_ip_allocation_method)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_ip_address and not isinstance(public_ip_address, dict):
            raise TypeError("Expected argument 'public_ip_address' to be a dict")
        pulumi.set(__self__, "public_ip_address", public_ip_address)
        if subnet and not isinstance(subnet, dict):
            raise TypeError("Expected argument 'subnet' to be a dict")
        pulumi.set(__self__, "subnet", subnet)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    def name(self) -> Optional[str]:
        """
        Name of the Ip Configuration.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateIPAddress")
    def private_ip_address(self) -> Optional[str]:
        """
        The private IP address of the IP configuration.
        """
        return pulumi.get(self, "private_ip_address")

    @property
    @pulumi.getter(name="privateIPAllocationMethod")
    def private_ip_allocation_method(self) -> Optional[str]:
        """
        The private IP address allocation method.
        """
        return pulumi.get(self, "private_ip_allocation_method")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the IP configuration resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicIPAddress")
    def public_ip_address(self) -> Optional['outputs.PublicIPAddressResponse']:
        """
        The reference to the public IP resource.
        """
        return pulumi.get(self, "public_ip_address")

    @property
    @pulumi.getter
    def subnet(self) -> Optional['outputs.SubnetResponse']:
        """
        The reference to the subnet resource.
        """
        return pulumi.get(self, "subnet")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Ipconfiguration type.
        """
        return pulumi.get(self, "type")


class AwaitableGetVirtualHubIpConfigurationResult(GetVirtualHubIpConfigurationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVirtualHubIpConfigurationResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            private_ip_address=self.private_ip_address,
            private_ip_allocation_method=self.private_ip_allocation_method,
            provisioning_state=self.provisioning_state,
            public_ip_address=self.public_ip_address,
            subnet=self.subnet,
            type=self.type)


def get_virtual_hub_ip_configuration(ip_config_name: Optional[str] = None,
                                     resource_group_name: Optional[str] = None,
                                     virtual_hub_name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVirtualHubIpConfigurationResult:
    """
    Retrieves the details of a Virtual Hub Ip configuration.


    :param str ip_config_name: The name of the ipconfig.
    :param str resource_group_name: The resource group name of the VirtualHub.
    :param str virtual_hub_name: The name of the VirtualHub.
    """
    __args__ = dict()
    __args__['ipConfigName'] = ip_config_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['virtualHubName'] = virtual_hub_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20210501:getVirtualHubIpConfiguration', __args__, opts=opts, typ=GetVirtualHubIpConfigurationResult).value

    return AwaitableGetVirtualHubIpConfigurationResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        private_ip_address=__ret__.private_ip_address,
        private_ip_allocation_method=__ret__.private_ip_allocation_method,
        provisioning_state=__ret__.provisioning_state,
        public_ip_address=__ret__.public_ip_address,
        subnet=__ret__.subnet,
        type=__ret__.type)


@_utilities.lift_output_func(get_virtual_hub_ip_configuration)
def get_virtual_hub_ip_configuration_output(ip_config_name: Optional[pulumi.Input[str]] = None,
                                            resource_group_name: Optional[pulumi.Input[str]] = None,
                                            virtual_hub_name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVirtualHubIpConfigurationResult]:
    """
    Retrieves the details of a Virtual Hub Ip configuration.


    :param str ip_config_name: The name of the ipconfig.
    :param str resource_group_name: The resource group name of the VirtualHub.
    :param str virtual_hub_name: The name of the VirtualHub.
    """
    ...
