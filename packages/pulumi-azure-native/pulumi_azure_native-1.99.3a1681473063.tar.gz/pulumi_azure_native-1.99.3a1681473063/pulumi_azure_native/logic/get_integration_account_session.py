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
    'GetIntegrationAccountSessionResult',
    'AwaitableGetIntegrationAccountSessionResult',
    'get_integration_account_session',
    'get_integration_account_session_output',
]

@pulumi.output_type
class GetIntegrationAccountSessionResult:
    """
    The integration account session.
    """
    def __init__(__self__, changed_time=None, content=None, created_time=None, id=None, location=None, name=None, tags=None, type=None):
        if changed_time and not isinstance(changed_time, str):
            raise TypeError("Expected argument 'changed_time' to be a str")
        pulumi.set(__self__, "changed_time", changed_time)
        if content and not isinstance(content, dict):
            raise TypeError("Expected argument 'content' to be a dict")
        pulumi.set(__self__, "content", content)
        if created_time and not isinstance(created_time, str):
            raise TypeError("Expected argument 'created_time' to be a str")
        pulumi.set(__self__, "created_time", created_time)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="changedTime")
    def changed_time(self) -> str:
        """
        The changed time.
        """
        return pulumi.get(self, "changed_time")

    @property
    @pulumi.getter
    def content(self) -> Optional[Any]:
        """
        The session content.
        """
        return pulumi.get(self, "content")

    @property
    @pulumi.getter(name="createdTime")
    def created_time(self) -> str:
        """
        The created time.
        """
        return pulumi.get(self, "created_time")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Gets the resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Gets the resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetIntegrationAccountSessionResult(GetIntegrationAccountSessionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetIntegrationAccountSessionResult(
            changed_time=self.changed_time,
            content=self.content,
            created_time=self.created_time,
            id=self.id,
            location=self.location,
            name=self.name,
            tags=self.tags,
            type=self.type)


def get_integration_account_session(integration_account_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    session_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetIntegrationAccountSessionResult:
    """
    Gets an integration account session.
    API Version: 2019-05-01.


    :param str integration_account_name: The integration account name.
    :param str resource_group_name: The resource group name.
    :param str session_name: The integration account session name.
    """
    __args__ = dict()
    __args__['integrationAccountName'] = integration_account_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['sessionName'] = session_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:logic:getIntegrationAccountSession', __args__, opts=opts, typ=GetIntegrationAccountSessionResult).value

    return AwaitableGetIntegrationAccountSessionResult(
        changed_time=__ret__.changed_time,
        content=__ret__.content,
        created_time=__ret__.created_time,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_integration_account_session)
def get_integration_account_session_output(integration_account_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           session_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetIntegrationAccountSessionResult]:
    """
    Gets an integration account session.
    API Version: 2019-05-01.


    :param str integration_account_name: The integration account name.
    :param str resource_group_name: The resource group name.
    :param str session_name: The integration account session name.
    """
    ...
