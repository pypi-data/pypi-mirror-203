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
    'GetPrivateDnsZoneGroupResult',
    'AwaitableGetPrivateDnsZoneGroupResult',
    'get_private_dns_zone_group',
    'get_private_dns_zone_group_output',
]

@pulumi.output_type
class GetPrivateDnsZoneGroupResult:
    """
    Private dns zone group resource.
    """
    def __init__(__self__, etag=None, id=None, name=None, private_dns_zone_configs=None, provisioning_state=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if private_dns_zone_configs and not isinstance(private_dns_zone_configs, list):
            raise TypeError("Expected argument 'private_dns_zone_configs' to be a list")
        pulumi.set(__self__, "private_dns_zone_configs", private_dns_zone_configs)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)

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
        Name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateDnsZoneConfigs")
    def private_dns_zone_configs(self) -> Optional[Sequence['outputs.PrivateDnsZoneConfigResponse']]:
        """
        A collection of private dns zone configurations of the private dns zone group.
        """
        return pulumi.get(self, "private_dns_zone_configs")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private dns zone group resource.
        """
        return pulumi.get(self, "provisioning_state")


class AwaitableGetPrivateDnsZoneGroupResult(GetPrivateDnsZoneGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetPrivateDnsZoneGroupResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            private_dns_zone_configs=self.private_dns_zone_configs,
            provisioning_state=self.provisioning_state)


def get_private_dns_zone_group(private_dns_zone_group_name: Optional[str] = None,
                               private_endpoint_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetPrivateDnsZoneGroupResult:
    """
    Gets the private dns zone group resource by specified private dns zone group name.


    :param str private_dns_zone_group_name: The name of the private dns zone group.
    :param str private_endpoint_name: The name of the private endpoint.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['privateDnsZoneGroupName'] = private_dns_zone_group_name
    __args__['privateEndpointName'] = private_endpoint_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20200801:getPrivateDnsZoneGroup', __args__, opts=opts, typ=GetPrivateDnsZoneGroupResult).value

    return AwaitableGetPrivateDnsZoneGroupResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        private_dns_zone_configs=__ret__.private_dns_zone_configs,
        provisioning_state=__ret__.provisioning_state)


@_utilities.lift_output_func(get_private_dns_zone_group)
def get_private_dns_zone_group_output(private_dns_zone_group_name: Optional[pulumi.Input[str]] = None,
                                      private_endpoint_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetPrivateDnsZoneGroupResult]:
    """
    Gets the private dns zone group resource by specified private dns zone group name.


    :param str private_dns_zone_group_name: The name of the private dns zone group.
    :param str private_endpoint_name: The name of the private endpoint.
    :param str resource_group_name: The name of the resource group.
    """
    ...
