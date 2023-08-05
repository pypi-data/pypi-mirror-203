# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetBandwidthSettingResult',
    'AwaitableGetBandwidthSettingResult',
    'get_bandwidth_setting',
    'get_bandwidth_setting_output',
]

@pulumi.output_type
class GetBandwidthSettingResult:
    """
    The bandwidth setting.
    """
    def __init__(__self__, id=None, kind=None, name=None, schedules=None, type=None, volume_count=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schedules and not isinstance(schedules, list):
            raise TypeError("Expected argument 'schedules' to be a list")
        pulumi.set(__self__, "schedules", schedules)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if volume_count and not isinstance(volume_count, int):
            raise TypeError("Expected argument 'volume_count' to be a int")
        pulumi.set(__self__, "volume_count", volume_count)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedules(self) -> Sequence['outputs.BandwidthScheduleResponse']:
        """
        The schedules.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="volumeCount")
    def volume_count(self) -> int:
        """
        The number of volumes that uses the bandwidth setting.
        """
        return pulumi.get(self, "volume_count")


class AwaitableGetBandwidthSettingResult(GetBandwidthSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetBandwidthSettingResult(
            id=self.id,
            kind=self.kind,
            name=self.name,
            schedules=self.schedules,
            type=self.type,
            volume_count=self.volume_count)


def get_bandwidth_setting(bandwidth_setting_name: Optional[str] = None,
                          manager_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetBandwidthSettingResult:
    """
    Returns the properties of the specified bandwidth setting name.
    API Version: 2017-06-01.


    :param str bandwidth_setting_name: The name of bandwidth setting to be fetched.
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    __args__ = dict()
    __args__['bandwidthSettingName'] = bandwidth_setting_name
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storsimple:getBandwidthSetting', __args__, opts=opts, typ=GetBandwidthSettingResult).value

    return AwaitableGetBandwidthSettingResult(
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        schedules=__ret__.schedules,
        type=__ret__.type,
        volume_count=__ret__.volume_count)


@_utilities.lift_output_func(get_bandwidth_setting)
def get_bandwidth_setting_output(bandwidth_setting_name: Optional[pulumi.Input[str]] = None,
                                 manager_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetBandwidthSettingResult]:
    """
    Returns the properties of the specified bandwidth setting name.
    API Version: 2017-06-01.


    :param str bandwidth_setting_name: The name of bandwidth setting to be fetched.
    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    ...
