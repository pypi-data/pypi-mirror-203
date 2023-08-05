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
    'GetIncidentRelationResult',
    'AwaitableGetIncidentRelationResult',
    'get_incident_relation',
    'get_incident_relation_output',
]

@pulumi.output_type
class GetIncidentRelationResult:
    """
    Represents a relation between two resources
    """
    def __init__(__self__, etag=None, id=None, name=None, related_resource_id=None, related_resource_kind=None, related_resource_name=None, related_resource_type=None, system_data=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if related_resource_id and not isinstance(related_resource_id, str):
            raise TypeError("Expected argument 'related_resource_id' to be a str")
        pulumi.set(__self__, "related_resource_id", related_resource_id)
        if related_resource_kind and not isinstance(related_resource_kind, str):
            raise TypeError("Expected argument 'related_resource_kind' to be a str")
        pulumi.set(__self__, "related_resource_kind", related_resource_kind)
        if related_resource_name and not isinstance(related_resource_name, str):
            raise TypeError("Expected argument 'related_resource_name' to be a str")
        pulumi.set(__self__, "related_resource_name", related_resource_name)
        if related_resource_type and not isinstance(related_resource_type, str):
            raise TypeError("Expected argument 'related_resource_type' to be a str")
        pulumi.set(__self__, "related_resource_type", related_resource_type)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="relatedResourceId")
    def related_resource_id(self) -> str:
        """
        The resource ID of the related resource
        """
        return pulumi.get(self, "related_resource_id")

    @property
    @pulumi.getter(name="relatedResourceKind")
    def related_resource_kind(self) -> str:
        """
        The resource kind of the related resource
        """
        return pulumi.get(self, "related_resource_kind")

    @property
    @pulumi.getter(name="relatedResourceName")
    def related_resource_name(self) -> str:
        """
        The name of the related resource
        """
        return pulumi.get(self, "related_resource_name")

    @property
    @pulumi.getter(name="relatedResourceType")
    def related_resource_type(self) -> str:
        """
        The resource type of the related resource
        """
        return pulumi.get(self, "related_resource_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetIncidentRelationResult(GetIncidentRelationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIncidentRelationResult(
            etag=self.etag,
            id=self.id,
            name=self.name,
            related_resource_id=self.related_resource_id,
            related_resource_kind=self.related_resource_kind,
            related_resource_name=self.related_resource_name,
            related_resource_type=self.related_resource_type,
            system_data=self.system_data,
            type=self.type)


def get_incident_relation(incident_id: Optional[str] = None,
                          relation_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          workspace_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIncidentRelationResult:
    """
    Gets an incident relation.


    :param str incident_id: Incident ID
    :param str relation_name: Relation Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['incidentId'] = incident_id
    __args__['relationName'] = relation_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20221001preview:getIncidentRelation', __args__, opts=opts, typ=GetIncidentRelationResult).value

    return AwaitableGetIncidentRelationResult(
        etag=__ret__.etag,
        id=__ret__.id,
        name=__ret__.name,
        related_resource_id=__ret__.related_resource_id,
        related_resource_kind=__ret__.related_resource_kind,
        related_resource_name=__ret__.related_resource_name,
        related_resource_type=__ret__.related_resource_type,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_incident_relation)
def get_incident_relation_output(incident_id: Optional[pulumi.Input[str]] = None,
                                 relation_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 workspace_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIncidentRelationResult]:
    """
    Gets an incident relation.


    :param str incident_id: Incident ID
    :param str relation_name: Relation Name
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
