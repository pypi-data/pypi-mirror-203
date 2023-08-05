# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetEventHubEventSourceResult',
    'AwaitableGetEventHubEventSourceResult',
    'get_event_hub_event_source',
    'get_event_hub_event_source_output',
]

@pulumi.output_type
class GetEventHubEventSourceResult:
    """
    An event source that receives its data from an Azure EventHub.
    """
    def __init__(__self__, consumer_group_name=None, creation_time=None, event_hub_name=None, event_source_resource_id=None, id=None, key_name=None, kind=None, location=None, name=None, provisioning_state=None, service_bus_namespace=None, tags=None, timestamp_property_name=None, type=None):
        if consumer_group_name and not isinstance(consumer_group_name, str):
            raise TypeError("Expected argument 'consumer_group_name' to be a str")
        pulumi.set(__self__, "consumer_group_name", consumer_group_name)
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if event_hub_name and not isinstance(event_hub_name, str):
            raise TypeError("Expected argument 'event_hub_name' to be a str")
        pulumi.set(__self__, "event_hub_name", event_hub_name)
        if event_source_resource_id and not isinstance(event_source_resource_id, str):
            raise TypeError("Expected argument 'event_source_resource_id' to be a str")
        pulumi.set(__self__, "event_source_resource_id", event_source_resource_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_name and not isinstance(key_name, str):
            raise TypeError("Expected argument 'key_name' to be a str")
        pulumi.set(__self__, "key_name", key_name)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if service_bus_namespace and not isinstance(service_bus_namespace, str):
            raise TypeError("Expected argument 'service_bus_namespace' to be a str")
        pulumi.set(__self__, "service_bus_namespace", service_bus_namespace)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if timestamp_property_name and not isinstance(timestamp_property_name, str):
            raise TypeError("Expected argument 'timestamp_property_name' to be a str")
        pulumi.set(__self__, "timestamp_property_name", timestamp_property_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="consumerGroupName")
    def consumer_group_name(self) -> str:
        """
        The name of the event hub's consumer group that holds the partitions from which events will be read.
        """
        return pulumi.get(self, "consumer_group_name")

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The time the resource was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="eventHubName")
    def event_hub_name(self) -> str:
        """
        The name of the event hub.
        """
        return pulumi.get(self, "event_hub_name")

    @property
    @pulumi.getter(name="eventSourceResourceId")
    def event_source_resource_id(self) -> str:
        """
        The resource id of the event source in Azure Resource Manager.
        """
        return pulumi.get(self, "event_source_resource_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> str:
        """
        The name of the SAS key that grants the Time Series Insights service access to the event hub. The shared access policies for this key must grant 'Listen' permissions to the event hub.
        """
        return pulumi.get(self, "key_name")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        The kind of the event source.
        Expected value is 'Microsoft.EventHub'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="serviceBusNamespace")
    def service_bus_namespace(self) -> str:
        """
        The name of the service bus that contains the event hub.
        """
        return pulumi.get(self, "service_bus_namespace")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timestampPropertyName")
    def timestamp_property_name(self) -> Optional[str]:
        """
        The event property that will be used as the event source's timestamp. If a value isn't specified for timestampPropertyName, or if null or empty-string is specified, the event creation time will be used.
        """
        return pulumi.get(self, "timestamp_property_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetEventHubEventSourceResult(GetEventHubEventSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventHubEventSourceResult(
            consumer_group_name=self.consumer_group_name,
            creation_time=self.creation_time,
            event_hub_name=self.event_hub_name,
            event_source_resource_id=self.event_source_resource_id,
            id=self.id,
            key_name=self.key_name,
            kind=self.kind,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            service_bus_namespace=self.service_bus_namespace,
            tags=self.tags,
            timestamp_property_name=self.timestamp_property_name,
            type=self.type)


def get_event_hub_event_source(environment_name: Optional[str] = None,
                               event_source_name: Optional[str] = None,
                               resource_group_name: Optional[str] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventHubEventSourceResult:
    """
    Gets the event source with the specified name in the specified environment.


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['eventSourceName'] = event_source_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:timeseriesinsights/v20170228preview:getEventHubEventSource', __args__, opts=opts, typ=GetEventHubEventSourceResult).value

    return AwaitableGetEventHubEventSourceResult(
        consumer_group_name=__ret__.consumer_group_name,
        creation_time=__ret__.creation_time,
        event_hub_name=__ret__.event_hub_name,
        event_source_resource_id=__ret__.event_source_resource_id,
        id=__ret__.id,
        key_name=__ret__.key_name,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        service_bus_namespace=__ret__.service_bus_namespace,
        tags=__ret__.tags,
        timestamp_property_name=__ret__.timestamp_property_name,
        type=__ret__.type)


@_utilities.lift_output_func(get_event_hub_event_source)
def get_event_hub_event_source_output(environment_name: Optional[pulumi.Input[str]] = None,
                                      event_source_name: Optional[pulumi.Input[str]] = None,
                                      resource_group_name: Optional[pulumi.Input[str]] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventHubEventSourceResult]:
    """
    Gets the event source with the specified name in the specified environment.


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str event_source_name: The name of the Time Series Insights event source associated with the specified environment.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    ...
