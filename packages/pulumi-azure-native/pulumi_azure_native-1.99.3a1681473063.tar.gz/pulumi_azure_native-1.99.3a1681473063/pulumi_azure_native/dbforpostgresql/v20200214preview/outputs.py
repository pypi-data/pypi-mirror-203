# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'IdentityResponse',
    'MaintenanceWindowResponse',
    'ServerPropertiesResponseDelegatedSubnetArguments',
    'ServerPropertiesResponsePrivateDnsZoneArguments',
    'SkuResponse',
    'StorageProfileResponse',
]

@pulumi.output_type
class IdentityResponse(dict):
    """
    Identity for the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Identity for the resource.
        :param str principal_id: The principal ID of resource identity.
        :param str tenant_id: The tenant ID of resource.
        :param str type: The identity type.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class MaintenanceWindowResponse(dict):
    """
    Maintenance window of a server.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "customWindow":
            suggest = "custom_window"
        elif key == "dayOfWeek":
            suggest = "day_of_week"
        elif key == "startHour":
            suggest = "start_hour"
        elif key == "startMinute":
            suggest = "start_minute"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MaintenanceWindowResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MaintenanceWindowResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MaintenanceWindowResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 custom_window: Optional[str] = None,
                 day_of_week: Optional[int] = None,
                 start_hour: Optional[int] = None,
                 start_minute: Optional[int] = None):
        """
        Maintenance window of a server.
        :param str custom_window: indicates whether custom window is enabled or disabled
        :param int day_of_week: day of week for maintenance window
        :param int start_hour: start hour for maintenance window
        :param int start_minute: start minute for maintenance window
        """
        if custom_window is not None:
            pulumi.set(__self__, "custom_window", custom_window)
        if day_of_week is not None:
            pulumi.set(__self__, "day_of_week", day_of_week)
        if start_hour is not None:
            pulumi.set(__self__, "start_hour", start_hour)
        if start_minute is not None:
            pulumi.set(__self__, "start_minute", start_minute)

    @property
    @pulumi.getter(name="customWindow")
    def custom_window(self) -> Optional[str]:
        """
        indicates whether custom window is enabled or disabled
        """
        return pulumi.get(self, "custom_window")

    @property
    @pulumi.getter(name="dayOfWeek")
    def day_of_week(self) -> Optional[int]:
        """
        day of week for maintenance window
        """
        return pulumi.get(self, "day_of_week")

    @property
    @pulumi.getter(name="startHour")
    def start_hour(self) -> Optional[int]:
        """
        start hour for maintenance window
        """
        return pulumi.get(self, "start_hour")

    @property
    @pulumi.getter(name="startMinute")
    def start_minute(self) -> Optional[int]:
        """
        start minute for maintenance window
        """
        return pulumi.get(self, "start_minute")


@pulumi.output_type
class ServerPropertiesResponseDelegatedSubnetArguments(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "subnetArmResourceId":
            suggest = "subnet_arm_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServerPropertiesResponseDelegatedSubnetArguments. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServerPropertiesResponseDelegatedSubnetArguments.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServerPropertiesResponseDelegatedSubnetArguments.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 subnet_arm_resource_id: Optional[str] = None):
        """
        :param str subnet_arm_resource_id: delegated subnet arm resource id.
        """
        if subnet_arm_resource_id is not None:
            pulumi.set(__self__, "subnet_arm_resource_id", subnet_arm_resource_id)

    @property
    @pulumi.getter(name="subnetArmResourceId")
    def subnet_arm_resource_id(self) -> Optional[str]:
        """
        delegated subnet arm resource id.
        """
        return pulumi.get(self, "subnet_arm_resource_id")


@pulumi.output_type
class ServerPropertiesResponsePrivateDnsZoneArguments(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateDnsZoneArmResourceId":
            suggest = "private_dns_zone_arm_resource_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServerPropertiesResponsePrivateDnsZoneArguments. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServerPropertiesResponsePrivateDnsZoneArguments.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServerPropertiesResponsePrivateDnsZoneArguments.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 private_dns_zone_arm_resource_id: Optional[str] = None):
        """
        :param str private_dns_zone_arm_resource_id: private dns zone arm resource id.
        """
        if private_dns_zone_arm_resource_id is not None:
            pulumi.set(__self__, "private_dns_zone_arm_resource_id", private_dns_zone_arm_resource_id)

    @property
    @pulumi.getter(name="privateDnsZoneArmResourceId")
    def private_dns_zone_arm_resource_id(self) -> Optional[str]:
        """
        private dns zone arm resource id.
        """
        return pulumi.get(self, "private_dns_zone_arm_resource_id")


@pulumi.output_type
class SkuResponse(dict):
    """
    Sku information related properties of a server.
    """
    def __init__(__self__, *,
                 name: str,
                 tier: str):
        """
        Sku information related properties of a server.
        :param str name: The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3.
        :param str tier: The tier of the particular SKU, e.g. Burstable.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the sku, typically, tier + family + cores, e.g. Standard_D4s_v3.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tier(self) -> str:
        """
        The tier of the particular SKU, e.g. Burstable.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class StorageProfileResponse(dict):
    """
    Storage Profile properties of a server
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "backupRetentionDays":
            suggest = "backup_retention_days"
        elif key == "geoRedundantBackup":
            suggest = "geo_redundant_backup"
        elif key == "storageMB":
            suggest = "storage_mb"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in StorageProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        StorageProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        StorageProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 backup_retention_days: Optional[int] = None,
                 geo_redundant_backup: Optional[str] = None,
                 storage_mb: Optional[int] = None):
        """
        Storage Profile properties of a server
        :param int backup_retention_days: Backup retention days for the server.
        :param str geo_redundant_backup: A value indicating whether Geo-Redundant backup is enabled on the server.
        :param int storage_mb: Max storage allowed for a server.
        """
        if backup_retention_days is not None:
            pulumi.set(__self__, "backup_retention_days", backup_retention_days)
        if geo_redundant_backup is not None:
            pulumi.set(__self__, "geo_redundant_backup", geo_redundant_backup)
        if storage_mb is not None:
            pulumi.set(__self__, "storage_mb", storage_mb)

    @property
    @pulumi.getter(name="backupRetentionDays")
    def backup_retention_days(self) -> Optional[int]:
        """
        Backup retention days for the server.
        """
        return pulumi.get(self, "backup_retention_days")

    @property
    @pulumi.getter(name="geoRedundantBackup")
    def geo_redundant_backup(self) -> Optional[str]:
        """
        A value indicating whether Geo-Redundant backup is enabled on the server.
        """
        return pulumi.get(self, "geo_redundant_backup")

    @property
    @pulumi.getter(name="storageMB")
    def storage_mb(self) -> Optional[int]:
        """
        Max storage allowed for a server.
        """
        return pulumi.get(self, "storage_mb")


