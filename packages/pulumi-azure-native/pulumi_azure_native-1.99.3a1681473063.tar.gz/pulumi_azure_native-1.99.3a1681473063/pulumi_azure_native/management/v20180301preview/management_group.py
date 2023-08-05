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

__all__ = ['ManagementGroupArgs', 'ManagementGroup']

@pulumi.input_type
class ManagementGroupArgs:
    def __init__(__self__, *,
                 details: Optional[pulumi.Input['CreateManagementGroupDetailsArgs']] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ManagementGroup resource.
        :param pulumi.Input['CreateManagementGroupDetailsArgs'] details: The details of a management group used during creation.
        :param pulumi.Input[str] display_name: The friendly name of the management group. If no value is passed then this  field will be set to the groupId.
        :param pulumi.Input[str] group_id: Management Group ID.
        :param pulumi.Input[str] name: The name of the management group. For example, 00000000-0000-0000-0000-000000000000
        """
        if details is not None:
            pulumi.set(__self__, "details", details)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if group_id is not None:
            pulumi.set(__self__, "group_id", group_id)
        if name is not None:
            pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def details(self) -> Optional[pulumi.Input['CreateManagementGroupDetailsArgs']]:
        """
        The details of a management group used during creation.
        """
        return pulumi.get(self, "details")

    @details.setter
    def details(self, value: Optional[pulumi.Input['CreateManagementGroupDetailsArgs']]):
        pulumi.set(self, "details", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The friendly name of the management group. If no value is passed then this  field will be set to the groupId.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="groupId")
    def group_id(self) -> Optional[pulumi.Input[str]]:
        """
        Management Group ID.
        """
        return pulumi.get(self, "group_id")

    @group_id.setter
    def group_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "group_id", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the management group. For example, 00000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)


warnings.warn("""Version 2018-03-01-preview will be removed in v2 of the provider.""", DeprecationWarning)


class ManagementGroup(pulumi.CustomResource):
    warnings.warn("""Version 2018-03-01-preview will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 details: Optional[pulumi.Input[pulumi.InputType['CreateManagementGroupDetailsArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The management group details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['CreateManagementGroupDetailsArgs']] details: The details of a management group used during creation.
        :param pulumi.Input[str] display_name: The friendly name of the management group. If no value is passed then this  field will be set to the groupId.
        :param pulumi.Input[str] group_id: Management Group ID.
        :param pulumi.Input[str] name: The name of the management group. For example, 00000000-0000-0000-0000-000000000000
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: Optional[ManagementGroupArgs] = None,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The management group details.

        :param str resource_name: The name of the resource.
        :param ManagementGroupArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ManagementGroupArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 details: Optional[pulumi.Input[pulumi.InputType['CreateManagementGroupDetailsArgs']]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 group_id: Optional[pulumi.Input[str]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        pulumi.log.warn("""ManagementGroup is deprecated: Version 2018-03-01-preview will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ManagementGroupArgs.__new__(ManagementGroupArgs)

            __props__.__dict__["details"] = details
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["group_id"] = group_id
            __props__.__dict__["name"] = name
            __props__.__dict__["children"] = None
            __props__.__dict__["roles"] = None
            __props__.__dict__["tenant_id"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:management:ManagementGroup"), pulumi.Alias(type_="azure-native:management/v20171101preview:ManagementGroup"), pulumi.Alias(type_="azure-native:management/v20180101preview:ManagementGroup"), pulumi.Alias(type_="azure-native:management/v20191101:ManagementGroup"), pulumi.Alias(type_="azure-native:management/v20200201:ManagementGroup"), pulumi.Alias(type_="azure-native:management/v20200501:ManagementGroup"), pulumi.Alias(type_="azure-native:management/v20201001:ManagementGroup"), pulumi.Alias(type_="azure-native:management/v20210401:ManagementGroup")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ManagementGroup, __self__).__init__(
            'azure-native:management/v20180301preview:ManagementGroup',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ManagementGroup':
        """
        Get an existing ManagementGroup resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ManagementGroupArgs.__new__(ManagementGroupArgs)

        __props__.__dict__["children"] = None
        __props__.__dict__["details"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["roles"] = None
        __props__.__dict__["tenant_id"] = None
        __props__.__dict__["type"] = None
        return ManagementGroup(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def children(self) -> pulumi.Output[Optional[Sequence['outputs.ManagementGroupChildInfoResponse']]]:
        """
        The list of children.
        """
        return pulumi.get(self, "children")

    @property
    @pulumi.getter
    def details(self) -> pulumi.Output[Optional['outputs.ManagementGroupDetailsResponse']]:
        """
        The details of a management group.
        """
        return pulumi.get(self, "details")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        The friendly name of the management group.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the management group. For example, 00000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def roles(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The role definitions associated with the management group.
        """
        return pulumi.get(self, "roles")

    @property
    @pulumi.getter(name="tenantId")
    def tenant_id(self) -> pulumi.Output[Optional[str]]:
        """
        The AAD Tenant ID associated with the management group. For example, 00000000-0000-0000-0000-000000000000
        """
        return pulumi.get(self, "tenant_id")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.  For example, /providers/Microsoft.Management/managementGroups
        """
        return pulumi.get(self, "type")

