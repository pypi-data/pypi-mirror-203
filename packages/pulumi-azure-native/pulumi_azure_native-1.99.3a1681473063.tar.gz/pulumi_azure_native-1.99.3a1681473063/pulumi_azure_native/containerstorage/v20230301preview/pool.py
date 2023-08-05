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

__all__ = ['PoolArgs', 'Pool']

@pulumi.input_type
class PoolArgs:
    def __init__(__self__, *,
                 assignments: pulumi.Input[Sequence[pulumi.Input[str]]],
                 elastic_san_pool_properties: pulumi.Input['ElasticSanPoolPropertiesArgs'],
                 pool_capacity_gi_b: pulumi.Input[float],
                 pool_type: pulumi.Input[float],
                 resource_group_name: pulumi.Input[str],
                 zones: pulumi.Input[Sequence[pulumi.Input[str]]],
                 disk_pool_properties: Optional[pulumi.Input['DiskPoolPropertiesArgs']] = None,
                 ephemeral_pool_properties: Optional[pulumi.Input['EphemeralPoolPropertiesArgs']] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Pool resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assignments: List of resources that should have access to the pool. Typically ARM references to AKS clusters or ACI Container Groups. For local and standard this must be a single reference. For portable there can be many.
        :param pulumi.Input['ElasticSanPoolPropertiesArgs'] elastic_san_pool_properties: Elastic San Pool Properties
        :param pulumi.Input[float] pool_capacity_gi_b: Initial capacity of the pool in GiB.
        :param pulumi.Input[float] pool_type: Type of the Pool: ephemeral, disk, managed, or elasticsan.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: List of availability zones that resources can be created in.
        :param pulumi.Input['DiskPoolPropertiesArgs'] disk_pool_properties: Disk Pool Properties
        :param pulumi.Input['EphemeralPoolPropertiesArgs'] ephemeral_pool_properties: Ephemeral Pool Properties
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] pool_name: Pool Object
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "assignments", assignments)
        pulumi.set(__self__, "elastic_san_pool_properties", elastic_san_pool_properties)
        pulumi.set(__self__, "pool_capacity_gi_b", pool_capacity_gi_b)
        pulumi.set(__self__, "pool_type", pool_type)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "zones", zones)
        if disk_pool_properties is not None:
            pulumi.set(__self__, "disk_pool_properties", disk_pool_properties)
        if ephemeral_pool_properties is not None:
            pulumi.set(__self__, "ephemeral_pool_properties", ephemeral_pool_properties)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if pool_name is not None:
            pulumi.set(__self__, "pool_name", pool_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def assignments(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of resources that should have access to the pool. Typically ARM references to AKS clusters or ACI Container Groups. For local and standard this must be a single reference. For portable there can be many.
        """
        return pulumi.get(self, "assignments")

    @assignments.setter
    def assignments(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "assignments", value)

    @property
    @pulumi.getter(name="elasticSanPoolProperties")
    def elastic_san_pool_properties(self) -> pulumi.Input['ElasticSanPoolPropertiesArgs']:
        """
        Elastic San Pool Properties
        """
        return pulumi.get(self, "elastic_san_pool_properties")

    @elastic_san_pool_properties.setter
    def elastic_san_pool_properties(self, value: pulumi.Input['ElasticSanPoolPropertiesArgs']):
        pulumi.set(self, "elastic_san_pool_properties", value)

    @property
    @pulumi.getter(name="poolCapacityGiB")
    def pool_capacity_gi_b(self) -> pulumi.Input[float]:
        """
        Initial capacity of the pool in GiB.
        """
        return pulumi.get(self, "pool_capacity_gi_b")

    @pool_capacity_gi_b.setter
    def pool_capacity_gi_b(self, value: pulumi.Input[float]):
        pulumi.set(self, "pool_capacity_gi_b", value)

    @property
    @pulumi.getter(name="poolType")
    def pool_type(self) -> pulumi.Input[float]:
        """
        Type of the Pool: ephemeral, disk, managed, or elasticsan.
        """
        return pulumi.get(self, "pool_type")

    @pool_type.setter
    def pool_type(self, value: pulumi.Input[float]):
        pulumi.set(self, "pool_type", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        List of availability zones that resources can be created in.
        """
        return pulumi.get(self, "zones")

    @zones.setter
    def zones(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "zones", value)

    @property
    @pulumi.getter(name="diskPoolProperties")
    def disk_pool_properties(self) -> Optional[pulumi.Input['DiskPoolPropertiesArgs']]:
        """
        Disk Pool Properties
        """
        return pulumi.get(self, "disk_pool_properties")

    @disk_pool_properties.setter
    def disk_pool_properties(self, value: Optional[pulumi.Input['DiskPoolPropertiesArgs']]):
        pulumi.set(self, "disk_pool_properties", value)

    @property
    @pulumi.getter(name="ephemeralPoolProperties")
    def ephemeral_pool_properties(self) -> Optional[pulumi.Input['EphemeralPoolPropertiesArgs']]:
        """
        Ephemeral Pool Properties
        """
        return pulumi.get(self, "ephemeral_pool_properties")

    @ephemeral_pool_properties.setter
    def ephemeral_pool_properties(self, value: Optional[pulumi.Input['EphemeralPoolPropertiesArgs']]):
        pulumi.set(self, "ephemeral_pool_properties", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="poolName")
    def pool_name(self) -> Optional[pulumi.Input[str]]:
        """
        Pool Object
        """
        return pulumi.get(self, "pool_name")

    @pool_name.setter
    def pool_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "pool_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Pool(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 disk_pool_properties: Optional[pulumi.Input[pulumi.InputType['DiskPoolPropertiesArgs']]] = None,
                 elastic_san_pool_properties: Optional[pulumi.Input[pulumi.InputType['ElasticSanPoolPropertiesArgs']]] = None,
                 ephemeral_pool_properties: Optional[pulumi.Input[pulumi.InputType['EphemeralPoolPropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_capacity_gi_b: Optional[pulumi.Input[float]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 pool_type: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Pool resource

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] assignments: List of resources that should have access to the pool. Typically ARM references to AKS clusters or ACI Container Groups. For local and standard this must be a single reference. For portable there can be many.
        :param pulumi.Input[pulumi.InputType['DiskPoolPropertiesArgs']] disk_pool_properties: Disk Pool Properties
        :param pulumi.Input[pulumi.InputType['ElasticSanPoolPropertiesArgs']] elastic_san_pool_properties: Elastic San Pool Properties
        :param pulumi.Input[pulumi.InputType['EphemeralPoolPropertiesArgs']] ephemeral_pool_properties: Ephemeral Pool Properties
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[float] pool_capacity_gi_b: Initial capacity of the pool in GiB.
        :param pulumi.Input[str] pool_name: Pool Object
        :param pulumi.Input[float] pool_type: Type of the Pool: ephemeral, disk, managed, or elasticsan.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] zones: List of availability zones that resources can be created in.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: PoolArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Pool resource

        :param str resource_name: The name of the resource.
        :param PoolArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(PoolArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 assignments: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 disk_pool_properties: Optional[pulumi.Input[pulumi.InputType['DiskPoolPropertiesArgs']]] = None,
                 elastic_san_pool_properties: Optional[pulumi.Input[pulumi.InputType['ElasticSanPoolPropertiesArgs']]] = None,
                 ephemeral_pool_properties: Optional[pulumi.Input[pulumi.InputType['EphemeralPoolPropertiesArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 pool_capacity_gi_b: Optional[pulumi.Input[float]] = None,
                 pool_name: Optional[pulumi.Input[str]] = None,
                 pool_type: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = PoolArgs.__new__(PoolArgs)

            if assignments is None and not opts.urn:
                raise TypeError("Missing required property 'assignments'")
            __props__.__dict__["assignments"] = assignments
            __props__.__dict__["disk_pool_properties"] = disk_pool_properties
            if elastic_san_pool_properties is None and not opts.urn:
                raise TypeError("Missing required property 'elastic_san_pool_properties'")
            __props__.__dict__["elastic_san_pool_properties"] = elastic_san_pool_properties
            __props__.__dict__["ephemeral_pool_properties"] = ephemeral_pool_properties
            __props__.__dict__["location"] = location
            if pool_capacity_gi_b is None and not opts.urn:
                raise TypeError("Missing required property 'pool_capacity_gi_b'")
            __props__.__dict__["pool_capacity_gi_b"] = pool_capacity_gi_b
            __props__.__dict__["pool_name"] = pool_name
            if pool_type is None and not opts.urn:
                raise TypeError("Missing required property 'pool_type'")
            __props__.__dict__["pool_type"] = pool_type
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            if zones is None and not opts.urn:
                raise TypeError("Missing required property 'zones'")
            __props__.__dict__["zones"] = zones
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:containerstorage:Pool")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Pool, __self__).__init__(
            'azure-native:containerstorage/v20230301preview:Pool',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Pool':
        """
        Get an existing Pool resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = PoolArgs.__new__(PoolArgs)

        __props__.__dict__["assignments"] = None
        __props__.__dict__["disk_pool_properties"] = None
        __props__.__dict__["elastic_san_pool_properties"] = None
        __props__.__dict__["ephemeral_pool_properties"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["pool_capacity_gi_b"] = None
        __props__.__dict__["pool_type"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["zones"] = None
        return Pool(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def assignments(self) -> pulumi.Output[Sequence[str]]:
        """
        List of resources that should have access to the pool. Typically ARM references to AKS clusters or ACI Container Groups. For local and standard this must be a single reference. For portable there can be many.
        """
        return pulumi.get(self, "assignments")

    @property
    @pulumi.getter(name="diskPoolProperties")
    def disk_pool_properties(self) -> pulumi.Output[Optional['outputs.DiskPoolPropertiesResponse']]:
        """
        Disk Pool Properties
        """
        return pulumi.get(self, "disk_pool_properties")

    @property
    @pulumi.getter(name="elasticSanPoolProperties")
    def elastic_san_pool_properties(self) -> pulumi.Output['outputs.ElasticSanPoolPropertiesResponse']:
        """
        Elastic San Pool Properties
        """
        return pulumi.get(self, "elastic_san_pool_properties")

    @property
    @pulumi.getter(name="ephemeralPoolProperties")
    def ephemeral_pool_properties(self) -> pulumi.Output[Optional['outputs.EphemeralPoolPropertiesResponse']]:
        """
        Ephemeral Pool Properties
        """
        return pulumi.get(self, "ephemeral_pool_properties")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="poolCapacityGiB")
    def pool_capacity_gi_b(self) -> pulumi.Output[float]:
        """
        Initial capacity of the pool in GiB.
        """
        return pulumi.get(self, "pool_capacity_gi_b")

    @property
    @pulumi.getter(name="poolType")
    def pool_type(self) -> pulumi.Output[float]:
        """
        Type of the Pool: ephemeral, disk, managed, or elasticsan.
        """
        return pulumi.get(self, "pool_type")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The status of the last operation.
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
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def zones(self) -> pulumi.Output[Sequence[str]]:
        """
        List of availability zones that resources can be created in.
        """
        return pulumi.get(self, "zones")

