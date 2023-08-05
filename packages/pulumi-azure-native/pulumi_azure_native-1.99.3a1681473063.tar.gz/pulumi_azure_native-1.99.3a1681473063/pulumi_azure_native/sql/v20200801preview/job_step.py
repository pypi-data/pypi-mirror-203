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

__all__ = ['JobStepArgs', 'JobStep']

@pulumi.input_type
class JobStepArgs:
    def __init__(__self__, *,
                 action: pulumi.Input['JobStepActionArgs'],
                 credential: pulumi.Input[str],
                 job_agent_name: pulumi.Input[str],
                 job_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 target_group: pulumi.Input[str],
                 execution_options: Optional[pulumi.Input['JobStepExecutionOptionsArgs']] = None,
                 output: Optional[pulumi.Input['JobStepOutputArgs']] = None,
                 step_id: Optional[pulumi.Input[int]] = None,
                 step_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a JobStep resource.
        :param pulumi.Input['JobStepActionArgs'] action: The action payload of the job step.
        :param pulumi.Input[str] credential: The resource ID of the job credential that will be used to connect to the targets.
        :param pulumi.Input[str] job_agent_name: The name of the job agent.
        :param pulumi.Input[str] job_name: The name of the job.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] target_group: The resource ID of the target group that the job step will be executed on.
        :param pulumi.Input['JobStepExecutionOptionsArgs'] execution_options: Execution options for the job step.
        :param pulumi.Input['JobStepOutputArgs'] output: Output destination properties of the job step.
        :param pulumi.Input[int] step_id: The job step's index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified.
        :param pulumi.Input[str] step_name: The name of the job step.
        """
        pulumi.set(__self__, "action", action)
        pulumi.set(__self__, "credential", credential)
        pulumi.set(__self__, "job_agent_name", job_agent_name)
        pulumi.set(__self__, "job_name", job_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        pulumi.set(__self__, "target_group", target_group)
        if execution_options is not None:
            pulumi.set(__self__, "execution_options", execution_options)
        if output is not None:
            pulumi.set(__self__, "output", output)
        if step_id is not None:
            pulumi.set(__self__, "step_id", step_id)
        if step_name is not None:
            pulumi.set(__self__, "step_name", step_name)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Input['JobStepActionArgs']:
        """
        The action payload of the job step.
        """
        return pulumi.get(self, "action")

    @action.setter
    def action(self, value: pulumi.Input['JobStepActionArgs']):
        pulumi.set(self, "action", value)

    @property
    @pulumi.getter
    def credential(self) -> pulumi.Input[str]:
        """
        The resource ID of the job credential that will be used to connect to the targets.
        """
        return pulumi.get(self, "credential")

    @credential.setter
    def credential(self, value: pulumi.Input[str]):
        pulumi.set(self, "credential", value)

    @property
    @pulumi.getter(name="jobAgentName")
    def job_agent_name(self) -> pulumi.Input[str]:
        """
        The name of the job agent.
        """
        return pulumi.get(self, "job_agent_name")

    @job_agent_name.setter
    def job_agent_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_agent_name", value)

    @property
    @pulumi.getter(name="jobName")
    def job_name(self) -> pulumi.Input[str]:
        """
        The name of the job.
        """
        return pulumi.get(self, "job_name")

    @job_name.setter
    def job_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "job_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="targetGroup")
    def target_group(self) -> pulumi.Input[str]:
        """
        The resource ID of the target group that the job step will be executed on.
        """
        return pulumi.get(self, "target_group")

    @target_group.setter
    def target_group(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_group", value)

    @property
    @pulumi.getter(name="executionOptions")
    def execution_options(self) -> Optional[pulumi.Input['JobStepExecutionOptionsArgs']]:
        """
        Execution options for the job step.
        """
        return pulumi.get(self, "execution_options")

    @execution_options.setter
    def execution_options(self, value: Optional[pulumi.Input['JobStepExecutionOptionsArgs']]):
        pulumi.set(self, "execution_options", value)

    @property
    @pulumi.getter
    def output(self) -> Optional[pulumi.Input['JobStepOutputArgs']]:
        """
        Output destination properties of the job step.
        """
        return pulumi.get(self, "output")

    @output.setter
    def output(self, value: Optional[pulumi.Input['JobStepOutputArgs']]):
        pulumi.set(self, "output", value)

    @property
    @pulumi.getter(name="stepId")
    def step_id(self) -> Optional[pulumi.Input[int]]:
        """
        The job step's index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified.
        """
        return pulumi.get(self, "step_id")

    @step_id.setter
    def step_id(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "step_id", value)

    @property
    @pulumi.getter(name="stepName")
    def step_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the job step.
        """
        return pulumi.get(self, "step_name")

    @step_name.setter
    def step_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "step_name", value)


