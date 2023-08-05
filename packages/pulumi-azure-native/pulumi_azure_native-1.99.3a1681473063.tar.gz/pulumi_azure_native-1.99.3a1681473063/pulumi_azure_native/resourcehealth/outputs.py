# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'EventImpactedResourceResponse',
    'KeyValueItemResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class EventImpactedResourceResponse(dict):
    """
    Impacted resource for an event.
    """
    def __init__(__self__, *,
                 id: str,
                 name: str,
                 system_data: 'outputs.SystemDataResponse',
                 target_region: str,
                 target_resource_id: str,
                 target_resource_type: str,
                 type: str,
                 info: Optional[Sequence['outputs.KeyValueItemResponse']] = None):
        """
        Impacted resource for an event.
        :param str id: Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param str name: The name of the resource
        :param 'SystemDataResponse' system_data: Azure Resource Manager metadata containing createdBy and modifiedBy information.
        :param str target_region: Impacted resource region name.
        :param str target_resource_id: Identity for resource within Microsoft cloud.
        :param str target_resource_type: Resource type within Microsoft cloud.
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param Sequence['KeyValueItemResponse'] info: Additional information.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "system_data", system_data)
        pulumi.set(__self__, "target_region", target_region)
        pulumi.set(__self__, "target_resource_id", target_resource_id)
        pulumi.set(__self__, "target_resource_type", target_resource_type)
        pulumi.set(__self__, "type", type)
        if info is not None:
            pulumi.set(__self__, "info", info)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

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
    @pulumi.getter(name="targetRegion")
    def target_region(self) -> str:
        """
        Impacted resource region name.
        """
        return pulumi.get(self, "target_region")

    @property
    @pulumi.getter(name="targetResourceId")
    def target_resource_id(self) -> str:
        """
        Identity for resource within Microsoft cloud.
        """
        return pulumi.get(self, "target_resource_id")

    @property
    @pulumi.getter(name="targetResourceType")
    def target_resource_type(self) -> str:
        """
        Resource type within Microsoft cloud.
        """
        return pulumi.get(self, "target_resource_type")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def info(self) -> Optional[Sequence['outputs.KeyValueItemResponse']]:
        """
        Additional information.
        """
        return pulumi.get(self, "info")


@pulumi.output_type
class KeyValueItemResponse(dict):
    """
    Key value tuple.
    """
    def __init__(__self__, *,
                 key: str,
                 value: str):
        """
        Key value tuple.
        :param str key: Key of tuple.
        :param str value: Value of tuple.
        """
        pulumi.set(__self__, "key", key)
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def key(self) -> str:
        """
        Key of tuple.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def value(self) -> str:
        """
        Value of tuple.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


