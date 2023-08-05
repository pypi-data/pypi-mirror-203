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
    'MigrationRequestPropertiesResponse',
    'MsixPackageApplicationsResponse',
    'MsixPackageDependenciesResponse',
    'RegistrationInfoResponse',
    'ResourceModelWithAllowedPropertySetResponseIdentity',
    'ResourceModelWithAllowedPropertySetResponsePlan',
    'ResourceModelWithAllowedPropertySetResponseSku',
    'ScalingHostPoolReferenceResponse',
    'ScalingScheduleResponse',
]

@pulumi.output_type
class MigrationRequestPropertiesResponse(dict):
    """
    Properties for arm migration.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "migrationPath":
            suggest = "migration_path"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MigrationRequestPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MigrationRequestPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MigrationRequestPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 migration_path: Optional[str] = None,
                 operation: Optional[str] = None):
        """
        Properties for arm migration.
        :param str migration_path: The path to the legacy object to migrate.
        :param str operation: The type of operation for migration.
        """
        if migration_path is not None:
            pulumi.set(__self__, "migration_path", migration_path)
        if operation is not None:
            pulumi.set(__self__, "operation", operation)

    @property
    @pulumi.getter(name="migrationPath")
    def migration_path(self) -> Optional[str]:
        """
        The path to the legacy object to migrate.
        """
        return pulumi.get(self, "migration_path")

    @property
    @pulumi.getter
    def operation(self) -> Optional[str]:
        """
        The type of operation for migration.
        """
        return pulumi.get(self, "operation")


@pulumi.output_type
class MsixPackageApplicationsResponse(dict):
    """
    Schema for MSIX Package Application properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "appId":
            suggest = "app_id"
        elif key == "appUserModelID":
            suggest = "app_user_model_id"
        elif key == "friendlyName":
            suggest = "friendly_name"
        elif key == "iconImageName":
            suggest = "icon_image_name"
        elif key == "rawIcon":
            suggest = "raw_icon"
        elif key == "rawPng":
            suggest = "raw_png"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MsixPackageApplicationsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MsixPackageApplicationsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MsixPackageApplicationsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 app_id: Optional[str] = None,
                 app_user_model_id: Optional[str] = None,
                 description: Optional[str] = None,
                 friendly_name: Optional[str] = None,
                 icon_image_name: Optional[str] = None,
                 raw_icon: Optional[str] = None,
                 raw_png: Optional[str] = None):
        """
        Schema for MSIX Package Application properties.
        :param str app_id: Package Application Id, found in appxmanifest.xml.
        :param str app_user_model_id: Used to activate Package Application. Consists of Package Name and ApplicationID. Found in appxmanifest.xml.
        :param str description: Description of Package Application.
        :param str friendly_name: User friendly name.
        :param str icon_image_name: User friendly name.
        :param str raw_icon: the icon a 64 bit string as a byte array.
        :param str raw_png: the icon a 64 bit string as a byte array.
        """
        if app_id is not None:
            pulumi.set(__self__, "app_id", app_id)
        if app_user_model_id is not None:
            pulumi.set(__self__, "app_user_model_id", app_user_model_id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if icon_image_name is not None:
            pulumi.set(__self__, "icon_image_name", icon_image_name)
        if raw_icon is not None:
            pulumi.set(__self__, "raw_icon", raw_icon)
        if raw_png is not None:
            pulumi.set(__self__, "raw_png", raw_png)

    @property
    @pulumi.getter(name="appId")
    def app_id(self) -> Optional[str]:
        """
        Package Application Id, found in appxmanifest.xml.
        """
        return pulumi.get(self, "app_id")

    @property
    @pulumi.getter(name="appUserModelID")
    def app_user_model_id(self) -> Optional[str]:
        """
        Used to activate Package Application. Consists of Package Name and ApplicationID. Found in appxmanifest.xml.
        """
        return pulumi.get(self, "app_user_model_id")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of Package Application.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        User friendly name.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="iconImageName")
    def icon_image_name(self) -> Optional[str]:
        """
        User friendly name.
        """
        return pulumi.get(self, "icon_image_name")

    @property
    @pulumi.getter(name="rawIcon")
    def raw_icon(self) -> Optional[str]:
        """
        the icon a 64 bit string as a byte array.
        """
        return pulumi.get(self, "raw_icon")

    @property
    @pulumi.getter(name="rawPng")
    def raw_png(self) -> Optional[str]:
        """
        the icon a 64 bit string as a byte array.
        """
        return pulumi.get(self, "raw_png")


