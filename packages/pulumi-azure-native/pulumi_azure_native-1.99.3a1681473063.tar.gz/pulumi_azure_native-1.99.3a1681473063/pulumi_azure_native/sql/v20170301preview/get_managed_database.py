# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetManagedDatabaseResult',
    'AwaitableGetManagedDatabaseResult',
    'get_managed_database',
    'get_managed_database_output',
]

@pulumi.output_type
class GetManagedDatabaseResult:
    """
    A managed database resource.
    """
    def __init__(__self__, catalog_collation=None, collation=None, creation_date=None, default_secondary_location=None, earliest_restore_point=None, failover_group_id=None, id=None, location=None, name=None, status=None, tags=None, type=None):
        if catalog_collation and not isinstance(catalog_collation, str):
            raise TypeError("Expected argument 'catalog_collation' to be a str")
        pulumi.set(__self__, "catalog_collation", catalog_collation)
        if collation and not isinstance(collation, str):
            raise TypeError("Expected argument 'collation' to be a str")
        pulumi.set(__self__, "collation", collation)
        if creation_date and not isinstance(creation_date, str):
            raise TypeError("Expected argument 'creation_date' to be a str")
        pulumi.set(__self__, "creation_date", creation_date)
        if default_secondary_location and not isinstance(default_secondary_location, str):
            raise TypeError("Expected argument 'default_secondary_location' to be a str")
        pulumi.set(__self__, "default_secondary_location", default_secondary_location)
        if earliest_restore_point and not isinstance(earliest_restore_point, str):
            raise TypeError("Expected argument 'earliest_restore_point' to be a str")
        pulumi.set(__self__, "earliest_restore_point", earliest_restore_point)
        if failover_group_id and not isinstance(failover_group_id, str):
            raise TypeError("Expected argument 'failover_group_id' to be a str")
        pulumi.set(__self__, "failover_group_id", failover_group_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="catalogCollation")
    def catalog_collation(self) -> Optional[str]:
        """
        Collation of the metadata catalog.
        """
        return pulumi.get(self, "catalog_collation")

    @property
    @pulumi.getter
    def collation(self) -> Optional[str]:
        """
        Collation of the managed database.
        """
        return pulumi.get(self, "collation")

    @property
    @pulumi.getter(name="creationDate")
    def creation_date(self) -> str:
        """
        Creation date of the database.
        """
        return pulumi.get(self, "creation_date")

    @property
    @pulumi.getter(name="defaultSecondaryLocation")
    def default_secondary_location(self) -> str:
        """
        Geo paired region.
        """
        return pulumi.get(self, "default_secondary_location")

    @property
    @pulumi.getter(name="earliestRestorePoint")
    def earliest_restore_point(self) -> str:
        """
        Earliest restore point in time for point in time restore.
        """
        return pulumi.get(self, "earliest_restore_point")

    @property
    @pulumi.getter(name="failoverGroupId")
    def failover_group_id(self) -> str:
        """
        Instance Failover Group resource identifier that this managed database belongs to.
        """
        return pulumi.get(self, "failover_group_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the database.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedDatabaseResult(GetManagedDatabaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedDatabaseResult(
            catalog_collation=self.catalog_collation,
            collation=self.collation,
            creation_date=self.creation_date,
            default_secondary_location=self.default_secondary_location,
            earliest_restore_point=self.earliest_restore_point,
            failover_group_id=self.failover_group_id,
            id=self.id,
            location=self.location,
            name=self.name,
            status=self.status,
            tags=self.tags,
            type=self.type)


def get_managed_database(database_name: Optional[str] = None,
                         managed_instance_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedDatabaseResult:
    """
    Gets a managed database.


    :param str database_name: The name of the database.
    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['databaseName'] = database_name
    __args__['managedInstanceName'] = managed_instance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20170301preview:getManagedDatabase', __args__, opts=opts, typ=GetManagedDatabaseResult).value

    return AwaitableGetManagedDatabaseResult(
        catalog_collation=__ret__.catalog_collation,
        collation=__ret__.collation,
        creation_date=__ret__.creation_date,
        default_secondary_location=__ret__.default_secondary_location,
        earliest_restore_point=__ret__.earliest_restore_point,
        failover_group_id=__ret__.failover_group_id,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        status=__ret__.status,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_managed_database)
def get_managed_database_output(database_name: Optional[pulumi.Input[str]] = None,
                                managed_instance_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedDatabaseResult]:
    """
    Gets a managed database.


    :param str database_name: The name of the database.
    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
