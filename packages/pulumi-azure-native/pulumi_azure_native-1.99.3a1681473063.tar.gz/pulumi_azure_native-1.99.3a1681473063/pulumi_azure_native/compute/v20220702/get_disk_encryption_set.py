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
    'GetDiskEncryptionSetResult',
    'AwaitableGetDiskEncryptionSetResult',
    'get_disk_encryption_set',
    'get_disk_encryption_set_output',
]

@pulumi.output_type
class GetDiskEncryptionSetResult:
    """
    disk encryption set resource.
    """
    def __init__(__self__, active_key=None, auto_key_rotation_error=None, encryption_type=None, federated_client_id=None, id=None, identity=None, last_key_rotation_timestamp=None, location=None, name=None, previous_keys=None, provisioning_state=None, rotation_to_latest_key_version_enabled=None, tags=None, type=None):
        if active_key and not isinstance(active_key, dict):
            raise TypeError("Expected argument 'active_key' to be a dict")
        pulumi.set(__self__, "active_key", active_key)
        if auto_key_rotation_error and not isinstance(auto_key_rotation_error, dict):
            raise TypeError("Expected argument 'auto_key_rotation_error' to be a dict")
        pulumi.set(__self__, "auto_key_rotation_error", auto_key_rotation_error)
        if encryption_type and not isinstance(encryption_type, str):
            raise TypeError("Expected argument 'encryption_type' to be a str")
        pulumi.set(__self__, "encryption_type", encryption_type)
        if federated_client_id and not isinstance(federated_client_id, str):
            raise TypeError("Expected argument 'federated_client_id' to be a str")
        pulumi.set(__self__, "federated_client_id", federated_client_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if last_key_rotation_timestamp and not isinstance(last_key_rotation_timestamp, str):
            raise TypeError("Expected argument 'last_key_rotation_timestamp' to be a str")
        pulumi.set(__self__, "last_key_rotation_timestamp", last_key_rotation_timestamp)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if previous_keys and not isinstance(previous_keys, list):
            raise TypeError("Expected argument 'previous_keys' to be a list")
        pulumi.set(__self__, "previous_keys", previous_keys)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if rotation_to_latest_key_version_enabled and not isinstance(rotation_to_latest_key_version_enabled, bool):
            raise TypeError("Expected argument 'rotation_to_latest_key_version_enabled' to be a bool")
        pulumi.set(__self__, "rotation_to_latest_key_version_enabled", rotation_to_latest_key_version_enabled)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="activeKey")
    def active_key(self) -> Optional['outputs.KeyForDiskEncryptionSetResponse']:
        """
        The key vault key which is currently used by this disk encryption set.
        """
        return pulumi.get(self, "active_key")

    @property
    @pulumi.getter(name="autoKeyRotationError")
    def auto_key_rotation_error(self) -> 'outputs.ApiErrorResponse':
        """
        The error that was encountered during auto-key rotation. If an error is present, then auto-key rotation will not be attempted until the error on this disk encryption set is fixed.
        """
        return pulumi.get(self, "auto_key_rotation_error")

    @property
    @pulumi.getter(name="encryptionType")
    def encryption_type(self) -> Optional[str]:
        """
        The type of key used to encrypt the data of the disk.
        """
        return pulumi.get(self, "encryption_type")

    @property
    @pulumi.getter(name="federatedClientId")
    def federated_client_id(self) -> Optional[str]:
        """
        Multi-tenant application client id to access key vault in a different tenant. Setting the value to 'None' will clear the property.
        """
        return pulumi.get(self, "federated_client_id")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.EncryptionSetIdentityResponse']:
        """
        The managed identity for the disk encryption set. It should be given permission on the key vault before it can be used to encrypt disks.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="lastKeyRotationTimestamp")
    def last_key_rotation_timestamp(self) -> str:
        """
        The time when the active key of this disk encryption set was updated.
        """
        return pulumi.get(self, "last_key_rotation_timestamp")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="previousKeys")
    def previous_keys(self) -> Sequence['outputs.KeyForDiskEncryptionSetResponse']:
        """
        A readonly collection of key vault keys previously used by this disk encryption set while a key rotation is in progress. It will be empty if there is no ongoing key rotation.
        """
        return pulumi.get(self, "previous_keys")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The disk encryption set provisioning state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rotationToLatestKeyVersionEnabled")
    def rotation_to_latest_key_version_enabled(self) -> Optional[bool]:
        """
        Set this flag to true to enable auto-updating of this disk encryption set to the latest key version.
        """
        return pulumi.get(self, "rotation_to_latest_key_version_enabled")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetDiskEncryptionSetResult(GetDiskEncryptionSetResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetDiskEncryptionSetResult(
            active_key=self.active_key,
            auto_key_rotation_error=self.auto_key_rotation_error,
            encryption_type=self.encryption_type,
            federated_client_id=self.federated_client_id,
            id=self.id,
            identity=self.identity,
            last_key_rotation_timestamp=self.last_key_rotation_timestamp,
            location=self.location,
            name=self.name,
            previous_keys=self.previous_keys,
            provisioning_state=self.provisioning_state,
            rotation_to_latest_key_version_enabled=self.rotation_to_latest_key_version_enabled,
            tags=self.tags,
            type=self.type)


def get_disk_encryption_set(disk_encryption_set_name: Optional[str] = None,
                            resource_group_name: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetDiskEncryptionSetResult:
    """
    Gets information about a disk encryption set.


    :param str disk_encryption_set_name: The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['diskEncryptionSetName'] = disk_encryption_set_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20220702:getDiskEncryptionSet', __args__, opts=opts, typ=GetDiskEncryptionSetResult).value

    return AwaitableGetDiskEncryptionSetResult(
        active_key=__ret__.active_key,
        auto_key_rotation_error=__ret__.auto_key_rotation_error,
        encryption_type=__ret__.encryption_type,
        federated_client_id=__ret__.federated_client_id,
        id=__ret__.id,
        identity=__ret__.identity,
        last_key_rotation_timestamp=__ret__.last_key_rotation_timestamp,
        location=__ret__.location,
        name=__ret__.name,
        previous_keys=__ret__.previous_keys,
        provisioning_state=__ret__.provisioning_state,
        rotation_to_latest_key_version_enabled=__ret__.rotation_to_latest_key_version_enabled,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_disk_encryption_set)
def get_disk_encryption_set_output(disk_encryption_set_name: Optional[pulumi.Input[str]] = None,
                                   resource_group_name: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetDiskEncryptionSetResult]:
    """
    Gets information about a disk encryption set.


    :param str disk_encryption_set_name: The name of the disk encryption set that is being created. The name can't be changed after the disk encryption set is created. Supported characters for the name are a-z, A-Z, 0-9, _ and -. The maximum name length is 80 characters.
    :param str resource_group_name: The name of the resource group.
    """
    ...
