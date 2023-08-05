# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetSignalRCustomCertificateResult',
    'AwaitableGetSignalRCustomCertificateResult',
    'get_signal_r_custom_certificate',
    'get_signal_r_custom_certificate_output',
]

@pulumi.output_type
class GetSignalRCustomCertificateResult:
    """
    A custom certificate.
    """
    def __init__(__self__, id=None, key_vault_base_uri=None, key_vault_secret_name=None, key_vault_secret_version=None, name=None, provisioning_state=None, system_data=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if key_vault_base_uri and not isinstance(key_vault_base_uri, str):
            raise TypeError("Expected argument 'key_vault_base_uri' to be a str")
        pulumi.set(__self__, "key_vault_base_uri", key_vault_base_uri)
        if key_vault_secret_name and not isinstance(key_vault_secret_name, str):
            raise TypeError("Expected argument 'key_vault_secret_name' to be a str")
        pulumi.set(__self__, "key_vault_secret_name", key_vault_secret_name)
        if key_vault_secret_version and not isinstance(key_vault_secret_version, str):
            raise TypeError("Expected argument 'key_vault_secret_version' to be a str")
        pulumi.set(__self__, "key_vault_secret_version", key_vault_secret_version)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id for the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="keyVaultBaseUri")
    def key_vault_base_uri(self) -> str:
        """
        Base uri of the KeyVault that stores certificate.
        """
        return pulumi.get(self, "key_vault_base_uri")

    @property
    @pulumi.getter(name="keyVaultSecretName")
    def key_vault_secret_name(self) -> str:
        """
        Certificate secret name.
        """
        return pulumi.get(self, "key_vault_secret_name")

    @property
    @pulumi.getter(name="keyVaultSecretVersion")
    def key_vault_secret_version(self) -> Optional[str]:
        """
        Certificate secret version.
        """
        return pulumi.get(self, "key_vault_secret_version")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource - e.g. "Microsoft.SignalRService/SignalR"
        """
        return pulumi.get(self, "type")


class AwaitableGetSignalRCustomCertificateResult(GetSignalRCustomCertificateResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSignalRCustomCertificateResult(
            id=self.id,
            key_vault_base_uri=self.key_vault_base_uri,
            key_vault_secret_name=self.key_vault_secret_name,
            key_vault_secret_version=self.key_vault_secret_version,
            name=self.name,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_signal_r_custom_certificate(certificate_name: Optional[str] = None,
                                    resource_group_name: Optional[str] = None,
                                    resource_name: Optional[str] = None,
                                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSignalRCustomCertificateResult:
    """
    Get a custom certificate.
    API Version: 2022-02-01.


    :param str certificate_name: Custom certificate name
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str resource_name: The name of the resource.
    """
    __args__ = dict()
    __args__['certificateName'] = certificate_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:signalrservice:getSignalRCustomCertificate', __args__, opts=opts, typ=GetSignalRCustomCertificateResult).value

    return AwaitableGetSignalRCustomCertificateResult(
        id=__ret__.id,
        key_vault_base_uri=__ret__.key_vault_base_uri,
        key_vault_secret_name=__ret__.key_vault_secret_name,
        key_vault_secret_version=__ret__.key_vault_secret_version,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_signal_r_custom_certificate)
def get_signal_r_custom_certificate_output(certificate_name: Optional[pulumi.Input[str]] = None,
                                           resource_group_name: Optional[pulumi.Input[str]] = None,
                                           resource_name: Optional[pulumi.Input[str]] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSignalRCustomCertificateResult]:
    """
    Get a custom certificate.
    API Version: 2022-02-01.


    :param str certificate_name: Custom certificate name
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str resource_name: The name of the resource.
    """
    ...
