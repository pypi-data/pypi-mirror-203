# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ReclaimPolicy',
    'VolumeMode',
]


class ReclaimPolicy(str, Enum):
    """
    Reclaim Policy, Delete or Retain
    """
    DELETE = "Delete"
    RETAIN = "Retain"


class VolumeMode(str, Enum):
    """
    Indicates how the volumes created from the snapshot should be attached
    """
    FILESYSTEM = "Filesystem"
    RAW = "Raw"
