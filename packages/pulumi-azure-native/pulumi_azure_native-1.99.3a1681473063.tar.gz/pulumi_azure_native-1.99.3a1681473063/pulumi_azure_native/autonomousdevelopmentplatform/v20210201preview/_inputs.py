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
    'DataPoolEncryptionArgs',
    'DataPoolLocationArgs',
]

@pulumi.input_type
class DataPoolEncryptionArgs:
    def __init__(__self__, *,
                 key_name: pulumi.Input[str],
                 key_vault_uri: pulumi.Input[str],
                 user_assigned_identity: pulumi.Input[str],
                 key_version: Optional[pulumi.Input[str]] = None):
        """
        Encryption properties of a Data Pool
        :param pulumi.Input[str] key_name: The name of Key Vault key
        :param pulumi.Input[str] key_vault_uri: The URI of a soft delete-enabled Key Vault that is in the same location as the Data Pool location
        :param pulumi.Input[str] user_assigned_identity: The resource ID of a user-assigned Managed Identity used to access the encryption key in the Key Vault. Requires access to the key operations get, wrap, unwrap, and recover
        :param pulumi.Input[str] key_version: The version of Key Vault key
        """
        pulumi.set(__self__, "key_name", key_name)
        pulumi.set(__self__, "key_vault_uri", key_vault_uri)
        pulumi.set(__self__, "user_assigned_identity", user_assigned_identity)
        if key_version is not None:
            pulumi.set(__self__, "key_version", key_version)

    @property
    @pulumi.getter(name="keyName")
    def key_name(self) -> pulumi.Input[str]:
        """
        The name of Key Vault key
        """
        return pulumi.get(self, "key_name")

    @key_name.setter
    def key_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_name", value)

    @property
    @pulumi.getter(name="keyVaultUri")
    def key_vault_uri(self) -> pulumi.Input[str]:
        """
        The URI of a soft delete-enabled Key Vault that is in the same location as the Data Pool location
        """
        return pulumi.get(self, "key_vault_uri")

    @key_vault_uri.setter
    def key_vault_uri(self, value: pulumi.Input[str]):
        pulumi.set(self, "key_vault_uri", value)

    @property
    @pulumi.getter(name="userAssignedIdentity")
    def user_assigned_identity(self) -> pulumi.Input[str]:
        """
        The resource ID of a user-assigned Managed Identity used to access the encryption key in the Key Vault. Requires access to the key operations get, wrap, unwrap, and recover
        """
        return pulumi.get(self, "user_assigned_identity")

    @user_assigned_identity.setter
    def user_assigned_identity(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_assigned_identity", value)

    @property
    @pulumi.getter(name="keyVersion")
    def key_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of Key Vault key
        """
        return pulumi.get(self, "key_version")

    @key_version.setter
    def key_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_version", value)


@pulumi.input_type
class DataPoolLocationArgs:
    def __init__(__self__, *,
                 name: pulumi.Input[str],
                 encryption: Optional[pulumi.Input['DataPoolEncryptionArgs']] = None):
        """
        Location of a Data Pool
        :param pulumi.Input[str] name: The location name
        :param pulumi.Input['DataPoolEncryptionArgs'] encryption: Encryption properties of a Data Pool location
        """
        pulumi.set(__self__, "name", name)
        if encryption is not None:
            pulumi.set(__self__, "encryption", encryption)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Input[str]:
        """
        The location name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: pulumi.Input[str]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def encryption(self) -> Optional[pulumi.Input['DataPoolEncryptionArgs']]:
        """
        Encryption properties of a Data Pool location
        """
        return pulumi.get(self, "encryption")

    @encryption.setter
    def encryption(self, value: Optional[pulumi.Input['DataPoolEncryptionArgs']]):
        pulumi.set(self, "encryption", value)


