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
    'GetFileEventTriggerResult',
    'AwaitableGetFileEventTriggerResult',
    'get_file_event_trigger',
    'get_file_event_trigger_output',
]

@pulumi.output_type
class GetFileEventTriggerResult:
    """
    Trigger details.
    """
    def __init__(__self__, custom_context_tag=None, id=None, kind=None, name=None, sink_info=None, source_info=None, system_data=None, type=None):
        if custom_context_tag and not isinstance(custom_context_tag, str):
            raise TypeError("Expected argument 'custom_context_tag' to be a str")
        pulumi.set(__self__, "custom_context_tag", custom_context_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sink_info and not isinstance(sink_info, dict):
            raise TypeError("Expected argument 'sink_info' to be a dict")
        pulumi.set(__self__, "sink_info", sink_info)
        if source_info and not isinstance(source_info, dict):
            raise TypeError("Expected argument 'source_info' to be a dict")
        pulumi.set(__self__, "source_info", source_info)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="customContextTag")
    def custom_context_tag(self) -> Optional[str]:
        """
        A custom context tag typically used to correlate the trigger against its usage. For example, if a periodic timer trigger is intended for certain specific IoT modules in the device, the tag can be the name or the image URL of the module.
        """
        return pulumi.get(self, "custom_context_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Trigger Kind.
        Expected value is 'FileEvent'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="sinkInfo")
    def sink_info(self) -> 'outputs.RoleSinkInfoResponse':
        """
        Role sink info.
        """
        return pulumi.get(self, "sink_info")

    @property
    @pulumi.getter(name="sourceInfo")
    def source_info(self) -> 'outputs.FileSourceInfoResponse':
        """
        File event source details.
        """
        return pulumi.get(self, "source_info")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Trigger in DataBoxEdge Resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")


class AwaitableGetFileEventTriggerResult(GetFileEventTriggerResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFileEventTriggerResult(
            custom_context_tag=self.custom_context_tag,
            id=self.id,
            kind=self.kind,
            name=self.name,
            sink_info=self.sink_info,
            source_info=self.source_info,
            system_data=self.system_data,
            type=self.type)


def get_file_event_trigger(device_name: Optional[str] = None,
                           name: Optional[str] = None,
                           resource_group_name: Optional[str] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFileEventTriggerResult:
    """
    Get a specific trigger by name.


    :param str device_name: The device name.
    :param str name: The trigger name.
    :param str resource_group_name: The resource group name.
    """
    __args__ = dict()
    __args__['deviceName'] = device_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:databoxedge/v20210201preview:getFileEventTrigger', __args__, opts=opts, typ=GetFileEventTriggerResult).value

    return AwaitableGetFileEventTriggerResult(
        custom_context_tag=__ret__.custom_context_tag,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        sink_info=__ret__.sink_info,
        source_info=__ret__.source_info,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_file_event_trigger)
def get_file_event_trigger_output(device_name: Optional[pulumi.Input[str]] = None,
                                  name: Optional[pulumi.Input[str]] = None,
                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFileEventTriggerResult]:
    """
    Get a specific trigger by name.


    :param str device_name: The device name.
    :param str name: The trigger name.
    :param str resource_group_name: The resource group name.
    """
    ...
