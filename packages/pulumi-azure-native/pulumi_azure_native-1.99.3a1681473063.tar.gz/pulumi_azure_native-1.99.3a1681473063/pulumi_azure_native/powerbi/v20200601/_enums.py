# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'PersistedConnectionStatus',
    'ResourceProvisioningState',
]


class PersistedConnectionStatus(str, Enum):
    """
    Status of the connection.
    """
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class ResourceProvisioningState(str, Enum):
    """
    Provisioning state of the Private Endpoint Connection.
    """
    CREATING = "Creating"
    UPDATING = "Updating"
    DELETING = "Deleting"
    SUCCEEDED = "Succeeded"
    CANCELED = "Canceled"
    FAILED = "Failed"
