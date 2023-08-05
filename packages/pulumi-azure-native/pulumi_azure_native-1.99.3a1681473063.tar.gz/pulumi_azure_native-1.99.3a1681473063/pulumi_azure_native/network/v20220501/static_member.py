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

__all__ = ['StaticMemberArgs', 'StaticMember']

@pulumi.input_type
class StaticMemberArgs:
    def __init__(__self__, *,
                 network_group_name: pulumi.Input[str],
                 network_manager_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 resource_id: Optional[pulumi.Input[str]] = None,
                 static_member_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a StaticMember resource.
        :param pulumi.Input[str] network_group_name: The name of the network group.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_id: Resource Id.
        :param pulumi.Input[str] static_member_name: The name of the static member.
        """
        pulumi.set(__self__, "network_group_name", network_group_name)
        pulumi.set(__self__, "network_manager_name", network_manager_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)
        if static_member_name is not None:
            pulumi.set(__self__, "static_member_name", static_member_name)

    @property
    @pulumi.getter(name="networkGroupName")
    def network_group_name(self) -> pulumi.Input[str]:
        """
        The name of the network group.
        """
        return pulumi.get(self, "network_group_name")

    @network_group_name.setter
    def network_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_group_name", value)

    @property
    @pulumi.getter(name="networkManagerName")
    def network_manager_name(self) -> pulumi.Input[str]:
        """
        The name of the network manager.
        """
        return pulumi.get(self, "network_manager_name")

    @network_manager_name.setter
    def network_manager_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_manager_name", value)

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
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        Resource Id.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)

    @property
    @pulumi.getter(name="staticMemberName")
    def static_member_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the static member.
        """
        return pulumi.get(self, "static_member_name")

    @static_member_name.setter
    def static_member_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "static_member_name", value)


class StaticMember(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_group_name: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 static_member_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        StaticMember Item.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] network_group_name: The name of the network group.
        :param pulumi.Input[str] network_manager_name: The name of the network manager.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] resource_id: Resource Id.
        :param pulumi.Input[str] static_member_name: The name of the static member.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StaticMemberArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        StaticMember Item.

        :param str resource_name: The name of the resource.
        :param StaticMemberArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StaticMemberArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 network_group_name: Optional[pulumi.Input[str]] = None,
                 network_manager_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_id: Optional[pulumi.Input[str]] = None,
                 static_member_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StaticMemberArgs.__new__(StaticMemberArgs)

            if network_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_group_name'")
            __props__.__dict__["network_group_name"] = network_group_name
            if network_manager_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_manager_name'")
            __props__.__dict__["network_manager_name"] = network_manager_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_id"] = resource_id
            __props__.__dict__["static_member_name"] = static_member_name
            __props__.__dict__["etag"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["region"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:network:StaticMember"), pulumi.Alias(type_="azure-native:network/v20210501preview:StaticMember"), pulumi.Alias(type_="azure-native:network/v20220101:StaticMember"), pulumi.Alias(type_="azure-native:network/v20220201preview:StaticMember"), pulumi.Alias(type_="azure-native:network/v20220401preview:StaticMember"), pulumi.Alias(type_="azure-native:network/v20220701:StaticMember"), pulumi.Alias(type_="azure-native:network/v20220901:StaticMember")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StaticMember, __self__).__init__(
            'azure-native:network/v20220501:StaticMember',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StaticMember':
        """
        Get an existing StaticMember resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StaticMemberArgs.__new__(StaticMemberArgs)

        __props__.__dict__["etag"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["region"] = None
        __props__.__dict__["resource_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return StaticMember(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[str]:
        """
        A unique read-only string that changes whenever the resource is updated.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the scope assignment resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def region(self) -> pulumi.Output[str]:
        """
        Resource region.
        """
        return pulumi.get(self, "region")

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Id.
        """
        return pulumi.get(self, "resource_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

