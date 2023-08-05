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
                 cer_blob: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 hosting_environment_profile: Optional[pulumi.Input['HostingEnvironmentProfileArgs']] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 issue_date: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 pfx_blob: Optional[pulumi.Input[str]] = None,
                 public_key_hash: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 subject_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 valid: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a Certificate resource.
        :param pulumi.Input[str] resource_group_name: Name of the resource group
        :param pulumi.Input[str] cer_blob: Raw bytes of .cer file
        :param pulumi.Input[str] expiration_date: Certificate expiration date
        :param pulumi.Input[str] friendly_name: Friendly name of the certificate
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_names: Host names the certificate applies to
        :param pulumi.Input['HostingEnvironmentProfileArgs'] hosting_environment_profile: Specification for the hosting environment (App Service Environment) to use for the certificate
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] issue_date: Certificate issue Date
        :param pulumi.Input[str] issuer: Certificate issuer
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] password: Certificate password
        :param pulumi.Input[str] pfx_blob: Pfx blob
        :param pulumi.Input[str] public_key_hash: Public key hash
        :param pulumi.Input[str] self_link: Self link
        :param pulumi.Input[str] site_name: App name
        :param pulumi.Input[str] subject_name: Subject name of the certificate
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] thumbprint: Certificate thumbprint
        :param pulumi.Input[str] type: Resource type
        :param pulumi.Input[bool] valid: Is the certificate valid?
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if cer_blob is not None:
            pulumi.set(__self__, "cer_blob", cer_blob)
        if expiration_date is not None:
            pulumi.set(__self__, "expiration_date", expiration_date)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if host_names is not None:
            pulumi.set(__self__, "host_names", host_names)
        if hosting_environment_profile is not None:
            pulumi.set(__self__, "hosting_environment_profile", hosting_environment_profile)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if issue_date is not None:
            pulumi.set(__self__, "issue_date", issue_date)
        if issuer is not None:
            pulumi.set(__self__, "issuer", issuer)
        if kind is not None:
            pulumi.set(__self__, "kind", kind)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if password is not None:
            pulumi.set(__self__, "password", password)
        if pfx_blob is not None:
            pulumi.set(__self__, "pfx_blob", pfx_blob)
        if public_key_hash is not None:
            pulumi.set(__self__, "public_key_hash", public_key_hash)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if site_name is not None:
            pulumi.set(__self__, "site_name", site_name)
        if subject_name is not None:
            pulumi.set(__self__, "subject_name", subject_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if thumbprint is not None:
            pulumi.set(__self__, "thumbprint", thumbprint)
        if type is not None:
            pulumi.set(__self__, "type", type)
        if valid is not None:
            pulumi.set(__self__, "valid", valid)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the resource group
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="cerBlob")
    def cer_blob(self) -> Optional[pulumi.Input[str]]:
        """
        Raw bytes of .cer file
        """
        return pulumi.get(self, "cer_blob")

    @cer_blob.setter
    def cer_blob(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cer_blob", value)

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate expiration date
        """
        return pulumi.get(self, "expiration_date")

    @expiration_date.setter
    def expiration_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration_date", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the certificate
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="hostNames")
    def host_names(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Host names the certificate applies to
        """
        return pulumi.get(self, "host_names")

    @host_names.setter
    def host_names(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "host_names", value)

    @property
    @pulumi.getter(name="hostingEnvironmentProfile")
    def hosting_environment_profile(self) -> Optional[pulumi.Input['HostingEnvironmentProfileArgs']]:
        """
        Specification for the hosting environment (App Service Environment) to use for the certificate
        """
        return pulumi.get(self, "hosting_environment_profile")

    @hosting_environment_profile.setter
    def hosting_environment_profile(self, value: Optional[pulumi.Input['HostingEnvironmentProfileArgs']]):
        pulumi.set(self, "hosting_environment_profile", value)

    @property
    @pulumi.getter
    def id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter(name="issueDate")
    def issue_date(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate issue Date
        """
        return pulumi.get(self, "issue_date")

    @issue_date.setter
    def issue_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issue_date", value)

    @property
    @pulumi.getter
    def issuer(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate issuer
        """
        return pulumi.get(self, "issuer")

    @issuer.setter
    def issuer(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issuer", value)

    @property
    @pulumi.getter
    def kind(self) -> Optional[pulumi.Input[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def password(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate password
        """
        return pulumi.get(self, "password")

    @password.setter
    def password(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "password", value)

    @property
    @pulumi.getter(name="pfxBlob")
    def pfx_blob(self) -> Optional[pulumi.Input[str]]:
        """
        Pfx blob
        """
        return pulumi.get(self, "pfx_blob")

    @pfx_blob.setter
    def pfx_blob(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pfx_blob", value)

    @property
    @pulumi.getter(name="publicKeyHash")
    def public_key_hash(self) -> Optional[pulumi.Input[str]]:
        """
        Public key hash
        """
        return pulumi.get(self, "public_key_hash")

    @public_key_hash.setter
    def public_key_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key_hash", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        Self link
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> Optional[pulumi.Input[str]]:
        """
        App name
        """
        return pulumi.get(self, "site_name")

    @site_name.setter
    def site_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "site_name", value)

    @property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> Optional[pulumi.Input[str]]:
        """
        Subject name of the certificate
        """
        return pulumi.get(self, "subject_name")

    @subject_name.setter
    def subject_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subject_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def thumbprint(self) -> Optional[pulumi.Input[str]]:
        """
        Certificate thumbprint
        """
        return pulumi.get(self, "thumbprint")

    @thumbprint.setter
    def thumbprint(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "thumbprint", value)

    @property
    @pulumi.getter
    def type(self) -> Optional[pulumi.Input[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @type.setter
    def type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "type", value)

    @property
    @pulumi.getter
    def valid(self) -> Optional[pulumi.Input[bool]]:
        """
        Is the certificate valid?
        """
        return pulumi.get(self, "valid")

    @valid.setter
    def valid(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "valid", value)


warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)


class Certificate(pulumi.CustomResource):
    warnings.warn("""Version 2015-08-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cer_blob: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 hosting_environment_profile: Optional[pulumi.Input[pulumi.InputType['HostingEnvironmentProfileArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 issue_date: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 pfx_blob: Optional[pulumi.Input[str]] = None,
                 public_key_hash: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 subject_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 valid: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        App certificate

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cer_blob: Raw bytes of .cer file
        :param pulumi.Input[str] expiration_date: Certificate expiration date
        :param pulumi.Input[str] friendly_name: Friendly name of the certificate
        :param pulumi.Input[Sequence[pulumi.Input[str]]] host_names: Host names the certificate applies to
        :param pulumi.Input[pulumi.InputType['HostingEnvironmentProfileArgs']] hosting_environment_profile: Specification for the hosting environment (App Service Environment) to use for the certificate
        :param pulumi.Input[str] id: Resource Id
        :param pulumi.Input[str] issue_date: Certificate issue Date
        :param pulumi.Input[str] issuer: Certificate issuer
        :param pulumi.Input[str] kind: Kind of resource
        :param pulumi.Input[str] location: Resource Location
        :param pulumi.Input[str] name: Resource Name
        :param pulumi.Input[str] password: Certificate password
        :param pulumi.Input[str] pfx_blob: Pfx blob
        :param pulumi.Input[str] public_key_hash: Public key hash
        :param pulumi.Input[str] resource_group_name: Name of the resource group
        :param pulumi.Input[str] self_link: Self link
        :param pulumi.Input[str] site_name: App name
        :param pulumi.Input[str] subject_name: Subject name of the certificate
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[str] thumbprint: Certificate thumbprint
        :param pulumi.Input[str] type: Resource type
        :param pulumi.Input[bool] valid: Is the certificate valid?
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: CertificateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        App certificate

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
                 cer_blob: Optional[pulumi.Input[str]] = None,
                 expiration_date: Optional[pulumi.Input[str]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 host_names: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 hosting_environment_profile: Optional[pulumi.Input[pulumi.InputType['HostingEnvironmentProfileArgs']]] = None,
                 id: Optional[pulumi.Input[str]] = None,
                 issue_date: Optional[pulumi.Input[str]] = None,
                 issuer: Optional[pulumi.Input[str]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 password: Optional[pulumi.Input[str]] = None,
                 pfx_blob: Optional[pulumi.Input[str]] = None,
                 public_key_hash: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 site_name: Optional[pulumi.Input[str]] = None,
                 subject_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 thumbprint: Optional[pulumi.Input[str]] = None,
                 type: Optional[pulumi.Input[str]] = None,
                 valid: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        pulumi.log.warn("""Certificate is deprecated: Version 2015-08-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = CertificateArgs.__new__(CertificateArgs)

            __props__.__dict__["cer_blob"] = cer_blob
            __props__.__dict__["expiration_date"] = expiration_date
            __props__.__dict__["friendly_name"] = friendly_name
            __props__.__dict__["host_names"] = host_names
            __props__.__dict__["hosting_environment_profile"] = hosting_environment_profile
            __props__.__dict__["id"] = id
            __props__.__dict__["issue_date"] = issue_date
            __props__.__dict__["issuer"] = issuer
            __props__.__dict__["kind"] = kind
            __props__.__dict__["location"] = location
            __props__.__dict__["name"] = name
            __props__.__dict__["password"] = password
            __props__.__dict__["pfx_blob"] = pfx_blob
            __props__.__dict__["public_key_hash"] = public_key_hash
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["self_link"] = self_link
            __props__.__dict__["site_name"] = site_name
            __props__.__dict__["subject_name"] = subject_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["thumbprint"] = thumbprint
            __props__.__dict__["type"] = type
            __props__.__dict__["valid"] = valid
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:web:Certificate"), pulumi.Alias(type_="azure-native:web/v20160301:Certificate"), pulumi.Alias(type_="azure-native:web/v20180201:Certificate"), pulumi.Alias(type_="azure-native:web/v20181101:Certificate"), pulumi.Alias(type_="azure-native:web/v20190801:Certificate"), pulumi.Alias(type_="azure-native:web/v20200601:Certificate"), pulumi.Alias(type_="azure-native:web/v20200901:Certificate"), pulumi.Alias(type_="azure-native:web/v20201001:Certificate"), pulumi.Alias(type_="azure-native:web/v20201201:Certificate"), pulumi.Alias(type_="azure-native:web/v20210101:Certificate"), pulumi.Alias(type_="azure-native:web/v20210115:Certificate"), pulumi.Alias(type_="azure-native:web/v20210201:Certificate"), pulumi.Alias(type_="azure-native:web/v20210301:Certificate"), pulumi.Alias(type_="azure-native:web/v20220301:Certificate"), pulumi.Alias(type_="azure-native:web/v20220901:Certificate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Certificate, __self__).__init__(
            'azure-native:web/v20150801:Certificate',
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

        __props__.__dict__["cer_blob"] = None
        __props__.__dict__["expiration_date"] = None
        __props__.__dict__["friendly_name"] = None
        __props__.__dict__["host_names"] = None
        __props__.__dict__["hosting_environment_profile"] = None
        __props__.__dict__["issue_date"] = None
        __props__.__dict__["issuer"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["password"] = None
        __props__.__dict__["pfx_blob"] = None
        __props__.__dict__["public_key_hash"] = None
        __props__.__dict__["self_link"] = None
        __props__.__dict__["site_name"] = None
        __props__.__dict__["subject_name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["thumbprint"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["valid"] = None
        return Certificate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="cerBlob")
    def cer_blob(self) -> pulumi.Output[Optional[str]]:
        """
        Raw bytes of .cer file
        """
        return pulumi.get(self, "cer_blob")

    @property
    @pulumi.getter(name="expirationDate")
    def expiration_date(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate expiration date
        """
        return pulumi.get(self, "expiration_date")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> pulumi.Output[Optional[str]]:
        """
        Friendly name of the certificate
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostNames")
    def host_names(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        Host names the certificate applies to
        """
        return pulumi.get(self, "host_names")

    @property
    @pulumi.getter(name="hostingEnvironmentProfile")
    def hosting_environment_profile(self) -> pulumi.Output[Optional['outputs.HostingEnvironmentProfileResponse']]:
        """
        Specification for the hosting environment (App Service Environment) to use for the certificate
        """
        return pulumi.get(self, "hosting_environment_profile")

    @property
    @pulumi.getter(name="issueDate")
    def issue_date(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate issue Date
        """
        return pulumi.get(self, "issue_date")

    @property
    @pulumi.getter
    def issuer(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate issuer
        """
        return pulumi.get(self, "issuer")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[Optional[str]]:
        """
        Kind of resource
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate password
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="pfxBlob")
    def pfx_blob(self) -> pulumi.Output[Optional[str]]:
        """
        Pfx blob
        """
        return pulumi.get(self, "pfx_blob")

    @property
    @pulumi.getter(name="publicKeyHash")
    def public_key_hash(self) -> pulumi.Output[Optional[str]]:
        """
        Public key hash
        """
        return pulumi.get(self, "public_key_hash")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[Optional[str]]:
        """
        Self link
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="siteName")
    def site_name(self) -> pulumi.Output[Optional[str]]:
        """
        App name
        """
        return pulumi.get(self, "site_name")

    @property
    @pulumi.getter(name="subjectName")
    def subject_name(self) -> pulumi.Output[Optional[str]]:
        """
        Subject name of the certificate
        """
        return pulumi.get(self, "subject_name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def thumbprint(self) -> pulumi.Output[Optional[str]]:
        """
        Certificate thumbprint
        """
        return pulumi.get(self, "thumbprint")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[Optional[str]]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def valid(self) -> pulumi.Output[Optional[bool]]:
        """
        Is the certificate valid?
        """
        return pulumi.get(self, "valid")

