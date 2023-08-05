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

__all__ = [
    'GetScalingPlanResult',
    'AwaitableGetScalingPlanResult',
    'get_scaling_plan',
    'get_scaling_plan_output',
]

warnings.warn("""Version 2020-11-10-preview will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetScalingPlanResult:
    """
    Represents a scaling plan definition.
    """
    def __init__(__self__, description=None, exclusion_tag=None, friendly_name=None, host_pool_references=None, host_pool_type=None, id=None, location=None, name=None, schedules=None, tags=None, time_zone=None, type=None):
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if exclusion_tag and not isinstance(exclusion_tag, str):
            raise TypeError("Expected argument 'exclusion_tag' to be a str")
        pulumi.set(__self__, "exclusion_tag", exclusion_tag)
        if friendly_name and not isinstance(friendly_name, str):
            raise TypeError("Expected argument 'friendly_name' to be a str")
        pulumi.set(__self__, "friendly_name", friendly_name)
        if host_pool_references and not isinstance(host_pool_references, list):
            raise TypeError("Expected argument 'host_pool_references' to be a list")
        pulumi.set(__self__, "host_pool_references", host_pool_references)
        if host_pool_type and not isinstance(host_pool_type, str):
            raise TypeError("Expected argument 'host_pool_type' to be a str")
        pulumi.set(__self__, "host_pool_type", host_pool_type)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if schedules and not isinstance(schedules, list):
            raise TypeError("Expected argument 'schedules' to be a list")
        pulumi.set(__self__, "schedules", schedules)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if time_zone and not isinstance(time_zone, str):
            raise TypeError("Expected argument 'time_zone' to be a str")
        pulumi.set(__self__, "time_zone", time_zone)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Description of scaling plan.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="exclusionTag")
    def exclusion_tag(self) -> Optional[str]:
        """
        Exclusion tag for scaling plan.
        """
        return pulumi.get(self, "exclusion_tag")

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[str]:
        """
        User friendly name of scaling plan.
        """
        return pulumi.get(self, "friendly_name")

    @property
    @pulumi.getter(name="hostPoolReferences")
    def host_pool_references(self) -> Optional[Sequence['outputs.ScalingHostPoolReferenceResponse']]:
        """
        List of ScalingHostPoolReference definitions.
        """
        return pulumi.get(self, "host_pool_references")

    @property
    @pulumi.getter(name="hostPoolType")
    def host_pool_type(self) -> Optional[str]:
        """
        HostPool type for scaling plan.
        """
        return pulumi.get(self, "host_pool_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def schedules(self) -> Optional[Sequence['outputs.ScalingScheduleResponse']]:
        """
        List of ScalingSchedule definitions.
        """
        return pulumi.get(self, "schedules")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter(name="timeZone")
    def time_zone(self) -> Optional[str]:
        """
        Timezone of the scaling plan.
        """
        return pulumi.get(self, "time_zone")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetScalingPlanResult(GetScalingPlanResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetScalingPlanResult(
            description=self.description,
            exclusion_tag=self.exclusion_tag,
            friendly_name=self.friendly_name,
            host_pool_references=self.host_pool_references,
            host_pool_type=self.host_pool_type,
            id=self.id,
            location=self.location,
            name=self.name,
            schedules=self.schedules,
            tags=self.tags,
            time_zone=self.time_zone,
            type=self.type)


def get_scaling_plan(resource_group_name: Optional[str] = None,
                     scaling_plan_name: Optional[str] = None,
                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetScalingPlanResult:
    """
    Get a scaling plan.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str scaling_plan_name: The name of the scaling plan.
    """
    pulumi.log.warn("""get_scaling_plan is deprecated: Version 2020-11-10-preview will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['scalingPlanName'] = scaling_plan_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:desktopvirtualization/v20201110preview:getScalingPlan', __args__, opts=opts, typ=GetScalingPlanResult).value

    return AwaitableGetScalingPlanResult(
        description=__ret__.description,
        exclusion_tag=__ret__.exclusion_tag,
        friendly_name=__ret__.friendly_name,
        host_pool_references=__ret__.host_pool_references,
        host_pool_type=__ret__.host_pool_type,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        schedules=__ret__.schedules,
        tags=__ret__.tags,
        time_zone=__ret__.time_zone,
        type=__ret__.type)


@_utilities.lift_output_func(get_scaling_plan)
def get_scaling_plan_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                            scaling_plan_name: Optional[pulumi.Input[str]] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetScalingPlanResult]:
    """
    Get a scaling plan.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str scaling_plan_name: The name of the scaling plan.
    """
    pulumi.log.warn("""get_scaling_plan is deprecated: Version 2020-11-10-preview will be removed in v2 of the provider.""")
    ...
