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
    'GetEnvironmentResult',
    'AwaitableGetEnvironmentResult',
    'get_environment',
    'get_environment_output',
]

warnings.warn("""Version 2017-11-15 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetEnvironmentResult:
    """
    An environment is a set of time-series data available for query, and is the top level Azure Time Series Insights resource.
    """
    def __init__(__self__, creation_time=None, data_access_fqdn=None, data_access_id=None, data_retention_time=None, id=None, location=None, name=None, partition_key_properties=None, provisioning_state=None, sku=None, status=None, storage_limit_exceeded_behavior=None, tags=None, type=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if data_access_fqdn and not isinstance(data_access_fqdn, str):
            raise TypeError("Expected argument 'data_access_fqdn' to be a str")
        pulumi.set(__self__, "data_access_fqdn", data_access_fqdn)
        if data_access_id and not isinstance(data_access_id, str):
            raise TypeError("Expected argument 'data_access_id' to be a str")
        pulumi.set(__self__, "data_access_id", data_access_id)
        if data_retention_time and not isinstance(data_retention_time, str):
            raise TypeError("Expected argument 'data_retention_time' to be a str")
        pulumi.set(__self__, "data_retention_time", data_retention_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if partition_key_properties and not isinstance(partition_key_properties, list):
            raise TypeError("Expected argument 'partition_key_properties' to be a list")
        pulumi.set(__self__, "partition_key_properties", partition_key_properties)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if storage_limit_exceeded_behavior and not isinstance(storage_limit_exceeded_behavior, str):
            raise TypeError("Expected argument 'storage_limit_exceeded_behavior' to be a str")
        pulumi.set(__self__, "storage_limit_exceeded_behavior", storage_limit_exceeded_behavior)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        The time the resource was created.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter(name="dataAccessFqdn")
    def data_access_fqdn(self) -> str:
        """
        The fully qualified domain name used to access the environment data, e.g. to query the environment's events or upload reference data for the environment.
        """
        return pulumi.get(self, "data_access_fqdn")

    @property
    @pulumi.getter(name="dataAccessId")
    def data_access_id(self) -> str:
        """
        An id used to access the environment data, e.g. to query the environment's events or upload reference data for the environment.
        """
        return pulumi.get(self, "data_access_id")

    @property
    @pulumi.getter(name="dataRetentionTime")
    def data_retention_time(self) -> str:
        """
        ISO8601 timespan specifying the minimum number of days the environment's events will be available for query.
        """
        return pulumi.get(self, "data_retention_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="partitionKeyProperties")
    def partition_key_properties(self) -> Optional[Sequence['outputs.PartitionKeyPropertyResponse']]:
        """
        The list of partition keys according to which the data in the environment will be ordered.
        """
        return pulumi.get(self, "partition_key_properties")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.SkuResponse']:
        """
        The sku determines the capacity of the environment, the SLA (in queries-per-minute and total capacity), and the billing rate.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.EnvironmentStatusResponse':
        """
        An object that represents the status of the environment, and its internal state in the Time Series Insights service.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageLimitExceededBehavior")
    def storage_limit_exceeded_behavior(self) -> Optional[str]:
        """
        The behavior the Time Series Insights service should take when the environment's capacity has been exceeded. If "PauseIngress" is specified, new events will not be read from the event source. If "PurgeOldData" is specified, new events will continue to be read and old events will be deleted from the environment. The default behavior is PurgeOldData.
        """
        return pulumi.get(self, "storage_limit_exceeded_behavior")

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


class AwaitableGetEnvironmentResult(GetEnvironmentResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetEnvironmentResult(
            creation_time=self.creation_time,
            data_access_fqdn=self.data_access_fqdn,
            data_access_id=self.data_access_id,
            data_retention_time=self.data_retention_time,
            id=self.id,
            location=self.location,
            name=self.name,
            partition_key_properties=self.partition_key_properties,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            status=self.status,
            storage_limit_exceeded_behavior=self.storage_limit_exceeded_behavior,
            tags=self.tags,
            type=self.type)


def get_environment(environment_name: Optional[str] = None,
                    expand: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetEnvironmentResult:
    """
    Gets the environment with the specified name in the specified subscription and resource group.


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str expand: Setting $expand=status will include the status of the internal services of the environment in the Time Series Insights service.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    pulumi.log.warn("""get_environment is deprecated: Version 2017-11-15 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['environmentName'] = environment_name
    __args__['expand'] = expand
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:timeseriesinsights/v20171115:getEnvironment', __args__, opts=opts, typ=GetEnvironmentResult).value

    return AwaitableGetEnvironmentResult(
        creation_time=__ret__.creation_time,
        data_access_fqdn=__ret__.data_access_fqdn,
        data_access_id=__ret__.data_access_id,
        data_retention_time=__ret__.data_retention_time,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        partition_key_properties=__ret__.partition_key_properties,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        status=__ret__.status,
        storage_limit_exceeded_behavior=__ret__.storage_limit_exceeded_behavior,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_environment)
def get_environment_output(environment_name: Optional[pulumi.Input[str]] = None,
                           expand: Optional[pulumi.Input[Optional[str]]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetEnvironmentResult]:
    """
    Gets the environment with the specified name in the specified subscription and resource group.


    :param str environment_name: The name of the Time Series Insights environment associated with the specified resource group.
    :param str expand: Setting $expand=status will include the status of the internal services of the environment in the Time Series Insights service.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    pulumi.log.warn("""get_environment is deprecated: Version 2017-11-15 will be removed in v2 of the provider.""")
    ...
