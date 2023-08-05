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

__all__ = ['VirtualMachineImageTemplateArgs', 'VirtualMachineImageTemplate']

@pulumi.input_type
class VirtualMachineImageTemplateArgs:
    def __init__(__self__, *,
                 distribute: pulumi.Input[Sequence[pulumi.Input[Union['ImageTemplateManagedImageDistributorArgs', 'ImageTemplateSharedImageDistributorArgs', 'ImageTemplateVhdDistributorArgs']]]],
                 resource_group_name: pulumi.Input[str],
                 source: pulumi.Input[Union['ImageTemplateIsoSourceArgs', 'ImageTemplateManagedImageSourceArgs', 'ImageTemplatePlatformImageSourceArgs', 'ImageTemplateSharedImageVersionSourceArgs']],
                 build_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 customize: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ImageTemplateFileCustomizerArgs', 'ImageTemplatePowerShellCustomizerArgs', 'ImageTemplateRestartCustomizerArgs', 'ImageTemplateShellCustomizerArgs']]]]] = None,
                 identity: Optional[pulumi.Input['ImageTemplateIdentityArgs']] = None,
                 image_template_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_profile: Optional[pulumi.Input['ImageTemplateVmProfileArgs']] = None):
        """
        The set of arguments for constructing a VirtualMachineImageTemplate resource.
        :param pulumi.Input[Sequence[pulumi.Input[Union['ImageTemplateManagedImageDistributorArgs', 'ImageTemplateSharedImageDistributorArgs', 'ImageTemplateVhdDistributorArgs']]]] distribute: The distribution targets where the image output needs to go to.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union['ImageTemplateIsoSourceArgs', 'ImageTemplateManagedImageSourceArgs', 'ImageTemplatePlatformImageSourceArgs', 'ImageTemplateSharedImageVersionSourceArgs']] source: Specifies the properties used to describe the source image.
        :param pulumi.Input[int] build_timeout_in_minutes: Maximum duration to wait while building the image template. Omit or specify 0 to use the default (4 hours).
        :param pulumi.Input[Sequence[pulumi.Input[Union['ImageTemplateFileCustomizerArgs', 'ImageTemplatePowerShellCustomizerArgs', 'ImageTemplateRestartCustomizerArgs', 'ImageTemplateShellCustomizerArgs']]]] customize: Specifies the properties used to describe the customization steps of the image, like Image source etc
        :param pulumi.Input['ImageTemplateIdentityArgs'] identity: The identity of the image template, if configured.
        :param pulumi.Input[str] image_template_name: The name of the image Template
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input['ImageTemplateVmProfileArgs'] vm_profile: Describes how virtual machine is set up to build images
        """
        pulumi.set(__self__, "distribute", distribute)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source", source)
        if build_timeout_in_minutes is not None:
            pulumi.set(__self__, "build_timeout_in_minutes", build_timeout_in_minutes)
        if customize is not None:
            pulumi.set(__self__, "customize", customize)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if image_template_name is not None:
            pulumi.set(__self__, "image_template_name", image_template_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if vm_profile is not None:
            pulumi.set(__self__, "vm_profile", vm_profile)

    @property
    @pulumi.getter
    def distribute(self) -> pulumi.Input[Sequence[pulumi.Input[Union['ImageTemplateManagedImageDistributorArgs', 'ImageTemplateSharedImageDistributorArgs', 'ImageTemplateVhdDistributorArgs']]]]:
        """
        The distribution targets where the image output needs to go to.
        """
        return pulumi.get(self, "distribute")

    @distribute.setter
    def distribute(self, value: pulumi.Input[Sequence[pulumi.Input[Union['ImageTemplateManagedImageDistributorArgs', 'ImageTemplateSharedImageDistributorArgs', 'ImageTemplateVhdDistributorArgs']]]]):
        pulumi.set(self, "distribute", value)

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
    @pulumi.getter
    def source(self) -> pulumi.Input[Union['ImageTemplateIsoSourceArgs', 'ImageTemplateManagedImageSourceArgs', 'ImageTemplatePlatformImageSourceArgs', 'ImageTemplateSharedImageVersionSourceArgs']]:
        """
        Specifies the properties used to describe the source image.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input[Union['ImageTemplateIsoSourceArgs', 'ImageTemplateManagedImageSourceArgs', 'ImageTemplatePlatformImageSourceArgs', 'ImageTemplateSharedImageVersionSourceArgs']]):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="buildTimeoutInMinutes")
    def build_timeout_in_minutes(self) -> Optional[pulumi.Input[int]]:
        """
        Maximum duration to wait while building the image template. Omit or specify 0 to use the default (4 hours).
        """
        return pulumi.get(self, "build_timeout_in_minutes")

    @build_timeout_in_minutes.setter
    def build_timeout_in_minutes(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "build_timeout_in_minutes", value)

    @property
    @pulumi.getter
    def customize(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union['ImageTemplateFileCustomizerArgs', 'ImageTemplatePowerShellCustomizerArgs', 'ImageTemplateRestartCustomizerArgs', 'ImageTemplateShellCustomizerArgs']]]]]:
        """
        Specifies the properties used to describe the customization steps of the image, like Image source etc
        """
        return pulumi.get(self, "customize")

    @customize.setter
    def customize(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union['ImageTemplateFileCustomizerArgs', 'ImageTemplatePowerShellCustomizerArgs', 'ImageTemplateRestartCustomizerArgs', 'ImageTemplateShellCustomizerArgs']]]]]):
        pulumi.set(self, "customize", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ImageTemplateIdentityArgs']]:
        """
        The identity of the image template, if configured.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ImageTemplateIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="imageTemplateName")
    def image_template_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the image Template
        """
        return pulumi.get(self, "image_template_name")

    @image_template_name.setter
    def image_template_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "image_template_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

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
    @pulumi.getter(name="vmProfile")
    def vm_profile(self) -> Optional[pulumi.Input['ImageTemplateVmProfileArgs']]:
        """
        Describes how virtual machine is set up to build images
        """
        return pulumi.get(self, "vm_profile")

    @vm_profile.setter
    def vm_profile(self, value: Optional[pulumi.Input['ImageTemplateVmProfileArgs']]):
        pulumi.set(self, "vm_profile", value)


warnings.warn("""Version 2019-05-01-preview will be removed in v2 of the provider.""", DeprecationWarning)


class VirtualMachineImageTemplate(pulumi.CustomResource):
    warnings.warn("""Version 2019-05-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 build_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 customize: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['ImageTemplateFileCustomizerArgs'], pulumi.InputType['ImageTemplatePowerShellCustomizerArgs'], pulumi.InputType['ImageTemplateRestartCustomizerArgs'], pulumi.InputType['ImageTemplateShellCustomizerArgs']]]]]] = None,
                 distribute: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['ImageTemplateManagedImageDistributorArgs'], pulumi.InputType['ImageTemplateSharedImageDistributorArgs'], pulumi.InputType['ImageTemplateVhdDistributorArgs']]]]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ImageTemplateIdentityArgs']]] = None,
                 image_template_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union[pulumi.InputType['ImageTemplateIsoSourceArgs'], pulumi.InputType['ImageTemplateManagedImageSourceArgs'], pulumi.InputType['ImageTemplatePlatformImageSourceArgs'], pulumi.InputType['ImageTemplateSharedImageVersionSourceArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_profile: Optional[pulumi.Input[pulumi.InputType['ImageTemplateVmProfileArgs']]] = None,
                 __props__=None):
        """
        Image template is an ARM resource managed by Microsoft.VirtualMachineImages provider

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[int] build_timeout_in_minutes: Maximum duration to wait while building the image template. Omit or specify 0 to use the default (4 hours).
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['ImageTemplateFileCustomizerArgs'], pulumi.InputType['ImageTemplatePowerShellCustomizerArgs'], pulumi.InputType['ImageTemplateRestartCustomizerArgs'], pulumi.InputType['ImageTemplateShellCustomizerArgs']]]]] customize: Specifies the properties used to describe the customization steps of the image, like Image source etc
        :param pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['ImageTemplateManagedImageDistributorArgs'], pulumi.InputType['ImageTemplateSharedImageDistributorArgs'], pulumi.InputType['ImageTemplateVhdDistributorArgs']]]]] distribute: The distribution targets where the image output needs to go to.
        :param pulumi.Input[pulumi.InputType['ImageTemplateIdentityArgs']] identity: The identity of the image template, if configured.
        :param pulumi.Input[str] image_template_name: The name of the image Template
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Union[pulumi.InputType['ImageTemplateIsoSourceArgs'], pulumi.InputType['ImageTemplateManagedImageSourceArgs'], pulumi.InputType['ImageTemplatePlatformImageSourceArgs'], pulumi.InputType['ImageTemplateSharedImageVersionSourceArgs']]] source: Specifies the properties used to describe the source image.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        :param pulumi.Input[pulumi.InputType['ImageTemplateVmProfileArgs']] vm_profile: Describes how virtual machine is set up to build images
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: VirtualMachineImageTemplateArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Image template is an ARM resource managed by Microsoft.VirtualMachineImages provider

        :param str resource_name: The name of the resource.
        :param VirtualMachineImageTemplateArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(VirtualMachineImageTemplateArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 build_timeout_in_minutes: Optional[pulumi.Input[int]] = None,
                 customize: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['ImageTemplateFileCustomizerArgs'], pulumi.InputType['ImageTemplatePowerShellCustomizerArgs'], pulumi.InputType['ImageTemplateRestartCustomizerArgs'], pulumi.InputType['ImageTemplateShellCustomizerArgs']]]]]] = None,
                 distribute: Optional[pulumi.Input[Sequence[pulumi.Input[Union[pulumi.InputType['ImageTemplateManagedImageDistributorArgs'], pulumi.InputType['ImageTemplateSharedImageDistributorArgs'], pulumi.InputType['ImageTemplateVhdDistributorArgs']]]]]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ImageTemplateIdentityArgs']]] = None,
                 image_template_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[Union[pulumi.InputType['ImageTemplateIsoSourceArgs'], pulumi.InputType['ImageTemplateManagedImageSourceArgs'], pulumi.InputType['ImageTemplatePlatformImageSourceArgs'], pulumi.InputType['ImageTemplateSharedImageVersionSourceArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 vm_profile: Optional[pulumi.Input[pulumi.InputType['ImageTemplateVmProfileArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""VirtualMachineImageTemplate is deprecated: Version 2019-05-01-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = VirtualMachineImageTemplateArgs.__new__(VirtualMachineImageTemplateArgs)

            __props__.__dict__["build_timeout_in_minutes"] = build_timeout_in_minutes
            __props__.__dict__["customize"] = customize
            if distribute is None and not opts.urn:
                raise TypeError("Missing required property 'distribute'")
            __props__.__dict__["distribute"] = distribute
            __props__.__dict__["identity"] = identity
            __props__.__dict__["image_template_name"] = image_template_name
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["vm_profile"] = vm_profile
            __props__.__dict__["last_run_status"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_error"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:virtualmachineimages:VirtualMachineImageTemplate"), pulumi.Alias(type_="azure-native:virtualmachineimages/v20180201preview:VirtualMachineImageTemplate"), pulumi.Alias(type_="azure-native:virtualmachineimages/v20190201preview:VirtualMachineImageTemplate"), pulumi.Alias(type_="azure-native:virtualmachineimages/v20200214:VirtualMachineImageTemplate"), pulumi.Alias(type_="azure-native:virtualmachineimages/v20211001:VirtualMachineImageTemplate"), pulumi.Alias(type_="azure-native:virtualmachineimages/v20220214:VirtualMachineImageTemplate"), pulumi.Alias(type_="azure-native:virtualmachineimages/v20220701:VirtualMachineImageTemplate")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(VirtualMachineImageTemplate, __self__).__init__(
            'azure-native:virtualmachineimages/v20190501preview:VirtualMachineImageTemplate',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'VirtualMachineImageTemplate':
        """
        Get an existing VirtualMachineImageTemplate resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = VirtualMachineImageTemplateArgs.__new__(VirtualMachineImageTemplateArgs)

        __props__.__dict__["build_timeout_in_minutes"] = None
        __props__.__dict__["customize"] = None
        __props__.__dict__["distribute"] = None
        __props__.__dict__["identity"] = None
        __props__.__dict__["last_run_status"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_error"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["vm_profile"] = None
        return VirtualMachineImageTemplate(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="buildTimeoutInMinutes")
    def build_timeout_in_minutes(self) -> pulumi.Output[Optional[int]]:
        """
        Maximum duration to wait while building the image template. Omit or specify 0 to use the default (4 hours).
        """
        return pulumi.get(self, "build_timeout_in_minutes")

    @property
    @pulumi.getter
    def customize(self) -> pulumi.Output[Optional[Sequence[Any]]]:
        """
        Specifies the properties used to describe the customization steps of the image, like Image source etc
        """
        return pulumi.get(self, "customize")

    @property
    @pulumi.getter
    def distribute(self) -> pulumi.Output[Sequence[Any]]:
        """
        The distribution targets where the image output needs to go to.
        """
        return pulumi.get(self, "distribute")

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ImageTemplateIdentityResponse']]:
        """
        The identity of the image template, if configured.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter(name="lastRunStatus")
    def last_run_status(self) -> pulumi.Output['outputs.ImageTemplateLastRunStatusResponse']:
        """
        State of 'run' that is currently executing or was last executed.
        """
        return pulumi.get(self, "last_run_status")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningError")
    def provisioning_error(self) -> pulumi.Output['outputs.ProvisioningErrorResponse']:
        """
        Provisioning error, if any
        """
        return pulumi.get(self, "provisioning_error")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Provisioning state of the resource
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Any]:
        """
        Specifies the properties used to describe the source image.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="vmProfile")
    def vm_profile(self) -> pulumi.Output[Optional['outputs.ImageTemplateVmProfileResponse']]:
        """
        Describes how virtual machine is set up to build images
        """
        return pulumi.get(self, "vm_profile")

