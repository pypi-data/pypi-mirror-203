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
    'GetDiskResult',
    'AwaitableGetDiskResult',
    'get_disk',
    'get_disk_output',
]

@pulumi.output_type
class GetDiskResult:
    """
    Disk resource.
    """
    def __init__(__self__, bursting_enabled=None, completion_percent=None, creation_data=None, disk_access_id=None, disk_iops_read_only=None, disk_iops_read_write=None, disk_m_bps_read_only=None, disk_m_bps_read_write=None, disk_size_bytes=None, disk_size_gb=None, disk_state=None, encryption=None, encryption_settings_collection=None, extended_location=None, hyper_v_generation=None, id=None, location=None, managed_by=None, managed_by_extended=None, max_shares=None, name=None, network_access_policy=None, os_type=None, property_updates_in_progress=None, provisioning_state=None, public_network_access=None, purchase_plan=None, security_profile=None, share_info=None, sku=None, supported_capabilities=None, supports_hibernation=None, tags=None, tier=None, time_created=None, type=None, unique_id=None, zones=None):
        if bursting_enabled and not isinstance(bursting_enabled, bool):
            raise TypeError("Expected argument 'bursting_enabled' to be a bool")
        pulumi.set(__self__, "bursting_enabled", bursting_enabled)
        if completion_percent and not isinstance(completion_percent, float):
            raise TypeError("Expected argument 'completion_percent' to be a float")
        pulumi.set(__self__, "completion_percent", completion_percent)
        if creation_data and not isinstance(creation_data, dict):
            raise TypeError("Expected argument 'creation_data' to be a dict")
        pulumi.set(__self__, "creation_data", creation_data)
        if disk_access_id and not isinstance(disk_access_id, str):
            raise TypeError("Expected argument 'disk_access_id' to be a str")
        pulumi.set(__self__, "disk_access_id", disk_access_id)
        if disk_iops_read_only and not isinstance(disk_iops_read_only, float):
            raise TypeError("Expected argument 'disk_iops_read_only' to be a float")
        pulumi.set(__self__, "disk_iops_read_only", disk_iops_read_only)
        if disk_iops_read_write and not isinstance(disk_iops_read_write, float):
            raise TypeError("Expected argument 'disk_iops_read_write' to be a float")
        pulumi.set(__self__, "disk_iops_read_write", disk_iops_read_write)
        if disk_m_bps_read_only and not isinstance(disk_m_bps_read_only, float):
            raise TypeError("Expected argument 'disk_m_bps_read_only' to be a float")
        pulumi.set(__self__, "disk_m_bps_read_only", disk_m_bps_read_only)
        if disk_m_bps_read_write and not isinstance(disk_m_bps_read_write, float):
            raise TypeError("Expected argument 'disk_m_bps_read_write' to be a float")
        pulumi.set(__self__, "disk_m_bps_read_write", disk_m_bps_read_write)
        if disk_size_bytes and not isinstance(disk_size_bytes, float):
            raise TypeError("Expected argument 'disk_size_bytes' to be a float")
        pulumi.set(__self__, "disk_size_bytes", disk_size_bytes)
        if disk_size_gb and not isinstance(disk_size_gb, int):
            raise TypeError("Expected argument 'disk_size_gb' to be a int")
        pulumi.set(__self__, "disk_size_gb", disk_size_gb)
        if disk_state and not isinstance(disk_state, str):
            raise TypeError("Expected argument 'disk_state' to be a str")
        pulumi.set(__self__, "disk_state", disk_state)
        if encryption and not isinstance(encryption, dict):
            raise TypeError("Expected argument 'encryption' to be a dict")
        pulumi.set(__self__, "encryption", encryption)
        if encryption_settings_collection and not isinstance(encryption_settings_collection, dict):
            raise TypeError("Expected argument 'encryption_settings_collection' to be a dict")
        pulumi.set(__self__, "encryption_settings_collection", encryption_settings_collection)
        if extended_location and not isinstance(extended_location, dict):
            raise TypeError("Expected argument 'extended_location' to be a dict")
        pulumi.set(__self__, "extended_location", extended_location)
        if hyper_v_generation and not isinstance(hyper_v_generation, str):
            raise TypeError("Expected argument 'hyper_v_generation' to be a str")
        pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if managed_by and not isinstance(managed_by, str):
            raise TypeError("Expected argument 'managed_by' to be a str")
        pulumi.set(__self__, "managed_by", managed_by)
        if managed_by_extended and not isinstance(managed_by_extended, list):
            raise TypeError("Expected argument 'managed_by_extended' to be a list")
        pulumi.set(__self__, "managed_by_extended", managed_by_extended)
        if max_shares and not isinstance(max_shares, int):
            raise TypeError("Expected argument 'max_shares' to be a int")
        pulumi.set(__self__, "max_shares", max_shares)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_access_policy and not isinstance(network_access_policy, str):
            raise TypeError("Expected argument 'network_access_policy' to be a str")
        pulumi.set(__self__, "network_access_policy", network_access_policy)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if property_updates_in_progress and not isinstance(property_updates_in_progress, dict):
            raise TypeError("Expected argument 'property_updates_in_progress' to be a dict")
        pulumi.set(__self__, "property_updates_in_progress", property_updates_in_progress)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_network_access and not isinstance(public_network_access, str):
            raise TypeError("Expected argument 'public_network_access' to be a str")
        pulumi.set(__self__, "public_network_access", public_network_access)
        if purchase_plan and not isinstance(purchase_plan, dict):
            raise TypeError("Expected argument 'purchase_plan' to be a dict")
        pulumi.set(__self__, "purchase_plan", purchase_plan)
        if security_profile and not isinstance(security_profile, dict):
            raise TypeError("Expected argument 'security_profile' to be a dict")
        pulumi.set(__self__, "security_profile", security_profile)
        if share_info and not isinstance(share_info, list):
            raise TypeError("Expected argument 'share_info' to be a list")
        pulumi.set(__self__, "share_info", share_info)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if supported_capabilities and not isinstance(supported_capabilities, dict):
            raise TypeError("Expected argument 'supported_capabilities' to be a dict")
        pulumi.set(__self__, "supported_capabilities", supported_capabilities)
        if supports_hibernation and not isinstance(supports_hibernation, bool):
            raise TypeError("Expected argument 'supports_hibernation' to be a bool")
        pulumi.set(__self__, "supports_hibernation", supports_hibernation)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tier and not isinstance(tier, str):
            raise TypeError("Expected argument 'tier' to be a str")
        pulumi.set(__self__, "tier", tier)
        if time_created and not isinstance(time_created, str):
            raise TypeError("Expected argument 'time_created' to be a str")
        pulumi.set(__self__, "time_created", time_created)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_id and not isinstance(unique_id, str):
            raise TypeError("Expected argument 'unique_id' to be a str")
        pulumi.set(__self__, "unique_id", unique_id)
        if zones and not isinstance(zones, list):
            raise TypeError("Expected argument 'zones' to be a list")
        pulumi.set(__self__, "zones", zones)

    @property
    @pulumi.getter(name="burstingEnabled")
    def bursting_enabled(self) -> Optional[bool]:
        """
        Set to true to enable bursting beyond the provisioned performance target of the disk. Bursting is disabled by default. Does not apply to Ultra disks.
        """
        return pulumi.get(self, "bursting_enabled")

    @property
    @pulumi.getter(name="completionPercent")
    def completion_percent(self) -> Optional[float]:
        """
        Percentage complete for the background copy when a resource is created via the CopyStart operation.
        """
        return pulumi.get(self, "completion_percent")

    @property
    @pulumi.getter(name="creationData")
    def creation_data(self) -> 'outputs.CreationDataResponse':
        """
        Disk source information. CreationData information cannot be changed after the disk has been created.
        """
        return pulumi.get(self, "creation_data")

    @property
    @pulumi.getter(name="diskAccessId")
    def disk_access_id(self) -> Optional[str]:
        """
        ARM id of the DiskAccess resource for using private endpoints on disks.
        """
        return pulumi.get(self, "disk_access_id")

    @property
    @pulumi.getter(name="diskIOPSReadOnly")
    def disk_iops_read_only(self) -> Optional[float]:
        """
        The total number of IOPS that will be allowed across all VMs mounting the shared disk as ReadOnly. One operation can transfer between 4k and 256k bytes.
        """
        return pulumi.get(self, "disk_iops_read_only")

    @property
    @pulumi.getter(name="diskIOPSReadWrite")
    def disk_iops_read_write(self) -> Optional[float]:
        """
        The number of IOPS allowed for this disk; only settable for UltraSSD disks. One operation can transfer between 4k and 256k bytes.
        """
        return pulumi.get(self, "disk_iops_read_write")

    @property
    @pulumi.getter(name="diskMBpsReadOnly")
    def disk_m_bps_read_only(self) -> Optional[float]:
        """
        The total throughput (MBps) that will be allowed across all VMs mounting the shared disk as ReadOnly. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.
        """
        return pulumi.get(self, "disk_m_bps_read_only")

    @property
    @pulumi.getter(name="diskMBpsReadWrite")
    def disk_m_bps_read_write(self) -> Optional[float]:
        """
        The bandwidth allowed for this disk; only settable for UltraSSD disks. MBps means millions of bytes per second - MB here uses the ISO notation, of powers of 10.
        """
        return pulumi.get(self, "disk_m_bps_read_write")

    @property
    @pulumi.getter(name="diskSizeBytes")
    def disk_size_bytes(self) -> float:
        """
        The size of the disk in bytes. This field is read only.
        """
        return pulumi.get(self, "disk_size_bytes")

    @property
    @pulumi.getter(name="diskSizeGB")
    def disk_size_gb(self) -> Optional[int]:
        """
        If creationData.createOption is Empty, this field is mandatory and it indicates the size of the disk to create. If this field is present for updates or creation with other options, it indicates a resize. Resizes are only allowed if the disk is not attached to a running VM, and can only increase the disk's size.
        """
        return pulumi.get(self, "disk_size_gb")

    @property
    @pulumi.getter(name="diskState")
    def disk_state(self) -> str:
        """
        The state of the disk.
        """
        return pulumi.get(self, "disk_state")

    @property
    @pulumi.getter
    def encryption(self) -> Optional['outputs.EncryptionResponse']:
        """
        Encryption property can be used to encrypt data at rest with customer managed keys or platform managed keys.
        """
        return pulumi.get(self, "encryption")

    @property
    @pulumi.getter(name="encryptionSettingsCollection")
    def encryption_settings_collection(self) -> Optional['outputs.EncryptionSettingsCollectionResponse']:
        """
        Encryption settings collection used for Azure Disk Encryption, can contain multiple encryption settings per disk or snapshot.
        """
        return pulumi.get(self, "encryption_settings_collection")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> Optional['outputs.ExtendedLocationResponse']:
        """
        The extended location where the disk will be created. Extended location cannot be changed.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[str]:
        """
        The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
        """
        return pulumi.get(self, "hyper_v_generation")

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
    @pulumi.getter(name="managedBy")
    def managed_by(self) -> str:
        """
        A relative URI containing the ID of the VM that has the disk attached.
        """
        return pulumi.get(self, "managed_by")

    @property
    @pulumi.getter(name="managedByExtended")
    def managed_by_extended(self) -> Sequence[str]:
        """
        List of relative URIs containing the IDs of the VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.
        """
        return pulumi.get(self, "managed_by_extended")

    @property
    @pulumi.getter(name="maxShares")
    def max_shares(self) -> Optional[int]:
        """
        The maximum number of VMs that can attach to the disk at the same time. Value greater than one indicates a disk that can be mounted on multiple VMs at the same time.
        """
        return pulumi.get(self, "max_shares")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkAccessPolicy")
    def network_access_policy(self) -> Optional[str]:
        """
        Policy for accessing the disk via network.
        """
        return pulumi.get(self, "network_access_policy")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        The Operating System type.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="propertyUpdatesInProgress")
    def property_updates_in_progress(self) -> 'outputs.PropertyUpdatesInProgressResponse':
        """
        Properties of the disk for which update is pending.
        """
        return pulumi.get(self, "property_updates_in_progress")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The disk provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Policy for controlling export on the disk.
        """
        return pulumi.get(self, "public_network_access")

    @property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(self) -> Optional['outputs.PurchasePlanResponse']:
        """
        Purchase plan information for the the image from which the OS disk was created. E.g. - {name: 2019-Datacenter, publisher: MicrosoftWindowsServer, product: WindowsServer}
        """
        return pulumi.get(self, "purchase_plan")

    @property
    @pulumi.getter(name="securityProfile")
    def security_profile(self) -> Optional['outputs.DiskSecurityProfileResponse']:
        """
        Contains the security related information for the resource.
        """
        return pulumi.get(self, "security_profile")

    @property
    @pulumi.getter(name="shareInfo")
    def share_info(self) -> Sequence['outputs.ShareInfoElementResponse']:
        """
        Details of the list of all VMs that have the disk attached. maxShares should be set to a value greater than one for disks to allow attaching them to multiple VMs.
        """
        return pulumi.get(self, "share_info")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.DiskSkuResponse']:
        """
        The disks sku name. Can be Standard_LRS, Premium_LRS, StandardSSD_LRS, UltraSSD_LRS, Premium_ZRS, or StandardSSD_ZRS.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="supportedCapabilities")
    def supported_capabilities(self) -> Optional['outputs.SupportedCapabilitiesResponse']:
        """
        List of supported capabilities for the image from which the OS disk was created.
        """
        return pulumi.get(self, "supported_capabilities")

    @property
    @pulumi.getter(name="supportsHibernation")
    def supports_hibernation(self) -> Optional[bool]:
        """
        Indicates the OS on a disk supports hibernation.
        """
        return pulumi.get(self, "supports_hibernation")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def tier(self) -> Optional[str]:
        """
        Performance tier of the disk (e.g, P4, S10) as described here: https://azure.microsoft.com/en-us/pricing/details/managed-disks/. Does not apply to Ultra disks.
        """
        return pulumi.get(self, "tier")

    @property
    @pulumi.getter(name="timeCreated")
    def time_created(self) -> str:
        """
        The time when the disk was created.
        """
        return pulumi.get(self, "time_created")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueId")
    def unique_id(self) -> str:
        """
        Unique Guid identifying the resource.
        """
        return pulumi.get(self, "unique_id")

    @property
    @pulumi.getter
    def zones(self) -> Optional[Sequence[str]]:
        """
        The Logical zone list for Disk.
        """
        return pulumi.get(self, "zones")


class AwaitableGetDiskResult(GetDiskResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiskResult(
            bursting_enabled=self.bursting_enabled,
            completion_percent=self.completion_percent,
            creation_data=self.creation_data,
            disk_access_id=self.disk_access_id,
            disk_iops_read_only=self.disk_iops_read_only,
            disk_iops_read_write=self.disk_iops_read_write,
            disk_m_bps_read_only=self.disk_m_bps_read_only,
            disk_m_bps_read_write=self.disk_m_bps_read_write,
            disk_size_bytes=self.disk_size_bytes,
            disk_size_gb=self.disk_size_gb,
            disk_state=self.disk_state,
            encryption=self.encryption,
            encryption_settings_collection=self.encryption_settings_collection,
            extended_location=self.extended_location,
            hyper_v_generation=self.hyper_v_generation,
            id=self.id,
            location=self.location,
            managed_by=self.managed_by,
            managed_by_extended=self.managed_by_extended,
            max_shares=self.max_shares,
            name=self.name,
            network_access_policy=self.network_access_policy,
            os_type=self.os_type,
            property_updates_in_progress=self.property_updates_in_progress,
            provisioning_state=self.provisioning_state,
            public_network_access=self.public_network_access,
            purchase_plan=self.purchase_plan,
            security_profile=self.security_profile,
            share_info=self.share_info,
            sku=self.sku,
            supported_capabilities=self.supported_capabilities,
            supports_hibernation=self.supports_hibernation,
            tags=self.tags,
            tier=self.tier,
            time_created=self.time_created,
            type=self.type,
            unique_id=self.unique_id,
            zones=self.zones)


def get_disk(disk_name: Optional[str] = None,
             resource_group_name: Optional[str] = None,
             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiskResult:
    """
    Gets information about a disk.


    :param str disk_name: The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['diskName'] = disk_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20210801:getDisk', __args__, opts=opts, typ=GetDiskResult).value

    return AwaitableGetDiskResult(
        bursting_enabled=__ret__.bursting_enabled,
        completion_percent=__ret__.completion_percent,
        creation_data=__ret__.creation_data,
        disk_access_id=__ret__.disk_access_id,
        disk_iops_read_only=__ret__.disk_iops_read_only,
        disk_iops_read_write=__ret__.disk_iops_read_write,
        disk_m_bps_read_only=__ret__.disk_m_bps_read_only,
        disk_m_bps_read_write=__ret__.disk_m_bps_read_write,
        disk_size_bytes=__ret__.disk_size_bytes,
        disk_size_gb=__ret__.disk_size_gb,
        disk_state=__ret__.disk_state,
        encryption=__ret__.encryption,
        encryption_settings_collection=__ret__.encryption_settings_collection,
        extended_location=__ret__.extended_location,
        hyper_v_generation=__ret__.hyper_v_generation,
        id=__ret__.id,
        location=__ret__.location,
        managed_by=__ret__.managed_by,
        managed_by_extended=__ret__.managed_by_extended,
        max_shares=__ret__.max_shares,
        name=__ret__.name,
        network_access_policy=__ret__.network_access_policy,
        os_type=__ret__.os_type,
        property_updates_in_progress=__ret__.property_updates_in_progress,
        provisioning_state=__ret__.provisioning_state,
        public_network_access=__ret__.public_network_access,
        purchase_plan=__ret__.purchase_plan,
        security_profile=__ret__.security_profile,
        share_info=__ret__.share_info,
        sku=__ret__.sku,
        supported_capabilities=__ret__.supported_capabilities,
        supports_hibernation=__ret__.supports_hibernation,
        tags=__ret__.tags,
        tier=__ret__.tier,
        time_created=__ret__.time_created,
        type=__ret__.type,
        unique_id=__ret__.unique_id,
        zones=__ret__.zones)


@_utilities.lift_output_func(get_disk)
def get_disk_output(disk_name: Optional[pulumi.Input[str]] = None,
                    resource_group_name: Optional[pulumi.Input[str]] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiskResult]:
    """
    Gets information about a disk.


    :param str disk_name: The name of the managed disk that is being created. The name can't be changed after the disk is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters.
    :param str resource_group_name: The name of the resource group.
    """
    ...
