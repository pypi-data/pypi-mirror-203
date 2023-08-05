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
    'GetEventHubDataConnectionResult',
    'AwaitableGetEventHubDataConnectionResult',
    'get_event_hub_data_connection',
    'get_event_hub_data_connection_output',
]

@pulumi.output_type
class GetEventHubDataConnectionResult:
    """
    Class representing an event hub data connection.
    """
    def __init__(__self__, compression=None, consumer_group=None, data_format=None, event_hub_resource_id=None, event_system_properties=None, id=None, kind=None, location=None, managed_identity_resource_id=None, mapping_rule_name=None, name=None, provisioning_state=None, table_name=None, type=None):
        if compression and not isinstance(compression, str):
            raise TypeError("Expected argument 'compression' to be a str")
        pulumi.set(__self__, "compression", compression)
        if consumer_group and not isinstance(consumer_group, str):
            raise TypeError("Expected argument 'consumer_group' to be a str")
        pulumi.set(__self__, "consumer_group", consumer_group)
        if data_format and not isinstance(data_format, str):
            raise TypeError("Expected argument 'data_format' to be a str")
        pulumi.set(__self__, "data_format", data_format)
        if event_hub_resource_id and not isinstance(event_hub_resource_id, str):
            raise TypeError("Expected argument 'event_hub_resource_id' to be a str")
        pulumi.set(__self__, "event_hub_resource_id", event_hub_resource_id)
        if event_system_properties and not isinstance(event_system_properties, list):
            raise TypeError("Expected argument 'event_system_properties' to be a list")
        pulumi.set(__self__, "event_system_properties", event_system_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_identity_resource_id and not isinstance(managed_identity_resource_id, str):
            raise TypeError("Expected argument 'managed_identity_resource_id' to be a str")
        pulumi.set(__self__, "managed_identity_resource_id", managed_identity_resource_id)
        if mapping_rule_name and not isinstance(mapping_rule_name, str):
            raise TypeError("Expected argument 'mapping_rule_name' to be a str")
        pulumi.set(__self__, "mapping_rule_name", mapping_rule_name)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if table_name and not isinstance(table_name, str):
            raise TypeError("Expected argument 'table_name' to be a str")
        pulumi.set(__self__, "table_name", table_name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def compression(self) -> Optional[str]:
        """
        The event hub messages compression type
        """
        return pulumi.get(self, "compression")

    @property
    @pulumi.getter(name="consumerGroup")
    def consumer_group(self) -> str:
        """
        The event hub consumer group.
        """
        return pulumi.get(self, "consumer_group")

    @property
    @pulumi.getter(name="dataFormat")
    def data_format(self) -> Optional[str]:
        """
        The data format of the message. Optionally the data format can be added to each message.
        """
        return pulumi.get(self, "data_format")

    @property
    @pulumi.getter(name="eventHubResourceId")
    def event_hub_resource_id(self) -> str:
        """
        The resource ID of the event hub to be used to create a data connection.
        """
        return pulumi.get(self, "event_hub_resource_id")

    @property
    @pulumi.getter(name="eventSystemProperties")
    def event_system_properties(self) -> Optional[Sequence[str]]:
        """
        System properties of the event hub
        """
        return pulumi.get(self, "event_system_properties")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of the endpoint for the data connection
        Expected value is 'EventHub'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managedIdentityResourceId")
    def managed_identity_resource_id(self) -> Optional[str]:
        """
        The resource ID of a managed identity (system or user assigned) to be used to authenticate with event hub.
        """
        return pulumi.get(self, "managed_identity_resource_id")

    @property
    @pulumi.getter(name="mappingRuleName")
    def mapping_rule_name(self) -> Optional[str]:
        """
        The mapping rule to be used to ingest the data. Optionally the mapping information can be added to each message.
        """
        return pulumi.get(self, "mapping_rule_name")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioned state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="tableName")
    def table_name(self) -> Optional[str]:
        """
        The table where the data should be ingested. Optionally the table information can be added to each message.
        """
        return pulumi.get(self, "table_name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetEventHubDataConnectionResult(GetEventHubDataConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEventHubDataConnectionResult(
            compression=self.compression,
            consumer_group=self.consumer_group,
            data_format=self.data_format,
            event_hub_resource_id=self.event_hub_resource_id,
            event_system_properties=self.event_system_properties,
            id=self.id,
            kind=self.kind,
            location=self.location,
            managed_identity_resource_id=self.managed_identity_resource_id,
            mapping_rule_name=self.mapping_rule_name,
            name=self.name,
            provisioning_state=self.provisioning_state,
            table_name=self.table_name,
            type=self.type)


def get_event_hub_data_connection(cluster_name: Optional[str] = None,
                                  data_connection_name: Optional[str] = None,
                                  database_name: Optional[str] = None,
                                  resource_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEventHubDataConnectionResult:
    """
    Returns a data connection.


    :param str cluster_name: The name of the Kusto cluster.
    :param str data_connection_name: The name of the data connection.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['dataConnectionName'] = data_connection_name
    __args__['databaseName'] = database_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:kusto/v20210101:getEventHubDataConnection', __args__, opts=opts, typ=GetEventHubDataConnectionResult).value

    return AwaitableGetEventHubDataConnectionResult(
        compression=__ret__.compression,
        consumer_group=__ret__.consumer_group,
        data_format=__ret__.data_format,
        event_hub_resource_id=__ret__.event_hub_resource_id,
        event_system_properties=__ret__.event_system_properties,
        id=__ret__.id,
        kind=__ret__.kind,
        location=__ret__.location,
        managed_identity_resource_id=__ret__.managed_identity_resource_id,
        mapping_rule_name=__ret__.mapping_rule_name,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        table_name=__ret__.table_name,
        type=__ret__.type)


@_utilities.lift_output_func(get_event_hub_data_connection)
def get_event_hub_data_connection_output(cluster_name: Optional[pulumi.Input[str]] = None,
                                         data_connection_name: Optional[pulumi.Input[str]] = None,
                                         database_name: Optional[pulumi.Input[str]] = None,
                                         resource_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEventHubDataConnectionResult]:
    """
    Returns a data connection.


    :param str cluster_name: The name of the Kusto cluster.
    :param str data_connection_name: The name of the data connection.
    :param str database_name: The name of the database in the Kusto cluster.
    :param str resource_group_name: The name of the resource group containing the Kusto cluster.
    """
    ...