@pulumi.output_type
class MsixPackageDependenciesResponse(dict):
    """
    Schema for MSIX Package Dependencies properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dependencyName":
            suggest = "dependency_name"
        elif key == "minVersion":
            suggest = "min_version"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MsixPackageDependenciesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MsixPackageDependenciesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MsixPackageDependenciesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dependency_name: Optional[str] = None,
                 min_version: Optional[str] = None,
                 publisher: Optional[str] = None):
        """
        Schema for MSIX Package Dependencies properties.
        :param str dependency_name: Name of package dependency.
        :param str min_version: Dependency version required.
        :param str publisher: Name of dependency publisher.
        """
        if dependency_name is not None:
            pulumi.set(__self__, "dependency_name", dependency_name)
        if min_version is not None:
            pulumi.set(__self__, "min_version", min_version)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)

    @property
    @pulumi.getter(name="dependencyName")
    def dependency_name(self) -> Optional[str]:
        """
        Name of package dependency.
        """
        return pulumi.get(self, "dependency_name")

    @property
    @pulumi.getter(name="minVersion")
    def min_version(self) -> Optional[str]:
        """
        Dependency version required.
        """
        return pulumi.get(self, "min_version")

    @property
    @pulumi.getter
    def publisher(self) -> Optional[str]:
        """
        Name of dependency publisher.
        """
        return pulumi.get(self, "publisher")


@pulumi.output_type
class RegistrationInfoResponse(dict):
    """
    Represents a RegistrationInfo definition.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "expirationTime":
            suggest = "expiration_time"
        elif key == "registrationTokenOperation":
            suggest = "registration_token_operation"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in RegistrationInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        RegistrationInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        RegistrationInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 expiration_time: Optional[str] = None,
                 registration_token_operation: Optional[str] = None,
                 token: Optional[str] = None):
        """
        Represents a RegistrationInfo definition.
        :param str expiration_time: Expiration time of registration token.
        :param str registration_token_operation: The type of resetting the token.
        :param str token: The registration token base64 encoded string.
        """
        if expiration_time is not None:
            pulumi.set(__self__, "expiration_time", expiration_time)
        if registration_token_operation is not None:
            pulumi.set(__self__, "registration_token_operation", registration_token_operation)
        if token is not None:
            pulumi.set(__self__, "token", token)

    @property
    @pulumi.getter(name="expirationTime")
    def expiration_time(self) -> Optional[str]:
        """
        Expiration time of registration token.
        """
        return pulumi.get(self, "expiration_time")

    @property
    @pulumi.getter(name="registrationTokenOperation")
    def registration_token_operation(self) -> Optional[str]:
        """
        The type of resetting the token.
        """
        return pulumi.get(self, "registration_token_operation")

    @property
    @pulumi.getter
    def token(self) -> Optional[str]:
        """
        The registration token base64 encoded string.
        """
        return pulumi.get(self, "token")


