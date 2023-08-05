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

__all__ = ['SubvolumeArgs', 'Subvolume']

@pulumi.input_type
class SubvolumeArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 pool_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 volume_name: pulumi.Input[str],
                 parent_path: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 subvolume_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a Subvolume resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] pool_name: The name of the capacity pool
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] volume_name: The name of the volume
        :param pulumi.Input[str] parent_path: parent path to the subvolume
        :param pulumi.Input[str] path: Path to the subvolume
        :param pulumi.Input[float] size: Truncate subvolume to the provided size in bytes
        :param pulumi.Input[str] subvolume_name: The name of the subvolume.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "pool_name", pool_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "volume_name", volume_name)
        if parent_path is not None:
            pulumi.set(__self__, "parent_path", parent_path)
        if path is not None:
            pulumi.set(__self__, "path", path)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if subvolume_name is not None:
            pulumi.set(__self__, "subvolume_name", subvolume_name)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The name of the NetApp account
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> pulumi.Input[str]:
        """
        The name of the capacity pool
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "pool_name", value)

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
    @pulumi.getter(name="volumeName")
    def volume_name(self) -> pulumi.Input[str]:
        """
        The name of the volume
        """
        return pulumi.get(self, "volume_name")

    @volume_name.setter
    def volume_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "volume_name", value)

    @property
    @pulumi.getter(name="parentPath")
    def parent_path(self) -> Optional[pulumi.Input[str]]:
        """
        parent path to the subvolume
        """
        return pulumi.get(self, "parent_path")

    @parent_path.setter
    def parent_path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "parent_path", value)

    @property
    @pulumi.getter
    def path(self) -> Optional[pulumi.Input[str]]:
        """
        Path to the subvolume
        """
        return pulumi.get(self, "path")

    @path.setter
    def path(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "path", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[float]]:
        """
        Truncate subvolume to the provided size in bytes
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="subvolumeName")
    def subvolume_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the subvolume.
        """
        return pulumi.get(self, "subvolume_name")

    @subvolume_name.setter
    def subvolume_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "subvolume_name", value)


class Subvolume(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 parent_path: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 subvolume_name: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Subvolume Information properties

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The name of the NetApp account
        :param pulumi.Input[str] parent_path: parent path to the subvolume
        :param pulumi.Input[str] path: Path to the subvolume
        :param pulumi.Input[str] pool_name: The name of the capacity pool
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[float] size: Truncate subvolume to the provided size in bytes
        :param pulumi.Input[str] subvolume_name: The name of the subvolume.
        :param pulumi.Input[str] volume_name: The name of the volume
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: SubvolumeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Subvolume Information properties

        :param str resource_name: The name of the resource.
        :param SubvolumeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(SubvolumeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 parent_path: Optional[pulumi.Input[str]] = None,
                 path: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[float]] = None,
                 subvolume_name: Optional[pulumi.Input[str]] = None,
                 volume_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = SubvolumeArgs.__new__(SubvolumeArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["parent_path"] = parent_path
            __props__.__dict__["path"] = path
            if pool_name is None and not opts.urn:
                raise TypeError("Missing required property 'pool_name'")
            __props__.__dict__["pool_name"] = pool_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["size"] = size
            __props__.__dict__["subvolume_name"] = subvolume_name
            if volume_name is None and not opts.urn:
                raise TypeError("Missing required property 'volume_name'")
            __props__.__dict__["volume_name"] = volume_name
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:netapp:Subvolume"), pulumi.Alias(type_="azure-native:netapp/v20211001:Subvolume"), pulumi.Alias(type_="azure-native:netapp/v20220101:Subvolume"), pulumi.Alias(type_="azure-native:netapp/v20220301:Subvolume"), pulumi.Alias(type_="azure-native:netapp/v20220901:Subvolume")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Subvolume, __self__).__init__(
            'azure-native:netapp/v20220501:Subvolume',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Subvolume':
        """
        Get an existing Subvolume resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = SubvolumeArgs.__new__(SubvolumeArgs)

        __props__.__dict__["name"] = None
        __props__.__dict__["parent_path"] = None
        __props__.__dict__["path"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return Subvolume(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="parentPath")
    def parent_path(self) -> pulumi.Output[Optional[str]]:
        """
        parent path to the subvolume
        """
        return pulumi.get(self, "parent_path")

    @property
    @pulumi.getter
    def path(self) -> pulumi.Output[Optional[str]]:
        """
        Path to the subvolume
        """
        return pulumi.get(self, "path")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Azure lifecycle management
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

