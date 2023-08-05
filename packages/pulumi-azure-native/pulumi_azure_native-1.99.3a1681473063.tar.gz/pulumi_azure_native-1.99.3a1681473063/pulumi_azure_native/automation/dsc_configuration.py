# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs
from ._enums import *
from ._inputs import *

__all__ = ['DscConfigurationArgs', 'DscConfiguration']

@pulumi.input_type
class DscConfigurationArgs:
    def __init__(__self__, *,
                 automation_account_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 source: pulumi.Input['ContentSourceArgs'],
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 log_progress: Optional[pulumi.Input[bool]] = None,
                 log_verbose: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input['DscConfigurationParameterArgs']]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a DscConfiguration resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input['ContentSourceArgs'] source: Gets or sets the source.
        :param pulumi.Input[str] configuration_name: The create or update parameters for configuration.
        :param pulumi.Input[str] description: Gets or sets the description of the configuration.
        :param pulumi.Input[str] location: Gets or sets the location of the resource.
        :param pulumi.Input[bool] log_progress: Gets or sets progress log option.
        :param pulumi.Input[bool] log_verbose: Gets or sets verbose log option.
        :param pulumi.Input[str] name: Gets or sets name of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input['DscConfigurationParameterArgs']]] parameters: Gets or sets the configuration parameters.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the tags attached to the resource.
        """
        pulumi.set(__self__, "automation_account_name", automation_account_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "source", source)
        if configuration_name is not None:
            pulumi.set(__self__, "configuration_name", configuration_name)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if log_progress is not None:
            pulumi.set(__self__, "log_progress", log_progress)
        if log_verbose is not None:
            pulumi.set(__self__, "log_verbose", log_verbose)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="automationAccountName")
    def automation_account_name(self) -> pulumi.Input[str]:
        """
        The name of the automation account.
        """
        return pulumi.get(self, "automation_account_name")

    @automation_account_name.setter
    def automation_account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "automation_account_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        Name of an Azure Resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter
    def source(self) -> pulumi.Input['ContentSourceArgs']:
        """
        Gets or sets the source.
        """
        return pulumi.get(self, "source")

    @source.setter
    def source(self, value: pulumi.Input['ContentSourceArgs']):
        pulumi.set(self, "source", value)

    @property
    @pulumi.getter(name="configurationName")
    def configuration_name(self) -> Optional[pulumi.Input[str]]:
        """
        The create or update parameters for configuration.
        """
        return pulumi.get(self, "configuration_name")

    @configuration_name.setter
    def configuration_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "configuration_name", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the description of the configuration.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets the location of the resource.
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="logProgress")
    def log_progress(self) -> Optional[pulumi.Input[bool]]:
        """
        Gets or sets progress log option.
        """
        return pulumi.get(self, "log_progress")

    @log_progress.setter
    def log_progress(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "log_progress", value)

    @property
    @pulumi.getter(name="logVerbose")
    def log_verbose(self) -> Optional[pulumi.Input[bool]]:
        """
        Gets or sets verbose log option.
        """
        return pulumi.get(self, "log_verbose")

    @log_verbose.setter
    def log_verbose(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "log_verbose", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets name of the resource.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['DscConfigurationParameterArgs']]]]:
        """
        Gets or sets the configuration parameters.
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['DscConfigurationParameterArgs']]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Gets or sets the tags attached to the resource.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class DscConfiguration(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 log_progress: Optional[pulumi.Input[bool]] = None,
                 log_verbose: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['DscConfigurationParameterArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ContentSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        Definition of the configuration type.
        API Version: 2019-06-01.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] automation_account_name: The name of the automation account.
        :param pulumi.Input[str] configuration_name: The create or update parameters for configuration.
        :param pulumi.Input[str] description: Gets or sets the description of the configuration.
        :param pulumi.Input[str] location: Gets or sets the location of the resource.
        :param pulumi.Input[bool] log_progress: Gets or sets progress log option.
        :param pulumi.Input[bool] log_verbose: Gets or sets verbose log option.
        :param pulumi.Input[str] name: Gets or sets name of the resource.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['DscConfigurationParameterArgs']]]] parameters: Gets or sets the configuration parameters.
        :param pulumi.Input[str] resource_group_name: Name of an Azure Resource group.
        :param pulumi.Input[pulumi.InputType['ContentSourceArgs']] source: Gets or sets the source.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Gets or sets the tags attached to the resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: DscConfigurationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Definition of the configuration type.
        API Version: 2019-06-01.

        :param str resource_name: The name of the resource.
        :param DscConfigurationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(DscConfigurationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 automation_account_name: Optional[pulumi.Input[str]] = None,
                 configuration_name: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 log_progress: Optional[pulumi.Input[bool]] = None,
                 log_verbose: Optional[pulumi.Input[bool]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['DscConfigurationParameterArgs']]]]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 source: Optional[pulumi.Input[pulumi.InputType['ContentSourceArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = DscConfigurationArgs.__new__(DscConfigurationArgs)

            if automation_account_name is None and not opts.urn:
                raise TypeError("Missing required property 'automation_account_name'")
            __props__.__dict__["automation_account_name"] = automation_account_name
            __props__.__dict__["configuration_name"] = configuration_name
            __props__.__dict__["description"] = description
            __props__.__dict__["location"] = location
            __props__.__dict__["log_progress"] = log_progress
            __props__.__dict__["log_verbose"] = log_verbose
            __props__.__dict__["name"] = name
            __props__.__dict__["parameters"] = parameters
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if source is None and not opts.urn:
                raise TypeError("Missing required property 'source'")
            __props__.__dict__["source"] = source
            __props__.__dict__["tags"] = tags
            __props__.__dict__["creation_time"] = None
            __props__.__dict__["etag"] = None
            __props__.__dict__["job_count"] = None
            __props__.__dict__["last_modified_time"] = None
            __props__.__dict__["node_configuration_count"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["state"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:automation/v20151031:DscConfiguration"), pulumi.Alias(type_="azure-native:automation/v20190601:DscConfiguration"), pulumi.Alias(type_="azure-native:automation/v20220808:DscConfiguration")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(DscConfiguration, __self__).__init__(
            'azure-native:automation:DscConfiguration',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'DscConfiguration':
        """
        Get an existing DscConfiguration resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = DscConfigurationArgs.__new__(DscConfigurationArgs)

        __props__.__dict__["creation_time"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["etag"] = None
        __props__.__dict__["job_count"] = None
        __props__.__dict__["last_modified_time"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["log_verbose"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["node_configuration_count"] = None
        __props__.__dict__["parameters"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["source"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return DscConfiguration(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="creationTime")
    def creation_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the creation time.
        """
        return pulumi.get(self, "creation_time")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def etag(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the etag of the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="jobCount")
    def job_count(self) -> pulumi.Output[Optional[int]]:
        """
        Gets or sets the job count of the configuration.
        """
        return pulumi.get(self, "job_count")

    @property
    @pulumi.getter(name="lastModifiedTime")
    def last_modified_time(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the last modified time.
        """
        return pulumi.get(self, "last_modified_time")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[Optional[str]]:
        """
        The Azure Region where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="logVerbose")
    def log_verbose(self) -> pulumi.Output[Optional[bool]]:
        """
        Gets or sets verbose log option.
        """
        return pulumi.get(self, "log_verbose")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeConfigurationCount")
    def node_configuration_count(self) -> pulumi.Output[Optional[int]]:
        """
        Gets the number of compiled node configurations.
        """
        return pulumi.get(self, "node_configuration_count")

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.DscConfigurationParameterResponse']]]:
        """
        Gets or sets the configuration parameters.
        """
        return pulumi.get(self, "parameters")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the provisioning state of the configuration.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> pulumi.Output[Optional['outputs.ContentSourceResponse']]:
        """
        Gets or sets the source.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        Gets or sets the state of the configuration.
        """
        return pulumi.get(self, "state")

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
        The type of the resource.
        """
        return pulumi.get(self, "type")

