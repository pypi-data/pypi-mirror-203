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
    'GetRelationshipResult',
    'AwaitableGetRelationshipResult',
    'get_relationship',
    'get_relationship_output',
]

@pulumi.output_type
class GetRelationshipResult:
    """
    The relationship resource format.
    """
    def __init__(__self__, cardinality=None, description=None, display_name=None, expiry_date_time_utc=None, fields=None, id=None, lookup_mappings=None, name=None, profile_type=None, provisioning_state=None, related_profile_type=None, relationship_guid_id=None, relationship_name=None, tenant_id=None, type=None):
        if cardinality and not isinstance(cardinality, str):
            raise TypeError("Expected argument 'cardinality' to be a str")
        pulumi.set(__self__, "cardinality", cardinality)
        if description and not isinstance(description, dict):
            raise TypeError("Expected argument 'description' to be a dict")
        pulumi.set(__self__, "description", description)
        if display_name and not isinstance(display_name, dict):
            raise TypeError("Expected argument 'display_name' to be a dict")
        pulumi.set(__self__, "display_name", display_name)
        if expiry_date_time_utc and not isinstance(expiry_date_time_utc, str):
            raise TypeError("Expected argument 'expiry_date_time_utc' to be a str")
        pulumi.set(__self__, "expiry_date_time_utc", expiry_date_time_utc)
        if fields and not isinstance(fields, list):
            raise TypeError("Expected argument 'fields' to be a list")
        pulumi.set(__self__, "fields", fields)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if lookup_mappings and not isinstance(lookup_mappings, list):
            raise TypeError("Expected argument 'lookup_mappings' to be a list")
        pulumi.set(__self__, "lookup_mappings", lookup_mappings)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if profile_type and not isinstance(profile_type, str):
            raise TypeError("Expected argument 'profile_type' to be a str")
        pulumi.set(__self__, "profile_type", profile_type)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if related_profile_type and not isinstance(related_profile_type, str):
            raise TypeError("Expected argument 'related_profile_type' to be a str")
        pulumi.set(__self__, "related_profile_type", related_profile_type)
        if relationship_guid_id and not isinstance(relationship_guid_id, str):
            raise TypeError("Expected argument 'relationship_guid_id' to be a str")
        pulumi.set(__self__, "relationship_guid_id", relationship_guid_id)
        if relationship_name and not isinstance(relationship_name, str):
            raise TypeError("Expected argument 'relationship_name' to be a str")
        pulumi.set(__self__, "relationship_name", relationship_name)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def cardinality(self) -> Optional[str]:
        """
        The Relationship Cardinality.
        """
        return pulumi.get(self, "cardinality")

    @property
    @pulumi.getter
    def description(self) -> Optional[Mapping[str, str]]:
        """
        Localized descriptions for the Relationship.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[Mapping[str, str]]:
        """
        Localized display name for the Relationship.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="expiryDateTimeUtc")
    def expiry_date_time_utc(self) -> Optional[str]:
        """
        The expiry date time in UTC.
        """
        return pulumi.get(self, "expiry_date_time_utc")

    @property
    @pulumi.getter
    def fields(self) -> Optional[Sequence['outputs.PropertyDefinitionResponse']]:
        """
        The properties of the Relationship.
        """
        return pulumi.get(self, "fields")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lookupMappings")
    def lookup_mappings(self) -> Optional[Sequence['outputs.RelationshipTypeMappingResponse']]:
        """
        Optional property to be used to map fields in profile to their strong ids in related profile.
        """
        return pulumi.get(self, "lookup_mappings")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="profileType")
    def profile_type(self) -> str:
        """
        Profile type.
        """
        return pulumi.get(self, "profile_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="relatedProfileType")
    def related_profile_type(self) -> str:
        """
        Related profile being referenced.
        """
        return pulumi.get(self, "related_profile_type")

    @property
    @pulumi.getter(name="relationshipGuidId")
    def relationship_guid_id(self) -> str:
        """
        The relationship guid id.
        """
        return pulumi.get(self, "relationship_guid_id")

    @property
    @pulumi.getter(name="relationshipName")
    def relationship_name(self) -> str:
        """
        The Relationship name.
        """
        return pulumi.get(self, "relationship_name")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The hub name.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetRelationshipResult(GetRelationshipResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRelationshipResult(
            cardinality=self.cardinality,
            description=self.description,
            display_name=self.display_name,
            expiry_date_time_utc=self.expiry_date_time_utc,
            fields=self.fields,
            id=self.id,
            lookup_mappings=self.lookup_mappings,
            name=self.name,
            profile_type=self.profile_type,
            provisioning_state=self.provisioning_state,
            related_profile_type=self.related_profile_type,
            relationship_guid_id=self.relationship_guid_id,
            relationship_name=self.relationship_name,
            tenant_id=self.tenant_id,
            type=self.type)


def get_relationship(hub_name: Optional[str] = None,
                     relationship_name: Optional[str] = None,
                     resource_group_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRelationshipResult:
    """
    Gets information about the specified relationship.


    :param str hub_name: The name of the hub.
    :param str relationship_name: The name of the relationship.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['hubName'] = hub_name
    __args__['relationshipName'] = relationship_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:customerinsights/v20170426:getRelationship', __args__, opts=opts, typ=GetRelationshipResult).value

    return AwaitableGetRelationshipResult(
        cardinality=__ret__.cardinality,
        description=__ret__.description,
        display_name=__ret__.display_name,
        expiry_date_time_utc=__ret__.expiry_date_time_utc,
        fields=__ret__.fields,
        id=__ret__.id,
        lookup_mappings=__ret__.lookup_mappings,
        name=__ret__.name,
        profile_type=__ret__.profile_type,
        provisioning_state=__ret__.provisioning_state,
        related_profile_type=__ret__.related_profile_type,
        relationship_guid_id=__ret__.relationship_guid_id,
        relationship_name=__ret__.relationship_name,
        tenant_id=__ret__.tenant_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_relationship)
def get_relationship_output(hub_name: Optional[pulumi.Input[str]] = None,
                            relationship_name: Optional[pulumi.Input[str]] = None,
                            resource_group_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRelationshipResult]:
    """
    Gets information about the specified relationship.


    :param str hub_name: The name of the hub.
    :param str relationship_name: The name of the relationship.
    :param str resource_group_name: The name of the resource group.
    """
    ...
