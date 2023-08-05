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
    'HybridComputePrivateLinkScopePropertiesArgs',
    'IdentityArgs',
    'LocationDataArgs',
    'MachineExtensionInstanceViewStatusArgs',
    'MachineExtensionInstanceViewArgs',
    'MachineExtensionPropertiesArgs',
    'MachinePropertiesArgs',
    'OSProfileLinuxConfigurationArgs',
    'OSProfileWindowsConfigurationArgs',
    'OSProfileArgs',
    'PrivateEndpointConnectionPropertiesArgs',
    'PrivateEndpointPropertyArgs',
    'PrivateLinkServiceConnectionStatePropertyArgs',
]

@pulumi.input_type
class HybridComputePrivateLinkScopePropertiesArgs:
    def __init__(__self__, *,
                 public_network_access: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]] = None):
        """
        Properties that define a Azure Arc PrivateLinkScope resource.
        :param pulumi.Input[Union[str, 'PublicNetworkAccessType']] public_network_access: Indicates whether machines associated with the private link scope can also use public Azure Arc service endpoints.
        """
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]:
        """
        Indicates whether machines associated with the private link scope can also use public Azure Arc service endpoints.
        """
        return pulumi.get(self, "public_network_access")

    @public_network_access.setter
    def public_network_access(self, value: Optional[pulumi.Input[Union[str, 'PublicNetworkAccessType']]]):
        pulumi.set(self, "public_network_access", value)


@pulumi.input_type
class IdentityArgs:
    def __init__(__self__, *,
                 type: Optional[pulumi.Input['ResourceIdentityType']] = None):
        """
        Identity for the resource.
        :param pulumi.Input['ResourceIdentityType'] type: The identity type.
        """
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input['ResourceIdentityType']]:
        """
        The identity type.
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input['ResourceIdentityType']]):
        pulumi.set(self, "type", value)


@pulumi.input_type
class LocationDataArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 city: Optional[pulumi.Input[str]] = None,
                 country_or_region: Optional[pulumi.Input[str]] = None,
                 district: Optional[pulumi.Input[str]] = None):
        """
        Metadata pertaining to the geographic location of the resource.
        :param pulumi.Input[str] name: A canonical name for the geographic or physical location.
        :param pulumi.Input[str] city: The city or locality where the resource is located.
        :param pulumi.Input[str] country_or_region: The country or region where the resource is located
        :param pulumi.Input[str] district: The district, state, or province where the resource is located.
        """
        pulumi.set(__self__, "name", name)
        if city is not None:
            pulumi.set(__self__, "city", city)
        if country_or_region is not None:
            pulumi.set(__self__, "country_or_region", country_or_region)
        if district is not None:
            pulumi.set(__self__, "district", district)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        A canonical name for the geographic or physical location.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def city(self) -> Optional[pulumi.Input[str]]:
        """
        The city or locality where the resource is located.
        """
        return pulumi.get(self, "city")

    @city.setter
    def city(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "city", value)

    @property
    @pulumi.getter(name="countryOrRegion")
    def country_or_region(self) -> Optional[pulumi.Input[str]]:
        """
        The country or region where the resource is located
        """
        return pulumi.get(self, "country_or_region")

    @country_or_region.setter
    def country_or_region(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country_or_region", value)

    @property
    @pulumi.getter
    def district(self) -> Optional[pulumi.Input[str]]:
        """
        The district, state, or province where the resource is located.
        """
        return pulumi.get(self, "district")

    @district.setter
    def district(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "district", value)


@pulumi.input_type
class MachineExtensionInstanceViewStatusArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[str]] = None,
                 display_status: Optional[pulumi.Input[str]] = None,
                 level: Optional[pulumi.Input[Union[str, 'StatusLevelTypes']]] = None,
                 message: Optional[pulumi.Input[str]] = None,
                 time: Optional[pulumi.Input[str]] = None):
        """
        Instance view status.
        :param pulumi.Input[str] code: The status code.
        :param pulumi.Input[str] display_status: The short localizable label for the status.
        :param pulumi.Input[Union[str, 'StatusLevelTypes']] level: The level code.
        :param pulumi.Input[str] message: The detailed status message, including for alerts and error messages.
        :param pulumi.Input[str] time: The time of the status.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)
        if display_status is not None:
            pulumi.set(__self__, "display_status", display_status)
        if level is not None:
            pulumi.set(__self__, "level", level)
        if message is not None:
            pulumi.set(__self__, "message", message)
        if time is not None:
            pulumi.set(__self__, "time", time)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[str]]:
        """
        The status code.
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code", value)

    @property
    @pulumi.getter(name="displayStatus")
    def display_status(self) -> Optional[pulumi.Input[str]]:
        """
        The short localizable label for the status.
        """
        return pulumi.get(self, "display_status")

    @display_status.setter
    def display_status(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_status", value)

    @property
    @pulumi.getter
    def level(self) -> Optional[pulumi.Input[Union[str, 'StatusLevelTypes']]]:
        """
        The level code.
        """
        return pulumi.get(self, "level")

    @level.setter
    def level(self, value: Optional[pulumi.Input[Union[str, 'StatusLevelTypes']]]):
        pulumi.set(self, "level", value)

    @property
    @pulumi.getter
    def message(self) -> Optional[pulumi.Input[str]]:
        """
        The detailed status message, including for alerts and error messages.
        """
        return pulumi.get(self, "message")

    @message.setter
    def message(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "message", value)

    @property
    @pulumi.getter
    def time(self) -> Optional[pulumi.Input[str]]:
        """
        The time of the status.
        """
        return pulumi.get(self, "time")

    @time.setter
    def time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "time", value)


@pulumi.input_type
class MachineExtensionInstanceViewArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input['MachineExtensionInstanceViewStatusArgs']] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_handler_version: Optional[pulumi.Input[str]] = None):
        """
        Describes the Machine Extension Instance View.
        :param pulumi.Input[str] name: The machine extension name.
        :param pulumi.Input['MachineExtensionInstanceViewStatusArgs'] status: Instance view status.
        :param pulumi.Input[str] type: Specifies the type of the extension; an example is "CustomScriptExtension".
        :param pulumi.Input[str] type_handler_version: Specifies the version of the script handler.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if status is not None:
            pulumi.set(__self__, "status", status)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if type_handler_version is not None:
            pulumi.set(__self__, "type_handler_version", type_handler_version)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The machine extension name.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input['MachineExtensionInstanceViewStatusArgs']]:
        """
        Instance view status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input['MachineExtensionInstanceViewStatusArgs']]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of the extension; an example is "CustomScriptExtension".
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the version of the script handler.
        """
        return pulumi.get(self, "type_handler_version")

    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_handler_version", value)


