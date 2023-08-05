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
from ._enums import *
from ._inputs import *

__all__ = ['StreamingPolicyArgs', 'StreamingPolicy']

@pulumi.input_type
class StreamingPolicyArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 common_encryption_cbcs: Optional[pulumi.Input['CommonEncryptionCbcsArgs']] = None,
                 common_encryption_cenc: Optional[pulumi.Input['CommonEncryptionCencArgs']] = None,
                 default_content_key_policy_name: Optional[pulumi.Input[str]] = None,
                 envelope_encryption: Optional[pulumi.Input['EnvelopeEncryptionArgs']] = None,
                 no_encryption: Optional[pulumi.Input['NoEncryptionArgs']] = None,
                 streaming_policy_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StreamingPolicy resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input['CommonEncryptionCbcsArgs'] common_encryption_cbcs: Configuration of CommonEncryptionCbcs
        :param pulumi.Input['CommonEncryptionCencArgs'] common_encryption_cenc: Configuration of CommonEncryptionCenc
        :param pulumi.Input[str] default_content_key_policy_name: Default ContentKey used by current Streaming Policy
        :param pulumi.Input['EnvelopeEncryptionArgs'] envelope_encryption: Configuration of EnvelopeEncryption
        :param pulumi.Input['NoEncryptionArgs'] no_encryption: Configurations of NoEncryption
        :param pulumi.Input[str] streaming_policy_name: The Streaming Policy name.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if common_encryption_cbcs is not None:
            pulumi.set(__self__, "common_encryption_cbcs", common_encryption_cbcs)
        if common_encryption_cenc is not None:
            pulumi.set(__self__, "common_encryption_cenc", common_encryption_cenc)
        if default_content_key_policy_name is not None:
            pulumi.set(__self__, "default_content_key_policy_name", default_content_key_policy_name)
        if envelope_encryption is not None:
            pulumi.set(__self__, "envelope_encryption", envelope_encryption)
        if no_encryption is not None:
            pulumi.set(__self__, "no_encryption", no_encryption)
        if streaming_policy_name is not None:
            pulumi.set(__self__, "streaming_policy_name", streaming_policy_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Media Services account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="commonEncryptionCbcs")
    def common_encryption_cbcs(self) -> Optional[pulumi.Input['CommonEncryptionCbcsArgs']]:
        """
        Configuration of CommonEncryptionCbcs
        """
        return pulumi.get(self, "common_encryption_cbcs")

    @common_encryption_cbcs.setter
    def common_encryption_cbcs(self, value: Optional[pulumi.Input['CommonEncryptionCbcsArgs']]):
        pulumi.set(self, "common_encryption_cbcs", value)

    @property
    @pulumi.getter(name="commonEncryptionCenc")
    def common_encryption_cenc(self) -> Optional[pulumi.Input['CommonEncryptionCencArgs']]:
        """
        Configuration of CommonEncryptionCenc
        """
        return pulumi.get(self, "common_encryption_cenc")

    @common_encryption_cenc.setter
    def common_encryption_cenc(self, value: Optional[pulumi.Input['CommonEncryptionCencArgs']]):
        pulumi.set(self, "common_encryption_cenc", value)

    @property
    @pulumi.getter(name="defaultContentKeyPolicyName")
    def default_content_key_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        Default ContentKey used by current Streaming Policy
        """
        return pulumi.get(self, "default_content_key_policy_name")

    @default_content_key_policy_name.setter
    def default_content_key_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_content_key_policy_name", value)

    @property
    @pulumi.getter(name="envelopeEncryption")
    def envelope_encryption(self) -> Optional[pulumi.Input['EnvelopeEncryptionArgs']]:
        """
        Configuration of EnvelopeEncryption
        """
        return pulumi.get(self, "envelope_encryption")

    @envelope_encryption.setter
    def envelope_encryption(self, value: Optional[pulumi.Input['EnvelopeEncryptionArgs']]):
        pulumi.set(self, "envelope_encryption", value)

    @property
    @pulumi.getter(name="noEncryption")
    def no_encryption(self) -> Optional[pulumi.Input['NoEncryptionArgs']]:
        """
        Configurations of NoEncryption
        """
        return pulumi.get(self, "no_encryption")

    @no_encryption.setter
    def no_encryption(self, value: Optional[pulumi.Input['NoEncryptionArgs']]):
        pulumi.set(self, "no_encryption", value)

    @property
    @pulumi.getter(name="streamingPolicyName")
    def streaming_policy_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Streaming Policy name.
        """
        return pulumi.get(self, "streaming_policy_name")

    @streaming_policy_name.setter
    def streaming_policy_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "streaming_policy_name", value)


