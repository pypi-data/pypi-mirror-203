# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CreatedByType',
    'Type',
]


class CreatedByType(str, Enum):
    """
    The type of identity that last modified the resource.
    """
    USER = "User"
    APPLICATION = "Application"
    MANAGED_IDENTITY = "ManagedIdentity"
    KEY = "Key"


class Type(str, Enum):
    """
    The type of endpoint.
    """
    DEFAULT = "default"
    CUSTOM = "custom"
