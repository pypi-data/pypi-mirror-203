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
    'GetArcSettingResult',
    'AwaitableGetArcSettingResult',
    'get_arc_setting',
    'get_arc_setting_output',
]

@pulumi.output_type
class GetArcSettingResult:
    """
    ArcSetting details.
    """
    def __init__(__self__, aggregate_state=None, arc_application_client_id=None, arc_application_object_id=None, arc_application_tenant_id=None, arc_instance_resource_group=None, arc_service_principal_object_id=None, connectivity_properties=None, id=None, name=None, per_node_details=None, provisioning_state=None, system_data=None, type=None):
        if aggregate_state and not isinstance(aggregate_state, str):
            raise TypeError("Expected argument 'aggregate_state' to be a str")
        pulumi.set(__self__, "aggregate_state", aggregate_state)
        if arc_application_client_id and not isinstance(arc_application_client_id, str):
            raise TypeError("Expected argument 'arc_application_client_id' to be a str")
        pulumi.set(__self__, "arc_application_client_id", arc_application_client_id)
        if arc_application_object_id and not isinstance(arc_application_object_id, str):
            raise TypeError("Expected argument 'arc_application_object_id' to be a str")
        pulumi.set(__self__, "arc_application_object_id", arc_application_object_id)
        if arc_application_tenant_id and not isinstance(arc_application_tenant_id, str):
            raise TypeError("Expected argument 'arc_application_tenant_id' to be a str")
        pulumi.set(__self__, "arc_application_tenant_id", arc_application_tenant_id)
        if arc_instance_resource_group and not isinstance(arc_instance_resource_group, str):
            raise TypeError("Expected argument 'arc_instance_resource_group' to be a str")
        pulumi.set(__self__, "arc_instance_resource_group", arc_instance_resource_group)
        if arc_service_principal_object_id and not isinstance(arc_service_principal_object_id, str):
            raise TypeError("Expected argument 'arc_service_principal_object_id' to be a str")
        pulumi.set(__self__, "arc_service_principal_object_id", arc_service_principal_object_id)
        if connectivity_properties and not isinstance(connectivity_properties, list):
            raise TypeError("Expected argument 'connectivity_properties' to be a list")
        pulumi.set(__self__, "connectivity_properties", connectivity_properties)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if per_node_details and not isinstance(per_node_details, list):
            raise TypeError("Expected argument 'per_node_details' to be a list")
        pulumi.set(__self__, "per_node_details", per_node_details)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="aggregateState")
    def aggregate_state(self) -> str:
        """
        Aggregate state of Arc agent across the nodes in this HCI cluster.
        """
        return pulumi.get(self, "aggregate_state")

    @property
    @pulumi.getter(name="arcApplicationClientId")
    def arc_application_client_id(self) -> Optional[str]:
        """
        App id of arc AAD identity.
        """
        return pulumi.get(self, "arc_application_client_id")

    @property
    @pulumi.getter(name="arcApplicationObjectId")
    def arc_application_object_id(self) -> Optional[str]:
        """
        Object id of arc AAD identity.
        """
        return pulumi.get(self, "arc_application_object_id")

    @property
    @pulumi.getter(name="arcApplicationTenantId")
    def arc_application_tenant_id(self) -> Optional[str]:
        """
        Tenant id of arc AAD identity.
        """
        return pulumi.get(self, "arc_application_tenant_id")

    @property
    @pulumi.getter(name="arcInstanceResourceGroup")
    def arc_instance_resource_group(self) -> Optional[str]:
        """
        The resource group that hosts the Arc agents, ie. Hybrid Compute Machine resources.
        """
        return pulumi.get(self, "arc_instance_resource_group")

    @property
    @pulumi.getter(name="arcServicePrincipalObjectId")
    def arc_service_principal_object_id(self) -> Optional[str]:
        """
        Object id of arc AAD service principal.
        """
        return pulumi.get(self, "arc_service_principal_object_id")

    @property
    @pulumi.getter(name="connectivityProperties")
    def connectivity_properties(self) -> Optional[Sequence['outputs.ArcConnectivityPropertiesResponse']]:
        """
        contains connectivity related configuration for ARC resources
        """
        return pulumi.get(self, "connectivity_properties")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="perNodeDetails")
    def per_node_details(self) -> Sequence['outputs.PerNodeStateResponse']:
        """
        State of Arc agent in each of the nodes.
        """
        return pulumi.get(self, "per_node_details")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the ArcSetting proxy resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")


class AwaitableGetArcSettingResult(GetArcSettingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetArcSettingResult(
            aggregate_state=self.aggregate_state,
            arc_application_client_id=self.arc_application_client_id,
            arc_application_object_id=self.arc_application_object_id,
            arc_application_tenant_id=self.arc_application_tenant_id,
            arc_instance_resource_group=self.arc_instance_resource_group,
            arc_service_principal_object_id=self.arc_service_principal_object_id,
            connectivity_properties=self.connectivity_properties,
            id=self.id,
            name=self.name,
            per_node_details=self.per_node_details,
            provisioning_state=self.provisioning_state,
            system_data=self.system_data,
            type=self.type)


def get_arc_setting(arc_setting_name: Optional[str] = None,
                    cluster_name: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetArcSettingResult:
    """
    Get ArcSetting resource details of HCI Cluster.


    :param str arc_setting_name: The name of the proxy resource holding details of HCI ArcSetting information.
    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    __args__ = dict()
    __args__['arcSettingName'] = arc_setting_name
    __args__['clusterName'] = cluster_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestackhci/v20230201:getArcSetting', __args__, opts=opts, typ=GetArcSettingResult).value

    return AwaitableGetArcSettingResult(
        aggregate_state=__ret__.aggregate_state,
        arc_application_client_id=__ret__.arc_application_client_id,
        arc_application_object_id=__ret__.arc_application_object_id,
        arc_application_tenant_id=__ret__.arc_application_tenant_id,
        arc_instance_resource_group=__ret__.arc_instance_resource_group,
        arc_service_principal_object_id=__ret__.arc_service_principal_object_id,
        connectivity_properties=__ret__.connectivity_properties,
        id=__ret__.id,
        name=__ret__.name,
        per_node_details=__ret__.per_node_details,
        provisioning_state=__ret__.provisioning_state,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_arc_setting)
def get_arc_setting_output(arc_setting_name: Optional[pulumi.Input[str]] = None,
                           cluster_name: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetArcSettingResult]:
    """
    Get ArcSetting resource details of HCI Cluster.


    :param str arc_setting_name: The name of the proxy resource holding details of HCI ArcSetting information.
    :param str cluster_name: The name of the cluster.
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    """
    ...
