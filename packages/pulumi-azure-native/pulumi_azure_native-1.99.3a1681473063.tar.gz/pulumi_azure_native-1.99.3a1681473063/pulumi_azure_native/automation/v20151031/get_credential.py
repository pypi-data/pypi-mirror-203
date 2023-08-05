# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetCredentialResult',
    'AwaitableGetCredentialResult',
    'get_credential',
    'get_credential_output',
]

@pulumi.output_type
class GetCredentialResult:
    """
    Definition of the credential.
    """
    def __init__(__self__, creation_time=None, description=None, id=None, last_modified_time=None, name=None, type=None, user_name=None):
        if creation_time and not isinstance(creation_time, str):
            raise TypeError("Expected argument 'creation_time' to be a str")
        pulumi.set(__self__, "creation_time", creation_time)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if last_modified_time and not isinstance(last_modified_time, str):
            raise TypeError("Expected argument 'last_modified_time' to be a str")
        pulumi.set(__self__, "last_modified_time", last_modified_time)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> str:
        """
        Gets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> str:
        """
        Gets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        """
        Gets the user name of the credential.
        """
        return pulumi.get(self, "user_name")


class AwaitableGetCredentialResult(GetCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCredentialResult(
            creation_time=self.creation_time,
            description=self.description,
            id=self.id,
            last_modified_time=self.last_modified_time,
            name=self.name,
            type=self.type,
            user_name=self.user_name)


def get_credential(automation_account_name: Optional[str] = None,
                   credential_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCredentialResult:
    """
    Retrieve the credential identified by credential name.


    :param str automation_account_name: The name of the automation account.
    :param str credential_name: The name of credential.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    __args__ = dict()
    __args__['automationAccountName'] = automation_account_name
    __args__['credentialName'] = credential_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:automation/v20151031:getCredential', __args__, opts=opts, typ=GetCredentialResult).value

    return AwaitableGetCredentialResult(
        creation_time=__ret__.creation_time,
        description=__ret__.description,
        id=__ret__.id,
        last_modified_time=__ret__.last_modified_time,
        name=__ret__.name,
        type=__ret__.type,
        user_name=__ret__.user_name)


@_utilities.lift_output_func(get_credential)
def get_credential_output(automation_account_name: Optional[pulumi.Input[str]] = None,
                          credential_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCredentialResult]:
    """
    Retrieve the credential identified by credential name.


    :param str automation_account_name: The name of the automation account.
    :param str credential_name: The name of credential.
    :param str resource_group_name: Name of an Azure Resource group.
    """
    ...
