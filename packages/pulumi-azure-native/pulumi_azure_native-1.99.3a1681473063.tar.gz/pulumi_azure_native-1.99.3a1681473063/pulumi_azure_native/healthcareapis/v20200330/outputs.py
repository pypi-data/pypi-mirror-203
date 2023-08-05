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
    'PrivateEndpointConnectionResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'ServiceAccessPolicyEntryResponse',
    'ServiceAuthenticationConfigurationInfoResponse',
    'ServiceCorsConfigurationInfoResponse',
    'ServiceCosmosDbConfigurationInfoResponse',
    'ServiceExportConfigurationInfoResponse',
    'ServicesPropertiesResponse',
    'ServicesResourceResponseIdentity',
]

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    The Private Endpoint Connection resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"
        elif key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "privateEndpoint":
            suggest = "private_endpoint"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 name: str,
                 private_link_service_connection_state: 'outputs.PrivateLinkServiceConnectionStateResponse',
                 provisioning_state: str,
                 type: str,
                 private_endpoint: Optional['outputs.PrivateEndpointResponse'] = None):
        """
        The Private Endpoint Connection resource.
        :param str id: Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        :param str name: The name of the resource
        :param 'PrivateLinkServiceConnectionStateResponse' private_link_service_connection_state: A collection of information about the state of the connection between service consumer and provider.
        :param str provisioning_state: The provisioning state of the private endpoint connection resource.
        :param str type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        :param 'PrivateEndpointResponse' private_endpoint: The resource of private end point.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "type", type)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)

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
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> 'outputs.PrivateLinkServiceConnectionStateResponse':
        """
        A collection of information about the state of the connection between service consumer and provider.
        """
        return pulumi.get(self, "private_link_service_connection_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the private endpoint connection resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointResponse']:
        """
        The resource of private end point.
        """
        return pulumi.get(self, "private_endpoint")


@pulumi.output_type
class PrivateEndpointResponse(dict):
    """
    The Private Endpoint resource.
    """
    def __init__(__self__, *,
                 id: str):
        """
        The Private Endpoint resource.
        :param str id: The ARM identifier for Private Endpoint
        """
        pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The ARM identifier for Private Endpoint
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStateResponse(dict):
    """
    A collection of information about the state of the connection between service consumer and provider.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStateResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStateResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: Optional[str] = None,
                 description: Optional[str] = None,
                 status: Optional[str] = None):
        """
        A collection of information about the state of the connection between service consumer and provider.
        :param str actions_required: A message indicating if changes on the service provider require any updates on the consumer.
        :param str description: The reason for approval/rejection of the connection.
        :param str status: Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        if actions_required is not None:
            pulumi.set(__self__, "actions_required", actions_required)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> Optional[str]:
        """
        A message indicating if changes on the service provider require any updates on the consumer.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The reason for approval/rejection of the connection.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates whether the connection has been Approved/Rejected/Removed by the owner of the service.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class ServiceAccessPolicyEntryResponse(dict):
    """
    An access policy entry.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "objectId":
            suggest = "object_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceAccessPolicyEntryResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceAccessPolicyEntryResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceAccessPolicyEntryResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 object_id: str):
        """
        An access policy entry.
        :param str object_id: An Azure AD object ID (User or Apps) that is allowed access to the FHIR service.
        """
        pulumi.set(__self__, "object_id", object_id)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        """
        An Azure AD object ID (User or Apps) that is allowed access to the FHIR service.
        """
        return pulumi.get(self, "object_id")


@pulumi.output_type
class ServiceAuthenticationConfigurationInfoResponse(dict):
    """
    Authentication configuration information
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "smartProxyEnabled":
            suggest = "smart_proxy_enabled"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceAuthenticationConfigurationInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceAuthenticationConfigurationInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceAuthenticationConfigurationInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 audience: Optional[str] = None,
                 authority: Optional[str] = None,
                 smart_proxy_enabled: Optional[bool] = None):
        """
        Authentication configuration information
        :param str audience: The audience url for the service
        :param str authority: The authority url for the service
        :param bool smart_proxy_enabled: If the SMART on FHIR proxy is enabled
        """
        if audience is not None:
            pulumi.set(__self__, "audience", audience)
        if authority is not None:
            pulumi.set(__self__, "authority", authority)
        if smart_proxy_enabled is not None:
            pulumi.set(__self__, "smart_proxy_enabled", smart_proxy_enabled)

    @property
    @pulumi.getter
    def audience(self) -> Optional[str]:
        """
        The audience url for the service
        """
        return pulumi.get(self, "audience")

    @property
    @pulumi.getter
    def authority(self) -> Optional[str]:
        """
        The authority url for the service
        """
        return pulumi.get(self, "authority")

    @property
    @pulumi.getter(name="smartProxyEnabled")
    def smart_proxy_enabled(self) -> Optional[bool]:
        """
        If the SMART on FHIR proxy is enabled
        """
        return pulumi.get(self, "smart_proxy_enabled")


