# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'ActiveDirectoryObjectArgs',
    'TokenCertificateArgs',
    'TokenCredentialsPropertiesArgs',
    'TokenPasswordArgs',
]

@pulumi.input_type
class ActiveDirectoryObjectArgs:
    def __init__(__self__, *,
                 object_id: Optional[pulumi.Input[str]] = None,
                 tenant_id: Optional[pulumi.Input[str]] = None):
        """
        The Active Directory Object that will be used for authenticating the token of a container registry.
        :param pulumi.Input[str] object_id: The user/group/application object ID for Active Directory Object that will be used for authenticating the token of a container registry.
        :param pulumi.Input[str] tenant_id: The tenant ID of user/group/application object Active Directory Object that will be used for authenticating the token of a container registry.
        """
        if object_id is not None:
            pulumi.set(__self__, "object_id", object_id)
        if tenant_id is not None:
            pulumi.set(__self__, "tenant_id", tenant_id)

    @property
    @pulumi.getter(name="objectId")
    def object_id(self) -> Optional[pulumi.Input[str]]:
        """
        The user/group/application object ID for Active Directory Object that will be used for authenticating the token of a container registry.
        """
        return pulumi.get(self, "object_id")

    @object_id.setter
    def object_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "object_id", value)

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> Optional[pulumi.Input[str]]:
        """
        The tenant ID of user/group/application object Active Directory Object that will be used for authenticating the token of a container registry.
        """
        return pulumi.get(self, "tenant_id")

    @tenant_id.setter
    def tenant_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "tenant_id", value)


@pulumi.input_type
class TokenCertificateArgs:
    def __init__(__self__, *,
                 encoded_pem_certificate: Optional[pulumi.Input[str]] = None,
                 expiry: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[Union[str, 'TokenCertificateName']]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None):
        """
        The properties of a certificate used for authenticating a token.
        :param pulumi.Input[str] encoded_pem_certificate: Base 64 encoded string of the public certificate1 in PEM format that will be used for authenticating the token.
        :param pulumi.Input[str] expiry: The expiry datetime of the certificate.
        :param pulumi.Input[str] thumbprint: The thumbprint of the certificate.
        """
        if encoded_pem_certificate is not None:
            pulumi.set(__self__, "encoded_pem_certificate", encoded_pem_certificate)
        if expiry is not None:
            pulumi.set(__self__, "expiry", expiry)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if thumbprint is not None:
            pulumi.set(__self__, "thumbprint", thumbprint)

    @property
    @pulumi.getter(name="encodedPemCertificate")
    def encoded_pem_certificate(self) -> Optional[pulumi.Input[str]]:
        """
        Base 64 encoded string of the public certificate1 in PEM format that will be used for authenticating the token.
        """
        return pulumi.get(self, "encoded_pem_certificate")

    @encoded_pem_certificate.setter
    def encoded_pem_certificate(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "encoded_pem_certificate", value)

    @property
    @pulumi.getter
    def expiry(self) -> Optional[pulumi.Input[str]]:
        """
        The expiry datetime of the certificate.
        """
        return pulumi.get(self, "expiry")

    @expiry.setter
    def expiry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[str, 'TokenCertificateName']]]:
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[str, 'TokenCertificateName']]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[str]]:
        """
        The thumbprint of the certificate.
        """
        return pulumi.get(self, "thumbprint")

    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "thumbprint", value)


@pulumi.input_type
class TokenCredentialsPropertiesArgs:
    def __init__(__self__, *,
                 active_directory_object: Optional[pulumi.Input['ActiveDirectoryObjectArgs']] = None,
                 certificates: Optional[pulumi.Input[Sequence[pulumi.Input['TokenCertificateArgs']]]] = None,
                 passwords: Optional[pulumi.Input[Sequence[pulumi.Input['TokenPasswordArgs']]]] = None):
        """
        The properties of the credentials that can be used for authenticating the token.
        :param pulumi.Input['ActiveDirectoryObjectArgs'] active_directory_object: The Active Directory Object that will be used for authenticating the token of a container registry.
        """
        if active_directory_object is not None:
            pulumi.set(__self__, "active_directory_object", active_directory_object)
        if certificates is not None:
            pulumi.set(__self__, "certificates", certificates)
        if passwords is not None:
            pulumi.set(__self__, "passwords", passwords)

    @property
    @pulumi.getter(name="activeDirectoryObject")
    def active_directory_object(self) -> Optional[pulumi.Input['ActiveDirectoryObjectArgs']]:
        """
        The Active Directory Object that will be used for authenticating the token of a container registry.
        """
        return pulumi.get(self, "active_directory_object")

    @active_directory_object.setter
    def active_directory_object(self, value: Optional[pulumi.Input['ActiveDirectoryObjectArgs']]):
        pulumi.set(self, "active_directory_object", value)

    @property
    @pulumi.getter
    def certificates(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TokenCertificateArgs']]]]:
        return pulumi.get(self, "certificates")

    @certificates.setter
    def certificates(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TokenCertificateArgs']]]]):
        pulumi.set(self, "certificates", value)

    @property
    @pulumi.getter
    def passwords(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['TokenPasswordArgs']]]]:
        return pulumi.get(self, "passwords")

    @passwords.setter
    def passwords(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['TokenPasswordArgs']]]]):
        pulumi.set(self, "passwords", value)


@pulumi.input_type
class TokenPasswordArgs:
    def __init__(__self__, *,
                 creation_time: Optional[pulumi.Input[str]] = None,
                 expiry: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[Union[str, 'TokenPasswordName']]] = None):
        """
        The password that will be used for authenticating the token of a container registry.
        :param pulumi.Input[str] creation_time: The creation datetime of the password.
        :param pulumi.Input[str] expiry: The expiry datetime of the password.
        :param pulumi.Input[Union[str, 'TokenPasswordName']] name: The password name "password1" or "password2"
        """
        if creation_time is not None:
            pulumi.set(__self__, "creation_time", creation_time)
        if expiry is not None:
            pulumi.set(__self__, "expiry", expiry)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> Optional[pulumi.Input[str]]:
        """
        The creation datetime of the password.
        """
        return pulumi.get(self, "creation_time")

    @creation_time.setter
    def creation_time(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "creation_time", value)

    @property
    @pulumi.getter
    def expiry(self) -> Optional[pulumi.Input[str]]:
        """
        The expiry datetime of the password.
        """
        return pulumi.get(self, "expiry")

    @expiry.setter
    def expiry(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiry", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[Union[str, 'TokenPasswordName']]]:
        """
        The password name "password1" or "password2"
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[Union[str, 'TokenPasswordName']]]):
        pulumi.set(self, "name", value)


