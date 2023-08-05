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

__all__ = [
    'RedisAccessKeysResponse',
    'RedisLinkedServerListResponse',
    'RedisLinkedServerResponse',
    'ScheduleEntryResponse',
    'SkuResponse',
]

@pulumi.output_type
class RedisAccessKeysResponse(dict):
    """
    Redis cache access keys.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "primaryKey":
            suggest = "primary_key"
        elif key == "secondaryKey":
            suggest = "secondary_key"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RedisAccessKeysResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RedisAccessKeysResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RedisAccessKeysResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 primary_key: str,
                 secondary_key: str):
        """
        Redis cache access keys.
        :param str primary_key: The current primary key that clients can use to authenticate with Redis cache.
        :param str secondary_key: The current secondary key that clients can use to authenticate with Redis cache.
        """
        pulumi.set(__self__, "primary_key", primary_key)
        pulumi.set(__self__, "secondary_key", secondary_key)

    @property
    @pulumi.getter(name="primaryKey")
    def primary_key(self) -> str:
        """
        The current primary key that clients can use to authenticate with Redis cache.
        """
        return pulumi.get(self, "primary_key")

    @property
    @pulumi.getter(name="secondaryKey")
    def secondary_key(self) -> str:
        """
        The current secondary key that clients can use to authenticate with Redis cache.
        """
        return pulumi.get(self, "secondary_key")


@pulumi.output_type
class RedisLinkedServerListResponse(dict):
    """
    List of linked server Ids of a Redis cache.
    """
    def __init__(__self__, *,
                 value: Sequence['outputs.RedisLinkedServerResponse']):
        """
        List of linked server Ids of a Redis cache.
        :param Sequence['RedisLinkedServerResponse'] value: List of linked server Ids of a Redis cache.
        """
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.RedisLinkedServerResponse']:
        """
        List of linked server Ids of a Redis cache.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class RedisLinkedServerResponse(dict):
    """
    Linked server Id
    """
    def __init__(__self__, *,
                 id: str):
        """
        Linked server Id
        :param str id: Linked server Id.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Linked server Id.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class ScheduleEntryResponse(dict):
    """
    Patch schedule entry for a Premium Redis Cache.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dayOfWeek":
            suggest = "day_of_week"
        elif key == "startHourUtc":
            suggest = "start_hour_utc"
        elif key == "maintenanceWindow":
            suggest = "maintenance_window"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScheduleEntryResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScheduleEntryResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScheduleEntryResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 day_of_week: str,
                 start_hour_utc: int,
                 maintenance_window: Optional[str] = None):
        """
        Patch schedule entry for a Premium Redis Cache.
        :param str day_of_week: Day of the week when a cache can be patched.
        :param int start_hour_utc: Start hour after which cache patching can start.
        :param str maintenance_window: ISO8601 timespan specifying how much time cache patching can take. 
        """
        pulumi.set(__self__, "day_of_week", day_of_week)
        pulumi.set(__self__, "start_hour_utc", start_hour_utc)
        if maintenance_window is not None:
            pulumi.set(__self__, "maintenance_window", maintenance_window)

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> str:
        """
        Day of the week when a cache can be patched.
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="startHourUtc")
    def start_hour_utc(self) -> int:
        """
        Start hour after which cache patching can start.
        """
        return pulumi.get(self, "start_hour_utc")

    @property
    @pulumi.getter(name="maintenanceWindow")
    def maintenance_window(self) -> Optional[str]:
        """
        ISO8601 timespan specifying how much time cache patching can take. 
        """
        return pulumi.get(self, "maintenance_window")


@pulumi.output_type
class SkuResponse(dict):
    """
    SKU parameters supplied to the create Redis operation.
    """
    def __init__(__self__, *,
                 capacity: int,
                 family: str,
                 name: str):
        """
        SKU parameters supplied to the create Redis operation.
        :param int capacity: The size of the Redis cache to deploy. Valid values: for C (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium) family (1, 2, 3, 4).
        :param str family: The SKU family to use. Valid values: (C, P). (C = Basic/Standard, P = Premium).
        :param str name: The type of Redis cache to deploy. Valid values: (Basic, Standard, Premium)
        """
        pulumi.set(__self__, "capacity", capacity)
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def capacity(self) -> int:
        """
        The size of the Redis cache to deploy. Valid values: for C (Basic/Standard) family (0, 1, 2, 3, 4, 5, 6), for P (Premium) family (1, 2, 3, 4).
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def family(self) -> str:
        """
        The SKU family to use. Valid values: (C, P). (C = Basic/Standard, P = Premium).
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The type of Redis cache to deploy. Valid values: (Basic, Standard, Premium)
        """
        return pulumi.get(self, "name")


