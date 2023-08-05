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
    'GetClusterResult',
    'AwaitableGetClusterResult',
    'get_cluster',
    'get_cluster_output',
]

@pulumi.output_type
class GetClusterResult:
    """
    Cluster details.
    """
    def __init__(__self__, aad_application_object_id=None, aad_client_id=None, aad_service_principal_object_id=None, aad_tenant_id=None, billing_model=None, cloud_id=None, cloud_management_endpoint=None, desired_properties=None, id=None, last_billing_timestamp=None, last_sync_timestamp=None, location=None, name=None, principal_id=None, provisioning_state=None, registration_timestamp=None, reported_properties=None, resource_provider_object_id=None, service_endpoint=None, software_assurance_properties=None, status=None, system_data=None, tags=None, tenant_id=None, trial_days_remaining=None, type=None, user_assigned_identities=None):
        if aad_application_object_id and not isinstance(aad_application_object_id, str):
            raise TypeError("Expected argument 'aad_application_object_id' to be a str")
        pulumi.set(__self__, "aad_application_object_id", aad_application_object_id)
        if aad_client_id and not isinstance(aad_client_id, str):
            raise TypeError("Expected argument 'aad_client_id' to be a str")
        pulumi.set(__self__, "aad_client_id", aad_client_id)
        if aad_service_principal_object_id and not isinstance(aad_service_principal_object_id, str):
            raise TypeError("Expected argument 'aad_service_principal_object_id' to be a str")
        pulumi.set(__self__, "aad_service_principal_object_id", aad_service_principal_object_id)
        if aad_tenant_id and not isinstance(aad_tenant_id, str):
            raise TypeError("Expected argument 'aad_tenant_id' to be a str")
        pulumi.set(__self__, "aad_tenant_id", aad_tenant_id)
        if billing_model and not isinstance(billing_model, str):
            raise TypeError("Expected argument 'billing_model' to be a str")
        pulumi.set(__self__, "billing_model", billing_model)
        if cloud_id and not isinstance(cloud_id, str):
            raise TypeError("Expected argument 'cloud_id' to be a str")
        pulumi.set(__self__, "cloud_id", cloud_id)
        if cloud_management_endpoint and not isinstance(cloud_management_endpoint, str):
            raise TypeError("Expected argument 'cloud_management_endpoint' to be a str")
        pulumi.set(__self__, "cloud_management_endpoint", cloud_management_endpoint)
        if desired_properties and not isinstance(desired_properties, dict):
            raise TypeError("Expected argument 'desired_properties' to be a dict")
        pulumi.set(__self__, "desired_properties", desired_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_billing_timestamp and not isinstance(last_billing_timestamp, str):
            raise TypeError("Expected argument 'last_billing_timestamp' to be a str")
        pulumi.set(__self__, "last_billing_timestamp", last_billing_timestamp)
        if last_sync_timestamp and not isinstance(last_sync_timestamp, str):
            raise TypeError("Expected argument 'last_sync_timestamp' to be a str")
        pulumi.set(__self__, "last_sync_timestamp", last_sync_timestamp)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if principal_id and not isinstance(principal_id, str):
            raise TypeError("Expected argument 'principal_id' to be a str")
        pulumi.set(__self__, "principal_id", principal_id)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if registration_timestamp and not isinstance(registration_timestamp, str):
            raise TypeError("Expected argument 'registration_timestamp' to be a str")
        pulumi.set(__self__, "registration_timestamp", registration_timestamp)
        if reported_properties and not isinstance(reported_properties, dict):
            raise TypeError("Expected argument 'reported_properties' to be a dict")
        pulumi.set(__self__, "reported_properties", reported_properties)
        if resource_provider_object_id and not isinstance(resource_provider_object_id, str):
            raise TypeError("Expected argument 'resource_provider_object_id' to be a str")
        pulumi.set(__self__, "resource_provider_object_id", resource_provider_object_id)
        if service_endpoint and not isinstance(service_endpoint, str):
            raise TypeError("Expected argument 'service_endpoint' to be a str")
        pulumi.set(__self__, "service_endpoint", service_endpoint)
        if software_assurance_properties and not isinstance(software_assurance_properties, dict):
            raise TypeError("Expected argument 'software_assurance_properties' to be a dict")
        pulumi.set(__self__, "software_assurance_properties", software_assurance_properties)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if trial_days_remaining and not isinstance(trial_days_remaining, float):
            raise TypeError("Expected argument 'trial_days_remaining' to be a float")
        pulumi.set(__self__, "trial_days_remaining", trial_days_remaining)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_assigned_identities and not isinstance(user_assigned_identities, dict):
            raise TypeError("Expected argument 'user_assigned_identities' to be a dict")
        pulumi.set(__self__, "user_assigned_identities", user_assigned_identities)

    @property
    @pulumi.getter(name="aadApplicationObjectId")
    def aad_application_object_id(self) -> Optional[str]:
        """
        Object id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_application_object_id")

    @property
    @pulumi.getter(name="aadClientId")
    def aad_client_id(self) -> Optional[str]:
        """
        App id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_client_id")

    @property
    @pulumi.getter(name="aadServicePrincipalObjectId")
    def aad_service_principal_object_id(self) -> Optional[str]:
        """
        Id of cluster identity service principal.
        """
        return pulumi.get(self, "aad_service_principal_object_id")

    @property
    @pulumi.getter(name="aadTenantId")
    def aad_tenant_id(self) -> Optional[str]:
        """
        Tenant id of cluster AAD identity.
        """
        return pulumi.get(self, "aad_tenant_id")

    @property
    @pulumi.getter(name="billingModel")
    def billing_model(self) -> str:
        """
        Type of billing applied to the resource.
        """
        return pulumi.get(self, "billing_model")

    @property
    @pulumi.getter(name="cloudId")
    def cloud_id(self) -> str:
        """
        Unique, immutable resource id.
        """
        return pulumi.get(self, "cloud_id")

    @property
    @pulumi.getter(name="cloudManagementEndpoint")
    def cloud_management_endpoint(self) -> Optional[str]:
        """
        Endpoint configured for management from the Azure portal.
        """
        return pulumi.get(self, "cloud_management_endpoint")

    @property
    @pulumi.getter(name="desiredProperties")
    def desired_properties(self) -> Optional['outputs.ClusterDesiredPropertiesResponse']:
        """
        Desired properties of the cluster.
        """
        return pulumi.get(self, "desired_properties")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastBillingTimestamp")
    def last_billing_timestamp(self) -> str:
        """
        Most recent billing meter timestamp.
        """
        return pulumi.get(self, "last_billing_timestamp")

    @property
    @pulumi.getter(name="lastSyncTimestamp")
    def last_sync_timestamp(self) -> str:
        """
        Most recent cluster sync timestamp.
        """
        return pulumi.get(self, "last_sync_timestamp")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The service principal ID of the system assigned identity. This property will only be provided for a system assigned identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="registrationTimestamp")
    def registration_timestamp(self) -> str:
        """
        First cluster sync timestamp.
        """
        return pulumi.get(self, "registration_timestamp")

    @property
    @pulumi.getter(name="reportedProperties")
    def reported_properties(self) -> 'outputs.ClusterReportedPropertiesResponse':
        """
        Properties reported by cluster agent.
        """
        return pulumi.get(self, "reported_properties")

    @property
    @pulumi.getter(name="resourceProviderObjectId")
    def resource_provider_object_id(self) -> str:
        """
        Object id of RP Service Principal
        """
        return pulumi.get(self, "resource_provider_object_id")

    @property
    @pulumi.getter(name="serviceEndpoint")
    def service_endpoint(self) -> str:
        """
        Region specific DataPath Endpoint of the cluster.
        """
        return pulumi.get(self, "service_endpoint")

    @property
    @pulumi.getter(name="softwareAssuranceProperties")
    def software_assurance_properties(self) -> Optional['outputs.SoftwareAssurancePropertiesResponse']:
        """
        Software Assurance properties of the cluster.
        """
        return pulumi.get(self, "software_assurance_properties")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        Status of the cluster agent.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the system assigned identity. This property will only be provided for a system assigned identity.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="trialDaysRemaining")
    def trial_days_remaining(self) -> float:
        """
        Number of days remaining in the trial period.
        """
        return pulumi.get(self, "trial_days_remaining")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userAssignedIdentities")
    def user_assigned_identities(self) -> Optional[Mapping[str, 'outputs.UserAssignedIdentityResponse']]:
        """
        The set of user assigned identities associated with the resource. The userAssignedIdentities dictionary keys will be ARM resource ids in the form: '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}. The dictionary values can be empty objects ({}) in requests.
        """
        return pulumi.get(self, "user_assigned_identities")


