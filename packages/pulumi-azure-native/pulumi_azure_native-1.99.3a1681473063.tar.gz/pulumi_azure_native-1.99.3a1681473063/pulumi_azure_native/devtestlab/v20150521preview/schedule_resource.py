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
from ._enums import *
from ._inputs import *

__all__ = ['ScheduleResourceArgs', 'ScheduleResource']

@pulumi.input_type
class ScheduleResourceArgs:
    def __init__(__self__, *,
                 lab_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 daily_recurrence: Optional[pulumi.Input['DayDetailsArgs']] = None,
                 hourly_recurrence: Optional[pulumi.Input['HourDetailsArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 task_type: Optional[pulumi.Input[Union[str, 'TaskType']]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weekly_recurrence: Optional[pulumi.Input['WeekDetailsArgs']] = None):
        """
        The set of arguments for constructing a ScheduleResource resource.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input['DayDetailsArgs'] daily_recurrence: The daily recurrence of the schedule.
        :param pulumi.Input['HourDetailsArgs'] hourly_recurrence: The hourly recurrence of the schedule.
        :param pulumi.Input[str] id: The identifier of the resource.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[Union[str, 'EnableStatus']] status: The status of the schedule.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[Union[str, 'TaskType']] task_type: The task type of the schedule.
        :param pulumi.Input[str] time_zone_id: The time zone id.
        :param pulumi.Input[str] type: The type of the resource.
        :param pulumi.Input['WeekDetailsArgs'] weekly_recurrence: The weekly recurrence of the schedule.
        """
        pulumi.set(__self__, "lab_name", lab_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if daily_recurrence is not None:
            pulumi.set(__self__, "daily_recurrence", daily_recurrence)
        if hourly_recurrence is not None:
            pulumi.set(__self__, "hourly_recurrence", hourly_recurrence)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if provisioning_state is not None:
            pulumi.set(__self__, "provisioning_state", provisioning_state)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if task_type is not None:
            pulumi.set(__self__, "task_type", task_type)
        if time_zone_id is not None:
            pulumi.set(__self__, "time_zone_id", time_zone_id)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if weekly_recurrence is not None:
            pulumi.set(__self__, "weekly_recurrence", weekly_recurrence)

    @property
    @pulumi.getter(name="labName")
    def lab_name(self) -> pulumi.Input[str]:
        """
        The name of the lab.
        """
        return pulumi.get(self, "lab_name")

    @lab_name.setter
    def lab_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "lab_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> Optional[pulumi.Input['DayDetailsArgs']]:
        """
        The daily recurrence of the schedule.
        """
        return pulumi.get(self, "daily_recurrence")

    @daily_recurrence.setter
    def daily_recurrence(self, value: Optional[pulumi.Input['DayDetailsArgs']]):
        pulumi.set(self, "daily_recurrence", value)

    @property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> Optional[pulumi.Input['HourDetailsArgs']]:
        """
        The hourly recurrence of the schedule.
        """
        return pulumi.get(self, "hourly_recurrence")

    @hourly_recurrence.setter
    def hourly_recurrence(self, value: Optional[pulumi.Input['HourDetailsArgs']]):
        pulumi.set(self, "hourly_recurrence", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[pulumi.Input[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @provisioning_state.setter
    def provisioning_state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "provisioning_state", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'EnableStatus']]]:
        """
        The status of the schedule.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'EnableStatus']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter(name="taskType")
    def task_type(self) -> Optional[pulumi.Input[Union[str, 'TaskType']]]:
        """
        The task type of the schedule.
        """
        return pulumi.get(self, "task_type")

    @task_type.setter
    def task_type(self, value: Optional[pulumi.Input[Union[str, 'TaskType']]]):
        pulumi.set(self, "task_type", value)

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> Optional[pulumi.Input[str]]:
        """
        The time zone id.
        """
        return pulumi.get(self, "time_zone_id")

    @time_zone_id.setter
    def time_zone_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time_zone_id", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> Optional[pulumi.Input['WeekDetailsArgs']]:
        """
        The weekly recurrence of the schedule.
        """
        return pulumi.get(self, "weekly_recurrence")

    @weekly_recurrence.setter
    def weekly_recurrence(self, value: Optional[pulumi.Input['WeekDetailsArgs']]):
        pulumi.set(self, "weekly_recurrence", value)


warnings.warn("""Version 2015-05-21-preview will be removed in v2 of the provider.""", DeprecationWarning)


class ScheduleResource(pulumi.CustomResource):
    warnings.warn("""Version 2015-05-21-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 daily_recurrence: Optional[pulumi.Input[pulumi.InputType['DayDetailsArgs']]] = None,
                 hourly_recurrence: Optional[pulumi.Input[pulumi.InputType['HourDetailsArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 task_type: Optional[pulumi.Input[Union[str, 'TaskType']]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weekly_recurrence: Optional[pulumi.Input[pulumi.InputType['WeekDetailsArgs']]] = None,
                 __props__=None):
        """
        A schedule.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['DayDetailsArgs']] daily_recurrence: The daily recurrence of the schedule.
        :param pulumi.Input[pulumi.InputType['HourDetailsArgs']] hourly_recurrence: The hourly recurrence of the schedule.
        :param pulumi.Input[str] id: The identifier of the resource.
        :param pulumi.Input[str] lab_name: The name of the lab.
        :param pulumi.Input[str] location: The location of the resource.
        :param pulumi.Input[str] name: The name of the resource.
        :param pulumi.Input[str] provisioning_state: The provisioning status of the resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[str, 'EnableStatus']] status: The status of the schedule.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: The tags of the resource.
        :param pulumi.Input[Union[str, 'TaskType']] task_type: The task type of the schedule.
        :param pulumi.Input[str] time_zone_id: The time zone id.
        :param pulumi.Input[str] type: The type of the resource.
        :param pulumi.Input[pulumi.InputType['WeekDetailsArgs']] weekly_recurrence: The weekly recurrence of the schedule.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ScheduleResourceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A schedule.

        :param str resource_name: The name of the resource.
        :param ScheduleResourceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ScheduleResourceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 daily_recurrence: Optional[pulumi.Input[pulumi.InputType['DayDetailsArgs']]] = None,
                 hourly_recurrence: Optional[pulumi.Input[pulumi.InputType['HourDetailsArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 lab_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 provisioning_state: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'EnableStatus']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 task_type: Optional[pulumi.Input[Union[str, 'TaskType']]] = None,
                 time_zone_id: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 weekly_recurrence: Optional[pulumi.Input[pulumi.InputType['WeekDetailsArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""ScheduleResource is deprecated: Version 2015-05-21-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ScheduleResourceArgs.__new__(ScheduleResourceArgs)

            __props__.__dict__["daily_recurrence"] = daily_recurrence
            __props__.__dict__["hourly_recurrence"] = hourly_recurrence
            __props__.__dict__["id"] = id
            if lab_name is None and not opts.urn:
                raise TypeError("Missing required property 'lab_name'")
            __props__.__dict__["lab_name"] = lab_name
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["provisioning_state"] = provisioning_state
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["status"] = status
            __props__.__dict__["tags"] = tags
            __props__.__dict__["task_type"] = task_type
            __props__.__dict__["time_zone_id"] = time_zone_id
            __props__.__dict__["type"] = type
            __props__.__dict__["weekly_recurrence"] = weekly_recurrence
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:devtestlab:ScheduleResource"), pulumi.Alias(type_="azure-native:devtestlab/v20160515:ScheduleResource"), pulumi.Alias(type_="azure-native:devtestlab/v20180915:ScheduleResource")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ScheduleResource, __self__).__init__(
            'azure-native:devtestlab/v20150521preview:ScheduleResource',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ScheduleResource':
        """
        Get an existing ScheduleResource resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ScheduleResourceArgs.__new__(ScheduleResourceArgs)

        __props__.__dict__["daily_recurrence"] = None
        __props__.__dict__["hourly_recurrence"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["task_type"] = None
        __props__.__dict__["time_zone_id"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["weekly_recurrence"] = None
        return ScheduleResource(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="dailyRecurrence")
    def daily_recurrence(self) -> pulumi.Output[Optional['outputs.DayDetailsResponse']]:
        """
        The daily recurrence of the schedule.
        """
        return pulumi.get(self, "daily_recurrence")

    @property
    @pulumi.getter(name="hourlyRecurrence")
    def hourly_recurrence(self) -> pulumi.Output[Optional['outputs.HourDetailsResponse']]:
        """
        The hourly recurrence of the schedule.
        """
        return pulumi.get(self, "hourly_recurrence")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The location of the resource.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[Optional[str]]:
        """
        The status of the schedule.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="taskType")
    def task_type(self) -> pulumi.Output[Optional[str]]:
        """
        The task type of the schedule.
        """
        return pulumi.get(self, "task_type")

    @property
    @pulumi.getter(name="timeZoneId")
    def time_zone_id(self) -> pulumi.Output[Optional[str]]:
        """
        The time zone id.
        """
        return pulumi.get(self, "time_zone_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="weeklyRecurrence")
    def weekly_recurrence(self) -> pulumi.Output[Optional['outputs.WeekDetailsResponse']]:
        """
        The weekly recurrence of the schedule.
        """
        return pulumi.get(self, "weekly_recurrence")

