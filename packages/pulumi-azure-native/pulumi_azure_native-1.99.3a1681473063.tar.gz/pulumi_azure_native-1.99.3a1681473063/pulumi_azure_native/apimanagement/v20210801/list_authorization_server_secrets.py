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
    'ListAuthorizationServerSecretsResult',
    'AwaitableListAuthorizationServerSecretsResult',
    'list_authorization_server_secrets',
    'list_authorization_server_secrets_output',
]

@pulumi.output_type
class ListAuthorizationServerSecretsResult:
    """
    OAuth Server Secrets Contract.
    """
    def __init__(__self__, client_secret=None, resource_owner_password=None, resource_owner_username=None):
        if client_secret and not isinstance(client_secret, str):
            raise TypeError("Expected argument 'client_secret' to be a str")
        pulumi.set(__self__, "client_secret", client_secret)
        if resource_owner_password and not isinstance(resource_owner_password, str):
            raise TypeError("Expected argument 'resource_owner_password' to be a str")
        pulumi.set(__self__, "resource_owner_password", resource_owner_password)
        if resource_owner_username and not isinstance(resource_owner_username, str):
            raise TypeError("Expected argument 'resource_owner_username' to be a str")
        pulumi.set(__self__, "resource_owner_username", resource_owner_username)

    @property
    @pulumi.getter(name="clientSecret")
    def client_secret(self) -> Optional[str]:
        """
        oAuth Authorization Server Secrets.
        """
        return pulumi.get(self, "client_secret")

    @property
    @pulumi.getter(name="resourceOwnerPassword")
    def resource_owner_password(self) -> Optional[str]:
        """
        Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner password.
        """
        return pulumi.get(self, "resource_owner_password")

    @property
    @pulumi.getter(name="resourceOwnerUsername")
    def resource_owner_username(self) -> Optional[str]:
        """
        Can be optionally specified when resource owner password grant type is supported by this authorization server. Default resource owner username.
        """
        return pulumi.get(self, "resource_owner_username")


class AwaitableListAuthorizationServerSecretsResult(ListAuthorizationServerSecretsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListAuthorizationServerSecretsResult(
            client_secret=self.client_secret,
            resource_owner_password=self.resource_owner_password,
            resource_owner_username=self.resource_owner_username)


def list_authorization_server_secrets(authsid: Optional[str] = None,
                                      resource_group_name: Optional[str] = None,
                                      service_name: Optional[str] = None,
                                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListAuthorizationServerSecretsResult:
    """
    Gets the client secret details of the authorization server.


    :param str authsid: Identifier of the authorization server.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['authsid'] = authsid
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20210801:listAuthorizationServerSecrets', __args__, opts=opts, typ=ListAuthorizationServerSecretsResult).value

    return AwaitableListAuthorizationServerSecretsResult(
        client_secret=__ret__.client_secret,
        resource_owner_password=__ret__.resource_owner_password,
        resource_owner_username=__ret__.resource_owner_username)


@_utilities.lift_output_func(list_authorization_server_secrets)
def list_authorization_server_secrets_output(authsid: Optional[pulumi.Input[str]] = None,
                                             resource_group_name: Optional[pulumi.Input[str]] = None,
                                             service_name: Optional[pulumi.Input[str]] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListAuthorizationServerSecretsResult]:
    """
    Gets the client secret details of the authorization server.


    :param str authsid: Identifier of the authorization server.
    :param str resource_group_name: The name of the resource group.
    :param str service_name: The name of the API Management service.
    """
    ...