class AwaitableGetClusterResult(GetClusterResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetClusterResult(
            aad_application_object_id=self.aad_application_object_id,
            aad_client_id=self.aad_client_id,
            aad_service_principal_object_id=self.aad_service_principal_object_id,
            aad_tenant_id=self.aad_tenant_id,
            billing_model=self.billing_model,
            cloud_id=self.cloud_id,
            cloud_management_endpoint=self.cloud_management_endpoint,
            desired_properties=self.desired_properties,
            id=self.id,
            last_billing_timestamp=self.last_billing_timestamp,
            last_sync_timestamp=self.last_sync_timestamp,
            location=self.location,
            name=self.name,
            principal_id=self.principal_id,
            provisioning_state=self.provisioning_state,
            registration_timestamp=self.registration_timestamp,
            reported_properties=self.reported_properties,
            resource_provider_object_id=self.resource_provider_object_id,
            service_endpoint=self.service_endpoint,
            software_assurance_properties=self.software_assurance_properties,
            status=self.status,
            system_data=self.system_data,
            tags=self.tags,
            tenant_id=self.tenant_id,
            trial_days_remaining=self.trial_days_remaining,
            type=self.type,
            user_assigned_identities=self.user_assigned_identities)


def get_cluster(cluster_name: Optional[str] = None,
                resource_group_name: Optional[str] = None,
                opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetClusterResult:
    """
    Get HCI cluster.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20221201:getCluster', __args__, opts=opts, typ=GetClusterResult).value

    return AwaitableGetClusterResult(
        aad_application_object_id=__ret__.aad_application_object_id,
        aad_client_id=__ret__.aad_client_id,
        aad_service_principal_object_id=__ret__.aad_service_principal_object_id,
        aad_tenant_id=__ret__.aad_tenant_id,
        billing_model=__ret__.billing_model,
        cloud_id=__ret__.cloud_id,
        cloud_management_endpoint=__ret__.cloud_management_endpoint,
        desired_properties=__ret__.desired_properties,
        id=__ret__.id,
        last_billing_timestamp=__ret__.last_billing_timestamp,
        last_sync_timestamp=__ret__.last_sync_timestamp,
        location=__ret__.location,
        name=__ret__.name,
        principal_id=__ret__.principal_id,
        provisioning_state=__ret__.provisioning_state,
        registration_timestamp=__ret__.registration_timestamp,
        reported_properties=__ret__.reported_properties,
        resource_provider_object_id=__ret__.resource_provider_object_id,
        service_endpoint=__ret__.service_endpoint,
        software_assurance_properties=__ret__.software_assurance_properties,
        status=__ret__.status,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        tenant_id=__ret__.tenant_id,
        trial_days_remaining=__ret__.trial_days_remaining,
        type=__ret__.type,
        user_assigned_identities=__ret__.user_assigned_identities)


@_utilities.lift_output_func(get_cluster)
def get_cluster_output(cluster_name: Optional[pulumi.Input[str]] = None,
                       resource_group_name: Optional[pulumi.Input[str]] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetClusterResult]:
    """
    Get HCI cluster.


    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
