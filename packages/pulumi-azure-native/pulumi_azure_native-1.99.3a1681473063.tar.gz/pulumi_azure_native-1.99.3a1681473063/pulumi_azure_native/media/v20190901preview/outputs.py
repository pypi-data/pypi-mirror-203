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
    'MediaGraphAssetSinkResponse',
    'MediaGraphRtspSourceResponse',
    'MediaGraphUserCredentialsResponse',
]

@pulumi.output_type
class MediaGraphAssetSinkResponse(dict):
    """
    Asset sink
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "assetName":
            suggest = "asset_name"
        elif key == "odataType":
            suggest = "odata_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MediaGraphAssetSinkResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MediaGraphAssetSinkResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MediaGraphAssetSinkResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 asset_name: str,
                 inputs: Sequence[str],
                 name: str,
                 odata_type: str):
        """
        Asset sink
        :param str asset_name: Asset name
        :param Sequence[str] inputs: Sink inputs
        :param str name: Sink name
        :param str odata_type: The discriminator for derived types.
               Expected value is '#Microsoft.Media.MediaGraphAssetSink'.
        """
        pulumi.set(__self__, "asset_name", asset_name)
        pulumi.set(__self__, "inputs", inputs)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "odata_type", '#Microsoft.Media.MediaGraphAssetSink')

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> str:
        """
        Asset name
        """
        return pulumi.get(self, "asset_name")

    @property
    @pulumi.getter
    def inputs(self) -> Sequence[str]:
        """
        Sink inputs
        """
        return pulumi.get(self, "inputs")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Sink name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> str:
        """
        The discriminator for derived types.
        Expected value is '#Microsoft.Media.MediaGraphAssetSink'.
        """
        return pulumi.get(self, "odata_type")


@pulumi.output_type
class MediaGraphRtspSourceResponse(dict):
    """
    RTSP source
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "odataType":
            suggest = "odata_type"
        elif key == "rtspUrl":
            suggest = "rtsp_url"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in MediaGraphRtspSourceResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        MediaGraphRtspSourceResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        MediaGraphRtspSourceResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 name: str,
                 odata_type: str,
                 rtsp_url: str,
                 credentials: Optional['outputs.MediaGraphUserCredentialsResponse'] = None):
        """
        RTSP source
        :param str name: Source name
        :param str odata_type: The discriminator for derived types.
               Expected value is '#Microsoft.Media.MediaGraphRtspSource'.
        :param str rtsp_url: RTSP URL
        :param 'MediaGraphUserCredentialsResponse' credentials: RTSP Credentials
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "odata_type", '#Microsoft.Media.MediaGraphRtspSource')
        pulumi.set(__self__, "rtsp_url", rtsp_url)
        if credentials is not None:
            pulumi.set(__self__, "credentials", credentials)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Source name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="odataType")
    def odata_type(self) -> str:
        """
        The discriminator for derived types.
        Expected value is '#Microsoft.Media.MediaGraphRtspSource'.
        """
        return pulumi.get(self, "odata_type")

    @property
    @pulumi.getter(name="rtspUrl")
    def rtsp_url(self) -> str:
        """
        RTSP URL
        """
        return pulumi.get(self, "rtsp_url")

    @property
    @pulumi.getter
    def credentials(self) -> Optional['outputs.MediaGraphUserCredentialsResponse']:
        """
        RTSP Credentials
        """
        return pulumi.get(self, "credentials")


@pulumi.output_type
class MediaGraphUserCredentialsResponse(dict):
    """
    Credentials to authenticate to Media Graph sources
    """
    def __init__(__self__, *,
                 password: str,
                 username: str):
        """
        Credentials to authenticate to Media Graph sources
        :param str password: Password credential
        :param str username: User name
        """
        pulumi.set(__self__, "password", password)
        pulumi.set(__self__, "username", username)

    @property
    @pulumi.getter
    def password(self) -> str:
        """
        Password credential
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter
    def username(self) -> str:
        """
        User name
        """
        return pulumi.get(self, "username")


