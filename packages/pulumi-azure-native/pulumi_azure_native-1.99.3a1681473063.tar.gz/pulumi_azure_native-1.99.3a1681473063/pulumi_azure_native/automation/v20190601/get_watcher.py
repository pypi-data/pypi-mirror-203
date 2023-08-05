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
    'GetWatcherResult',
    'AwaitableGetWatcherResult',
    'get_watcher',
    'get_watcher_output',
]

@pulumi.output_type
class GetWatcherResult:
    """
    Definition of the watcher type.
    """
    def __init__(__self__, creation_time=None, description=None, etag=None, execution_frequency_in_seconds=None, id=None, last_modified_by=None, last_modified_time=None, location=None, name=None, script_name=None, script_parameters=None, script_run_on=None, status=None, tags=None, type=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if execution_frequency_in_seconds and not isinstance(execution_frequency_in_seconds, float):
            raise TypeError("Expected argument 'execution_frequency_in_seconds' to be a float")
        pulumi.set(__self__, "execution_frequency_in_seconds", execution_frequency_in_seconds)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_by and not isinstance(last_modified_by, str):
            raise TypeError("Expected argument 'last_modified_by' to be a str")
        pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if script_name and not isinstance(script_name, str):
            raise TypeError("Expected argument 'script_name' to be a str")
        pulumi.set(__self__, "script_name", script_name)
        if script_parameters and not isinstance(script_parameters, dict):
            raise TypeError("Expected argument 'script_parameters' to be a dict")
        pulumi.set(__self__, "script_parameters", script_parameters)
        if script_run_on and not isinstance(script_run_on, str):
            raise TypeError("Expected argument 'script_run_on' to be a str")
        pulumi.set(__self__, "script_run_on", script_run_on)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
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
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Gets or sets the etag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="executionFrequencyInSeconds")
    def execution_frequency_in_seconds(self) -> Optional[float]:
        """
        Gets or sets the frequency at which the watcher is invoked.
        """
        return pulumi.get(self, "execution_frequency_in_seconds")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> str:
        """
        Details of the user who last modified the watcher.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="scriptName")
    def script_name(self) -> Optional[str]:
        """
        Gets or sets the name of the script the watcher is attached to, i.e. the name of an existing runbook.
        """
        return pulumi.get(self, "script_name")

    @property
    @pulumi.getter(name="scriptParameters")
    def script_parameters(self) -> Optional[Mapping[str, str]]:
        """
        Gets or sets the parameters of the script.
        """
        return pulumi.get(self, "script_parameters")

    @property
    @pulumi.getter(name="scriptRunOn")
    def script_run_on(self) -> Optional[str]:
        """
        Gets or sets the name of the hybrid worker group the watcher will run on.
        """
        return pulumi.get(self, "script_run_on")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Gets the current status of the watcher.
        """
        return pulumi.get(self, "status")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetWatcherResult(GetWatcherResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWatcherResult(
            creation_time=self.creation_time,
            description=self.description,
            etag=self.etag,
            execution_frequency_in_seconds=self.execution_frequency_in_seconds,
            id=self.id,
            last_modified_by=self.last_modified_by,
            last_modified_time=self.last_modified_time,
            location=self.location,
            name=self.name,
            script_name=self.script_name,
            script_parameters=self.script_parameters,
            script_run_on=self.script_run_on,
            status=self.status,
            tags=self.tags,
            type=self.type)


def get_watcher(automation_account_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                watcher_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWatcherResult:
    """
    Retrieve the watcher identified by watcher name.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    :param str watcher_name: The watcher name.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['watcherName'] = watcher_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20190601:getWatcher', __args__, opts=opts, typ=GetWatcherResult).value

    return AwaitableGetWatcherResult(
        creation_time=__ret__.creation_time,
        description=__ret__.description,
        etag=__ret__.etag,
        execution_frequency_in_seconds=__ret__.execution_frequency_in_seconds,
        id=__ret__.id,
        last_modified_by=__ret__.last_modified_by,
        last_modified_time=__ret__.last_modified_time,
        location=__ret__.location,
        name=__ret__.name,
        script_name=__ret__.script_name,
        script_parameters=__ret__.script_parameters,
        script_run_on=__ret__.script_run_on,
        status=__ret__.status,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_watcher)
def get_watcher_output(automation_account_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       watcher_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWatcherResult]:
    """
    Retrieve the watcher identified by watcher name.


    :param str automation_account_name: The name of the automation account.
    :param str resource_group_name: Name of an Azure Resource group.
    :param str watcher_name: The watcher name.
    """
    ...