@pulumi.input_type
class MachineExtensionPropertiesArgs:
    def __init__(__self__, *,
                 auto_upgrade_minor_version: Optional[pulumi.Input[bool]] = None,
                 force_update_tag: Optional[pulumi.Input[str]] = None,
                 instance_view: Optional[pulumi.Input['MachineExtensionInstanceViewArgs']] = None,
                 protected_settings: Optional[Any] = None,
                 publisher: Optional[pulumi.Input[str]] = None,
                 settings: Optional[Any] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 type_handler_version: Optional[pulumi.Input[str]] = None):
        """
        Describes the properties of a Machine Extension.
        :param pulumi.Input[bool] auto_upgrade_minor_version: Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
        :param pulumi.Input[str] force_update_tag: How the extension handler should be forced to update even if the extension configuration has not changed.
        :param pulumi.Input['MachineExtensionInstanceViewArgs'] instance_view: The machine extension instance view.
        :param Any protected_settings: The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all.
        :param pulumi.Input[str] publisher: The name of the extension handler publisher.
        :param Any settings: Json formatted public settings for the extension.
        :param pulumi.Input[str] type: Specifies the type of the extension; an example is "CustomScriptExtension".
        :param pulumi.Input[str] type_handler_version: Specifies the version of the script handler.
        """
        if auto_upgrade_minor_version is not None:
            pulumi.set(__self__, "auto_upgrade_minor_version", auto_upgrade_minor_version)
        if force_update_tag is not None:
            pulumi.set(__self__, "force_update_tag", force_update_tag)
        if instance_view is not None:
            pulumi.set(__self__, "instance_view", instance_view)
        if protected_settings is not None:
            pulumi.set(__self__, "protected_settings", protected_settings)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)
        if settings is not None:
            pulumi.set(__self__, "settings", settings)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if type_handler_version is not None:
            pulumi.set(__self__, "type_handler_version", type_handler_version)

    @property
    @pulumi.getter(name="autoUpgradeMinorVersion")
    def auto_upgrade_minor_version(self) -> Optional[pulumi.Input[bool]]:
        """
        Indicates whether the extension should use a newer minor version if one is available at deployment time. Once deployed, however, the extension will not upgrade minor versions unless redeployed, even with this property set to true.
        """
        return pulumi.get(self, "auto_upgrade_minor_version")

    @auto_upgrade_minor_version.setter
    def auto_upgrade_minor_version(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_upgrade_minor_version", value)

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[pulumi.Input[str]]:
        """
        How the extension handler should be forced to update even if the extension configuration has not changed.
        """
        return pulumi.get(self, "force_update_tag")

    @force_update_tag.setter
    def force_update_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "force_update_tag", value)

    @property
    @pulumi.getter(name="instanceView")
    def instance_view(self) -> Optional[pulumi.Input['MachineExtensionInstanceViewArgs']]:
        """
        The machine extension instance view.
        """
        return pulumi.get(self, "instance_view")

    @instance_view.setter
    def instance_view(self, value: Optional[pulumi.Input['MachineExtensionInstanceViewArgs']]):
        pulumi.set(self, "instance_view", value)

    @property
    @pulumi.getter(name="protectedSettings")
    def protected_settings(self) -> Optional[Any]:
        """
        The extension can contain either protectedSettings or protectedSettingsFromKeyVault or no protected settings at all.
        """
        return pulumi.get(self, "protected_settings")

    @protected_settings.setter
    def protected_settings(self, value: Optional[Any]):
        pulumi.set(self, "protected_settings", value)

    @property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the extension handler publisher.
        """
        return pulumi.get(self, "publisher")

    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publisher", value)

    @property
    @pulumi.getter
    def settings(self) -> Optional[Any]:
        """
        Json formatted public settings for the extension.
        """
        return pulumi.get(self, "settings")

    @settings.setter
    def settings(self, value: Optional[Any]):
        pulumi.set(self, "settings", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the type of the extension; an example is "CustomScriptExtension".
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter(name="typeHandlerVersion")
    def type_handler_version(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the version of the script handler.
        """
        return pulumi.get(self, "type_handler_version")

    @type_handler_version.setter
    def type_handler_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type_handler_version", value)


