# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AzureStorageBlobContainerEndpointPropertiesArgs',
    'NfsMountEndpointPropertiesArgs',
]

@pulumi.input_type
class AzureStorageBlobContainerEndpointPropertiesArgs:
    def __init__(__self__, *,
                 blob_container_name: pulumi.Input[str],
                 endpoint_type: pulumi.Input[str],
                 storage_account_resource_id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] blob_container_name: The name of the Storage blob container that is the target destination.
        :param pulumi.Input[str] endpoint_type: The Endpoint resource type.
               Expected value is 'AzureStorageBlobContainer'.
        :param pulumi.Input[str] storage_account_resource_id: The Azure Resource ID of the storage account that is the target destination.
        :param pulumi.Input[str] description: A description for the Endpoint.
        """
        pulumi.set(__self__, "blob_container_name", blob_container_name)
        pulumi.set(__self__, "endpoint_type", 'AzureStorageBlobContainer')
        pulumi.set(__self__, "storage_account_resource_id", storage_account_resource_id)
        if description is not None:
            pulumi.set(__self__, "description", description)

    @property
    @pulumi.getter(name="blobContainerName")
    def blob_container_name(self) -> pulumi.Input[str]:
        """
        The name of the Storage blob container that is the target destination.
        """
        return pulumi.get(self, "blob_container_name")

    @blob_container_name.setter
    def blob_container_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "blob_container_name", value)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The Endpoint resource type.
        Expected value is 'AzureStorageBlobContainer'.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter(name="storageAccountResourceId")
    def storage_account_resource_id(self) -> pulumi.Input[str]:
        """
        The Azure Resource ID of the storage account that is the target destination.
        """
        return pulumi.get(self, "storage_account_resource_id")

    @storage_account_resource_id.setter
    def storage_account_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_account_resource_id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)


@pulumi.input_type
class NfsMountEndpointPropertiesArgs:
    def __init__(__self__, *,
                 endpoint_type: pulumi.Input[str],
                 export: pulumi.Input[str],
                 host: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 nfs_version: Optional[pulumi.Input[Union[str, 'NfsVersion']]] = None):
        """
        :param pulumi.Input[str] endpoint_type: The Endpoint resource type.
               Expected value is 'NfsMount'.
        :param pulumi.Input[str] export: The directory being exported from the server.
        :param pulumi.Input[str] host: The host name or IP address of the server exporting the file system.
        :param pulumi.Input[str] description: A description for the Endpoint.
        :param pulumi.Input[Union[str, 'NfsVersion']] nfs_version: The NFS protocol version.
        """
        pulumi.set(__self__, "endpoint_type", 'NfsMount')
        pulumi.set(__self__, "export", export)
        pulumi.set(__self__, "host", host)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if nfs_version is not None:
            pulumi.set(__self__, "nfs_version", nfs_version)

    @property
    @pulumi.getter(name="endpointType")
    def endpoint_type(self) -> pulumi.Input[str]:
        """
        The Endpoint resource type.
        Expected value is 'NfsMount'.
        """
        return pulumi.get(self, "endpoint_type")

    @endpoint_type.setter
    def endpoint_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "endpoint_type", value)

    @property
    @pulumi.getter
    def export(self) -> pulumi.Input[str]:
        """
        The directory being exported from the server.
        """
        return pulumi.get(self, "export")

    @export.setter
    def export(self, value: pulumi.Input[str]):
        pulumi.set(self, "export", value)

    @property
    @pulumi.getter
    def host(self) -> pulumi.Input[str]:
        """
        The host name or IP address of the server exporting the file system.
        """
        return pulumi.get(self, "host")

    @host.setter
    def host(self, value: pulumi.Input[str]):
        pulumi.set(self, "host", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the Endpoint.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="nfsVersion")
    def nfs_version(self) -> Optional[pulumi.Input[Union[str, 'NfsVersion']]]:
        """
        The NFS protocol version.
        """
        return pulumi.get(self, "nfs_version")

    @nfs_version.setter
    def nfs_version(self, value: Optional[pulumi.Input[Union[str, 'NfsVersion']]]):
        pulumi.set(self, "nfs_version", value)