@pulumi.output_type
class ResourceModelWithAllowedPropertySetResponseIdentity(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceModelWithAllowedPropertySetResponseIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceModelWithAllowedPropertySetResponseIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceModelWithAllowedPropertySetResponseIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
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
class ResourceModelWithAllowedPropertySetResponsePlan(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "promotionCode":
            suggest = "promotion_code"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ResourceModelWithAllowedPropertySetResponsePlan. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ResourceModelWithAllowedPropertySetResponsePlan.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ResourceModelWithAllowedPropertySetResponsePlan.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 product: str,
                 publisher: str,
                 promotion_code: Optional[str] = None,
                 version: Optional[str] = None):
        """
        :param str name: A user defined name of the 3rd Party Artifact that is being procured.
        :param str product: The 3rd Party artifact that is being procured. E.g. NewRelic. Product maps to the OfferID specified for the artifact at the time of Data Market onboarding. 
        :param str publisher: The publisher of the 3rd Party Artifact that is being bought. E.g. NewRelic
        :param str promotion_code: A publisher provided promotion code as provisioned in Data Market for the said product/artifact.
        :param str version: The version of the desired product/artifact.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "product", product)
        pulumi.set(__self__, "publisher", publisher)
        if promotion_code is not None:
            pulumi.set(__self__, "promotion_code", promotion_code)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        A user defined name of the 3rd Party Artifact that is being procured.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def product(self) -> str:
        """
        The 3rd Party artifact that is being procured. E.g. NewRelic. Product maps to the OfferID specified for the artifact at the time of Data Market onboarding. 
        """
        return pulumi.get(self, "product")

    @property
    @pulumi.getter
    def publisher(self) -> str:
        """
        The publisher of the 3rd Party Artifact that is being bought. E.g. NewRelic
        """
        return pulumi.get(self, "publisher")

    @property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[str]:
        """
        A publisher provided promotion code as provisioned in Data Market for the said product/artifact.
        """
        return pulumi.get(self, "promotion_code")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the desired product/artifact.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class ResourceModelWithAllowedPropertySetResponseSku(dict):
    def __init__(__self__, *,
                 name: str,
                 capacity: Optional[int] = None,
                 family: Optional[str] = None,
                 size: Optional[str] = None,
                 tier: Optional[str] = None):
        """
        :param str name: The name of the SKU. Ex - P3. It is typically a letter+number code
        :param int capacity: If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        :param str family: If the service has different generations of hardware, for the same SKU, then that can be captured here.
        :param str size: The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        :param str tier: This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        pulumi.set(__self__, "name", name)
        if capacity is not None:
            pulumi.set(__self__, "capacity", capacity)
        if family is not None:
            pulumi.set(__self__, "family", family)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the SKU. Ex - P3. It is typically a letter+number code
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def capacity(self) -> Optional[int]:
        """
        If the SKU supports scale out/in then the capacity integer should be included. If scale out/in is not possible for the resource this may be omitted.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter
    def family(self) -> Optional[str]:
        """
        If the service has different generations of hardware, for the same SKU, then that can be captured here.
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def size(self) -> Optional[str]:
        """
        The SKU size. When the name field is the combination of tier and some other value, this would be the standalone code. 
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        This field is required to be implemented by the Resource Provider if the service has more than one tier, but is not required on a PUT.
        """
        return pulumi.get(self, "tier")


@pulumi.output_type
class ScalingHostPoolReferenceResponse(dict):
    """
    Scaling plan reference to hostpool.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "hostPoolArmPath":
            suggest = "host_pool_arm_path"
        elif key == "scalingPlanEnabled":
            suggest = "scaling_plan_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingHostPoolReferenceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingHostPoolReferenceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingHostPoolReferenceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 host_pool_arm_path: Optional[str] = None,
                 scaling_plan_enabled: Optional[bool] = None):
        """
        Scaling plan reference to hostpool.
        :param str host_pool_arm_path: Arm path of referenced hostpool.
        :param bool scaling_plan_enabled: Is the scaling plan enabled for this hostpool.
        """
        if host_pool_arm_path is not None:
            pulumi.set(__self__, "host_pool_arm_path", host_pool_arm_path)
        if scaling_plan_enabled is not None:
            pulumi.set(__self__, "scaling_plan_enabled", scaling_plan_enabled)

    @property
    @pulumi.getter(name="hostPoolArmPath")
    def host_pool_arm_path(self) -> Optional[str]:
        """
        Arm path of referenced hostpool.
        """
        return pulumi.get(self, "host_pool_arm_path")

    @property
    @pulumi.getter(name="scalingPlanEnabled")
    def scaling_plan_enabled(self) -> Optional[bool]:
        """
        Is the scaling plan enabled for this hostpool.
        """
        return pulumi.get(self, "scaling_plan_enabled")


@pulumi.output_type
class ScalingScheduleResponse(dict):
    """
    Scaling plan schedule.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "daysOfWeek":
            suggest = "days_of_week"
        elif key == "offPeakLoadBalancingAlgorithm":
            suggest = "off_peak_load_balancing_algorithm"
        elif key == "offPeakStartTime":
            suggest = "off_peak_start_time"
        elif key == "peakLoadBalancingAlgorithm":
            suggest = "peak_load_balancing_algorithm"
        elif key == "peakStartTime":
            suggest = "peak_start_time"
        elif key == "rampDownCapacityThresholdPct":
            suggest = "ramp_down_capacity_threshold_pct"
        elif key == "rampDownForceLogoffUsers":
            suggest = "ramp_down_force_logoff_users"
        elif key == "rampDownLoadBalancingAlgorithm":
            suggest = "ramp_down_load_balancing_algorithm"
        elif key == "rampDownMinimumHostsPct":
            suggest = "ramp_down_minimum_hosts_pct"
        elif key == "rampDownNotificationMessage":
            suggest = "ramp_down_notification_message"
        elif key == "rampDownStartTime":
            suggest = "ramp_down_start_time"
        elif key == "rampDownStopHostsWhen":
            suggest = "ramp_down_stop_hosts_when"
        elif key == "rampDownWaitTimeMinutes":
            suggest = "ramp_down_wait_time_minutes"
        elif key == "rampUpCapacityThresholdPct":
            suggest = "ramp_up_capacity_threshold_pct"
        elif key == "rampUpLoadBalancingAlgorithm":
            suggest = "ramp_up_load_balancing_algorithm"
        elif key == "rampUpMinimumHostsPct":
            suggest = "ramp_up_minimum_hosts_pct"
        elif key == "rampUpStartTime":
            suggest = "ramp_up_start_time"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ScalingScheduleResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ScalingScheduleResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ScalingScheduleResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 days_of_week: Optional[Sequence[str]] = None,
                 name: Optional[str] = None,
                 off_peak_load_balancing_algorithm: Optional[str] = None,
                 off_peak_start_time: Optional[str] = None,
                 peak_load_balancing_algorithm: Optional[str] = None,
                 peak_start_time: Optional[str] = None,
                 ramp_down_capacity_threshold_pct: Optional[int] = None,
                 ramp_down_force_logoff_users: Optional[bool] = None,
                 ramp_down_load_balancing_algorithm: Optional[str] = None,
                 ramp_down_minimum_hosts_pct: Optional[int] = None,
                 ramp_down_notification_message: Optional[str] = None,
                 ramp_down_start_time: Optional[str] = None,
                 ramp_down_stop_hosts_when: Optional[str] = None,
                 ramp_down_wait_time_minutes: Optional[int] = None,
                 ramp_up_capacity_threshold_pct: Optional[int] = None,
                 ramp_up_load_balancing_algorithm: Optional[str] = None,
                 ramp_up_minimum_hosts_pct: Optional[int] = None,
                 ramp_up_start_time: Optional[str] = None):
        """
        Scaling plan schedule.
        :param Sequence[str] days_of_week: Set of days of the week on which this schedule is active.
        :param str name: Name of the scaling schedule.
        :param str off_peak_load_balancing_algorithm: Load balancing algorithm for off-peak period.
        :param str off_peak_start_time: Starting time for off-peak period.
        :param str peak_load_balancing_algorithm: Load balancing algorithm for peak period.
        :param str peak_start_time: Starting time for peak period.
        :param int ramp_down_capacity_threshold_pct: Capacity threshold for ramp down period.
        :param bool ramp_down_force_logoff_users: Should users be logged off forcefully from hosts.
        :param str ramp_down_load_balancing_algorithm: Load balancing algorithm for ramp down period.
        :param int ramp_down_minimum_hosts_pct: Minimum host percentage for ramp down period.
        :param str ramp_down_notification_message: Notification message for users during ramp down period.
        :param str ramp_down_start_time: Starting time for ramp down period.
        :param str ramp_down_stop_hosts_when: Specifies when to stop hosts during ramp down period.
        :param int ramp_down_wait_time_minutes: Number of minutes to wait to stop hosts during ramp down period.
        :param int ramp_up_capacity_threshold_pct: Capacity threshold for ramp up period.
        :param str ramp_up_load_balancing_algorithm: Load balancing algorithm for ramp up period.
        :param int ramp_up_minimum_hosts_pct: Minimum host percentage for ramp up period.
        :param str ramp_up_start_time: Starting time for ramp up period.
        """
        if days_of_week is not None:
            pulumi.set(__self__, "days_of_week", days_of_week)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if off_peak_load_balancing_algorithm is not None:
            pulumi.set(__self__, "off_peak_load_balancing_algorithm", off_peak_load_balancing_algorithm)
        if off_peak_start_time is not None:
            pulumi.set(__self__, "off_peak_start_time", off_peak_start_time)
        if peak_load_balancing_algorithm is not None:
            pulumi.set(__self__, "peak_load_balancing_algorithm", peak_load_balancing_algorithm)
        if peak_start_time is not None:
            pulumi.set(__self__, "peak_start_time", peak_start_time)
        if ramp_down_capacity_threshold_pct is not None:
            pulumi.set(__self__, "ramp_down_capacity_threshold_pct", ramp_down_capacity_threshold_pct)
        if ramp_down_force_logoff_users is not None:
            pulumi.set(__self__, "ramp_down_force_logoff_users", ramp_down_force_logoff_users)
        if ramp_down_load_balancing_algorithm is not None:
            pulumi.set(__self__, "ramp_down_load_balancing_algorithm", ramp_down_load_balancing_algorithm)
        if ramp_down_minimum_hosts_pct is not None:
            pulumi.set(__self__, "ramp_down_minimum_hosts_pct", ramp_down_minimum_hosts_pct)
        if ramp_down_notification_message is not None:
            pulumi.set(__self__, "ramp_down_notification_message", ramp_down_notification_message)
        if ramp_down_start_time is not None:
            pulumi.set(__self__, "ramp_down_start_time", ramp_down_start_time)
        if ramp_down_stop_hosts_when is not None:
            pulumi.set(__self__, "ramp_down_stop_hosts_when", ramp_down_stop_hosts_when)
        if ramp_down_wait_time_minutes is not None:
            pulumi.set(__self__, "ramp_down_wait_time_minutes", ramp_down_wait_time_minutes)
        if ramp_up_capacity_threshold_pct is not None:
            pulumi.set(__self__, "ramp_up_capacity_threshold_pct", ramp_up_capacity_threshold_pct)
        if ramp_up_load_balancing_algorithm is not None:
            pulumi.set(__self__, "ramp_up_load_balancing_algorithm", ramp_up_load_balancing_algorithm)
        if ramp_up_minimum_hosts_pct is not None:
            pulumi.set(__self__, "ramp_up_minimum_hosts_pct", ramp_up_minimum_hosts_pct)
        if ramp_up_start_time is not None:
            pulumi.set(__self__, "ramp_up_start_time", ramp_up_start_time)

    @property
    @pulumi.getter(name="daysOfWeek")
    def days_of_week(self) -> Optional[Sequence[str]]:
        """
        Set of days of the week on which this schedule is active.
        """
        return pulumi.get(self, "days_of_week")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the scaling schedule.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="offPeakLoadBalancingAlgorithm")
    def off_peak_load_balancing_algorithm(self) -> Optional[str]:
        """
        Load balancing algorithm for off-peak period.
        """
        return pulumi.get(self, "off_peak_load_balancing_algorithm")

    @property
    @pulumi.getter(name="offPeakStartTime")
    def off_peak_start_time(self) -> Optional[str]:
        """
        Starting time for off-peak period.
        """
        return pulumi.get(self, "off_peak_start_time")

    @property
    @pulumi.getter(name="peakLoadBalancingAlgorithm")
    def peak_load_balancing_algorithm(self) -> Optional[str]:
        """
        Load balancing algorithm for peak period.
        """
        return pulumi.get(self, "peak_load_balancing_algorithm")

    @property
    @pulumi.getter(name="peakStartTime")
    def peak_start_time(self) -> Optional[str]:
        """
        Starting time for peak period.
        """
        return pulumi.get(self, "peak_start_time")

    @property
    @pulumi.getter(name="rampDownCapacityThresholdPct")
    def ramp_down_capacity_threshold_pct(self) -> Optional[int]:
        """
        Capacity threshold for ramp down period.
        """
        return pulumi.get(self, "ramp_down_capacity_threshold_pct")

    @property
    @pulumi.getter(name="rampDownForceLogoffUsers")
    def ramp_down_force_logoff_users(self) -> Optional[bool]:
        """
        Should users be logged off forcefully from hosts.
        """
        return pulumi.get(self, "ramp_down_force_logoff_users")

    @property
    @pulumi.getter(name="rampDownLoadBalancingAlgorithm")
    def ramp_down_load_balancing_algorithm(self) -> Optional[str]:
        """
        Load balancing algorithm for ramp down period.
        """
        return pulumi.get(self, "ramp_down_load_balancing_algorithm")

    @property
    @pulumi.getter(name="rampDownMinimumHostsPct")
    def ramp_down_minimum_hosts_pct(self) -> Optional[int]:
        """
        Minimum host percentage for ramp down period.
        """
        return pulumi.get(self, "ramp_down_minimum_hosts_pct")

    @property
    @pulumi.getter(name="rampDownNotificationMessage")
    def ramp_down_notification_message(self) -> Optional[str]:
        """
        Notification message for users during ramp down period.
        """
        return pulumi.get(self, "ramp_down_notification_message")

    @property
    @pulumi.getter(name="rampDownStartTime")
    def ramp_down_start_time(self) -> Optional[str]:
        """
        Starting time for ramp down period.
        """
        return pulumi.get(self, "ramp_down_start_time")

    @property
    @pulumi.getter(name="rampDownStopHostsWhen")
    def ramp_down_stop_hosts_when(self) -> Optional[str]:
        """
        Specifies when to stop hosts during ramp down period.
        """
        return pulumi.get(self, "ramp_down_stop_hosts_when")

    @property
    @pulumi.getter(name="rampDownWaitTimeMinutes")
    def ramp_down_wait_time_minutes(self) -> Optional[int]:
        """
        Number of minutes to wait to stop hosts during ramp down period.
        """
        return pulumi.get(self, "ramp_down_wait_time_minutes")

    @property
    @pulumi.getter(name="rampUpCapacityThresholdPct")
    def ramp_up_capacity_threshold_pct(self) -> Optional[int]:
        """
        Capacity threshold for ramp up period.
        """
        return pulumi.get(self, "ramp_up_capacity_threshold_pct")

    @property
    @pulumi.getter(name="rampUpLoadBalancingAlgorithm")
    def ramp_up_load_balancing_algorithm(self) -> Optional[str]:
        """
        Load balancing algorithm for ramp up period.
        """
        return pulumi.get(self, "ramp_up_load_balancing_algorithm")

    @property
    @pulumi.getter(name="rampUpMinimumHostsPct")
    def ramp_up_minimum_hosts_pct(self) -> Optional[int]:
        """
        Minimum host percentage for ramp up period.
        """
        return pulumi.get(self, "ramp_up_minimum_hosts_pct")

    @property
    @pulumi.getter(name="rampUpStartTime")
    def ramp_up_start_time(self) -> Optional[str]:
        """
        Starting time for ramp up period.
        """
        return pulumi.get(self, "ramp_up_start_time")