@pulumi.output_type
class ServiceCorsConfigurationInfoResponse(dict):
    """
    The settings for the CORS configuration of the service instance.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "allowCredentials":
            suggest = "allow_credentials"
        elif key == "maxAge":
            suggest = "max_age"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceCorsConfigurationInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceCorsConfigurationInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceCorsConfigurationInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 allow_credentials: Optional[bool] = None,
                 headers: Optional[Sequence[str]] = None,
                 max_age: Optional[int] = None,
                 methods: Optional[Sequence[str]] = None,
                 origins: Optional[Sequence[str]] = None):
        """
        The settings for the CORS configuration of the service instance.
        :param bool allow_credentials: If credentials are allowed via CORS.
        :param Sequence[str] headers: The headers to be allowed via CORS.
        :param int max_age: The max age to be allowed via CORS.
        :param Sequence[str] methods: The methods to be allowed via CORS.
        :param Sequence[str] origins: The origins to be allowed via CORS.
        """
        if allow_credentials is not None:
            pulumi.set(__self__, "allow_credentials", allow_credentials)
        if headers is not None:
            pulumi.set(__self__, "headers", headers)
        if max_age is not None:
            pulumi.set(__self__, "max_age", max_age)
        if methods is not None:
            pulumi.set(__self__, "methods", methods)
        if origins is not None:
            pulumi.set(__self__, "origins", origins)

    @property
    @pulumi.getter(name="allowCredentials")
    def allow_credentials(self) -> Optional[bool]:
        """
        If credentials are allowed via CORS.
        """
        return pulumi.get(self, "allow_credentials")

    @property
    @pulumi.getter
    def headers(self) -> Optional[Sequence[str]]:
        """
        The headers to be allowed via CORS.
        """
        return pulumi.get(self, "headers")

    @property
    @pulumi.getter(name="maxAge")
    def max_age(self) -> Optional[int]:
        """
        The max age to be allowed via CORS.
        """
        return pulumi.get(self, "max_age")

    @property
    @pulumi.getter
    def methods(self) -> Optional[Sequence[str]]:
        """
        The methods to be allowed via CORS.
        """
        return pulumi.get(self, "methods")

    @property
    @pulumi.getter
    def origins(self) -> Optional[Sequence[str]]:
        """
        The origins to be allowed via CORS.
        """
        return pulumi.get(self, "origins")


@pulumi.output_type
class ServiceCosmosDbConfigurationInfoResponse(dict):
    """
    The settings for the Cosmos DB database backing the service.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyVaultKeyUri":
            suggest = "key_vault_key_uri"
        elif key == "offerThroughput":
            suggest = "offer_throughput"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceCosmosDbConfigurationInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceCosmosDbConfigurationInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceCosmosDbConfigurationInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_vault_key_uri: Optional[str] = None,
                 offer_throughput: Optional[int] = None):
        """
        The settings for the Cosmos DB database backing the service.
        :param str key_vault_key_uri: The URI of the customer-managed key for the backing database.
        :param int offer_throughput: The provisioned throughput for the backing database.
        """
        if key_vault_key_uri is not None:
            pulumi.set(__self__, "key_vault_key_uri", key_vault_key_uri)
        if offer_throughput is not None:
            pulumi.set(__self__, "offer_throughput", offer_throughput)

    @property
    @pulumi.getter(name="keyVaultKeyUri")
    def key_vault_key_uri(self) -> Optional[str]:
        """
        The URI of the customer-managed key for the backing database.
        """
        return pulumi.get(self, "key_vault_key_uri")

    @property
    @pulumi.getter(name="offerThroughput")
    def offer_throughput(self) -> Optional[int]:
        """
        The provisioned throughput for the backing database.
        """
        return pulumi.get(self, "offer_throughput")