@pulumi.input_type
class MachinePropertiesArgs:
    def __init__(__self__, *,
                 client_public_key: Optional[pulumi.Input[str]] = None,
                 extensions: Optional[pulumi.Input[Sequence[pulumi.Input['MachineExtensionInstanceViewArgs']]]] = None,
                 location_data: Optional[pulumi.Input['LocationDataArgs']] = None,
                 mssql_discovered: Optional[pulumi.Input[str]] = None,
                 os_profile: Optional[pulumi.Input['OSProfileArgs']] = None,
                 os_type: Optional[pulumi.Input[str]] = None,
                 parent_cluster_resource_id: Optional[pulumi.Input[str]] = None,
                 private_link_scope_resource_id: Optional[pulumi.Input[str]] = None,
                 vm_id: Optional[pulumi.Input[str]] = None):
        """
        Describes the properties of a hybrid machine.
        :param pulumi.Input[str] client_public_key: Public Key that the client provides to be used during initial resource onboarding
        :param pulumi.Input[Sequence[pulumi.Input['MachineExtensionInstanceViewArgs']]] extensions: Machine Extensions information
        :param pulumi.Input['LocationDataArgs'] location_data: Metadata pertaining to the geographic location of the resource.
        :param pulumi.Input[str] mssql_discovered: Specifies whether any MS SQL instance is discovered on the machine.
        :param pulumi.Input['OSProfileArgs'] os_profile: Specifies the operating system settings for the hybrid machine.
        :param pulumi.Input[str] os_type: The type of Operating System (windows/linux).
        :param pulumi.Input[str] parent_cluster_resource_id: The resource id of the parent cluster (Azure HCI) this machine is assigned to, if any.
        :param pulumi.Input[str] private_link_scope_resource_id: The resource id of the private link scope this machine is assigned to, if any.
        :param pulumi.Input[str] vm_id: Specifies the hybrid machine unique ID.
        """
        if client_public_key is not None:
            pulumi.set(__self__, "client_public_key", client_public_key)
        if extensions is not None:
            pulumi.set(__self__, "extensions", extensions)
        if location_data is not None:
            pulumi.set(__self__, "location_data", location_data)
        if mssql_discovered is not None:
            pulumi.set(__self__, "mssql_discovered", mssql_discovered)
        if os_profile is not None:
            pulumi.set(__self__, "os_profile", os_profile)
        if os_type is not None:
            pulumi.set(__self__, "os_type", os_type)
        if parent_cluster_resource_id is not None:
            pulumi.set(__self__, "parent_cluster_resource_id", parent_cluster_resource_id)
        if private_link_scope_resource_id is not None:
            pulumi.set(__self__, "private_link_scope_resource_id", private_link_scope_resource_id)
        if vm_id is not None:
            pulumi.set(__self__, "vm_id", vm_id)

    @property
    @pulumi.getter(name="clientPublicKey")
    def client_public_key(self) -> Optional[pulumi.Input[str]]:
        """
        Public Key that the client provides to be used during initial resource onboarding
        """
        return pulumi.get(self, "client_public_key")

    @client_public_key.setter
    def client_public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "client_public_key", value)

    @property
    @pulumi.getter
    def extensions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['MachineExtensionInstanceViewArgs']]]]:
        """
        Machine Extensions information
        """
        return pulumi.get(self, "extensions")

    @extensions.setter
    def extensions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['MachineExtensionInstanceViewArgs']]]]):
        pulumi.set(self, "extensions", value)

    @property
    @pulumi.getter(name="locationData")
    def location_data(self) -> Optional[pulumi.Input['LocationDataArgs']]:
        """
        Metadata pertaining to the geographic location of the resource.
        """
        return pulumi.get(self, "location_data")

    @location_data.setter
    def location_data(self, value: Optional[pulumi.Input['LocationDataArgs']]):
        pulumi.set(self, "location_data", value)

    @property
    @pulumi.getter(name="mssqlDiscovered")
    def mssql_discovered(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies whether any MS SQL instance is discovered on the machine.
        """
        return pulumi.get(self, "mssql_discovered")

    @mssql_discovered.setter
    def mssql_discovered(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "mssql_discovered", value)

    @property
    @pulumi.getter(name="osProfile")
    def os_profile(self) -> Optional[pulumi.Input['OSProfileArgs']]:
        """
        Specifies the operating system settings for the hybrid machine.
        """
        return pulumi.get(self, "os_profile")

    @os_profile.setter
    def os_profile(self, value: Optional[pulumi.Input['OSProfileArgs']]):
        pulumi.set(self, "os_profile", value)

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[pulumi.Input[str]]:
        """
        The type of Operating System (windows/linux).
        """
        return pulumi.get(self, "os_type")

    @os_type.setter
    def os_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "os_type", value)

    @property
    @pulumi.getter(name="parentClusterResourceId")
    def parent_cluster_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the parent cluster (Azure HCI) this machine is assigned to, if any.
        """
        return pulumi.get(self, "parent_cluster_resource_id")

    @parent_cluster_resource_id.setter
    def parent_cluster_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_cluster_resource_id", value)

    @property
    @pulumi.getter(name="privateLinkScopeResourceId")
    def private_link_scope_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource id of the private link scope this machine is assigned to, if any.
        """
        return pulumi.get(self, "private_link_scope_resource_id")

    @private_link_scope_resource_id.setter
    def private_link_scope_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "private_link_scope_resource_id", value)

    @property
    @pulumi.getter(name="vmId")
    def vm_id(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the hybrid machine unique ID.
        """
        return pulumi.get(self, "vm_id")

    @vm_id.setter
    def vm_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "vm_id", value)


