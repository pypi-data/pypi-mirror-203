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
    'GetManagerExtendedInfoResult',
    'AwaitableGetManagerExtendedInfoResult',
    'get_manager_extended_info',
    'get_manager_extended_info_output',
]

@pulumi.output_type
class GetManagerExtendedInfoResult:
    """
    The extended info of the manager.
    """
    def __init__(__self__, algorithm=None, encryption_key=None, encryption_key_thumbprint=None, etag=None, id=None, integrity_key=None, kind=None, name=None, portal_certificate_thumbprint=None, type=None, version=None):
        if algorithm and not isinstance(algorithm, str):
            raise TypeError("Expected argument 'algorithm' to be a str")
        pulumi.set(__self__, "algorithm", algorithm)
        if encryption_key and not isinstance(encryption_key, str):
            raise TypeError("Expected argument 'encryption_key' to be a str")
        pulumi.set(__self__, "encryption_key", encryption_key)
        if encryption_key_thumbprint and not isinstance(encryption_key_thumbprint, str):
            raise TypeError("Expected argument 'encryption_key_thumbprint' to be a str")
        pulumi.set(__self__, "encryption_key_thumbprint", encryption_key_thumbprint)
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if integrity_key and not isinstance(integrity_key, str):
            raise TypeError("Expected argument 'integrity_key' to be a str")
        pulumi.set(__self__, "integrity_key", integrity_key)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if portal_certificate_thumbprint and not isinstance(portal_certificate_thumbprint, str):
            raise TypeError("Expected argument 'portal_certificate_thumbprint' to be a str")
        pulumi.set(__self__, "portal_certificate_thumbprint", portal_certificate_thumbprint)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def algorithm(self) -> str:
        """
        Represents the encryption algorithm used to encrypt the keys. None - if Key is saved in plain text format. Algorithm name - if key is encrypted
        """
        return pulumi.get(self, "algorithm")

    @property
    @pulumi.getter(name="encryptionKey")
    def encryption_key(self) -> Optional[str]:
        """
        Represents the CEK of the resource.
        """
        return pulumi.get(self, "encryption_key")

    @property
    @pulumi.getter(name="encryptionKeyThumbprint")
    def encryption_key_thumbprint(self) -> Optional[str]:
        """
        Represents the Cert thumbprint that was used to encrypt the CEK.
        """
        return pulumi.get(self, "encryption_key_thumbprint")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        The etag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The path ID that uniquely identifies the object.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="integrityKey")
    def integrity_key(self) -> str:
        """
        Represents the CIK of the resource.
        """
        return pulumi.get(self, "integrity_key")

    @property
    @pulumi.getter
    def kind(self) -> Optional[str]:
        """
        The Kind of the object. Currently only Series8000 is supported
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the object.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="portalCertificateThumbprint")
    def portal_certificate_thumbprint(self) -> Optional[str]:
        """
        Represents the portal thumbprint which can be used optionally to encrypt the entire data before storing it.
        """
        return pulumi.get(self, "portal_certificate_thumbprint")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version of the extended info being persisted.
        """
        return pulumi.get(self, "version")


class AwaitableGetManagerExtendedInfoResult(GetManagerExtendedInfoResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetManagerExtendedInfoResult(
            algorithm=self.algorithm,
            encryption_key=self.encryption_key,
            encryption_key_thumbprint=self.encryption_key_thumbprint,
            etag=self.etag,
            id=self.id,
            integrity_key=self.integrity_key,
            kind=self.kind,
            name=self.name,
            portal_certificate_thumbprint=self.portal_certificate_thumbprint,
            type=self.type,
            version=self.version)


def get_manager_extended_info(manager_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetManagerExtendedInfoResult:
    """
    Returns the extended information of the specified manager name.
    API Version: 2017-06-01.


    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    __args__ = dict()
    __args__['managerName'] = manager_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storsimple:getManagerExtendedInfo', __args__, opts=opts, typ=GetManagerExtendedInfoResult).value

    return AwaitableGetManagerExtendedInfoResult(
        algorithm=__ret__.algorithm,
        encryption_key=__ret__.encryption_key,
        encryption_key_thumbprint=__ret__.encryption_key_thumbprint,
        etag=__ret__.etag,
        id=__ret__.id,
        integrity_key=__ret__.integrity_key,
        kind=__ret__.kind,
        name=__ret__.name,
        portal_certificate_thumbprint=__ret__.portal_certificate_thumbprint,
        type=__ret__.type,
        version=__ret__.version)


@_utilities.lift_output_func(get_manager_extended_info)
def get_manager_extended_info_output(manager_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetManagerExtendedInfoResult]:
    """
    Returns the extended information of the specified manager name.
    API Version: 2017-06-01.


    :param str manager_name: The manager name
    :param str resource_group_name: The resource group name
    """
    ...
