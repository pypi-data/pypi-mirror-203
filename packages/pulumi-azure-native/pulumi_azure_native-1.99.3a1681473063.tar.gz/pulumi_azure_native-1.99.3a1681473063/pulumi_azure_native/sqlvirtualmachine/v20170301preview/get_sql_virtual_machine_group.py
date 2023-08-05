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
    'GetSqlVirtualMachineGroupResult',
    'AwaitableGetSqlVirtualMachineGroupResult',
    'get_sql_virtual_machine_group',
    'get_sql_virtual_machine_group_output',
]

@pulumi.output_type
class GetSqlVirtualMachineGroupResult:
    """
    A SQL virtual machine group.
    """
    def __init__(__self__, cluster_configuration=None, cluster_manager_type=None, id=None, location=None, name=None, provisioning_state=None, scale_type=None, sql_image_offer=None, sql_image_sku=None, tags=None, type=None, wsfc_domain_profile=None):
        if cluster_configuration and not isinstance(cluster_configuration, str):
            raise TypeError("Expected argument 'cluster_configuration' to be a str")
        pulumi.set(__self__, "cluster_configuration", cluster_configuration)
        if cluster_manager_type and not isinstance(cluster_manager_type, str):
            raise TypeError("Expected argument 'cluster_manager_type' to be a str")
        pulumi.set(__self__, "cluster_manager_type", cluster_manager_type)
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
        if scale_type and not isinstance(scale_type, str):
            raise TypeError("Expected argument 'scale_type' to be a str")
        pulumi.set(__self__, "scale_type", scale_type)
        if sql_image_offer and not isinstance(sql_image_offer, str):
            raise TypeError("Expected argument 'sql_image_offer' to be a str")
        pulumi.set(__self__, "sql_image_offer", sql_image_offer)
        if sql_image_sku and not isinstance(sql_image_sku, str):
            raise TypeError("Expected argument 'sql_image_sku' to be a str")
        pulumi.set(__self__, "sql_image_sku", sql_image_sku)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if wsfc_domain_profile and not isinstance(wsfc_domain_profile, dict):
            raise TypeError("Expected argument 'wsfc_domain_profile' to be a dict")
        pulumi.set(__self__, "wsfc_domain_profile", wsfc_domain_profile)

    @property
    @pulumi.getter(name="clusterConfiguration")
    def cluster_configuration(self) -> str:
        """
        Cluster type.
        """
        return pulumi.get(self, "cluster_configuration")

    @property
    @pulumi.getter(name="clusterManagerType")
    def cluster_manager_type(self) -> str:
        """
        Type of cluster manager: Windows Server Failover Cluster (WSFC), implied by the scale type of the group and the OS type.
        """
        return pulumi.get(self, "cluster_manager_type")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state to track the async operation status.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="scaleType")
    def scale_type(self) -> str:
        """
        Scale type.
        """
        return pulumi.get(self, "scale_type")

    @property
    @pulumi.getter(name="sqlImageOffer")
    def sql_image_offer(self) -> Optional[str]:
        """
        SQL image offer. Examples may include SQL2016-WS2016, SQL2017-WS2016.
        """
        return pulumi.get(self, "sql_image_offer")

    @property
    @pulumi.getter(name="sqlImageSku")
    def sql_image_sku(self) -> Optional[str]:
        """
        SQL image sku.
        """
        return pulumi.get(self, "sql_image_sku")

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
        Resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="wsfcDomainProfile")
    def wsfc_domain_profile(self) -> Optional['outputs.WsfcDomainProfileResponse']:
        """
        Cluster Active Directory domain profile.
        """
        return pulumi.get(self, "wsfc_domain_profile")


class AwaitableGetSqlVirtualMachineGroupResult(GetSqlVirtualMachineGroupResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSqlVirtualMachineGroupResult(
            cluster_configuration=self.cluster_configuration,
            cluster_manager_type=self.cluster_manager_type,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            scale_type=self.scale_type,
            sql_image_offer=self.sql_image_offer,
            sql_image_sku=self.sql_image_sku,
            tags=self.tags,
            type=self.type,
            wsfc_domain_profile=self.wsfc_domain_profile)


def get_sql_virtual_machine_group(resource_group_name: Optional[str] = None,
                                  sql_virtual_machine_group_name: Optional[str] = None,
                                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSqlVirtualMachineGroupResult:
    """
    Gets a SQL virtual machine group.


    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_virtual_machine_group_name: Name of the SQL virtual machine group.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['sqlVirtualMachineGroupName'] = sql_virtual_machine_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sqlvirtualmachine/v20170301preview:getSqlVirtualMachineGroup', __args__, opts=opts, typ=GetSqlVirtualMachineGroupResult).value

    return AwaitableGetSqlVirtualMachineGroupResult(
        cluster_configuration=__ret__.cluster_configuration,
        cluster_manager_type=__ret__.cluster_manager_type,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        scale_type=__ret__.scale_type,
        sql_image_offer=__ret__.sql_image_offer,
        sql_image_sku=__ret__.sql_image_sku,
        tags=__ret__.tags,
        type=__ret__.type,
        wsfc_domain_profile=__ret__.wsfc_domain_profile)


@_utilities.lift_output_func(get_sql_virtual_machine_group)
def get_sql_virtual_machine_group_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                         sql_virtual_machine_group_name: Optional[pulumi.Input[str]] = None,
                                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSqlVirtualMachineGroupResult]:
    """
    Gets a SQL virtual machine group.


    :param str resource_group_name: Name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str sql_virtual_machine_group_name: Name of the SQL virtual machine group.
    """
    ...