@pulumi.input_type
class OSProfileLinuxConfigurationArgs:
    def __init__(__self__, *,
                 assessment_mode: Optional[pulumi.Input[str]] = None):
        """
        Specifies the linux configuration for update management.
        :param pulumi.Input[str] assessment_mode: Specifies the assessment mode.
        """
        if assessment_mode is not None:
            pulumi.set(__self__, "assessment_mode", assessment_mode)

    @property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the assessment mode.
        """
        return pulumi.get(self, "assessment_mode")

    @assessment_mode.setter
    def assessment_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_mode", value)


@pulumi.input_type
class OSProfileWindowsConfigurationArgs:
    def __init__(__self__, *,
                 assessment_mode: Optional[pulumi.Input[str]] = None):
        """
        Specifies the windows configuration for update management.
        :param pulumi.Input[str] assessment_mode: Specifies the assessment mode.
        """
        if assessment_mode is not None:
            pulumi.set(__self__, "assessment_mode", assessment_mode)

    @property
    @pulumi.getter(name="assessmentMode")
    def assessment_mode(self) -> Optional[pulumi.Input[str]]:
        """
        Specifies the assessment mode.
        """
        return pulumi.get(self, "assessment_mode")

    @assessment_mode.setter
    def assessment_mode(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "assessment_mode", value)


@pulumi.input_type
class OSProfileArgs:
    def __init__(__self__, *,
                 linux_configuration: Optional[pulumi.Input['OSProfileLinuxConfigurationArgs']] = None,
                 windows_configuration: Optional[pulumi.Input['OSProfileWindowsConfigurationArgs']] = None):
        """
        Specifies the operating system settings for the hybrid machine.
        :param pulumi.Input['OSProfileLinuxConfigurationArgs'] linux_configuration: Specifies the linux configuration for update management.
        :param pulumi.Input['OSProfileWindowsConfigurationArgs'] windows_configuration: Specifies the windows configuration for update management.
        """
        if linux_configuration is not None:
            pulumi.set(__self__, "linux_configuration", linux_configuration)
        if windows_configuration is not None:
            pulumi.set(__self__, "windows_configuration", windows_configuration)

    @property
    @pulumi.getter(name="linuxConfiguration")
    def linux_configuration(self) -> Optional[pulumi.Input['OSProfileLinuxConfigurationArgs']]:
        """
        Specifies the linux configuration for update management.
        """
        return pulumi.get(self, "linux_configuration")

    @linux_configuration.setter
    def linux_configuration(self, value: Optional[pulumi.Input['OSProfileLinuxConfigurationArgs']]):
        pulumi.set(self, "linux_configuration", value)

    @property
    @pulumi.getter(name="windowsConfiguration")
    def windows_configuration(self) -> Optional[pulumi.Input['OSProfileWindowsConfigurationArgs']]:
        """
        Specifies the windows configuration for update management.
        """
        return pulumi.get(self, "windows_configuration")

    @windows_configuration.setter
    def windows_configuration(self, value: Optional[pulumi.Input['OSProfileWindowsConfigurationArgs']]):
        pulumi.set(self, "windows_configuration", value)


@pulumi.input_type
class PrivateEndpointConnectionPropertiesArgs:
    def __init__(__self__, *,
                 private_endpoint: Optional[pulumi.Input['PrivateEndpointPropertyArgs']] = None,
                 private_link_service_connection_state: Optional[pulumi.Input['PrivateLinkServiceConnectionStatePropertyArgs']] = None):
        """
        Properties of a private endpoint connection.
        :param pulumi.Input['PrivateEndpointPropertyArgs'] private_endpoint: Private endpoint which the connection belongs to.
        :param pulumi.Input['PrivateLinkServiceConnectionStatePropertyArgs'] private_link_service_connection_state: Connection state of the private endpoint connection.
        """
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional[pulumi.Input['PrivateEndpointPropertyArgs']]:
        """
        Private endpoint which the connection belongs to.
        """
        return pulumi.get(self, "private_endpoint")

    @private_endpoint.setter
    def private_endpoint(self, value: Optional[pulumi.Input['PrivateEndpointPropertyArgs']]):
        pulumi.set(self, "private_endpoint", value)

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional[pulumi.Input['PrivateLinkServiceConnectionStatePropertyArgs']]:
        """
        Connection state of the private endpoint connection.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @private_link_service_connection_state.setter
    def private_link_service_connection_state(self, value: Optional[pulumi.Input['PrivateLinkServiceConnectionStatePropertyArgs']]):
        pulumi.set(self, "private_link_service_connection_state", value)


@pulumi.input_type
class PrivateEndpointPropertyArgs:
    def __init__(__self__, *,
                 id: Optional[pulumi.Input[str]] = None):
        """
        Private endpoint which the connection belongs to.
        :param pulumi.Input[str] id: Resource id of the private endpoint.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource id of the private endpoint.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)


@pulumi.input_type
class PrivateLinkServiceConnectionStatePropertyArgs:
    def __init__(__self__, *,
                 description: pulumi.Input[str],
                 status: pulumi.Input[str]):
        """
        State of the private endpoint connection.
        :param pulumi.Input[str] description: The private link service connection description.
        :param pulumi.Input[str] status: The private link service connection status.
        """
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        The private link service connection description.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def status(self) -> pulumi.Input[str]:
        """
        The private link service connection status.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: pulumi.Input[str]):
        pulumi.set(self, "status", value)


