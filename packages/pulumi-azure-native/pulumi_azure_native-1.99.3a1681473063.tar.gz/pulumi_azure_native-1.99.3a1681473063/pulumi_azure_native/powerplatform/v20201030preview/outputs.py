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
    'EnterprisePolicyIdentityResponse',
    'KeyPropertiesResponse',
    'KeyVaultPropertiesResponse',
    'PrivateEndpointResponse',
    'PrivateLinkServiceConnectionStateResponse',
    'PropertiesResponseEncryption',
    'PropertiesResponseLockbox',
    'PropertiesResponseNetworkInjection',
    'SubnetPropertiesResponse',
    'SystemDataResponse',
    'VirtualNetworkPropertiesListResponse',
    'VirtualNetworkPropertiesResponse',
]

@pulumi.output_type
class EnterprisePolicyIdentityResponse(dict):
    """
    The identity of the EnterprisePolicy.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "systemAssignedIdentityPrincipalId":
            suggest = "system_assigned_identity_principal_id"
        elif key == "tenantId":
            suggest = "tenant_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in EnterprisePolicyIdentityResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        EnterprisePolicyIdentityResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        EnterprisePolicyIdentityResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 system_assigned_identity_principal_id: str,
                 tenant_id: str,
                 type: Optional[str] = None):
        """
        The identity of the EnterprisePolicy.
        :param str system_assigned_identity_principal_id: The principal id of EnterprisePolicy identity.
        :param str tenant_id: The tenant id associated with the EnterprisePolicy.
        :param str type: The type of identity used for the EnterprisePolicy. Currently, the only supported type is 'SystemAssigned', which implicitly creates an identity.
        """
        pulumi.set(__self__, "system_assigned_identity_principal_id", system_assigned_identity_principal_id)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="systemAssignedIdentityPrincipalId")
    def system_assigned_identity_principal_id(self) -> str:
        """
        The principal id of EnterprisePolicy identity.
        """
        return pulumi.get(self, "system_assigned_identity_principal_id")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The tenant id associated with the EnterprisePolicy.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        The type of identity used for the EnterprisePolicy. Currently, the only supported type is 'SystemAssigned', which implicitly creates an identity.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class KeyPropertiesResponse(dict):
    """
    Url and version of the KeyVault Secret
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 version: Optional[str] = None):
        """
        Url and version of the KeyVault Secret
        :param str name: The identifier of the key vault key used to encrypt data.
        :param str version: The version of the identity which will be used to access key vault.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        The identifier of the key vault key used to encrypt data.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the identity which will be used to access key vault.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class KeyVaultPropertiesResponse(dict):
    """
    Settings concerning key vault encryption for a configuration store.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 key: Optional['outputs.KeyPropertiesResponse'] = None):
        """
        Settings concerning key vault encryption for a configuration store.
        :param str id: Uri of KeyVault
        :param 'KeyPropertiesResponse' key: Identity of the secret that includes name and version.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if key is not None:
            pulumi.set(__self__, "key", key)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Uri of KeyVault
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def key(self) -> Optional['outputs.KeyPropertiesResponse']:
        """
        Identity of the secret that includes name and version.
        """
        return pulumi.get(self, "key")


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
class PropertiesResponseEncryption(dict):
    """
    The encryption settings for a configuration store.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyVault":
            suggest = "key_vault"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PropertiesResponseEncryption. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PropertiesResponseEncryption.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PropertiesResponseEncryption.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_vault: Optional['outputs.KeyVaultPropertiesResponse'] = None,
                 state: Optional[str] = None):
        """
        The encryption settings for a configuration store.
        :param 'KeyVaultPropertiesResponse' key_vault: Key vault properties.
        :param str state: The state of onboarding, which only appears in the response.
        """
        if key_vault is not None:
            pulumi.set(__self__, "key_vault", key_vault)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional['outputs.KeyVaultPropertiesResponse']:
        """
        Key vault properties.
        """
        return pulumi.get(self, "key_vault")

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        The state of onboarding, which only appears in the response.
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class PropertiesResponseLockbox(dict):
    """
    Settings concerning lockbox.
    """
    def __init__(__self__, *,
                 state: Optional[str] = None):
        """
        Settings concerning lockbox.
        :param str state: lockbox configuration
        """
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter
    def state(self) -> Optional[str]:
        """
        lockbox configuration
        """
        return pulumi.get(self, "state")


@pulumi.output_type
class PropertiesResponseNetworkInjection(dict):
    """
    Settings concerning network injection.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "virtualNetworks":
            suggest = "virtual_networks"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PropertiesResponseNetworkInjection. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PropertiesResponseNetworkInjection.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PropertiesResponseNetworkInjection.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 virtual_networks: Optional['outputs.VirtualNetworkPropertiesListResponse'] = None):
        """
        Settings concerning network injection.
        :param 'VirtualNetworkPropertiesListResponse' virtual_networks: Network injection configuration
        """
        if virtual_networks is not None:
            pulumi.set(__self__, "virtual_networks", virtual_networks)

    @property
    @pulumi.getter(name="virtualNetworks")
    def virtual_networks(self) -> Optional['outputs.VirtualNetworkPropertiesListResponse']:
        """
        Network injection configuration
        """
        return pulumi.get(self, "virtual_networks")


@pulumi.output_type
class SubnetPropertiesResponse(dict):
    """
    Properties of a subnet.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None):
        """
        Properties of a subnet.
        :param str name: Subnet name.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Subnet name.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class SystemDataResponse(dict):
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
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

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


@pulumi.output_type
class VirtualNetworkPropertiesListResponse(dict):
    """
    A list of private link resources
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "nextLink":
            suggest = "next_link"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VirtualNetworkPropertiesListResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VirtualNetworkPropertiesListResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VirtualNetworkPropertiesListResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 next_link: Optional[str] = None,
                 value: Optional[Sequence['outputs.VirtualNetworkPropertiesResponse']] = None):
        """
        A list of private link resources
        :param str next_link: Next page link if any.
        :param Sequence['VirtualNetworkPropertiesResponse'] value: Array of virtual networks.
        """
        if next_link is not None:
            pulumi.set(__self__, "next_link", next_link)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> Optional[str]:
        """
        Next page link if any.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.VirtualNetworkPropertiesResponse']]:
        """
        Array of virtual networks.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class VirtualNetworkPropertiesResponse(dict):
    """
    Settings concerning the virtual network.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None,
                 subnet: Optional['outputs.SubnetPropertiesResponse'] = None):
        """
        Settings concerning the virtual network.
        :param str id: Uri of the virtual network.
        :param 'SubnetPropertiesResponse' subnet: Properties of a subnet.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)
        if subnet is not None:
            pulumi.set(__self__, "subnet", subnet)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Uri of the virtual network.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def subnet(self) -> Optional['outputs.SubnetPropertiesResponse']:
        """
        Properties of a subnet.
        """
        return pulumi.get(self, "subnet")


