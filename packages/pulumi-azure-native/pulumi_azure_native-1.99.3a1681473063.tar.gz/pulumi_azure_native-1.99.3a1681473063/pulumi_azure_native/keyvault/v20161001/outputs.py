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
    'AccessPolicyEntryResponse',
    'PermissionsResponse',
    'SecretAttributesResponse',
    'SecretPropertiesResponse',
    'SkuResponse',
    'VaultPropertiesResponse',
]

@pulumi.output_type
class AccessPolicyEntryResponse(dict):
    """
    An identity that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "objectId":
            suggest = "object_id"
        elif key == "tenantId":
            suggest = "tenant_id"
        elif key == "applicationId":
            suggest = "application_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in AccessPolicyEntryResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        AccessPolicyEntryResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        AccessPolicyEntryResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 object_id: str,
                 permissions: 'outputs.PermissionsResponse',
                 tenant_id: str,
                 application_id: Optional[str] = None):
        """
        An identity that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID.
        :param str object_id: The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies.
        :param 'PermissionsResponse' permissions: Permissions the identity has for keys, secrets and certificates.
        :param str tenant_id: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.
        :param str application_id:  Application ID of the client making request on behalf of a principal
        """
        pulumi.set(__self__, "object_id", object_id)
        pulumi.set(__self__, "permissions", permissions)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> str:
        """
        The object ID of a user, service principal or security group in the Azure Active Directory tenant for the vault. The object ID must be unique for the list of access policies.
        """
        return pulumi.get(self, "object_id")

    @property
    @pulumi.getter
    def permissions(self) -> 'outputs.PermissionsResponse':
        """
        Permissions the identity has for keys, secrets and certificates.
        """
        return pulumi.get(self, "permissions")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[str]:
        """
         Application ID of the client making request on behalf of a principal
        """
        return pulumi.get(self, "application_id")


@pulumi.output_type
class PermissionsResponse(dict):
    """
    Permissions the identity has for keys, secrets, certificates and storage.
    """
    def __init__(__self__, *,
                 certificates: Optional[Sequence[str]] = None,
                 keys: Optional[Sequence[str]] = None,
                 secrets: Optional[Sequence[str]] = None,
                 storage: Optional[Sequence[str]] = None):
        """
        Permissions the identity has for keys, secrets, certificates and storage.
        :param Sequence[str] certificates: Permissions to certificates
        :param Sequence[str] keys: Permissions to keys
        :param Sequence[str] secrets: Permissions to secrets
        :param Sequence[str] storage: Permissions to storage accounts
        """
        if certificates is not None:
            pulumi.set(__self__, "certificates", certificates)
        if keys is not None:
            pulumi.set(__self__, "keys", keys)
        if secrets is not None:
            pulumi.set(__self__, "secrets", secrets)
        if storage is not None:
            pulumi.set(__self__, "storage", storage)

    @property
    @pulumi.getter
    def certificates(self) -> Optional[Sequence[str]]:
        """
        Permissions to certificates
        """
        return pulumi.get(self, "certificates")

    @property
    @pulumi.getter
    def keys(self) -> Optional[Sequence[str]]:
        """
        Permissions to keys
        """
        return pulumi.get(self, "keys")

    @property
    @pulumi.getter
    def secrets(self) -> Optional[Sequence[str]]:
        """
        Permissions to secrets
        """
        return pulumi.get(self, "secrets")

    @property
    @pulumi.getter
    def storage(self) -> Optional[Sequence[str]]:
        """
        Permissions to storage accounts
        """
        return pulumi.get(self, "storage")


@pulumi.output_type
class SecretAttributesResponse(dict):
    """
    The secret management attributes.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "notBefore":
            suggest = "not_before"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecretAttributesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecretAttributesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecretAttributesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created: int,
                 updated: int,
                 enabled: Optional[bool] = None,
                 expires: Optional[int] = None,
                 not_before: Optional[int] = None):
        """
        The secret management attributes.
        :param int created: Creation time in seconds since 1970-01-01T00:00:00Z.
        :param int updated: Last updated time in seconds since 1970-01-01T00:00:00Z.
        :param bool enabled: Determines whether the object is enabled.
        :param int expires: Expiry date in seconds since 1970-01-01T00:00:00Z.
        :param int not_before: Not before date in seconds since 1970-01-01T00:00:00Z.
        """
        pulumi.set(__self__, "created", created)
        pulumi.set(__self__, "updated", updated)
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if expires is not None:
            pulumi.set(__self__, "expires", expires)
        if not_before is not None:
            pulumi.set(__self__, "not_before", not_before)

    @property
    @pulumi.getter
    def created(self) -> int:
        """
        Creation time in seconds since 1970-01-01T00:00:00Z.
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter
    def updated(self) -> int:
        """
        Last updated time in seconds since 1970-01-01T00:00:00Z.
        """
        return pulumi.get(self, "updated")

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        Determines whether the object is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def expires(self) -> Optional[int]:
        """
        Expiry date in seconds since 1970-01-01T00:00:00Z.
        """
        return pulumi.get(self, "expires")

    @property
    @pulumi.getter(name="notBefore")
    def not_before(self) -> Optional[int]:
        """
        Not before date in seconds since 1970-01-01T00:00:00Z.
        """
        return pulumi.get(self, "not_before")


@pulumi.output_type
class SecretPropertiesResponse(dict):
    """
    Properties of the secret
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "secretUri":
            suggest = "secret_uri"
        elif key == "secretUriWithVersion":
            suggest = "secret_uri_with_version"
        elif key == "contentType":
            suggest = "content_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SecretPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SecretPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SecretPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 secret_uri: str,
                 secret_uri_with_version: str,
                 attributes: Optional['outputs.SecretAttributesResponse'] = None,
                 content_type: Optional[str] = None,
                 value: Optional[str] = None):
        """
        Properties of the secret
        :param str secret_uri: The URI to retrieve the current version of the secret.
        :param str secret_uri_with_version: The URI to retrieve the specific version of the secret.
        :param 'SecretAttributesResponse' attributes: The attributes of the secret.
        :param str content_type: The content type of the secret.
        :param str value: The value of the secret. NOTE: 'value' will never be returned from the service, as APIs using this model are is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.
        """
        pulumi.set(__self__, "secret_uri", secret_uri)
        pulumi.set(__self__, "secret_uri_with_version", secret_uri_with_version)
        if attributes is not None:
            pulumi.set(__self__, "attributes", attributes)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="secretUri")
    def secret_uri(self) -> str:
        """
        The URI to retrieve the current version of the secret.
        """
        return pulumi.get(self, "secret_uri")

    @property
    @pulumi.getter(name="secretUriWithVersion")
    def secret_uri_with_version(self) -> str:
        """
        The URI to retrieve the specific version of the secret.
        """
        return pulumi.get(self, "secret_uri_with_version")

    @property
    @pulumi.getter
    def attributes(self) -> Optional['outputs.SecretAttributesResponse']:
        """
        The attributes of the secret.
        """
        return pulumi.get(self, "attributes")

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[str]:
        """
        The content type of the secret.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter
    def value(self) -> Optional[str]:
        """
        The value of the secret. NOTE: 'value' will never be returned from the service, as APIs using this model are is intended for internal use in ARM deployments. Users should use the data-plane REST service for interaction with vault secrets.
        """
        return pulumi.get(self, "value")


@pulumi.output_type
class SkuResponse(dict):
    """
    SKU details
    """
    def __init__(__self__, *,
                 family: str,
                 name: str):
        """
        SKU details
        :param str family: SKU family name
        :param str name: SKU name to specify whether the key vault is a standard vault or a premium vault.
        """
        pulumi.set(__self__, "family", family)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def family(self) -> str:
        """
        SKU family name
        """
        return pulumi.get(self, "family")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        SKU name to specify whether the key vault is a standard vault or a premium vault.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class VaultPropertiesResponse(dict):
    """
    Properties of the vault
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "tenantId":
            suggest = "tenant_id"
        elif key == "accessPolicies":
            suggest = "access_policies"
        elif key == "createMode":
            suggest = "create_mode"
        elif key == "enablePurgeProtection":
            suggest = "enable_purge_protection"
        elif key == "enableSoftDelete":
            suggest = "enable_soft_delete"
        elif key == "enabledForDeployment":
            suggest = "enabled_for_deployment"
        elif key == "enabledForDiskEncryption":
            suggest = "enabled_for_disk_encryption"
        elif key == "enabledForTemplateDeployment":
            suggest = "enabled_for_template_deployment"
        elif key == "vaultUri":
            suggest = "vault_uri"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in VaultPropertiesResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        VaultPropertiesResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        VaultPropertiesResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 sku: 'outputs.SkuResponse',
                 tenant_id: str,
                 access_policies: Optional[Sequence['outputs.AccessPolicyEntryResponse']] = None,
                 create_mode: Optional[str] = None,
                 enable_purge_protection: Optional[bool] = None,
                 enable_soft_delete: Optional[bool] = None,
                 enabled_for_deployment: Optional[bool] = None,
                 enabled_for_disk_encryption: Optional[bool] = None,
                 enabled_for_template_deployment: Optional[bool] = None,
                 vault_uri: Optional[str] = None):
        """
        Properties of the vault
        :param 'SkuResponse' sku: SKU details
        :param str tenant_id: The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.
        :param Sequence['AccessPolicyEntryResponse'] access_policies: An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID. When `createMode` is set to `recover`, access policies are not required. Otherwise, access policies are required.
        :param str create_mode: The vault's create mode to indicate whether the vault need to be recovered or not.
        :param bool enable_purge_protection: Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value.
        :param bool enable_soft_delete: Property specifying whether recoverable deletion is enabled for this key vault. Setting this property to true activates the soft delete feature, whereby vaults or vault entities can be recovered after deletion. Enabling this functionality is irreversible - that is, the property does not accept false as its value.
        :param bool enabled_for_deployment: Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.
        :param bool enabled_for_disk_encryption: Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
        :param bool enabled_for_template_deployment: Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.
        :param str vault_uri: The URI of the vault for performing operations on keys and secrets.
        """
        pulumi.set(__self__, "sku", sku)
        pulumi.set(__self__, "tenant_id", tenant_id)
        if access_policies is not None:
            pulumi.set(__self__, "access_policies", access_policies)
        if create_mode is not None:
            pulumi.set(__self__, "create_mode", create_mode)
        if enable_purge_protection is not None:
            pulumi.set(__self__, "enable_purge_protection", enable_purge_protection)
        if enable_soft_delete is not None:
            pulumi.set(__self__, "enable_soft_delete", enable_soft_delete)
        if enabled_for_deployment is not None:
            pulumi.set(__self__, "enabled_for_deployment", enabled_for_deployment)
        if enabled_for_disk_encryption is not None:
            pulumi.set(__self__, "enabled_for_disk_encryption", enabled_for_disk_encryption)
        if enabled_for_template_deployment is not None:
            pulumi.set(__self__, "enabled_for_template_deployment", enabled_for_template_deployment)
        if vault_uri is not None:
            pulumi.set(__self__, "vault_uri", vault_uri)

    @property
    @pulumi.getter
    def sku(self) -> 'outputs.SkuResponse':
        """
        SKU details
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> str:
        """
        The Azure Active Directory tenant ID that should be used for authenticating requests to the key vault.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter(name="accessPolicies")
    def access_policies(self) -> Optional[Sequence['outputs.AccessPolicyEntryResponse']]:
        """
        An array of 0 to 16 identities that have access to the key vault. All identities in the array must use the same tenant ID as the key vault's tenant ID. When `createMode` is set to `recover`, access policies are not required. Otherwise, access policies are required.
        """
        return pulumi.get(self, "access_policies")

    @property
    @pulumi.getter(name="createMode")
    def create_mode(self) -> Optional[str]:
        """
        The vault's create mode to indicate whether the vault need to be recovered or not.
        """
        return pulumi.get(self, "create_mode")

    @property
    @pulumi.getter(name="enablePurgeProtection")
    def enable_purge_protection(self) -> Optional[bool]:
        """
        Property specifying whether protection against purge is enabled for this vault. Setting this property to true activates protection against purge for this vault and its content - only the Key Vault service may initiate a hard, irrecoverable deletion. The setting is effective only if soft delete is also enabled. Enabling this functionality is irreversible - that is, the property does not accept false as its value.
        """
        return pulumi.get(self, "enable_purge_protection")

    @property
    @pulumi.getter(name="enableSoftDelete")
    def enable_soft_delete(self) -> Optional[bool]:
        """
        Property specifying whether recoverable deletion is enabled for this key vault. Setting this property to true activates the soft delete feature, whereby vaults or vault entities can be recovered after deletion. Enabling this functionality is irreversible - that is, the property does not accept false as its value.
        """
        return pulumi.get(self, "enable_soft_delete")

    @property
    @pulumi.getter(name="enabledForDeployment")
    def enabled_for_deployment(self) -> Optional[bool]:
        """
        Property to specify whether Azure Virtual Machines are permitted to retrieve certificates stored as secrets from the key vault.
        """
        return pulumi.get(self, "enabled_for_deployment")

    @property
    @pulumi.getter(name="enabledForDiskEncryption")
    def enabled_for_disk_encryption(self) -> Optional[bool]:
        """
        Property to specify whether Azure Disk Encryption is permitted to retrieve secrets from the vault and unwrap keys.
        """
        return pulumi.get(self, "enabled_for_disk_encryption")

    @property
    @pulumi.getter(name="enabledForTemplateDeployment")
    def enabled_for_template_deployment(self) -> Optional[bool]:
        """
        Property to specify whether Azure Resource Manager is permitted to retrieve secrets from the key vault.
        """
        return pulumi.get(self, "enabled_for_template_deployment")

    @property
    @pulumi.getter(name="vaultUri")
    def vault_uri(self) -> Optional[str]:
        """
        The URI of the vault for performing operations on keys and secrets.
        """
        return pulumi.get(self, "vault_uri")


