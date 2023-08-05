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

__all__ = [
    'GetSynapseWorkspaceSqlPoolTableDataSetMappingResult',
    'AwaitableGetSynapseWorkspaceSqlPoolTableDataSetMappingResult',
    'get_synapse_workspace_sql_pool_table_data_set_mapping',
    'get_synapse_workspace_sql_pool_table_data_set_mapping_output',
]

@pulumi.output_type
class GetSynapseWorkspaceSqlPoolTableDataSetMappingResult:
    """
    A Synapse Workspace Sql Pool Table data set mapping
    """
    def __init__(__self__, data_set_id=None, data_set_mapping_status=None, id=None, kind=None, name=None, provisioning_state=None, synapse_workspace_sql_pool_table_resource_id=None, system_data=None, type=None):
        if data_set_id and not isinstance(data_set_id, str):
            raise TypeError("Expected argument 'data_set_id' to be a str")
        pulumi.set(__self__, "data_set_id", data_set_id)
        if data_set_mapping_status and not isinstance(data_set_mapping_status, str):
            raise TypeError("Expected argument 'data_set_mapping_status' to be a str")
        pulumi.set(__self__, "data_set_mapping_status", data_set_mapping_status)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if synapse_workspace_sql_pool_table_resource_id and not isinstance(synapse_workspace_sql_pool_table_resource_id, str):
            raise TypeError("Expected argument 'synapse_workspace_sql_pool_table_resource_id' to be a str")
        pulumi.set(__self__, "synapse_workspace_sql_pool_table_resource_id", synapse_workspace_sql_pool_table_resource_id)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="dataSetId")
    def data_set_id(self) -> str:
        """
        The id of the source data set.
        """
        return pulumi.get(self, "data_set_id")

    @property
    @pulumi.getter(name="dataSetMappingStatus")
    def data_set_mapping_status(self) -> str:
        """
        Gets the status of the data set mapping.
        """
        return pulumi.get(self, "data_set_mapping_status")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource id of the azure resource
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Kind of data set mapping.
        Expected value is 'SynapseWorkspaceSqlPoolTable'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the azure resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Provisioning state of the data set mapping.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="synapseWorkspaceSqlPoolTableResourceId")
    def synapse_workspace_sql_pool_table_resource_id(self) -> str:
        """
        Resource id of the Synapse Workspace SQL Pool Table
        """
        return pulumi.get(self, "synapse_workspace_sql_pool_table_resource_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        System Data of the Azure resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of the azure resource
        """
        return pulumi.get(self, "type")


class AwaitableGetSynapseWorkspaceSqlPoolTableDataSetMappingResult(GetSynapseWorkspaceSqlPoolTableDataSetMappingResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSynapseWorkspaceSqlPoolTableDataSetMappingResult(
            data_set_id=self.data_set_id,
            data_set_mapping_status=self.data_set_mapping_status,
            id=self.id,
            kind=self.kind,
            name=self.name,
            provisioning_state=self.provisioning_state,
            synapse_workspace_sql_pool_table_resource_id=self.synapse_workspace_sql_pool_table_resource_id,
            system_data=self.system_data,
            type=self.type)


def get_synapse_workspace_sql_pool_table_data_set_mapping(account_name: Optional[str] = None,
                                                          data_set_mapping_name: Optional[str] = None,
                                                          resource_group_name: Optional[str] = None,
                                                          share_subscription_name: Optional[str] = None,
                                                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSynapseWorkspaceSqlPoolTableDataSetMappingResult:
    """
    Get a DataSetMapping in a shareSubscription
    API Version: 2020-09-01.


    :param str account_name: The name of the share account.
    :param str data_set_mapping_name: The name of the dataSetMapping.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the shareSubscription.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['dataSetMappingName'] = data_set_mapping_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['shareSubscriptionName'] = share_subscription_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:datashare:getSynapseWorkspaceSqlPoolTableDataSetMapping', __args__, opts=opts, typ=GetSynapseWorkspaceSqlPoolTableDataSetMappingResult).value

    return AwaitableGetSynapseWorkspaceSqlPoolTableDataSetMappingResult(
        data_set_id=__ret__.data_set_id,
        data_set_mapping_status=__ret__.data_set_mapping_status,
        id=__ret__.id,
        kind=__ret__.kind,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        synapse_workspace_sql_pool_table_resource_id=__ret__.synapse_workspace_sql_pool_table_resource_id,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_synapse_workspace_sql_pool_table_data_set_mapping)
def get_synapse_workspace_sql_pool_table_data_set_mapping_output(account_name: Optional[pulumi.Input[str]] = None,
                                                                 data_set_mapping_name: Optional[pulumi.Input[str]] = None,
                                                                 resource_group_name: Optional[pulumi.Input[str]] = None,
                                                                 share_subscription_name: Optional[pulumi.Input[str]] = None,
                                                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSynapseWorkspaceSqlPoolTableDataSetMappingResult]:
    """
    Get a DataSetMapping in a shareSubscription
    API Version: 2020-09-01.


    :param str account_name: The name of the share account.
    :param str data_set_mapping_name: The name of the dataSetMapping.
    :param str resource_group_name: The resource group name.
    :param str share_subscription_name: The name of the shareSubscription.
    """
    ...
