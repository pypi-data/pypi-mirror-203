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
    'GetVolumeResult',
    'AwaitableGetVolumeResult',
    'get_volume',
    'get_volume_output',
]

@pulumi.output_type
class GetVolumeResult:
    """
    Volume resource
    """
    def __init__(__self__, avs_data_store=None, backup_id=None, baremetal_tenant_id=None, capacity_pool_resource_id=None, clone_progress=None, cool_access=None, coolness_period=None, creation_token=None, data_protection=None, default_group_quota_in_ki_bs=None, default_user_quota_in_ki_bs=None, enable_subvolumes=None, encryption_key_source=None, etag=None, export_policy=None, file_system_id=None, id=None, is_default_quota_enabled=None, is_restoring=None, kerberos_enabled=None, ldap_enabled=None, location=None, maximum_number_of_files=None, mount_targets=None, name=None, network_features=None, network_sibling_set_id=None, placement_rules=None, protocol_types=None, provisioning_state=None, proximity_placement_group=None, security_style=None, service_level=None, smb_continuously_available=None, smb_encryption=None, snapshot_directory_visible=None, snapshot_id=None, storage_to_network_proximity=None, subnet_id=None, system_data=None, t2_network=None, tags=None, throughput_mibps=None, type=None, unix_permissions=None, usage_threshold=None, volume_group_name=None, volume_spec_name=None, volume_type=None):
        if avs_data_store and not isinstance(avs_data_store, str):
            raise TypeError("Expected argument 'avs_data_store' to be a str")
        pulumi.set(__self__, "avs_data_store", avs_data_store)
        if backup_id and not isinstance(backup_id, str):
            raise TypeError("Expected argument 'backup_id' to be a str")
        pulumi.set(__self__, "backup_id", backup_id)
        if baremetal_tenant_id and not isinstance(baremetal_tenant_id, str):
            raise TypeError("Expected argument 'baremetal_tenant_id' to be a str")
        pulumi.set(__self__, "baremetal_tenant_id", baremetal_tenant_id)
        if capacity_pool_resource_id and not isinstance(capacity_pool_resource_id, str):
            raise TypeError("Expected argument 'capacity_pool_resource_id' to be a str")
        pulumi.set(__self__, "capacity_pool_resource_id", capacity_pool_resource_id)
        if clone_progress and not isinstance(clone_progress, int):
            raise TypeError("Expected argument 'clone_progress' to be a int")
        pulumi.set(__self__, "clone_progress", clone_progress)
        if cool_access and not isinstance(cool_access, bool):
            raise TypeError("Expected argument 'cool_access' to be a bool")
        pulumi.set(__self__, "cool_access", cool_access)
        if coolness_period and not isinstance(coolness_period, int):
            raise TypeError("Expected argument 'coolness_period' to be a int")
        pulumi.set(__self__, "coolness_period", coolness_period)
        if creation_token and not isinstance(creation_token, str):
            raise TypeError("Expected argument 'creation_token' to be a str")
        pulumi.set(__self__, "creation_token", creation_token)
        if data_protection and not isinstance(data_protection, dict):
            raise TypeError("Expected argument 'data_protection' to be a dict")
        pulumi.set(__self__, "data_protection", data_protection)
        if default_group_quota_in_ki_bs and not isinstance(default_group_quota_in_ki_bs, float):
            raise TypeError("Expected argument 'default_group_quota_in_ki_bs' to be a float")
        pulumi.set(__self__, "default_group_quota_in_ki_bs", default_group_quota_in_ki_bs)
        if default_user_quota_in_ki_bs and not isinstance(default_user_quota_in_ki_bs, float):
            raise TypeError("Expected argument 'default_user_quota_in_ki_bs' to be a float")
        pulumi.set(__self__, "default_user_quota_in_ki_bs", default_user_quota_in_ki_bs)
        if enable_subvolumes and not isinstance(enable_subvolumes, str):
            raise TypeError("Expected argument 'enable_subvolumes' to be a str")
        pulumi.set(__self__, "enable_subvolumes", enable_subvolumes)
        if encryption_key_source and not isinstance(encryption_key_source, str):
            raise TypeError("Expected argument 'encryption_key_source' to be a str")
        pulumi.set(__self__, "encryption_key_source", encryption_key_source)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if export_policy and not isinstance(export_policy, dict):
            raise TypeError("Expected argument 'export_policy' to be a dict")
        pulumi.set(__self__, "export_policy", export_policy)
        if file_system_id and not isinstance(file_system_id, str):
            raise TypeError("Expected argument 'file_system_id' to be a str")
        pulumi.set(__self__, "file_system_id", file_system_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_default_quota_enabled and not isinstance(is_default_quota_enabled, bool):
            raise TypeError("Expected argument 'is_default_quota_enabled' to be a bool")
        pulumi.set(__self__, "is_default_quota_enabled", is_default_quota_enabled)
        if is_restoring and not isinstance(is_restoring, bool):
            raise TypeError("Expected argument 'is_restoring' to be a bool")
        pulumi.set(__self__, "is_restoring", is_restoring)
        if kerberos_enabled and not isinstance(kerberos_enabled, bool):
            raise TypeError("Expected argument 'kerberos_enabled' to be a bool")
        pulumi.set(__self__, "kerberos_enabled", kerberos_enabled)
        if ldap_enabled and not isinstance(ldap_enabled, bool):
            raise TypeError("Expected argument 'ldap_enabled' to be a bool")
        pulumi.set(__self__, "ldap_enabled", ldap_enabled)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if maximum_number_of_files and not isinstance(maximum_number_of_files, float):
            raise TypeError("Expected argument 'maximum_number_of_files' to be a float")
        pulumi.set(__self__, "maximum_number_of_files", maximum_number_of_files)
        if mount_targets and not isinstance(mount_targets, list):
            raise TypeError("Expected argument 'mount_targets' to be a list")
        pulumi.set(__self__, "mount_targets", mount_targets)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_features and not isinstance(network_features, str):
            raise TypeError("Expected argument 'network_features' to be a str")
        pulumi.set(__self__, "network_features", network_features)
        if network_sibling_set_id and not isinstance(network_sibling_set_id, str):
            raise TypeError("Expected argument 'network_sibling_set_id' to be a str")
        pulumi.set(__self__, "network_sibling_set_id", network_sibling_set_id)
        if placement_rules and not isinstance(placement_rules, list):
            raise TypeError("Expected argument 'placement_rules' to be a list")
        pulumi.set(__self__, "placement_rules", placement_rules)
        if protocol_types and not isinstance(protocol_types, list):
            raise TypeError("Expected argument 'protocol_types' to be a list")
        pulumi.set(__self__, "protocol_types", protocol_types)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if proximity_placement_group and not isinstance(proximity_placement_group, str):
            raise TypeError("Expected argument 'proximity_placement_group' to be a str")
        pulumi.set(__self__, "proximity_placement_group", proximity_placement_group)
        if security_style and not isinstance(security_style, str):
            raise TypeError("Expected argument 'security_style' to be a str")
        pulumi.set(__self__, "security_style", security_style)
        if service_level and not isinstance(service_level, str):
            raise TypeError("Expected argument 'service_level' to be a str")
        pulumi.set(__self__, "service_level", service_level)
        if smb_continuously_available and not isinstance(smb_continuously_available, bool):
            raise TypeError("Expected argument 'smb_continuously_available' to be a bool")
        pulumi.set(__self__, "smb_continuously_available", smb_continuously_available)
        if smb_encryption and not isinstance(smb_encryption, bool):
            raise TypeError("Expected argument 'smb_encryption' to be a bool")
        pulumi.set(__self__, "smb_encryption", smb_encryption)
        if snapshot_directory_visible and not isinstance(snapshot_directory_visible, bool):
            raise TypeError("Expected argument 'snapshot_directory_visible' to be a bool")
        pulumi.set(__self__, "snapshot_directory_visible", snapshot_directory_visible)
        if snapshot_id and not isinstance(snapshot_id, str):
            raise TypeError("Expected argument 'snapshot_id' to be a str")
        pulumi.set(__self__, "snapshot_id", snapshot_id)
        if storage_to_network_proximity and not isinstance(storage_to_network_proximity, str):
            raise TypeError("Expected argument 'storage_to_network_proximity' to be a str")
        pulumi.set(__self__, "storage_to_network_proximity", storage_to_network_proximity)
        if subnet_id and not isinstance(subnet_id, str):
            raise TypeError("Expected argument 'subnet_id' to be a str")
        pulumi.set(__self__, "subnet_id", subnet_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if t2_network and not isinstance(t2_network, str):
            raise TypeError("Expected argument 't2_network' to be a str")
        pulumi.set(__self__, "t2_network", t2_network)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if throughput_mibps and not isinstance(throughput_mibps, float):
            raise TypeError("Expected argument 'throughput_mibps' to be a float")
        pulumi.set(__self__, "throughput_mibps", throughput_mibps)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unix_permissions and not isinstance(unix_permissions, str):
            raise TypeError("Expected argument 'unix_permissions' to be a str")
        pulumi.set(__self__, "unix_permissions", unix_permissions)
        if usage_threshold and not isinstance(usage_threshold, float):
            raise TypeError("Expected argument 'usage_threshold' to be a float")
        pulumi.set(__self__, "usage_threshold", usage_threshold)
        if volume_group_name and not isinstance(volume_group_name, str):
            raise TypeError("Expected argument 'volume_group_name' to be a str")
        pulumi.set(__self__, "volume_group_name", volume_group_name)
        if volume_spec_name and not isinstance(volume_spec_name, str):
            raise TypeError("Expected argument 'volume_spec_name' to be a str")
        pulumi.set(__self__, "volume_spec_name", volume_spec_name)
        if volume_type and not isinstance(volume_type, str):
            raise TypeError("Expected argument 'volume_type' to be a str")
        pulumi.set(__self__, "volume_type", volume_type)

    @property
    @pulumi.getter(name="avsDataStore")
    def avs_data_store(self) -> Optional[str]:
        """
        Specifies whether the volume is enabled for Azure VMware Solution (AVS) datastore purpose
        """
        return pulumi.get(self, "avs_data_store")

    @property
    @pulumi.getter(name="backupId")
    def backup_id(self) -> Optional[str]:
        """
        UUID v4 or resource identifier used to identify the Backup.
        """
        return pulumi.get(self, "backup_id")

    @property
    @pulumi.getter(name="baremetalTenantId")
    def baremetal_tenant_id(self) -> str:
        """
        Unique Baremetal Tenant Identifier.
        """
        return pulumi.get(self, "baremetal_tenant_id")

    @property
    @pulumi.getter(name="capacityPoolResourceId")
    def capacity_pool_resource_id(self) -> Optional[str]:
        """
        Pool Resource Id used in case of creating a volume through volume group
        """
        return pulumi.get(self, "capacity_pool_resource_id")

    @property
    @pulumi.getter(name="cloneProgress")
    def clone_progress(self) -> int:
        """
        When a volume is being restored from another volume's snapshot, will show the percentage completion of this cloning process. When this value is empty/null there is no cloning process currently happening on this volume. This value will update every 5 minutes during cloning.
        """
        return pulumi.get(self, "clone_progress")

    @property
    @pulumi.getter(name="coolAccess")
    def cool_access(self) -> Optional[bool]:
        """
        Specifies whether Cool Access(tiering) is enabled for the volume.
        """
        return pulumi.get(self, "cool_access")

    @property
    @pulumi.getter(name="coolnessPeriod")
    def coolness_period(self) -> Optional[int]:
        """
        Specifies the number of days after which data that is not accessed by clients will be tiered.
        """
        return pulumi.get(self, "coolness_period")

    @property
    @pulumi.getter(name="creationToken")
    def creation_token(self) -> str:
        """
        A unique file path for the volume. Used when creating mount targets
        """
        return pulumi.get(self, "creation_token")

    @property
    @pulumi.getter(name="dataProtection")
    def data_protection(self) -> Optional['outputs.VolumePropertiesResponseDataProtection']:
        """
        DataProtection type volumes include an object containing details of the replication
        """
        return pulumi.get(self, "data_protection")

    @property
    @pulumi.getter(name="defaultGroupQuotaInKiBs")
    def default_group_quota_in_ki_bs(self) -> Optional[float]:
        """
        Default group quota for volume in KiBs. If isDefaultQuotaEnabled is set, the minimum value of 4 KiBs applies.
        """
        return pulumi.get(self, "default_group_quota_in_ki_bs")

    @property
    @pulumi.getter(name="defaultUserQuotaInKiBs")
    def default_user_quota_in_ki_bs(self) -> Optional[float]:
        """
        Default user quota for volume in KiBs. If isDefaultQuotaEnabled is set, the minimum value of 4 KiBs applies .
        """
        return pulumi.get(self, "default_user_quota_in_ki_bs")

    @property
    @pulumi.getter(name="enableSubvolumes")
    def enable_subvolumes(self) -> Optional[str]:
        """
        Flag indicating whether subvolume operations are enabled on the volume
        """
        return pulumi.get(self, "enable_subvolumes")

    @property
    @pulumi.getter(name="encryptionKeySource")
    def encryption_key_source(self) -> Optional[str]:
        """
        Encryption Key Source. Possible values are: 'Microsoft.NetApp'
        """
        return pulumi.get(self, "encryption_key_source")

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="exportPolicy")
    def export_policy(self) -> Optional['outputs.VolumePropertiesResponseExportPolicy']:
        """
        Set of export policy rules
        """
        return pulumi.get(self, "export_policy")

    @property
    @pulumi.getter(name="fileSystemId")
    def file_system_id(self) -> str:
        """
        Unique FileSystem Identifier.
        """
        return pulumi.get(self, "file_system_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDefaultQuotaEnabled")
    def is_default_quota_enabled(self) -> Optional[bool]:
        """
        Specifies if default quota is enabled for the volume.
        """
        return pulumi.get(self, "is_default_quota_enabled")

    @property
    @pulumi.getter(name="isRestoring")
    def is_restoring(self) -> Optional[bool]:
        """
        Restoring
        """
        return pulumi.get(self, "is_restoring")

    @property
    @pulumi.getter(name="kerberosEnabled")
    def kerberos_enabled(self) -> Optional[bool]:
        """
        Describe if a volume is KerberosEnabled. To be use with swagger version 2020-05-01 or later
        """
        return pulumi.get(self, "kerberos_enabled")

    @property
    @pulumi.getter(name="ldapEnabled")
    def ldap_enabled(self) -> Optional[bool]:
        """
        Specifies whether LDAP is enabled or not for a given NFS volume.
        """
        return pulumi.get(self, "ldap_enabled")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="maximumNumberOfFiles")
    def maximum_number_of_files(self) -> float:
        """
        Maximum number of files allowed. Needs a service request in order to be changed. Only allowed to be changed if volume quota is more than 4TiB.
        """
        return pulumi.get(self, "maximum_number_of_files")

    @property
    @pulumi.getter(name="mountTargets")
    def mount_targets(self) -> Sequence['outputs.MountTargetPropertiesResponse']:
        """
        List of mount targets
        """
        return pulumi.get(self, "mount_targets")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkFeatures")
    def network_features(self) -> Optional[str]:
        """
        Basic network, or Standard features available to the volume.
        """
        return pulumi.get(self, "network_features")

    @property
    @pulumi.getter(name="networkSiblingSetId")
    def network_sibling_set_id(self) -> str:
        """
        Network Sibling Set ID for the the group of volumes sharing networking resources.
        """
        return pulumi.get(self, "network_sibling_set_id")

    @property
    @pulumi.getter(name="placementRules")
    def placement_rules(self) -> Optional[Sequence['outputs.PlacementKeyValuePairsResponse']]:
        """
        Application specific placement rules for the particular volume
        """
        return pulumi.get(self, "placement_rules")

    @property
    @pulumi.getter(name="protocolTypes")
    def protocol_types(self) -> Optional[Sequence[str]]:
        """
        Set of protocol types, default NFSv3, CIFS for SMB protocol
        """
        return pulumi.get(self, "protocol_types")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="proximityPlacementGroup")
    def proximity_placement_group(self) -> Optional[str]:
        """
        Proximity placement group associated with the volume
        """
        return pulumi.get(self, "proximity_placement_group")

    @property
    @pulumi.getter(name="securityStyle")
    def security_style(self) -> Optional[str]:
        """
        The security style of volume, default unix, defaults to ntfs for dual protocol or CIFS protocol
        """
        return pulumi.get(self, "security_style")

    @property
    @pulumi.getter(name="serviceLevel")
    def service_level(self) -> Optional[str]:
        """
        The service level of the file system
        """
        return pulumi.get(self, "service_level")

    @property
    @pulumi.getter(name="smbContinuouslyAvailable")
    def smb_continuously_available(self) -> Optional[bool]:
        """
        Enables continuously available share property for smb volume. Only applicable for SMB volume
        """
        return pulumi.get(self, "smb_continuously_available")

    @property
    @pulumi.getter(name="smbEncryption")
    def smb_encryption(self) -> Optional[bool]:
        """
        Enables encryption for in-flight smb3 data. Only applicable for SMB/DualProtocol volume. To be used with swagger version 2020-08-01 or later
        """
        return pulumi.get(self, "smb_encryption")

    @property
    @pulumi.getter(name="snapshotDirectoryVisible")
    def snapshot_directory_visible(self) -> Optional[bool]:
        """
        If enabled (true) the volume will contain a read-only snapshot directory which provides access to each of the volume's snapshots (default to true).
        """
        return pulumi.get(self, "snapshot_directory_visible")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[str]:
        """
        UUID v4 or resource identifier used to identify the Snapshot.
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter(name="storageToNetworkProximity")
    def storage_to_network_proximity(self) -> str:
        """
        Provides storage to network proximity information for the volume.
        """
        return pulumi.get(self, "storage_to_network_proximity")

    @property
    @pulumi.getter(name="subnetId")
    def subnet_id(self) -> str:
        """
        The Azure Resource URI for a delegated subnet. Must have the delegation Microsoft.NetApp/volumes
        """
        return pulumi.get(self, "subnet_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="t2Network")
    def t2_network(self) -> str:
        """
        T2 network information
        """
        return pulumi.get(self, "t2_network")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="throughputMibps")
    def throughput_mibps(self) -> Optional[float]:
        return pulumi.get(self, "throughput_mibps")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="unixPermissions")
    def unix_permissions(self) -> Optional[str]:
        """
        UNIX permissions for NFS volume accepted in octal 4 digit format. First digit selects the set user ID(4), set group ID (2) and sticky (1) attributes. Second digit selects permission for the owner of the file: read (4), write (2) and execute (1). Third selects permissions for other users in the same group. the fourth for other users not in the group. 0755 - gives read/write/execute permissions to owner and read/execute to group and other users.
        """
        return pulumi.get(self, "unix_permissions")

    @property
    @pulumi.getter(name="usageThreshold")
    def usage_threshold(self) -> float:
        """
        Maximum storage quota allowed for a file system in bytes. This is a soft quota used for alerting only. Minimum size is 100 GiB. Upper limit is 100TiB. Specified in bytes.
        """
        return pulumi.get(self, "usage_threshold")

    @property
    @pulumi.getter(name="volumeGroupName")
    def volume_group_name(self) -> str:
        """
        Volume Group Name
        """
        return pulumi.get(self, "volume_group_name")

    @property
    @pulumi.getter(name="volumeSpecName")
    def volume_spec_name(self) -> Optional[str]:
        """
        Volume spec name is the application specific designation or identifier for the particular volume in a volume group for e.g. data, log
        """
        return pulumi.get(self, "volume_spec_name")

    @property
    @pulumi.getter(name="volumeType")
    def volume_type(self) -> Optional[str]:
        """
        What type of volume is this. For destination volumes in Cross Region Replication, set type to DataProtection
        """
        return pulumi.get(self, "volume_type")


class AwaitableGetVolumeResult(GetVolumeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeResult(
            avs_data_store=self.avs_data_store,
            backup_id=self.backup_id,
            baremetal_tenant_id=self.baremetal_tenant_id,
            capacity_pool_resource_id=self.capacity_pool_resource_id,
            clone_progress=self.clone_progress,
            cool_access=self.cool_access,
            coolness_period=self.coolness_period,
            creation_token=self.creation_token,
            data_protection=self.data_protection,
            default_group_quota_in_ki_bs=self.default_group_quota_in_ki_bs,
            default_user_quota_in_ki_bs=self.default_user_quota_in_ki_bs,
            enable_subvolumes=self.enable_subvolumes,
            encryption_key_source=self.encryption_key_source,
            etag=self.etag,
            export_policy=self.export_policy,
            file_system_id=self.file_system_id,
            id=self.id,
            is_default_quota_enabled=self.is_default_quota_enabled,
            is_restoring=self.is_restoring,
            kerberos_enabled=self.kerberos_enabled,
            ldap_enabled=self.ldap_enabled,
            location=self.location,
            maximum_number_of_files=self.maximum_number_of_files,
            mount_targets=self.mount_targets,
            name=self.name,
            network_features=self.network_features,
            network_sibling_set_id=self.network_sibling_set_id,
            placement_rules=self.placement_rules,
            protocol_types=self.protocol_types,
            provisioning_state=self.provisioning_state,
            proximity_placement_group=self.proximity_placement_group,
            security_style=self.security_style,
            service_level=self.service_level,
            smb_continuously_available=self.smb_continuously_available,
            smb_encryption=self.smb_encryption,
            snapshot_directory_visible=self.snapshot_directory_visible,
            snapshot_id=self.snapshot_id,
            storage_to_network_proximity=self.storage_to_network_proximity,
            subnet_id=self.subnet_id,
            system_data=self.system_data,
            t2_network=self.t2_network,
            tags=self.tags,
            throughput_mibps=self.throughput_mibps,
            type=self.type,
            unix_permissions=self.unix_permissions,
            usage_threshold=self.usage_threshold,
            volume_group_name=self.volume_group_name,
            volume_spec_name=self.volume_spec_name,
            volume_type=self.volume_type)


def get_volume(account_name: Optional[str] = None,
               pool_name: Optional[str] = None,
               resource_group_name: Optional[str] = None,
               volume_name: Optional[str] = None,
               opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeResult:
    """
    Get the details of the specified volume


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group.
    :param str volume_name: The name of the volume
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['volumeName'] = volume_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20211001:getVolume', __args__, opts=opts, typ=GetVolumeResult).value

    return AwaitableGetVolumeResult(
        avs_data_store=__ret__.avs_data_store,
        backup_id=__ret__.backup_id,
        baremetal_tenant_id=__ret__.baremetal_tenant_id,
        capacity_pool_resource_id=__ret__.capacity_pool_resource_id,
        clone_progress=__ret__.clone_progress,
        cool_access=__ret__.cool_access,
        coolness_period=__ret__.coolness_period,
        creation_token=__ret__.creation_token,
        data_protection=__ret__.data_protection,
        default_group_quota_in_ki_bs=__ret__.default_group_quota_in_ki_bs,
        default_user_quota_in_ki_bs=__ret__.default_user_quota_in_ki_bs,
        enable_subvolumes=__ret__.enable_subvolumes,
        encryption_key_source=__ret__.encryption_key_source,
        etag=__ret__.etag,
        export_policy=__ret__.export_policy,
        file_system_id=__ret__.file_system_id,
        id=__ret__.id,
        is_default_quota_enabled=__ret__.is_default_quota_enabled,
        is_restoring=__ret__.is_restoring,
        kerberos_enabled=__ret__.kerberos_enabled,
        ldap_enabled=__ret__.ldap_enabled,
        location=__ret__.location,
        maximum_number_of_files=__ret__.maximum_number_of_files,
        mount_targets=__ret__.mount_targets,
        name=__ret__.name,
        network_features=__ret__.network_features,
        network_sibling_set_id=__ret__.network_sibling_set_id,
        placement_rules=__ret__.placement_rules,
        protocol_types=__ret__.protocol_types,
        provisioning_state=__ret__.provisioning_state,
        proximity_placement_group=__ret__.proximity_placement_group,
        security_style=__ret__.security_style,
        service_level=__ret__.service_level,
        smb_continuously_available=__ret__.smb_continuously_available,
        smb_encryption=__ret__.smb_encryption,
        snapshot_directory_visible=__ret__.snapshot_directory_visible,
        snapshot_id=__ret__.snapshot_id,
        storage_to_network_proximity=__ret__.storage_to_network_proximity,
        subnet_id=__ret__.subnet_id,
        system_data=__ret__.system_data,
        t2_network=__ret__.t2_network,
        tags=__ret__.tags,
        throughput_mibps=__ret__.throughput_mibps,
        type=__ret__.type,
        unix_permissions=__ret__.unix_permissions,
        usage_threshold=__ret__.usage_threshold,
        volume_group_name=__ret__.volume_group_name,
        volume_spec_name=__ret__.volume_spec_name,
        volume_type=__ret__.volume_type)


@_utilities.lift_output_func(get_volume)
def get_volume_output(account_name: Optional[pulumi.Input[str]] = None,
                      pool_name: Optional[pulumi.Input[str]] = None,
                      resource_group_name: Optional[pulumi.Input[str]] = None,
                      volume_name: Optional[pulumi.Input[str]] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeResult]:
    """
    Get the details of the specified volume


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group.
    :param str volume_name: The name of the volume
    """
    ...