class JobStep(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['JobStepActionArgs']]] = None,
                 credential: Optional[pulumi.Input[str]] = None,
                 execution_options: Optional[pulumi.Input[pulumi.InputType['JobStepExecutionOptionsArgs']]] = None,
                 job_agent_name: Optional[pulumi.Input[str]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 output: Optional[pulumi.Input[pulumi.InputType['JobStepOutputArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 step_id: Optional[pulumi.Input[int]] = None,
                 step_name: Optional[pulumi.Input[str]] = None,
                 target_group: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        A job step.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['JobStepActionArgs']] action: The action payload of the job step.
        :param pulumi.Input[str] credential: The resource ID of the job credential that will be used to connect to the targets.
        :param pulumi.Input[pulumi.InputType['JobStepExecutionOptionsArgs']] execution_options: Execution options for the job step.
        :param pulumi.Input[str] job_agent_name: The name of the job agent.
        :param pulumi.Input[str] job_name: The name of the job.
        :param pulumi.Input[pulumi.InputType['JobStepOutputArgs']] output: Output destination properties of the job step.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[int] step_id: The job step's index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified.
        :param pulumi.Input[str] step_name: The name of the job step.
        :param pulumi.Input[str] target_group: The resource ID of the target group that the job step will be executed on.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: JobStepArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A job step.

        :param str resource_name: The name of the resource.
        :param JobStepArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(JobStepArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 action: Optional[pulumi.Input[pulumi.InputType['JobStepActionArgs']]] = None,
                 credential: Optional[pulumi.Input[str]] = None,
                 execution_options: Optional[pulumi.Input[pulumi.InputType['JobStepExecutionOptionsArgs']]] = None,
                 job_agent_name: Optional[pulumi.Input[str]] = None,
                 job_name: Optional[pulumi.Input[str]] = None,
                 output: Optional[pulumi.Input[pulumi.InputType['JobStepOutputArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 step_id: Optional[pulumi.Input[int]] = None,
                 step_name: Optional[pulumi.Input[str]] = None,
                 target_group: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = JobStepArgs.__new__(JobStepArgs)

            if action is None and not opts.urn:
                raise TypeError("Missing required property 'action'")
            __props__.__dict__["action"] = action
            if credential is None and not opts.urn:
                raise TypeError("Missing required property 'credential'")
            __props__.__dict__["credential"] = credential
            __props__.__dict__["execution_options"] = execution_options
            if job_agent_name is None and not opts.urn:
                raise TypeError("Missing required property 'job_agent_name'")
            __props__.__dict__["job_agent_name"] = job_agent_name
            if job_name is None and not opts.urn:
                raise TypeError("Missing required property 'job_name'")
            __props__.__dict__["job_name"] = job_name
            __props__.__dict__["output"] = output
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["step_id"] = step_id
            __props__.__dict__["step_name"] = step_name
            if target_group is None and not opts.urn:
                raise TypeError("Missing required property 'target_group'")
            __props__.__dict__["target_group"] = target_group
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:JobStep"), pulumi.Alias(type_="azure-native:sql/v20170301preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20200202preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20201101preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20210201preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20210501preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20210801preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20211101:JobStep"), pulumi.Alias(type_="azure-native:sql/v20211101preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20220201preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20220501preview:JobStep"), pulumi.Alias(type_="azure-native:sql/v20220801preview:JobStep")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(JobStep, __self__).__init__(
            'azure-native:sql/v20200801preview:JobStep',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'JobStep':
        """
        Get an existing JobStep resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = JobStepArgs.__new__(JobStepArgs)

        __props__.__dict__["action"] = None
        __props__.__dict__["credential"] = None
        __props__.__dict__["execution_options"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["output"] = None
        __props__.__dict__["step_id"] = None
        __props__.__dict__["target_group"] = None
        __props__.__dict__["type"] = None
        return JobStep(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def action(self) -> pulumi.Output['outputs.JobStepActionResponse']:
        """
        The action payload of the job step.
        """
        return pulumi.get(self, "action")

    @property
    @pulumi.getter
    def credential(self) -> pulumi.Output[str]:
        """
        The resource ID of the job credential that will be used to connect to the targets.
        """
        return pulumi.get(self, "credential")

    @property
    @pulumi.getter(name="executionOptions")
    def execution_options(self) -> pulumi.Output[Optional['outputs.JobStepExecutionOptionsResponse']]:
        """
        Execution options for the job step.
        """
        return pulumi.get(self, "execution_options")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def output(self) -> pulumi.Output[Optional['outputs.JobStepOutputResponse']]:
        """
        Output destination properties of the job step.
        """
        return pulumi.get(self, "output")

    @property
    @pulumi.getter(name="stepId")
    def step_id(self) -> pulumi.Output[Optional[int]]:
        """
        The job step's index within the job. If not specified when creating the job step, it will be created as the last step. If not specified when updating the job step, the step id is not modified.
        """
        return pulumi.get(self, "step_id")

    @property
    @pulumi.getter(name="targetGroup")
    def target_group(self) -> pulumi.Output[str]:
        """
        The resource ID of the target group that the job step will be executed on.
        """
        return pulumi.get(self, "target_group")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

