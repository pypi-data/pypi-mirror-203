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
    'GetManagedInstanceAdministratorResult',
    'AwaitableGetManagedInstanceAdministratorResult',
    'get_managed_instance_administrator',
    'get_managed_instance_administrator_output',
]

@pulumi.output_type
class GetManagedInstanceAdministratorResult:
    """
    An Azure SQL managed instance administrator.
    """
    def __init__(__self__, administrator_type=None, id=None, login=None, name=None, sid=None, tenant_id=None, type=None):
        if administrator_type and not isinstance(administrator_type, str):
            raise TypeError("Expected argument 'administrator_type' to be a str")
        pulumi.set(__self__, "administrator_type", administrator_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if login and not isinstance(login, str):
            raise TypeError("Expected argument 'login' to be a str")
        pulumi.set(__self__, "login", login)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if sid and not isinstance(sid, str):
            raise TypeError("Expected argument 'sid' to be a str")
        pulumi.set(__self__, "sid", sid)
        if tenant_id and not isinstance(tenant_id, str):
            raise TypeError("Expected argument 'tenant_id' to be a str")
        pulumi.set(__self__, "tenant_id", tenant_id)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="administratorType")
    def administrator_type(self) -> str:
        """
        Type of the managed instance administrator.
        """
        return pulumi.get(self, "administrator_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def login(self) -> str:
        """
        Login name of the managed instance administrator.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def sid(self) -> str:
        """
        SID (object ID) of the managed instance administrator.
        """
        return pulumi.get(self, "sid")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[str]:
        """
        Tenant ID of the managed instance administrator.
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetManagedInstanceAdministratorResult(GetManagedInstanceAdministratorResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagedInstanceAdministratorResult(
            administrator_type=self.administrator_type,
            id=self.id,
            login=self.login,
            name=self.name,
            sid=self.sid,
            tenant_id=self.tenant_id,
            type=self.type)


def get_managed_instance_administrator(administrator_name: Optional[str] = None,
                                       managed_instance_name: Optional[str] = None,
                                       resource_group_name: Optional[str] = None,
                                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagedInstanceAdministratorResult:
    """
    Gets a managed instance administrator.


    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    __args__ = dict()
    __args__['administratorName'] = administrator_name
    __args__['managedInstanceName'] = managed_instance_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql/v20201101preview:getManagedInstanceAdministrator', __args__, opts=opts, typ=GetManagedInstanceAdministratorResult).value

    return AwaitableGetManagedInstanceAdministratorResult(
        administrator_type=__ret__.administrator_type,
        id=__ret__.id,
        login=__ret__.login,
        name=__ret__.name,
        sid=__ret__.sid,
        tenant_id=__ret__.tenant_id,
        type=__ret__.type)


@_utilities.lift_output_func(get_managed_instance_administrator)
def get_managed_instance_administrator_output(administrator_name: Optional[pulumi.Input[str]] = None,
                                              managed_instance_name: Optional[pulumi.Input[str]] = None,
                                              resource_group_name: Optional[pulumi.Input[str]] = None,
                                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagedInstanceAdministratorResult]:
    """
    Gets a managed instance administrator.


    :param str managed_instance_name: The name of the managed instance.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    """
    ...
