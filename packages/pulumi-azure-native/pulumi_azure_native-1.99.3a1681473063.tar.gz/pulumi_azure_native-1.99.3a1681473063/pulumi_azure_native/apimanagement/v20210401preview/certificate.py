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
from ._inputs import *

__all__ = ['CertificateArgs', 'Certificate']

@pulumi.input_type
class CertificateArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 key_vault: Optional[pulumi.Input['KeyVaultContractCreatePropertiesArgs']] = None,
                 password: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Certificate resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] data: Base 64 encoded certificate using the application/x-pkcs12 representation.
        :param pulumi.Input['KeyVaultContractCreatePropertiesArgs'] key_vault: KeyVault location details of the certificate.
        :param pulumi.Input[str] password: Password for the Certificate
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        if certificate_id is not None:
            pulumi.set(__self__, "certificate_id", certificate_id)
        if data is not None:
            pulumi.set(__self__, "data", data)
        if key_vault is not None:
            pulumi.set(__self__, "key_vault", key_vault)
        if password is not None:
            pulumi.set(__self__, "password", password)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter(name="certificateId")
    def certificate_id(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of the certificate entity. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "certificate_id")

    @certificate_id.setter
    def certificate_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "certificate_id", value)

    @property
    @pulumi.getter
    def data(self) -> Optional[pulumi.Input[str]]:
        """
        Base 64 encoded certificate using the application/x-pkcs12 representation.
        """
        return pulumi.get(self, "data")

    @data.setter
    def data(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "data", value)

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> Optional[pulumi.Input['KeyVaultContractCreatePropertiesArgs']]:
        """
        KeyVault location details of the certificate.
        """
        return pulumi.get(self, "key_vault")

    @key_vault.setter
    def key_vault(self, value: Optional[pulumi.Input['KeyVaultContractCreatePropertiesArgs']]):
        pulumi.set(self, "key_vault", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Password for the Certificate
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)


class Certificate(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 key_vault: Optional[pulumi.Input[pulumi.InputType['KeyVaultContractCreatePropertiesArgs']]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Certificate details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] certificate_id: Identifier of the certificate entity. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] data: Base 64 encoded certificate using the application/x-pkcs12 representation.
        :param pulumi.Input[pulumi.InputType['KeyVaultContractCreatePropertiesArgs']] key_vault: KeyVault location details of the certificate.
        :param pulumi.Input[str] password: Password for the Certificate
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Certificate details.

        :param str resource_name: The name of the resource.
        :param CertificateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(CertificateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 certificate_id: Optional[pulumi.Input[str]] = None,
                 data: Optional[pulumi.Input[str]] = None,
                 key_vault: Optional[pulumi.Input[pulumi.InputType['KeyVaultContractCreatePropertiesArgs']]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CertificateArgs.__new__(CertificateArgs)

            __props__.__dict__["certificate_id"] = certificate_id
            __props__.__dict__["data"] = data
            __props__.__dict__["key_vault"] = key_vault
            __props__.__dict__["password"] = password
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["expiration_date"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["subject"] = None
            __props__.__dict__["thumbprint"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20160707:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20161010:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20201201:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:Certificate"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:Certificate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Certificate, __self__).__init__(
            'azure-native:apimanagement/v20210401preview:Certificate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Certificate':
        """
        Get an existing Certificate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = CertificateArgs.__new__(CertificateArgs)

        __props__.__dict__["expiration_date"] = None
        __props__.__dict__["key_vault"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["subject"] = None
        __props__.__dict__["thumbprint"] = None
        __props__.__dict__["type"] = None
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[str]:
        """
        Expiration date of the certificate. The date conforms to the following format: `yyyy-MM-ddTHH:mm:ssZ` as specified by the ISO 8601 standard.
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="keyVault")
    def key_vault(self) -> pulumi.Output[Optional['outputs.KeyVaultContractPropertiesResponse']]:
        """
        KeyVault location details of the certificate.
        """
        return pulumi.get(self, "key_vault")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def subject(self) -> pulumi.Output[str]:
        """
        Subject attribute of the certificate.
        """
        return pulumi.get(self, "subject")

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Output[str]:
        """
        Thumbprint of the certificate.
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

