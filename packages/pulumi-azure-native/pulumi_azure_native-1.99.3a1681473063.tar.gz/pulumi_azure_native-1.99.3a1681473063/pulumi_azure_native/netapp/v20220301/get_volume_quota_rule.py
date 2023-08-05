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
    'GetVolumeQuotaRuleResult',
    'AwaitableGetVolumeQuotaRuleResult',
    'get_volume_quota_rule',
    'get_volume_quota_rule_output',
]

@pulumi.output_type
class GetVolumeQuotaRuleResult:
    """
    Quota Rule of a Volume
    """
    def __init__(__self__, id=None, location=None, name=None, provisioning_state=None, quota_size_in_ki_bs=None, quota_target=None, quota_type=None, system_data=None, tags=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if quota_size_in_ki_bs and not isinstance(quota_size_in_ki_bs, float):
            raise TypeError("Expected argument 'quota_size_in_ki_bs' to be a float")
        pulumi.set(__self__, "quota_size_in_ki_bs", quota_size_in_ki_bs)
        if quota_target and not isinstance(quota_target, str):
            raise TypeError("Expected argument 'quota_target' to be a str")
        pulumi.set(__self__, "quota_target", quota_target)
        if quota_type and not isinstance(quota_type, str):
            raise TypeError("Expected argument 'quota_type' to be a str")
        pulumi.set(__self__, "quota_type", quota_type)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets the status of the VolumeQuotaRule at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="quotaSizeInKiBs")
    def quota_size_in_ki_bs(self) -> Optional[float]:
        """
        Size of quota
        """
        return pulumi.get(self, "quota_size_in_ki_bs")

    @property
    @pulumi.getter(name="quotaTarget")
    def quota_target(self) -> Optional[str]:
        """
        UserID/GroupID/SID based on the quota target type. UserID and groupID can be found by running ‘id’ or ‘getent’ command for the user or group and SID can be found by running <wmic useraccount where name='user-name' get sid>
        """
        return pulumi.get(self, "quota_target")

    @property
    @pulumi.getter(name="quotaType")
    def quota_type(self) -> Optional[str]:
        """
        Type of quota
        """
        return pulumi.get(self, "quota_type")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetVolumeQuotaRuleResult(GetVolumeQuotaRuleResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetVolumeQuotaRuleResult(
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            quota_size_in_ki_bs=self.quota_size_in_ki_bs,
            quota_target=self.quota_target,
            quota_type=self.quota_type,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type)


def get_volume_quota_rule(account_name: Optional[str] = None,
                          pool_name: Optional[str] = None,
                          resource_group_name: Optional[str] = None,
                          volume_name: Optional[str] = None,
                          volume_quota_rule_name: Optional[str] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetVolumeQuotaRuleResult:
    """
    Get details of the specified quota rule


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group.
    :param str volume_name: The name of the volume
    :param str volume_quota_rule_name: The name of volume quota rule
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['poolName'] = pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['volumeName'] = volume_name
    __args__['volumeQuotaRuleName'] = volume_quota_rule_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:netapp/v20220301:getVolumeQuotaRule', __args__, opts=opts, typ=GetVolumeQuotaRuleResult).value

    return AwaitableGetVolumeQuotaRuleResult(
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        quota_size_in_ki_bs=__ret__.quota_size_in_ki_bs,
        quota_target=__ret__.quota_target,
        quota_type=__ret__.quota_type,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_volume_quota_rule)
def get_volume_quota_rule_output(account_name: Optional[pulumi.Input[str]] = None,
                                 pool_name: Optional[pulumi.Input[str]] = None,
                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                 volume_name: Optional[pulumi.Input[str]] = None,
                                 volume_quota_rule_name: Optional[pulumi.Input[str]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetVolumeQuotaRuleResult]:
    """
    Get details of the specified quota rule


    :param str account_name: The name of the NetApp account
    :param str pool_name: The name of the capacity pool
    :param str resource_group_name: The name of the resource group.
    :param str volume_name: The name of the volume
    :param str volume_quota_rule_name: The name of volume quota rule
    """
    ...
