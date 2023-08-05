# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'CreateMode',
    'GeoRedundantBackup',
    'MinimalTlsVersionEnum',
    'PublicNetworkAccessEnum',
    'ServerVersion',
    'SkuTier',
    'SslEnforcementEnum',
    'StorageAutogrow',
]


class CreateMode(str, Enum):
    """
    The mode to create a new server.
    """
    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    GEO_RESTORE = "GeoRestore"
    REPLICA = "Replica"


class GeoRedundantBackup(str, Enum):
    """
    Enable Geo-redundant or not for server backup.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class MinimalTlsVersionEnum(str, Enum):
    """
    Enforce a minimal Tls version for the server.
    """
    TLS1_0 = "TLS1_0"
    TLS1_1 = "TLS1_1"
    TLS1_2 = "TLS1_2"
    TLS_ENFORCEMENT_DISABLED = "TLSEnforcementDisabled"


class PublicNetworkAccessEnum(str, Enum):
    """
    Whether or not public network access is allowed for this server. Value is optional but if passed in, must be 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ServerVersion(str, Enum):
    """
    Server version.
    """
    SERVER_VERSION_10_2 = "10.2"
    SERVER_VERSION_10_3 = "10.3"


class SkuTier(str, Enum):
    """
    The tier of the particular SKU, e.g. Basic.
    """
    BASIC = "Basic"
    GENERAL_PURPOSE = "GeneralPurpose"
    MEMORY_OPTIMIZED = "MemoryOptimized"


class SslEnforcementEnum(str, Enum):
    """
    Enable ssl enforcement or not when connect to server.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class StorageAutogrow(str, Enum):
    """
    Enable Storage Auto Grow.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
