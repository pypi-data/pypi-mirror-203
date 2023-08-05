# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetRegistryBuildSourceUploadUrlResult',
    'AwaitableGetRegistryBuildSourceUploadUrlResult',
    'get_registry_build_source_upload_url',
    'get_registry_build_source_upload_url_output',
]

@pulumi.output_type
class GetRegistryBuildSourceUploadUrlResult:
    """
    The properties of a response to source upload request.
    """
    def __init__(__self__, relative_path=None, upload_url=None):
        if relative_path and not isinstance(relative_path, str):
            raise TypeError("Expected argument 'relative_path' to be a str")
        pulumi.set(__self__, "relative_path", relative_path)
        if upload_url and not isinstance(upload_url, str):
            raise TypeError("Expected argument 'upload_url' to be a str")
        pulumi.set(__self__, "upload_url", upload_url)

    @property
    @pulumi.getter(name="relativePath")
    def relative_path(self) -> Optional[str]:
        """
        The relative path to the source. This is used to submit the subsequent queue build request.
        """
        return pulumi.get(self, "relative_path")

    @property
    @pulumi.getter(name="uploadUrl")
    def upload_url(self) -> Optional[str]:
        """
        The URL where the client can upload the source.
        """
        return pulumi.get(self, "upload_url")


class AwaitableGetRegistryBuildSourceUploadUrlResult(GetRegistryBuildSourceUploadUrlResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetRegistryBuildSourceUploadUrlResult(
            relative_path=self.relative_path,
            upload_url=self.upload_url)


def get_registry_build_source_upload_url(registry_name: Optional[str] = None,
                                         resource_group_name: Optional[str] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetRegistryBuildSourceUploadUrlResult:
    """
    Get the upload location for the user to be able to upload the source.
    API Version: 2018-02-01-preview.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    __args__ = dict()
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry:getRegistryBuildSourceUploadUrl', __args__, opts=opts, typ=GetRegistryBuildSourceUploadUrlResult).value

    return AwaitableGetRegistryBuildSourceUploadUrlResult(
        relative_path=__ret__.relative_path,
        upload_url=__ret__.upload_url)


@_utilities.lift_output_func(get_registry_build_source_upload_url)
def get_registry_build_source_upload_url_output(registry_name: Optional[pulumi.Input[str]] = None,
                                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetRegistryBuildSourceUploadUrlResult]:
    """
    Get the upload location for the user to be able to upload the source.
    API Version: 2018-02-01-preview.


    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    ...
