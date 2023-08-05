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
    'GetNamespaceResult',
    'AwaitableGetNamespaceResult',
    'get_namespace',
    'get_namespace_output',
]

@pulumi.output_type
class GetNamespaceResult:
    """
    Description of a Namespace resource.
    """
    def __init__(__self__, created_at=None, critical=None, data_center=None, enabled=None, id=None, location=None, metric_id=None, name=None, namespace_type=None, provisioning_state=None, region=None, scale_unit=None, service_bus_endpoint=None, sku=None, status=None, subscription_id=None, tags=None, type=None, updated_at=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if critical and not isinstance(critical, bool):
            raise TypeError("Expected argument 'critical' to be a bool")
        pulumi.set(__self__, "critical", critical)
        if data_center and not isinstance(data_center, str):
            raise TypeError("Expected argument 'data_center' to be a str")
        pulumi.set(__self__, "data_center", data_center)
        if enabled and not isinstance(enabled, bool):
            raise TypeError("Expected argument 'enabled' to be a bool")
        pulumi.set(__self__, "enabled", enabled)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if metric_id and not isinstance(metric_id, str):
            raise TypeError("Expected argument 'metric_id' to be a str")
        pulumi.set(__self__, "metric_id", metric_id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if namespace_type and not isinstance(namespace_type, str):
            raise TypeError("Expected argument 'namespace_type' to be a str")
        pulumi.set(__self__, "namespace_type", namespace_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if region and not isinstance(region, str):
            raise TypeError("Expected argument 'region' to be a str")
        pulumi.set(__self__, "region", region)
        if scale_unit and not isinstance(scale_unit, str):
            raise TypeError("Expected argument 'scale_unit' to be a str")
        pulumi.set(__self__, "scale_unit", scale_unit)
        if service_bus_endpoint and not isinstance(service_bus_endpoint, str):
            raise TypeError("Expected argument 'service_bus_endpoint' to be a str")
        pulumi.set(__self__, "service_bus_endpoint", service_bus_endpoint)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if subscription_id and not isinstance(subscription_id, str):
            raise TypeError("Expected argument 'subscription_id' to be a str")
        pulumi.set(__self__, "subscription_id", subscription_id)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_at and not isinstance(updated_at, str):
            raise TypeError("Expected argument 'updated_at' to be a str")
        pulumi.set(__self__, "updated_at", updated_at)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The time the namespace was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter
    def critical(self) -> Optional[bool]:
        """
        Whether or not the namespace is set as Critical.
        """
        return pulumi.get(self, "critical")

    @property
    @pulumi.getter(name="dataCenter")
    def data_center(self) -> Optional[str]:
        """
        Data center for the namespace
        """
        return pulumi.get(self, "data_center")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Whether or not the namespace is currently enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="metricId")
    def metric_id(self) -> str:
        """
        Identifier for Azure Insights metrics
        """
        return pulumi.get(self, "metric_id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="namespaceType")
    def namespace_type(self) -> Optional[str]:
        """
        The namespace type.
        """
        return pulumi.get(self, "namespace_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        Provisioning state of the Namespace.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def region(self) -> Optional[str]:
        """
        Specifies the targeted region in which the namespace should be created. It can be any of the following values: Australia East, Australia Southeast, Central US, East US, East US 2, West US, North Central US, South Central US, East Asia, Southeast Asia, Brazil South, Japan East, Japan West, North Europe, West Europe
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="scaleUnit")
    def scale_unit(self) -> Optional[str]:
        """
        ScaleUnit where the namespace gets created
        """
        return pulumi.get(self, "scale_unit")

    @property
    @pulumi.getter(name="serviceBusEndpoint")
    def service_bus_endpoint(self) -> Optional[str]:
        """
        Endpoint you can use to perform NotificationHub operations.
        """
        return pulumi.get(self, "service_bus_endpoint")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The sku of the created namespace
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of the namespace. It can be any of these values:1 = Created/Active2 = Creating3 = Suspended4 = Deleting
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[str]:
        """
        The Id of the Azure subscription associated with the namespace.
        """
        return pulumi.get(self, "subscription_id")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedAt")
    def updated_at(self) -> Optional[str]:
        """
        The time the namespace was updated.
        """
        return pulumi.get(self, "updated_at")


class AwaitableGetNamespaceResult(GetNamespaceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNamespaceResult(
            created_at=self.created_at,
            critical=self.critical,
            data_center=self.data_center,
            enabled=self.enabled,
            id=self.id,
            location=self.location,
            metric_id=self.metric_id,
            name=self.name,
            namespace_type=self.namespace_type,
            provisioning_state=self.provisioning_state,
            region=self.region,
            scale_unit=self.scale_unit,
            service_bus_endpoint=self.service_bus_endpoint,
            sku=self.sku,
            status=self.status,
            subscription_id=self.subscription_id,
            tags=self.tags,
            type=self.type,
            updated_at=self.updated_at)


def get_namespace(namespace_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNamespaceResult:
    """
    Returns the description for the specified namespace.


    :param str namespace_name: The namespace name.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['namespaceName'] = namespace_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:notificationhubs/v20170401:getNamespace', __args__, opts=opts, typ=GetNamespaceResult).value

    return AwaitableGetNamespaceResult(
        created_at=__ret__.created_at,
        critical=__ret__.critical,
        data_center=__ret__.data_center,
        enabled=__ret__.enabled,
        id=__ret__.id,
        location=__ret__.location,
        metric_id=__ret__.metric_id,
        name=__ret__.name,
        namespace_type=__ret__.namespace_type,
        provisioning_state=__ret__.provisioning_state,
        region=__ret__.region,
        scale_unit=__ret__.scale_unit,
        service_bus_endpoint=__ret__.service_bus_endpoint,
        sku=__ret__.sku,
        status=__ret__.status,
        subscription_id=__ret__.subscription_id,
        tags=__ret__.tags,
        type=__ret__.type,
        updated_at=__ret__.updated_at)


@_utilities.lift_output_func(get_namespace)
def get_namespace_output(namespace_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNamespaceResult]:
    """
    Returns the description for the specified namespace.


    :param str namespace_name: The namespace name.
    :param str resource_group_name: The name of the resource group.
    """
    ...
