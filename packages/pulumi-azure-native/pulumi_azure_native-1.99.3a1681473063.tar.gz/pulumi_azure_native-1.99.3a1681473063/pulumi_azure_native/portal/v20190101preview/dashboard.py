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

__all__ = ['DashboardArgs', 'Dashboard']

@pulumi.input_type
class DashboardArgs:
    def __init__(__self__, *,
                 resource_group_name: pulumi.Input[str],
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 lenses: Optional[pulumi.Input[Mapping[str, pulumi.Input['DashboardLensArgs']]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Dashboard resource.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] dashboard_name: The name of the dashboard.
        :param pulumi.Input[Mapping[str, pulumi.Input['DashboardLensArgs']]] lenses: The dashboard lenses.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Mapping[str, Any]] metadata: The dashboard metadata.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if dashboard_name is not None:
            pulumi.set(__self__, "dashboard_name", dashboard_name)
        if lenses is not None:
            pulumi.set(__self__, "lenses", lenses)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if metadata is not None:
            pulumi.set(__self__, "metadata", metadata)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

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
    @pulumi.getter(name="dashboardName")
    def dashboard_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the dashboard.
        """
        return pulumi.get(self, "dashboard_name")

    @dashboard_name.setter
    def dashboard_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dashboard_name", value)

    @property
    @pulumi.getter
    def lenses(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['DashboardLensArgs']]]]:
        """
        The dashboard lenses.
        """
        return pulumi.get(self, "lenses")

    @lenses.setter
    def lenses(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['DashboardLensArgs']]]]):
        pulumi.set(self, "lenses", value)

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
    def metadata(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The dashboard metadata.
        """
        return pulumi.get(self, "metadata")

    @metadata.setter
    def metadata(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "metadata", value)

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


class Dashboard(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 lenses: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['DashboardLensArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        The shared dashboard resource definition.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] dashboard_name: The name of the dashboard.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['DashboardLensArgs']]]] lenses: The dashboard lenses.
        :param pulumi.Input[str] location: Resource location
        :param pulumi.Input[Mapping[str, Any]] metadata: The dashboard metadata.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DashboardArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The shared dashboard resource definition.

        :param str resource_name: The name of the resource.
        :param DashboardArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DashboardArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 dashboard_name: Optional[pulumi.Input[str]] = None,
                 lenses: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['DashboardLensArgs']]]]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 metadata: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DashboardArgs.__new__(DashboardArgs)

            __props__.__dict__["dashboard_name"] = dashboard_name
            __props__.__dict__["lenses"] = lenses
            __props__.__dict__["location"] = location
            __props__.__dict__["metadata"] = metadata
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:portal:Dashboard"), pulumi.Alias(type_="azure-native:portal/v20150801preview:Dashboard"), pulumi.Alias(type_="azure-native:portal/v20181001preview:Dashboard"), pulumi.Alias(type_="azure-native:portal/v20200901preview:Dashboard")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Dashboard, __self__).__init__(
            'azure-native:portal/v20190101preview:Dashboard',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Dashboard':
        """
        Get an existing Dashboard resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DashboardArgs.__new__(DashboardArgs)

        __props__.__dict__["lenses"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["metadata"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return Dashboard(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def lenses(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.DashboardLensResponse']]]:
        """
        The dashboard lenses.
        """
        return pulumi.get(self, "lenses")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def metadata(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        The dashboard metadata.
        """
        return pulumi.get(self, "metadata")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name
        """
        return pulumi.get(self, "name")

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

