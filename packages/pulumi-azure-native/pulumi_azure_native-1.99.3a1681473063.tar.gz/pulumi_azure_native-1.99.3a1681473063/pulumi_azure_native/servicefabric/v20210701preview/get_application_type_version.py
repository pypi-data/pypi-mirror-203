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
    'GetApplicationTypeVersionResult',
    'AwaitableGetApplicationTypeVersionResult',
    'get_application_type_version',
    'get_application_type_version_output',
]

@pulumi.output_type
class GetApplicationTypeVersionResult:
    """
    An application type version resource for the specified application type name resource.
    """
    def __init__(__self__, app_package_url=None, id=None, location=None, name=None, provisioning_state=None, system_data=None, tags=None, type=None):
        if app_package_url and not isinstance(app_package_url, str):
            raise TypeError("Expected argument 'app_package_url' to be a str")
        pulumi.set(__self__, "app_package_url", app_package_url)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
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
    @pulumi.getter(name="appPackageUrl")
    def app_package_url(self) -> str:
        """
        The URL to the application package
        """
        return pulumi.get(self, "app_package_url")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location depends on the parent resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment or provisioning state, which only appears in the response
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetApplicationTypeVersionResult(GetApplicationTypeVersionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApplicationTypeVersionResult(
            app_package_url=self.app_package_url,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_application_type_version(application_type_name: Optional[str] = None,
                                 cluster_name: Optional[str] = None,
                                 resource_group_name: Optional[str] = None,
                                 version: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApplicationTypeVersionResult:
    """
    Get a Service Fabric managed application type version resource created or in the process of being created in the Service Fabric managed application type name resource.


    :param str application_type_name: The name of the application type name resource.
    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    :param str version: The application type version.
    """
    __args__ = dict()
    __args__['applicationTypeName'] = application_type_name
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['version'] = version
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric/v20210701preview:getApplicationTypeVersion', __args__, opts=opts, typ=GetApplicationTypeVersionResult).value

    return AwaitableGetApplicationTypeVersionResult(
        app_package_url=__ret__.app_package_url,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_application_type_version)
def get_application_type_version_output(application_type_name: Optional[pulumi.Input[str]] = None,
                                        cluster_name: Optional[pulumi.Input[str]] = None,
                                        resource_group_name: Optional[pulumi.Input[str]] = None,
                                        version: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApplicationTypeVersionResult]:
    """
    Get a Service Fabric managed application type version resource created or in the process of being created in the Service Fabric managed application type name resource.


    :param str application_type_name: The name of the application type name resource.
    :param str cluster_name: The name of the cluster resource.
    :param str resource_group_name: The name of the resource group.
    :param str version: The application type version.
    """
    ...
