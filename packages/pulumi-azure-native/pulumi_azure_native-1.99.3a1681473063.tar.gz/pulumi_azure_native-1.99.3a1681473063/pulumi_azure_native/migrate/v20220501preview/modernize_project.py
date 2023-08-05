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

__all__ = ['ModernizeProjectArgs', 'ModernizeProject']

@pulumi.input_type
class ModernizeProjectArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 identity: Optional[pulumi.Input['ResourceIdentityArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 modernize_project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input['ModernizeProjectModelPropertiesArgs']] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a ModernizeProject resource.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input[str] location: Gets or sets the location of the modernizeProject.
        :param pulumi.Input[str] modernize_project_name: ModernizeProject Name.
        :param pulumi.Input['ModernizeProjectModelPropertiesArgs'] properties: ModernizeProject properties.
        :param pulumi.Input[str] subscription_id: Azure Subscription Id in which project was created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the resource tags.
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if modernize_project_name is not None:
            pulumi.set(__self__, "modernize_project_name", modernize_project_name)
        if properties is not None:
            pulumi.set(__self__, "properties", properties)
        if subscription_id is not None:
            pulumi.set(__self__, "subscription_id", subscription_id)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of the Azure Resource Group that project is part of.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ResourceIdentityArgs']]:
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ResourceIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the location of the modernizeProject.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="modernizeProjectName")
    def modernize_project_name(self) -> Optional[pulumi.Input[str]]:
        """
        ModernizeProject Name.
        """
        return pulumi.get(self, "modernize_project_name")

    @modernize_project_name.setter
    def modernize_project_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "modernize_project_name", value)

    @property
    @pulumi.getter
    def properties(self) -> Optional[pulumi.Input['ModernizeProjectModelPropertiesArgs']]:
        """
        ModernizeProject properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: Optional[pulumi.Input['ModernizeProjectModelPropertiesArgs']]):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="subscriptionId")
    def subscription_id(self) -> Optional[pulumi.Input[str]]:
        """
        Azure Subscription Id in which project was created.
        """
        return pulumi.get(self, "subscription_id")

    @subscription_id.setter
    def subscription_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subscription_id", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class ModernizeProject(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ResourceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 modernize_project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ModernizeProjectModelPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        ModernizeProject model.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] location: Gets or sets the location of the modernizeProject.
        :param pulumi.Input[str] modernize_project_name: ModernizeProject Name.
        :param pulumi.Input[pulumi.InputType['ModernizeProjectModelPropertiesArgs']] properties: ModernizeProject properties.
        :param pulumi.Input[str] resource_group_name: Name of the Azure Resource Group that project is part of.
        :param pulumi.Input[str] subscription_id: Azure Subscription Id in which project was created.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ModernizeProjectArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ModernizeProject model.

        :param str resource_name: The name of the resource.
        :param ModernizeProjectArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ModernizeProjectArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ResourceIdentityArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 modernize_project_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['ModernizeProjectModelPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 subscription_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ModernizeProjectArgs.__new__(ModernizeProjectArgs)

            __props__.__dict__["identity"] = identity
            __props__.__dict__["location"] = location
            __props__.__dict__["modernize_project_name"] = modernize_project_name
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["subscription_id"] = subscription_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        super(ModernizeProject, __self__).__init__(
            'azure-native:migrate/v20220501preview:ModernizeProject',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ModernizeProject':
        """
        Get an existing ModernizeProject resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ModernizeProjectArgs.__new__(ModernizeProjectArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return ModernizeProject(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ResourceIdentityResponse']]:
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the location of the modernizeProject.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Gets or sets the name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.ModernizeProjectModelPropertiesResponse']:
        """
        ModernizeProject properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.ModernizeProjectModelResponseSystemData']:
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Gets or sets the resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Gets or sets the type of the resource.
        """
        return pulumi.get(self, "type")

