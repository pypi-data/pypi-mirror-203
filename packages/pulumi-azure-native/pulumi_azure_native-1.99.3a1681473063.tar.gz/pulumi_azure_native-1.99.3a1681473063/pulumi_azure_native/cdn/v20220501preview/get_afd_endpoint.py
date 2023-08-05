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
    'GetAFDEndpointResult',
    'AwaitableGetAFDEndpointResult',
    'get_afd_endpoint',
    'get_afd_endpoint_output',
]

@pulumi.output_type
class GetAFDEndpointResult:
    """
    CDN endpoint is the entity within a CDN profile containing configuration information such as origin, protocol, content caching and delivery behavior. The AzureFrontDoor endpoint uses the URL format <endpointname>.azureedge.net.
    """
    def __init__(__self__, auto_generated_domain_name_label_scope=None, deployment_status=None, enabled_state=None, host_name=None, id=None, location=None, name=None, profile_name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if auto_generated_domain_name_label_scope and not isinstance(auto_generated_domain_name_label_scope, str):
            raise TypeError("Expected argument 'auto_generated_domain_name_label_scope' to be a str")
        pulumi.set(__self__, "auto_generated_domain_name_label_scope", auto_generated_domain_name_label_scope)
        if deployment_status and not isinstance(deployment_status, str):
            raise TypeError("Expected argument 'deployment_status' to be a str")
        pulumi.set(__self__, "deployment_status", deployment_status)
        if enabled_state and not isinstance(enabled_state, str):
            raise TypeError("Expected argument 'enabled_state' to be a str")
        pulumi.set(__self__, "enabled_state", enabled_state)
        if host_name and not isinstance(host_name, str):
            raise TypeError("Expected argument 'host_name' to be a str")
        pulumi.set(__self__, "host_name", host_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if profile_name and not isinstance(profile_name, str):
            raise TypeError("Expected argument 'profile_name' to be a str")
        pulumi.set(__self__, "profile_name", profile_name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="autoGeneratedDomainNameLabelScope")
    def auto_generated_domain_name_label_scope(self) -> Optional[str]:
        """
        Indicates the endpoint name reuse scope. The default value is TenantReuse.
        """
        return pulumi.get(self, "auto_generated_domain_name_label_scope")

    @property
    @pulumi.getter(name="deploymentStatus")
    def deployment_status(self) -> str:
        return pulumi.get(self, "deployment_status")

    @property
    @pulumi.getter(name="enabledState")
    def enabled_state(self) -> Optional[str]:
        """
        Whether to enable use of this rule. Permitted values are 'Enabled' or 'Disabled'
        """
        return pulumi.get(self, "enabled_state")

    @property
    @pulumi.getter(name="hostName")
    def host_name(self) -> str:
        """
        The host name of the endpoint structured as {endpointName}.{DNSZone}, e.g. contoso.azureedge.net
        """
        return pulumi.get(self, "host_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="profileName")
    def profile_name(self) -> str:
        """
        The name of the profile which holds the endpoint.
        """
        return pulumi.get(self, "profile_name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning status
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Read only system data
        """
        return pulumi.get(self, "system_data")

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


class AwaitableGetAFDEndpointResult(GetAFDEndpointResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAFDEndpointResult(
            auto_generated_domain_name_label_scope=self.auto_generated_domain_name_label_scope,
            deployment_status=self.deployment_status,
            enabled_state=self.enabled_state,
            host_name=self.host_name,
            id=self.id,
            location=self.location,
            name=self.name,
            profile_name=self.profile_name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_afd_endpoint(endpoint_name: Optional[str] = None,
                     profile_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAFDEndpointResult:
    """
    Gets an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile.


    :param str endpoint_name: Name of the endpoint under the profile which is unique globally.
    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    __args__ = dict()
    __args__['endpointName'] = endpoint_name
    __args__['profileName'] = profile_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:cdn/v20220501preview:getAFDEndpoint', __args__, opts=opts, typ=GetAFDEndpointResult).value

    return AwaitableGetAFDEndpointResult(
        auto_generated_domain_name_label_scope=__ret__.auto_generated_domain_name_label_scope,
        deployment_status=__ret__.deployment_status,
        enabled_state=__ret__.enabled_state,
        host_name=__ret__.host_name,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        profile_name=__ret__.profile_name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_afd_endpoint)
def get_afd_endpoint_output(endpoint_name: Optional[pulumi.Input[str]] = None,
                            profile_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAFDEndpointResult]:
    """
    Gets an existing AzureFrontDoor endpoint with the specified endpoint name under the specified subscription, resource group and profile.


    :param str endpoint_name: Name of the endpoint under the profile which is unique globally.
    :param str profile_name: Name of the Azure Front Door Standard or Azure Front Door Premium profile which is unique within the resource group.
    :param str resource_group_name: Name of the Resource group within the Azure subscription.
    """
    ...
