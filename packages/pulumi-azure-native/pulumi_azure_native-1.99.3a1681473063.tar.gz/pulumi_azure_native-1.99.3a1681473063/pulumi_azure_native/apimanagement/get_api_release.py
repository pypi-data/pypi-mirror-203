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
    'GetApiReleaseResult',
    'AwaitableGetApiReleaseResult',
    'get_api_release',
    'get_api_release_output',
]

@pulumi.output_type
class GetApiReleaseResult:
    """
    ApiRelease details.
    """
    def __init__(__self__, api_id=None, created_date_time=None, id=None, name=None, notes=None, type=None, updated_date_time=None):
        if api_id and not isinstance(api_id, str):
            raise TypeError("Expected argument 'api_id' to be a str")
        pulumi.set(__self__, "api_id", api_id)
        if created_date_time and not isinstance(created_date_time, str):
            raise TypeError("Expected argument 'created_date_time' to be a str")
        pulumi.set(__self__, "created_date_time", created_date_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if notes and not isinstance(notes, str):
            raise TypeError("Expected argument 'notes' to be a str")
        pulumi.set(__self__, "notes", notes)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if updated_date_time and not isinstance(updated_date_time, str):
            raise TypeError("Expected argument 'updated_date_time' to be a str")
        pulumi.set(__self__, "updated_date_time", updated_date_time)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> Optional[str]:
        """
        Identifier of the API the release belongs to.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="createdDateTime")
    def created_date_time(self) -> str:
        """
        The time the API was released. The date conforms to the following format: yyyy-MM-ddTHH:mm:ssZ as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "created_date_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notes(self) -> Optional[str]:
        """
        Release Notes
        """
        return pulumi.get(self, "notes")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="updatedDateTime")
    def updated_date_time(self) -> str:
        """
        The time the API release was updated.
        """
        return pulumi.get(self, "updated_date_time")


class AwaitableGetApiReleaseResult(GetApiReleaseResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetApiReleaseResult(
            api_id=self.api_id,
            created_date_time=self.created_date_time,
            id=self.id,
            name=self.name,
            notes=self.notes,
            type=self.type,
            updated_date_time=self.updated_date_time)


def get_api_release(api_id: Optional[str] = None,
                    release_id: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    service_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetApiReleaseResult:
    """
    Returns the details of an API release.
    API Version: 2020-12-01.


    :param str api_id: API identifier. Must be unique in the current API Management service instance.
    :param str release_id: Release identifier within an API. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['apiId'] = api_id
    __args__['releaseId'] = release_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement:getApiRelease', __args__, opts=opts, typ=GetApiReleaseResult).value

    return AwaitableGetApiReleaseResult(
        api_id=__ret__.api_id,
        created_date_time=__ret__.created_date_time,
        id=__ret__.id,
        name=__ret__.name,
        notes=__ret__.notes,
        type=__ret__.type,
        updated_date_time=__ret__.updated_date_time)


@_utilities.lift_output_func(get_api_release)
def get_api_release_output(api_id: Optional[pulumi.Input[str]] = None,
                           release_id: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           service_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetApiReleaseResult]:
    """
    Returns the details of an API release.
    API Version: 2020-12-01.


    :param str api_id: API identifier. Must be unique in the current API Management service instance.
    :param str release_id: Release identifier within an API. Must be unique in the current API Management service instance.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...
