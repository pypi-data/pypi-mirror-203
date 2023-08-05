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
    'GetAuthorizationResult',
    'AwaitableGetAuthorizationResult',
    'get_authorization',
    'get_authorization_output',
]

@pulumi.output_type
class GetAuthorizationResult:
    """
    Authorization contract.
    """
    def __init__(__self__, authorization_type=None, error=None, id=None, name=None, o_auth2_grant_type=None, parameters=None, status=None, type=None):
        if authorization_type and not isinstance(authorization_type, str):
            raise TypeError("Expected argument 'authorization_type' to be a str")
        pulumi.set(__self__, "authorization_type", authorization_type)
        if error and not isinstance(error, dict):
            raise TypeError("Expected argument 'error' to be a dict")
        pulumi.set(__self__, "error", error)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if o_auth2_grant_type and not isinstance(o_auth2_grant_type, str):
            raise TypeError("Expected argument 'o_auth2_grant_type' to be a str")
        pulumi.set(__self__, "o_auth2_grant_type", o_auth2_grant_type)
        if parameters and not isinstance(parameters, dict):
            raise TypeError("Expected argument 'parameters' to be a dict")
        pulumi.set(__self__, "parameters", parameters)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="authorizationType")
    def authorization_type(self) -> Optional[str]:
        """
        Authorization type options
        """
        return pulumi.get(self, "authorization_type")

    @property
    @pulumi.getter
    def error(self) -> Optional['outputs.AuthorizationErrorResponse']:
        """
        Authorization error details.
        """
        return pulumi.get(self, "error")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="oAuth2GrantType")
    def o_auth2_grant_type(self) -> Optional[str]:
        """
        OAuth2 grant type options
        """
        return pulumi.get(self, "o_auth2_grant_type")

    @property
    @pulumi.getter
    def parameters(self) -> Optional[Mapping[str, str]]:
        """
        Authorization parameters
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Status of the Authorization
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetAuthorizationResult(GetAuthorizationResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAuthorizationResult(
            authorization_type=self.authorization_type,
            error=self.error,
            id=self.id,
            name=self.name,
            o_auth2_grant_type=self.o_auth2_grant_type,
            parameters=self.parameters,
            status=self.status,
            type=self.type)


def get_authorization(authorization_id: Optional[str] = None,
                      authorization_provider_id: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      service_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAuthorizationResult:
    """
    Gets the details of the authorization specified by its identifier.


    :param str authorization_id: Identifier of the authorization.
    :param str authorization_provider_id: Identifier of the authorization provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    __args__ = dict()
    __args__['authorizationId'] = authorization_id
    __args__['authorizationProviderId'] = authorization_provider_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['serviceName'] = service_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:apimanagement/v20220401preview:getAuthorization', __args__, opts=opts, typ=GetAuthorizationResult).value

    return AwaitableGetAuthorizationResult(
        authorization_type=__ret__.authorization_type,
        error=__ret__.error,
        id=__ret__.id,
        name=__ret__.name,
        o_auth2_grant_type=__ret__.o_auth2_grant_type,
        parameters=__ret__.parameters,
        status=__ret__.status,
        type=__ret__.type)


@_utilities.lift_output_func(get_authorization)
def get_authorization_output(authorization_id: Optional[pulumi.Input[str]] = None,
                             authorization_provider_id: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             service_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAuthorizationResult]:
    """
    Gets the details of the authorization specified by its identifier.


    :param str authorization_id: Identifier of the authorization.
    :param str authorization_provider_id: Identifier of the authorization provider.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str service_name: The name of the API Management service.
    """
    ...