class StreamingPolicy(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 common_encryption_cbcs: Optional[pulumi.Input[pulumi.InputType['CommonEncryptionCbcsArgs']]] = None,
                 common_encryption_cenc: Optional[pulumi.Input[pulumi.InputType['CommonEncryptionCencArgs']]] = None,
                 default_content_key_policy_name: Optional[pulumi.Input[str]] = None,
                 envelope_encryption: Optional[pulumi.Input[pulumi.InputType['EnvelopeEncryptionArgs']]] = None,
                 no_encryption: Optional[pulumi.Input[pulumi.InputType['NoEncryptionArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 streaming_policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A Streaming Policy resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[pulumi.InputType['CommonEncryptionCbcsArgs']] common_encryption_cbcs: Configuration of CommonEncryptionCbcs
        :param pulumi.Input[pulumi.InputType['CommonEncryptionCencArgs']] common_encryption_cenc: Configuration of CommonEncryptionCenc
        :param pulumi.Input[str] default_content_key_policy_name: Default ContentKey used by current Streaming Policy
        :param pulumi.Input[pulumi.InputType['EnvelopeEncryptionArgs']] envelope_encryption: Configuration of EnvelopeEncryption
        :param pulumi.Input[pulumi.InputType['NoEncryptionArgs']] no_encryption: Configurations of NoEncryption
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[str] streaming_policy_name: The Streaming Policy name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StreamingPolicyArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A Streaming Policy resource

        :param str resource_name: The name of the resource.
        :param StreamingPolicyArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StreamingPolicyArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 common_encryption_cbcs: Optional[pulumi.Input[pulumi.InputType['CommonEncryptionCbcsArgs']]] = None,
                 common_encryption_cenc: Optional[pulumi.Input[pulumi.InputType['CommonEncryptionCencArgs']]] = None,
                 default_content_key_policy_name: Optional[pulumi.Input[str]] = None,
                 envelope_encryption: Optional[pulumi.Input[pulumi.InputType['EnvelopeEncryptionArgs']]] = None,
                 no_encryption: Optional[pulumi.Input[pulumi.InputType['NoEncryptionArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 streaming_policy_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StreamingPolicyArgs.__new__(StreamingPolicyArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["common_encryption_cbcs"] = common_encryption_cbcs
            __props__.__dict__["common_encryption_cenc"] = common_encryption_cenc
            __props__.__dict__["default_content_key_policy_name"] = default_content_key_policy_name
            __props__.__dict__["envelope_encryption"] = envelope_encryption
            __props__.__dict__["no_encryption"] = no_encryption
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["streaming_policy_name"] = streaming_policy_name
            __props__.__dict__["created"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:media:StreamingPolicy"), pulumi.Alias(type_="azure-native:media/v20180330preview:StreamingPolicy"), pulumi.Alias(type_="azure-native:media/v20180601preview:StreamingPolicy"), pulumi.Alias(type_="azure-native:media/v20180701:StreamingPolicy"), pulumi.Alias(type_="azure-native:media/v20200501:StreamingPolicy"), pulumi.Alias(type_="azure-native:media/v20210601:StreamingPolicy"), pulumi.Alias(type_="azure-native:media/v20211101:StreamingPolicy"), pulumi.Alias(type_="azure-native:media/v20230101:StreamingPolicy")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StreamingPolicy, __self__).__init__(
            'azure-native:media/v20220801:StreamingPolicy',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StreamingPolicy':
        """
        Get an existing StreamingPolicy resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StreamingPolicyArgs.__new__(StreamingPolicyArgs)

        __props__.__dict__["common_encryption_cbcs"] = None
        __props__.__dict__["common_encryption_cenc"] = None
        __props__.__dict__["created"] = None
        __props__.__dict__["default_content_key_policy_name"] = None
        __props__.__dict__["envelope_encryption"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["no_encryption"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return StreamingPolicy(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="commonEncryptionCbcs")
    def common_encryption_cbcs(self) -> pulumi.Output[Optional['outputs.CommonEncryptionCbcsResponse']]:
        """
        Configuration of CommonEncryptionCbcs
        """
        return pulumi.get(self, "common_encryption_cbcs")

    @property
    @pulumi.getter(name="commonEncryptionCenc")
    def common_encryption_cenc(self) -> pulumi.Output[Optional['outputs.CommonEncryptionCencResponse']]:
        """
        Configuration of CommonEncryptionCenc
        """
        return pulumi.get(self, "common_encryption_cenc")

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        Creation time of Streaming Policy
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="defaultContentKeyPolicyName")
    def default_content_key_policy_name(self) -> pulumi.Output[Optional[str]]:
        """
        Default ContentKey used by current Streaming Policy
        """
        return pulumi.get(self, "default_content_key_policy_name")

    @property
    @pulumi.getter(name="envelopeEncryption")
    def envelope_encryption(self) -> pulumi.Output[Optional['outputs.EnvelopeEncryptionResponse']]:
        """
        Configuration of EnvelopeEncryption
        """
        return pulumi.get(self, "envelope_encryption")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="noEncryption")
    def no_encryption(self) -> pulumi.Output[Optional['outputs.NoEncryptionResponse']]:
        """
        Configurations of NoEncryption
        """
        return pulumi.get(self, "no_encryption")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

