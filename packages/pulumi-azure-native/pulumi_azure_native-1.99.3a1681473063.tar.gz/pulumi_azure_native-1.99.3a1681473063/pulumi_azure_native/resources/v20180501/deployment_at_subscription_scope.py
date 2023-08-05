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

__all__ = ['DeploymentAtSubscriptionScopeArgs', 'DeploymentAtSubscriptionScope']

@pulumi.input_type
class DeploymentAtSubscriptionScopeArgs:
    def __init__(__self__, *,
                 properties: pulumi.Input['DeploymentPropertiesArgs'],
                 deployment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a DeploymentAtSubscriptionScope resource.
        :param pulumi.Input['DeploymentPropertiesArgs'] properties: The deployment properties.
        :param pulumi.Input[str] deployment_name: The name of the deployment.
        :param pulumi.Input[str] location: The location to store the deployment data.
        """
        pulumi.set(__self__, "properties", properties)
        if deployment_name is not None:
            pulumi.set(__self__, "deployment_name", deployment_name)
        if location is not None:
            pulumi.set(__self__, "location", location)

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Input['DeploymentPropertiesArgs']:
        """
        The deployment properties.
        """
        return pulumi.get(self, "properties")

    @properties.setter
    def properties(self, value: pulumi.Input['DeploymentPropertiesArgs']):
        pulumi.set(self, "properties", value)

    @property
    @pulumi.getter(name="deploymentName")
    def deployment_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the deployment.
        """
        return pulumi.get(self, "deployment_name")

    @deployment_name.setter
    def deployment_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "deployment_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The location to store the deployment data.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)


warnings.warn("""Version 2018-05-01 will be removed in v2 of the provider.""", DeprecationWarning)


class DeploymentAtSubscriptionScope(pulumi.CustomResource):
    warnings.warn("""Version 2018-05-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['DeploymentPropertiesArgs']]] = None,
                 __props__=None):
        """
        Deployment information.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] deployment_name: The name of the deployment.
        :param pulumi.Input[str] location: The location to store the deployment data.
        :param pulumi.Input[pulumi.InputType['DeploymentPropertiesArgs']] properties: The deployment properties.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DeploymentAtSubscriptionScopeArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Deployment information.

        :param str resource_name: The name of the resource.
        :param DeploymentAtSubscriptionScopeArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DeploymentAtSubscriptionScopeArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 deployment_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 properties: Optional[pulumi.Input[pulumi.InputType['DeploymentPropertiesArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""DeploymentAtSubscriptionScope is deprecated: Version 2018-05-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DeploymentAtSubscriptionScopeArgs.__new__(DeploymentAtSubscriptionScopeArgs)

            __props__.__dict__["deployment_name"] = deployment_name
            __props__.__dict__["location"] = location
            if properties is None and not opts.urn:
                raise TypeError("Missing required property 'properties'")
            __props__.__dict__["properties"] = properties
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:resources:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20190301:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20190501:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20190510:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20190701:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20190801:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20191001:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20200601:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20200801:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20201001:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20210101:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20210401:DeploymentAtSubscriptionScope"), pulumi.Alias(type_="azure-native:resources/v20220901:DeploymentAtSubscriptionScope")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DeploymentAtSubscriptionScope, __self__).__init__(
            'azure-native:resources/v20180501:DeploymentAtSubscriptionScope',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DeploymentAtSubscriptionScope':
        """
        Get an existing DeploymentAtSubscriptionScope resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DeploymentAtSubscriptionScopeArgs.__new__(DeploymentAtSubscriptionScopeArgs)

        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["properties"] = None
        __props__.__dict__["type"] = None
        return DeploymentAtSubscriptionScope(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        the location of the deployment.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the deployment.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def properties(self) -> pulumi.Output['outputs.DeploymentPropertiesExtendedResponse']:
        """
        Deployment properties.
        """
        return pulumi.get(self, "properties")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the deployment.
        """
        return pulumi.get(self, "type")

