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
    'GetWatchlistItemResult',
    'AwaitableGetWatchlistItemResult',
    'get_watchlist_item',
    'get_watchlist_item_output',
]

@pulumi.output_type
class GetWatchlistItemResult:
    """
    Represents a Watchlist item in Azure Security Insights.
    """
    def __init__(__self__, created=None, created_by=None, entity_mapping=None, etag=None, id=None, is_deleted=None, items_key_value=None, name=None, system_data=None, tenant_id=None, type=None, updated=None, updated_by=None, watchlist_item_id=None, watchlist_item_type=None):
        if created and not isinstance(created, str):
            raise TypeError("Expected argument 'created' to be a str")
        pulumi.set(__self__, "created", created)
        if created_by and not isinstance(created_by, dict):
            raise TypeError("Expected argument 'created_by' to be a dict")
        pulumi.set(__self__, "created_by", created_by)
        if entity_mapping and not isinstance(entity_mapping, dict):
            raise TypeError("Expected argument 'entity_mapping' to be a dict")
        pulumi.set(__self__, "entity_mapping", entity_mapping)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_deleted and not isinstance(is_deleted, bool):
            raise TypeError("Expected argument 'is_deleted' to be a bool")
        pulumi.set(__self__, "is_deleted", is_deleted)
        if items_key_value and not isinstance(items_key_value, dict):
            raise TypeError("Expected argument 'items_key_value' to be a dict")
        pulumi.set(__self__, "items_key_value", items_key_value)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated and not isinstance(updated, str):
            raise TypeError("Expected argument 'updated' to be a str")
        pulumi.set(__self__, "updated", updated)
        if updated_by and not isinstance(updated_by, dict):
            raise TypeError("Expected argument 'updated_by' to be a dict")
        pulumi.set(__self__, "updated_by", updated_by)
        if watchlist_item_id and not isinstance(watchlist_item_id, str):
            raise TypeError("Expected argument 'watchlist_item_id' to be a str")
        pulumi.set(__self__, "watchlist_item_id", watchlist_item_id)
        if watchlist_item_type and not isinstance(watchlist_item_type, str):
            raise TypeError("Expected argument 'watchlist_item_type' to be a str")
        pulumi.set(__self__, "watchlist_item_type", watchlist_item_type)

    @property
    @pulumi.getter
    def created(self) -> Optional[str]:
        """
        The time the watchlist item was created
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional['outputs.WatchlistUserInfoResponse']:
        """
        Describes a user that created the watchlist item
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="entityMapping")
    def entity_mapping(self) -> Optional[Any]:
        """
        key-value pairs for a watchlist item entity mapping
        """
        return pulumi.get(self, "entity_mapping")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isDeleted")
    def is_deleted(self) -> Optional[bool]:
        """
        A flag that indicates if the watchlist item is deleted or not
        """
        return pulumi.get(self, "is_deleted")

    @property
    @pulumi.getter(name="itemsKeyValue")
    def items_key_value(self) -> Any:
        """
        key-value pairs for a watchlist item
        """
        return pulumi.get(self, "items_key_value")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        The tenantId to which the watchlist item belongs to
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def updated(self) -> Optional[str]:
        """
        The last time the watchlist item was updated
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter(name="updatedBy")
    def updated_by(self) -> Optional['outputs.WatchlistUserInfoResponse']:
        """
        Describes a user that updated the watchlist item
        """
        return pulumi.get(self, "updated_by")

    @property
    @pulumi.getter(name="watchlistItemId")
    def watchlist_item_id(self) -> Optional[str]:
        """
        The id (a Guid) of the watchlist item
        """
        return pulumi.get(self, "watchlist_item_id")

    @property
    @pulumi.getter(name="watchlistItemType")
    def watchlist_item_type(self) -> Optional[str]:
        """
        The type of the watchlist item
        """
        return pulumi.get(self, "watchlist_item_type")


class AwaitableGetWatchlistItemResult(GetWatchlistItemResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetWatchlistItemResult(
            created=self.created,
            created_by=self.created_by,
            entity_mapping=self.entity_mapping,
            etag=self.etag,
            id=self.id,
            is_deleted=self.is_deleted,
            items_key_value=self.items_key_value,
            name=self.name,
            system_data=self.system_data,
            tenant_id=self.tenant_id,
            type=self.type,
            updated=self.updated,
            updated_by=self.updated_by,
            watchlist_item_id=self.watchlist_item_id,
            watchlist_item_type=self.watchlist_item_type)


def get_watchlist_item(resource_group_name: Optional[str] = None,
                       watchlist_alias: Optional[str] = None,
                       watchlist_item_id: Optional[str] = None,
                       workspace_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetWatchlistItemResult:
    """
    Gets a watchlist, without its watchlist items.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str watchlist_alias: Watchlist Alias
    :param str watchlist_item_id: Watchlist Item Id (GUID)
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['watchlistAlias'] = watchlist_alias
    __args__['watchlistItemId'] = watchlist_item_id
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20220901preview:getWatchlistItem', __args__, opts=opts, typ=GetWatchlistItemResult).value

    return AwaitableGetWatchlistItemResult(
        created=__ret__.created,
        created_by=__ret__.created_by,
        entity_mapping=__ret__.entity_mapping,
        etag=__ret__.etag,
        id=__ret__.id,
        is_deleted=__ret__.is_deleted,
        items_key_value=__ret__.items_key_value,
        name=__ret__.name,
        system_data=__ret__.system_data,
        tenant_id=__ret__.tenant_id,
        type=__ret__.type,
        updated=__ret__.updated,
        updated_by=__ret__.updated_by,
        watchlist_item_id=__ret__.watchlist_item_id,
        watchlist_item_type=__ret__.watchlist_item_type)


@_utilities.lift_output_func(get_watchlist_item)
def get_watchlist_item_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                              watchlist_alias: Optional[pulumi.Input[str]] = None,
                              watchlist_item_id: Optional[pulumi.Input[str]] = None,
                              workspace_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetWatchlistItemResult]:
    """
    Gets a watchlist, without its watchlist items.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str watchlist_alias: Watchlist Alias
    :param str watchlist_item_id: Watchlist Item Id (GUID)
    :param str workspace_name: The name of the workspace.
    """
    ...
