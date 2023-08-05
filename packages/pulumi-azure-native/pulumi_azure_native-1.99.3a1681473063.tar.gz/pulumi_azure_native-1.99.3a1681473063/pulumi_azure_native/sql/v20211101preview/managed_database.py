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

__all__ = ['ManagedDatabaseArgs', 'ManagedDatabase']

@pulumi.input_type
class ManagedDatabaseArgs:
    def __init__(__self__, *,
                 managed_instance_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auto_complete_restore: Optional[pulumi.Input[bool]] = None,
                 catalog_collation: Optional[pulumi.Input[Union[str, 'CatalogCollationType']]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'ManagedDatabaseCreateMode']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 last_backup_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 long_term_retention_backup_resource_id: Optional[pulumi.Input[str]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 restorable_dropped_database_id: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 storage_container_sas_token: Optional[pulumi.Input[str]] = None,
                 storage_container_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ManagedDatabase resource.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[bool] auto_complete_restore: Whether to auto complete restore of this managed database.
        :param pulumi.Input[Union[str, 'CatalogCollationType']] catalog_collation: Collation of the metadata catalog.
        :param pulumi.Input[str] collation: Collation of the managed database.
        :param pulumi.Input[Union[str, 'ManagedDatabaseCreateMode']] create_mode: Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required).
        :param pulumi.Input[str] database_name: The name of the database.
        :param pulumi.Input[str] last_backup_name: Last backup file name for restore of this managed database.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] long_term_retention_backup_resource_id: The name of the Long Term Retention backup to be used for restore of this managed database.
        :param pulumi.Input[str] recoverable_database_id: The resource identifier of the recoverable database associated with create operation of this database.
        :param pulumi.Input[str] restorable_dropped_database_id: The restorable dropped database resource id to restore when creating this database.
        :param pulumi.Input[str] restore_point_in_time: Conditional. If createMode is PointInTimeRestore, this value is required. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.
        :param pulumi.Input[str] source_database_id: The resource identifier of the source database associated with create operation of this database.
        :param pulumi.Input[str] storage_container_sas_token: Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the storage container sas token.
        :param pulumi.Input[str] storage_container_uri: Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the uri of the storage container where backups for this restore are stored.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "managed_instance_name", managed_instance_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_complete_restore is not None:
            pulumi.set(__self__, "auto_complete_restore", auto_complete_restore)
        if catalog_collation is not None:
            pulumi.set(__self__, "catalog_collation", catalog_collation)
        if collation is not None:
            pulumi.set(__self__, "collation", collation)
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if database_name is not None:
            pulumi.set(__self__, "database_name", database_name)
        if last_backup_name is not None:
            pulumi.set(__self__, "last_backup_name", last_backup_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if long_term_retention_backup_resource_id is not None:
            pulumi.set(__self__, "long_term_retention_backup_resource_id", long_term_retention_backup_resource_id)
        if recoverable_database_id is not None:
            pulumi.set(__self__, "recoverable_database_id", recoverable_database_id)
        if restorable_dropped_database_id is not None:
            pulumi.set(__self__, "restorable_dropped_database_id", restorable_dropped_database_id)
        if restore_point_in_time is not None:
            pulumi.set(__self__, "restore_point_in_time", restore_point_in_time)
        if source_database_id is not None:
            pulumi.set(__self__, "source_database_id", source_database_id)
        if storage_container_sas_token is not None:
            pulumi.set(__self__, "storage_container_sas_token", storage_container_sas_token)
        if storage_container_uri is not None:
            pulumi.set(__self__, "storage_container_uri", storage_container_uri)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="managedInstanceName")
    def managed_instance_name(self) -> pulumi.Input[str]:
        """
        The name of the managed instance.
        """
        return pulumi.get(self, "managed_instance_name")

    @managed_instance_name.setter
    def managed_instance_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "managed_instance_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="autoCompleteRestore")
    def auto_complete_restore(self) -> Optional[pulumi.Input[bool]]:
        """
        Whether to auto complete restore of this managed database.
        """
        return pulumi.get(self, "auto_complete_restore")

    @auto_complete_restore.setter
    def auto_complete_restore(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_complete_restore", value)

    @property
    @pulumi.getter(name="catalogCollation")
    def catalog_collation(self) -> Optional[pulumi.Input[Union[str, 'CatalogCollationType']]]:
        """
        Collation of the metadata catalog.
        """
        return pulumi.get(self, "catalog_collation")

    @catalog_collation.setter
    def catalog_collation(self, value: Optional[pulumi.Input[Union[str, 'CatalogCollationType']]]):
        pulumi.set(self, "catalog_collation", value)

    @property
    @pulumi.getter
    def collation(self) -> Optional[pulumi.Input[str]]:
        """
        Collation of the managed database.
        """
        return pulumi.get(self, "collation")

    @collation.setter
    def collation(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "collation", value)

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[pulumi.Input[Union[str, 'ManagedDatabaseCreateMode']]]:
        """
        Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required).
        """
        return pulumi.get(self, "create_mode")

    @create_mode.setter
    def create_mode(self, value: Optional[pulumi.Input[Union[str, 'ManagedDatabaseCreateMode']]]):
        pulumi.set(self, "create_mode", value)

    @property
    @pulumi.getter(name="databaseName")
    def database_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the database.
        """
        return pulumi.get(self, "database_name")

    @database_name.setter
    def database_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "database_name", value)

    @property
    @pulumi.getter(name="lastBackupName")
    def last_backup_name(self) -> Optional[pulumi.Input[str]]:
        """
        Last backup file name for restore of this managed database.
        """
        return pulumi.get(self, "last_backup_name")

    @last_backup_name.setter
    def last_backup_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "last_backup_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="longTermRetentionBackupResourceId")
    def long_term_retention_backup_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the Long Term Retention backup to be used for restore of this managed database.
        """
        return pulumi.get(self, "long_term_retention_backup_resource_id")

    @long_term_retention_backup_resource_id.setter
    def long_term_retention_backup_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "long_term_retention_backup_resource_id", value)

    @property
    @pulumi.getter(name="recoverableDatabaseId")
    def recoverable_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of the recoverable database associated with create operation of this database.
        """
        return pulumi.get(self, "recoverable_database_id")

    @recoverable_database_id.setter
    def recoverable_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "recoverable_database_id", value)

    @property
    @pulumi.getter(name="restorableDroppedDatabaseId")
    def restorable_dropped_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The restorable dropped database resource id to restore when creating this database.
        """
        return pulumi.get(self, "restorable_dropped_database_id")

    @restorable_dropped_database_id.setter
    def restorable_dropped_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restorable_dropped_database_id", value)

    @property
    @pulumi.getter(name="restorePointInTime")
    def restore_point_in_time(self) -> Optional[pulumi.Input[str]]:
        """
        Conditional. If createMode is PointInTimeRestore, this value is required. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.
        """
        return pulumi.get(self, "restore_point_in_time")

    @restore_point_in_time.setter
    def restore_point_in_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restore_point_in_time", value)

    @property
    @pulumi.getter(name="sourceDatabaseId")
    def source_database_id(self) -> Optional[pulumi.Input[str]]:
        """
        The resource identifier of the source database associated with create operation of this database.
        """
        return pulumi.get(self, "source_database_id")

    @source_database_id.setter
    def source_database_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_database_id", value)

    @property
    @pulumi.getter(name="storageContainerSasToken")
    def storage_container_sas_token(self) -> Optional[pulumi.Input[str]]:
        """
        Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the storage container sas token.
        """
        return pulumi.get(self, "storage_container_sas_token")

    @storage_container_sas_token.setter
    def storage_container_sas_token(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_container_sas_token", value)

    @property
    @pulumi.getter(name="storageContainerUri")
    def storage_container_uri(self) -> Optional[pulumi.Input[str]]:
        """
        Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the uri of the storage container where backups for this restore are stored.
        """
        return pulumi.get(self, "storage_container_uri")

    @storage_container_uri.setter
    def storage_container_uri(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_container_uri", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ManagedDatabase(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_complete_restore: Optional[pulumi.Input[bool]] = None,
                 catalog_collation: Optional[pulumi.Input[Union[str, 'CatalogCollationType']]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'ManagedDatabaseCreateMode']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 last_backup_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 long_term_retention_backup_resource_id: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restorable_dropped_database_id: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 storage_container_sas_token: Optional[pulumi.Input[str]] = None,
                 storage_container_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        A managed database resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[bool] auto_complete_restore: Whether to auto complete restore of this managed database.
        :param pulumi.Input[Union[str, 'CatalogCollationType']] catalog_collation: Collation of the metadata catalog.
        :param pulumi.Input[str] collation: Collation of the managed database.
        :param pulumi.Input[Union[str, 'ManagedDatabaseCreateMode']] create_mode: Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required).
        :param pulumi.Input[str] database_name: The name of the database.
        :param pulumi.Input[str] last_backup_name: Last backup file name for restore of this managed database.
        :param pulumi.Input[str] location: Resource location.
        :param pulumi.Input[str] long_term_retention_backup_resource_id: The name of the Long Term Retention backup to be used for restore of this managed database.
        :param pulumi.Input[str] managed_instance_name: The name of the managed instance.
        :param pulumi.Input[str] recoverable_database_id: The resource identifier of the recoverable database associated with create operation of this database.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] restorable_dropped_database_id: The restorable dropped database resource id to restore when creating this database.
        :param pulumi.Input[str] restore_point_in_time: Conditional. If createMode is PointInTimeRestore, this value is required. Specifies the point in time (ISO8601 format) of the source database that will be restored to create the new database.
        :param pulumi.Input[str] source_database_id: The resource identifier of the source database associated with create operation of this database.
        :param pulumi.Input[str] storage_container_sas_token: Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the storage container sas token.
        :param pulumi.Input[str] storage_container_uri: Conditional. If createMode is RestoreExternalBackup, this value is required. Specifies the uri of the storage container where backups for this restore are stored.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ManagedDatabaseArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A managed database resource.

        :param str resource_name: The name of the resource.
        :param ManagedDatabaseArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagedDatabaseArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auto_complete_restore: Optional[pulumi.Input[bool]] = None,
                 catalog_collation: Optional[pulumi.Input[Union[str, 'CatalogCollationType']]] = None,
                 collation: Optional[pulumi.Input[str]] = None,
                 create_mode: Optional[pulumi.Input[Union[str, 'ManagedDatabaseCreateMode']]] = None,
                 database_name: Optional[pulumi.Input[str]] = None,
                 last_backup_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 long_term_retention_backup_resource_id: Optional[pulumi.Input[str]] = None,
                 managed_instance_name: Optional[pulumi.Input[str]] = None,
                 recoverable_database_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 restorable_dropped_database_id: Optional[pulumi.Input[str]] = None,
                 restore_point_in_time: Optional[pulumi.Input[str]] = None,
                 source_database_id: Optional[pulumi.Input[str]] = None,
                 storage_container_sas_token: Optional[pulumi.Input[str]] = None,
                 storage_container_uri: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagedDatabaseArgs.__new__(ManagedDatabaseArgs)

            __props__.__dict__["auto_complete_restore"] = auto_complete_restore
            __props__.__dict__["catalog_collation"] = catalog_collation
            __props__.__dict__["collation"] = collation
            __props__.__dict__["create_mode"] = create_mode
            __props__.__dict__["database_name"] = database_name
            __props__.__dict__["last_backup_name"] = last_backup_name
            __props__.__dict__["location"] = location
            __props__.__dict__["long_term_retention_backup_resource_id"] = long_term_retention_backup_resource_id
            if managed_instance_name is None and not opts.urn:
                raise TypeError("Missing required property 'managed_instance_name'")
            __props__.__dict__["managed_instance_name"] = managed_instance_name
            __props__.__dict__["recoverable_database_id"] = recoverable_database_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["restorable_dropped_database_id"] = restorable_dropped_database_id
            __props__.__dict__["restore_point_in_time"] = restore_point_in_time
            __props__.__dict__["source_database_id"] = source_database_id
            __props__.__dict__["storage_container_sas_token"] = storage_container_sas_token
            __props__.__dict__["storage_container_uri"] = storage_container_uri
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_date"] = None
            __props__.__dict__["default_secondary_location"] = None
            __props__.__dict__["earliest_restore_point"] = None
            __props__.__dict__["failover_group_id"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20170301preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20180601preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20190601preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20200801preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20210201preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20210801preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20211101:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20220201preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20220501preview:ManagedDatabase"), pulumi.Alias(type_="azure-native:sql/v20220801preview:ManagedDatabase")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagedDatabase, __self__).__init__(
            'azure-native:sql/v20211101preview:ManagedDatabase',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagedDatabase':
        """
        Get an existing ManagedDatabase resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagedDatabaseArgs.__new__(ManagedDatabaseArgs)

        __props__.__dict__["catalog_collation"] = None
        __props__.__dict__["collation"] = None
        __props__.__dict__["creation_date"] = None
        __props__.__dict__["default_secondary_location"] = None
        __props__.__dict__["earliest_restore_point"] = None
        __props__.__dict__["failover_group_id"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ManagedDatabase(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="catalogCollation")
    def catalog_collation(self) -> pulumi.Output[Optional[str]]:
        """
        Collation of the metadata catalog.
        """
        return pulumi.get(self, "catalog_collation")

    @property
    @pulumi.getter
    def collation(self) -> pulumi.Output[Optional[str]]:
        """
        Collation of the managed database.
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> pulumi.Output[str]:
        """
        Creation date of the database.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="defaultSecondaryLocation")
    def default_secondary_location(self) -> pulumi.Output[str]:
        """
        Geo paired region.
        """
        return pulumi.get(self, "default_secondary_location")

    @property
    @pulumi.getter(name="earliestRestorePoint")
    def earliest_restore_point(self) -> pulumi.Output[str]:
        """
        Earliest restore point in time for point in time restore.
        """
        return pulumi.get(self, "earliest_restore_point")

    @property
    @pulumi.getter(name="failoverGroupId")
    def failover_group_id(self) -> pulumi.Output[str]:
        """
        Instance Failover Group resource identifier that this managed database belongs to.
        """
        return pulumi.get(self, "failover_group_id")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        Status of the database.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

