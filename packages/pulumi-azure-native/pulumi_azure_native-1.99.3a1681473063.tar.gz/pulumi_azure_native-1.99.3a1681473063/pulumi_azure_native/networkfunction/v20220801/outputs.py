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
from ._enums import *

__all__ = [
    'CollectorPolicyResponse',
    'EmissionPoliciesPropertiesFormatResponse',
    'EmissionPolicyDestinationResponse',
    'IngestionPolicyPropertiesFormatResponse',
    'IngestionSourcesPropertiesFormatResponse',
    'ResourceReferenceResponse',
    'TrackedResourceResponseSystemData',
]

@pulumi.output_type
class CollectorPolicyResponse(dict):
    """
    Collector policy resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "systemData":
            suggest = "system_data"
        elif key == "emissionPolicies":
            suggest = "emission_policies"
        elif key == "ingestionPolicy":
            suggest = "ingestion_policy"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in CollectorPolicyResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        CollectorPolicyResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        CollectorPolicyResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 etag: str,
                 id: str,
                 name: str,
                 provisioning_state: str,
                 system_data: 'outputs.TrackedResourceResponseSystemData',
                 type: str,
                 emission_policies: Optional[Sequence['outputs.EmissionPoliciesPropertiesFormatResponse']] = None,
                 ingestion_policy: Optional['outputs.IngestionPolicyPropertiesFormatResponse'] = None,
                 location: Optional[str] = None,
                 tags: Optional[Mapping[str, str]] = None):
        """
        Collector policy resource.
        :param str etag: A unique read-only string that changes whenever the resource is updated.
        :param str id: Resource ID.
        :param str name: Resource name.
        :param str provisioning_state: The provisioning state.
        :param 'TrackedResourceResponseSystemData' system_data: Metadata pertaining to creation and last modification of the resource.
        :param str type: Resource type.
        :param Sequence['EmissionPoliciesPropertiesFormatResponse'] emission_policies: Emission policies.
        :param 'IngestionPolicyPropertiesFormatResponse' ingestion_policy: Ingestion policies.
        :param str location: Resource location.
        :param Mapping[str, str] tags: Resource tags.
        """
        pulumi.set(__self__, "etag", etag)
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "system_data", system_data)
        pulumi.set(__self__, "type", type)
        if emission_policies is not None:
            pulumi.set(__self__, "emission_policies", emission_policies)
        if ingestion_policy is not None:
            pulumi.set(__self__, "ingestion_policy", ingestion_policy)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def etag(self) -> str:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.TrackedResourceResponseSystemData':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="emissionPolicies")
    def emission_policies(self) -> Optional[Sequence['outputs.EmissionPoliciesPropertiesFormatResponse']]:
        """
        Emission policies.
        """
        return pulumi.get(self, "emission_policies")

    @property
    @pulumi.getter(name="ingestionPolicy")
    def ingestion_policy(self) -> Optional['outputs.IngestionPolicyPropertiesFormatResponse']:
        """
        Ingestion policies.
        """
        return pulumi.get(self, "ingestion_policy")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")


@pulumi.output_type
class EmissionPoliciesPropertiesFormatResponse(dict):
    """
    Emission policy properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "emissionDestinations":
            suggest = "emission_destinations"
        elif key == "emissionType":
            suggest = "emission_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EmissionPoliciesPropertiesFormatResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EmissionPoliciesPropertiesFormatResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EmissionPoliciesPropertiesFormatResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 emission_destinations: Optional[Sequence['outputs.EmissionPolicyDestinationResponse']] = None,
                 emission_type: Optional[str] = None):
        """
        Emission policy properties.
        :param Sequence['EmissionPolicyDestinationResponse'] emission_destinations: Emission policy destinations.
        :param str emission_type: Emission format type.
        """
        if emission_destinations is not None:
            pulumi.set(__self__, "emission_destinations", emission_destinations)
        if emission_type is not None:
            pulumi.set(__self__, "emission_type", emission_type)

    @property
    @pulumi.getter(name="emissionDestinations")
    def emission_destinations(self) -> Optional[Sequence['outputs.EmissionPolicyDestinationResponse']]:
        """
        Emission policy destinations.
        """
        return pulumi.get(self, "emission_destinations")

    @property
    @pulumi.getter(name="emissionType")
    def emission_type(self) -> Optional[str]:
        """
        Emission format type.
        """
        return pulumi.get(self, "emission_type")


@pulumi.output_type
class EmissionPolicyDestinationResponse(dict):
    """
    Emission policy destination properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "destinationType":
            suggest = "destination_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EmissionPolicyDestinationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EmissionPolicyDestinationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EmissionPolicyDestinationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 destination_type: Optional[str] = None):
        """
        Emission policy destination properties.
        :param str destination_type: Emission destination type.
        """
        if destination_type is not None:
            pulumi.set(__self__, "destination_type", destination_type)

    @property
    @pulumi.getter(name="destinationType")
    def destination_type(self) -> Optional[str]:
        """
        Emission destination type.
        """
        return pulumi.get(self, "destination_type")


@pulumi.output_type
class IngestionPolicyPropertiesFormatResponse(dict):
    """
    Ingestion Policy properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "ingestionSources":
            suggest = "ingestion_sources"
        elif key == "ingestionType":
            suggest = "ingestion_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IngestionPolicyPropertiesFormatResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IngestionPolicyPropertiesFormatResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IngestionPolicyPropertiesFormatResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 ingestion_sources: Optional[Sequence['outputs.IngestionSourcesPropertiesFormatResponse']] = None,
                 ingestion_type: Optional[str] = None):
        """
        Ingestion Policy properties.
        :param Sequence['IngestionSourcesPropertiesFormatResponse'] ingestion_sources: Ingestion Sources.
        :param str ingestion_type: The ingestion type.
        """
        if ingestion_sources is not None:
            pulumi.set(__self__, "ingestion_sources", ingestion_sources)
        if ingestion_type is not None:
            pulumi.set(__self__, "ingestion_type", ingestion_type)

    @property
    @pulumi.getter(name="ingestionSources")
    def ingestion_sources(self) -> Optional[Sequence['outputs.IngestionSourcesPropertiesFormatResponse']]:
        """
        Ingestion Sources.
        """
        return pulumi.get(self, "ingestion_sources")

    @property
    @pulumi.getter(name="ingestionType")
    def ingestion_type(self) -> Optional[str]:
        """
        The ingestion type.
        """
        return pulumi.get(self, "ingestion_type")


@pulumi.output_type
class IngestionSourcesPropertiesFormatResponse(dict):
    """
    Ingestion policy properties.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceId":
            suggest = "resource_id"
        elif key == "sourceType":
            suggest = "source_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in IngestionSourcesPropertiesFormatResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        IngestionSourcesPropertiesFormatResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        IngestionSourcesPropertiesFormatResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 resource_id: Optional[str] = None,
                 source_type: Optional[str] = None):
        """
        Ingestion policy properties.
        :param str resource_id: Resource ID.
        :param str source_type: Ingestion source type.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if source_type is not None:
            pulumi.set(__self__, "source_type", source_type)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[str]:
        """
        Resource ID.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[str]:
        """
        Ingestion source type.
        """
        return pulumi.get(self, "source_type")


@pulumi.output_type
class ResourceReferenceResponse(dict):
    """
    Resource reference properties.
    """
    def __init__(__self__, *,
                 id: str):
        """
        Resource reference properties.
        :param str id: Resource ID.
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class TrackedResourceResponseSystemData(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in TrackedResourceResponseSystemData. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        TrackedResourceResponseSystemData.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        TrackedResourceResponseSystemData.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
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


