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

__all__ = ['ReplicationNetworkMappingArgs', 'ReplicationNetworkMapping']

@pulumi.input_type
class ReplicationNetworkMappingArgs:
    def __init__(__self__, *,
                 fabric_name: pulumi.Input[str],
                 network_name: pulumi.Input[str],
                 properties: pulumi.Input['CreateNetworkMappingInputPropertiesArgs'],
                 resource_group_name: pulumi.Input[str],
                 resource_name: pulumi.Input[str],
                 network_mapping_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ReplicationNetworkMapping resource.
        :param pulumi.Input[str] fabric_name: Primary fabric name.
        :param pulumi.Input[str] network_name: Primary network name.
        :param pulumi.Input['CreateNetworkMappingInputPropertiesArgs'] properties: Input properties for creating network mapping.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the recovery services vault is present.
        :param pulumi.Input[str] resource_name: The name of the recovery services vault.
        :param pulumi.Input[str] network_mapping_name: Network mapping name.
        """
        pulumi.set(__self__, "fabric_name", fabric_name)
        pulumi.set(__self__, "network_name", network_name)
        pulumi.set(__self__, "properties", properties)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "resource_name", resource_name)
        if network_mapping_name is not None:
            pulumi.set(__self__, "network_mapping_name", network_mapping_name)

    @property
    @pulumi.getter(name="fabricName")
    def fabric_name(self) -> pulumi.Input[str]:
        """
        Primary fabric name.
        """
        return pulumi.get(self, "fabric_name")

    @fabric_name.setter
    def fabric_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "fabric_name", value)

    @property
    @pulumi.getter(name="networkName")
    def network_name(self) -> pulumi.Input[str]:
        """
        Primary network name.
        """
        return pulumi.get(self, "network_name")

    @network_name.setter
    def network_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "network_name", value)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['CreateNetworkMappingInputPropertiesArgs']:
        """
        Input properties for creating network mapping.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['CreateNetworkMappingInputPropertiesArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group where the recovery services vault is present.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="resourceName")
    def resource_name(self) -> pulumi.Input[str]:
        """
        The name of the recovery services vault.
        """
        return pulumi.get(self, "resource_name")

    @resource_name.setter
    def resource_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_name", value)

    @property
    @pulumi.getter(name="networkMappingName")
    def network_mapping_name(self) -> Optional[pulumi.Input[str]]:
        """
        Network mapping name.
        """
        return pulumi.get(self, "network_mapping_name")

    @network_mapping_name.setter
    def network_mapping_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "network_mapping_name", value)


class ReplicationNetworkMapping(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fabric_name: Optional[pulumi.Input[str]] = None,
                 network_mapping_name: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['CreateNetworkMappingInputPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Network Mapping model. Ideally it should have been possible to inherit this class from prev version in InheritedModels as long as there is no difference in structure or method signature. Since there were no base Models for certain fields and methods viz NetworkMappingProperties and Load with required return type, the class has been introduced in its entirety with references to base models to facilitate extensions in subsequent versions.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] fabric_name: Primary fabric name.
        :param pulumi.Input[str] network_mapping_name: Network mapping name.
        :param pulumi.Input[str] network_name: Primary network name.
        :param pulumi.Input[pulumi.InputType['CreateNetworkMappingInputPropertiesArgs']] properties: Input properties for creating network mapping.
        :param pulumi.Input[str] resource_group_name: The name of the resource group where the recovery services vault is present.
        :param pulumi.Input[str] resource_name_: The name of the recovery services vault.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ReplicationNetworkMappingArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Network Mapping model. Ideally it should have been possible to inherit this class from prev version in InheritedModels as long as there is no difference in structure or method signature. Since there were no base Models for certain fields and methods viz NetworkMappingProperties and Load with required return type, the class has been introduced in its entirety with references to base models to facilitate extensions in subsequent versions.

        :param str resource_name: The name of the resource.
        :param ReplicationNetworkMappingArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ReplicationNetworkMappingArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 fabric_name: Optional[pulumi.Input[str]] = None,
                 network_mapping_name: Optional[pulumi.Input[str]] = None,
                 network_name: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['CreateNetworkMappingInputPropertiesArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_name_: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ReplicationNetworkMappingArgs.__new__(ReplicationNetworkMappingArgs)

            if fabric_name is None and not opts.urn:
                raise TypeError("Missing required property 'fabric_name'")
            __props__.__dict__["fabric_name"] = fabric_name
            __props__.__dict__["network_mapping_name"] = network_mapping_name
            if network_name is None and not opts.urn:
                raise TypeError("Missing required property 'network_name'")
            __props__.__dict__["network_name"] = network_name
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if resource_name_ is None and not opts.urn:
                raise TypeError("Missing required property 'resource_name_'")
            __props__.__dict__["resource_name"] = resource_name_
            __props__.__dict__["location"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:recoveryservices:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20160810:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20180110:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20180710:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20210210:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20210301:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20210401:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20210601:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20210701:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20210801:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20211001:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20211101:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20211201:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20220101:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20220301:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20220401:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20220501:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20220801:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20220910:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20221001:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20230101:ReplicationNetworkMapping"), pulumi.Alias(type_="azure-native:recoveryservices/v20230201:ReplicationNetworkMapping")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ReplicationNetworkMapping, __self__).__init__(
            'azure-native:recoveryservices/v20220201:ReplicationNetworkMapping',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ReplicationNetworkMapping':
        """
        Get an existing ReplicationNetworkMapping resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ReplicationNetworkMappingArgs.__new__(ReplicationNetworkMappingArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return ReplicationNetworkMapping(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        Resource Location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource Name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.NetworkMappingPropertiesResponse']:
        """
        The Network Mapping Properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource Type
        """
        return pulumi.get(self, "type")