@pulumi.output_type
class ServiceExportConfigurationInfoResponse(dict):
    """
    Export operation configuration information
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "storageAccountName":
            suggest = "storage_account_name"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServiceExportConfigurationInfoResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServiceExportConfigurationInfoResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServiceExportConfigurationInfoResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 storage_account_name: Optional[str] = None):
        """
        Export operation configuration information
        :param str storage_account_name: The name of the default export storage account.
        """
        if storage_account_name is not None:
            pulumi.set(__self__, "storage_account_name", storage_account_name)

    @property
    @pulumi.getter(name="storageAccountName")
    def storage_account_name(self) -> Optional[str]:
        """
        The name of the default export storage account.
        """
        return pulumi.get(self, "storage_account_name")


@pulumi.output_type
class ServicesPropertiesResponse(dict):
    """
    The properties of a service instance.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "accessPolicies":
            suggest = "access_policies"
        elif key == "authenticationConfiguration":
            suggest = "authentication_configuration"
        elif key == "corsConfiguration":
            suggest = "cors_configuration"
        elif key == "cosmosDbConfiguration":
            suggest = "cosmos_db_configuration"
        elif key == "exportConfiguration":
            suggest = "export_configuration"
        elif key == "privateEndpointConnections":
            suggest = "private_endpoint_connections"
        elif key == "publicNetworkAccess":
            suggest = "public_network_access"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServicesPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServicesPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServicesPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 provisioning_state: str,
                 access_policies: Optional[Sequence['outputs.ServiceAccessPolicyEntryResponse']] = None,
                 authentication_configuration: Optional['outputs.ServiceAuthenticationConfigurationInfoResponse'] = None,
                 cors_configuration: Optional['outputs.ServiceCorsConfigurationInfoResponse'] = None,
                 cosmos_db_configuration: Optional['outputs.ServiceCosmosDbConfigurationInfoResponse'] = None,
                 export_configuration: Optional['outputs.ServiceExportConfigurationInfoResponse'] = None,
                 private_endpoint_connections: Optional[Sequence['outputs.PrivateEndpointConnectionResponse']] = None,
                 public_network_access: Optional[str] = None):
        """
        The properties of a service instance.
        :param str provisioning_state: The provisioning state.
        :param Sequence['ServiceAccessPolicyEntryResponse'] access_policies: The access policies of the service instance.
        :param 'ServiceAuthenticationConfigurationInfoResponse' authentication_configuration: The authentication configuration for the service instance.
        :param 'ServiceCorsConfigurationInfoResponse' cors_configuration: The settings for the CORS configuration of the service instance.
        :param 'ServiceCosmosDbConfigurationInfoResponse' cosmos_db_configuration: The settings for the Cosmos DB database backing the service.
        :param 'ServiceExportConfigurationInfoResponse' export_configuration: The settings for the export operation of the service instance.
        :param Sequence['PrivateEndpointConnectionResponse'] private_endpoint_connections: The list of private endpoint connections that are set up for this resource.
        :param str public_network_access: Control permission for data plane traffic coming from public networks while private endpoint is enabled.
        """
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if access_policies is not None:
            pulumi.set(__self__, "access_policies", access_policies)
        if authentication_configuration is not None:
            pulumi.set(__self__, "authentication_configuration", authentication_configuration)
        if cors_configuration is not None:
            pulumi.set(__self__, "cors_configuration", cors_configuration)
        if cosmos_db_configuration is not None:
            pulumi.set(__self__, "cosmos_db_configuration", cosmos_db_configuration)
        if export_configuration is not None:
            pulumi.set(__self__, "export_configuration", export_configuration)
        if private_endpoint_connections is not None:
            pulumi.set(__self__, "private_endpoint_connections", private_endpoint_connections)
        if public_network_access is not None:
            pulumi.set(__self__, "public_network_access", public_network_access)

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Sequence['outputs.ServiceAccessPolicyEntryResponse']]:
        """
        The access policies of the service instance.
        """
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="authenticationConfiguration")
    def authentication_configuration(self) -> Optional['outputs.ServiceAuthenticationConfigurationInfoResponse']:
        """
        The authentication configuration for the service instance.
        """
        return pulumi.get(self, "authentication_configuration")

    @property
    @pulumi.getter(name="corsConfiguration")
    def cors_configuration(self) -> Optional['outputs.ServiceCorsConfigurationInfoResponse']:
        """
        The settings for the CORS configuration of the service instance.
        """
        return pulumi.get(self, "cors_configuration")

    @property
    @pulumi.getter(name="cosmosDbConfiguration")
    def cosmos_db_configuration(self) -> Optional['outputs.ServiceCosmosDbConfigurationInfoResponse']:
        """
        The settings for the Cosmos DB database backing the service.
        """
        return pulumi.get(self, "cosmos_db_configuration")

    @property
    @pulumi.getter(name="exportConfiguration")
    def export_configuration(self) -> Optional['outputs.ServiceExportConfigurationInfoResponse']:
        """
        The settings for the export operation of the service instance.
        """
        return pulumi.get(self, "export_configuration")

    @property
    @pulumi.getter(name="privateEndpointConnections")
    def private_endpoint_connections(self) -> Optional[Sequence['outputs.PrivateEndpointConnectionResponse']]:
        """
        The list of private endpoint connections that are set up for this resource.
        """
        return pulumi.get(self, "private_endpoint_connections")

    @property
    @pulumi.getter(name="publicNetworkAccess")
    def public_network_access(self) -> Optional[str]:
        """
        Control permission for data plane traffic coming from public networks while private endpoint is enabled.
        """
        return pulumi.get(self, "public_network_access")


@pulumi.output_type
class ServicesResourceResponseIdentity(dict):
    """
    Setting indicating whether the service has a managed identity associated with it.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "principalId":
            suggest = "principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ServicesResourceResponseIdentity. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ServicesResourceResponseIdentity.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ServicesResourceResponseIdentity.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        Setting indicating whether the service has a managed identity associated with it.
        :param str principal_id: The principal ID of the resource identity.
        :param str tenant_id: The tenant ID of the resource.
        :param str type: Type of identity being specified, currently SystemAssigned and None are allowed.
        """
        pulumi.set(__self__, "principal_id", principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="principalId")
    def principal_id(self) -> str:
        """
        The principal ID of the resource identity.
        """
        return pulumi.get(self, "principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant ID of the resource.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Type of identity being specified, currently SystemAssigned and None are allowed.
        """
        return pulumi.get(self, "type")


