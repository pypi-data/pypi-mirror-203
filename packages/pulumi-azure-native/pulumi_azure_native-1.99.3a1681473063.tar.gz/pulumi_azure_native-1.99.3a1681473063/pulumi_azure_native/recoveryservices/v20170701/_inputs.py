# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'AzureRecoveryServiceVaultProtectionIntentArgs',
    'AzureResourceProtectionIntentArgs',
    'AzureWorkloadAutoProtectionIntentArgs',
    'AzureWorkloadSQLAutoProtectionIntentArgs',
]

@pulumi.input_type
class AzureRecoveryServiceVaultProtectionIntentArgs:
    def __init__(__self__, *,
                 backup_management_type: Optional[pulumi.Input[Union[str, 'BackupManagementType']]] = None,
                 item_id: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 protection_intent_item_type: Optional[pulumi.Input[str]] = None,
                 protection_state: Optional[pulumi.Input[Union[str, 'ProtectionStatus']]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Azure Recovery Services Vault specific protection intent item.
        :param pulumi.Input[Union[str, 'BackupManagementType']] backup_management_type: Type of backup management for the backed up item.
        :param pulumi.Input[str] item_id: ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId
        :param pulumi.Input[str] policy_id: ID of the backup policy with which this item is backed up.
        :param pulumi.Input[str] protection_intent_item_type: backup protectionIntent type.
               Expected value is 'RecoveryServiceVaultItem'.
        :param pulumi.Input[Union[str, 'ProtectionStatus']] protection_state: Backup state of this backup item.
        :param pulumi.Input[str] source_resource_id: ARM ID of the resource to be backed up.
        """
        if backup_management_type is not None:
            pulumi.set(__self__, "backup_management_type", backup_management_type)
        if item_id is not None:
            pulumi.set(__self__, "item_id", item_id)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if protection_intent_item_type is not None:
            pulumi.set(__self__, "protection_intent_item_type", 'RecoveryServiceVaultItem')
        if protection_state is not None:
            pulumi.set(__self__, "protection_state", protection_state)
        if source_resource_id is not None:
            pulumi.set(__self__, "source_resource_id", source_resource_id)

    @property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[pulumi.Input[Union[str, 'BackupManagementType']]]:
        """
        Type of backup management for the backed up item.
        """
        return pulumi.get(self, "backup_management_type")

    @backup_management_type.setter
    def backup_management_type(self, value: Optional[pulumi.Input[Union[str, 'BackupManagementType']]]):
        pulumi.set(self, "backup_management_type", value)

    @property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId
        """
        return pulumi.get(self, "item_id")

    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "item_id", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the backup policy with which this item is backed up.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> Optional[pulumi.Input[str]]:
        """
        backup protectionIntent type.
        Expected value is 'RecoveryServiceVaultItem'.
        """
        return pulumi.get(self, "protection_intent_item_type")

    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protection_intent_item_type", value)

    @property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[pulumi.Input[Union[str, 'ProtectionStatus']]]:
        """
        Backup state of this backup item.
        """
        return pulumi.get(self, "protection_state")

    @protection_state.setter
    def protection_state(self, value: Optional[pulumi.Input[Union[str, 'ProtectionStatus']]]):
        pulumi.set(self, "protection_state", value)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM ID of the resource to be backed up.
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_id", value)


@pulumi.input_type
class AzureResourceProtectionIntentArgs:
    def __init__(__self__, *,
                 backup_management_type: Optional[pulumi.Input[Union[str, 'BackupManagementType']]] = None,
                 friendly_name: Optional[pulumi.Input[str]] = None,
                 item_id: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 protection_intent_item_type: Optional[pulumi.Input[str]] = None,
                 protection_state: Optional[pulumi.Input[Union[str, 'ProtectionStatus']]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None):
        """
        IaaS VM specific backup protection intent item.
        :param pulumi.Input[Union[str, 'BackupManagementType']] backup_management_type: Type of backup management for the backed up item.
        :param pulumi.Input[str] friendly_name: Friendly name of the VM represented by this backup item.
        :param pulumi.Input[str] item_id: ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId
        :param pulumi.Input[str] policy_id: ID of the backup policy with which this item is backed up.
        :param pulumi.Input[str] protection_intent_item_type: backup protectionIntent type.
               Expected value is 'AzureResourceItem'.
        :param pulumi.Input[Union[str, 'ProtectionStatus']] protection_state: Backup state of this backup item.
        :param pulumi.Input[str] source_resource_id: ARM ID of the resource to be backed up.
        """
        if backup_management_type is not None:
            pulumi.set(__self__, "backup_management_type", backup_management_type)
        if friendly_name is not None:
            pulumi.set(__self__, "friendly_name", friendly_name)
        if item_id is not None:
            pulumi.set(__self__, "item_id", item_id)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if protection_intent_item_type is not None:
            pulumi.set(__self__, "protection_intent_item_type", 'AzureResourceItem')
        if protection_state is not None:
            pulumi.set(__self__, "protection_state", protection_state)
        if source_resource_id is not None:
            pulumi.set(__self__, "source_resource_id", source_resource_id)

    @property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[pulumi.Input[Union[str, 'BackupManagementType']]]:
        """
        Type of backup management for the backed up item.
        """
        return pulumi.get(self, "backup_management_type")

    @backup_management_type.setter
    def backup_management_type(self, value: Optional[pulumi.Input[Union[str, 'BackupManagementType']]]):
        pulumi.set(self, "backup_management_type", value)

    @property
    @pulumi.getter(name="friendlyName")
    def friendly_name(self) -> Optional[pulumi.Input[str]]:
        """
        Friendly name of the VM represented by this backup item.
        """
        return pulumi.get(self, "friendly_name")

    @friendly_name.setter
    def friendly_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "friendly_name", value)

    @property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId
        """
        return pulumi.get(self, "item_id")

    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "item_id", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the backup policy with which this item is backed up.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> Optional[pulumi.Input[str]]:
        """
        backup protectionIntent type.
        Expected value is 'AzureResourceItem'.
        """
        return pulumi.get(self, "protection_intent_item_type")

    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protection_intent_item_type", value)

    @property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[pulumi.Input[Union[str, 'ProtectionStatus']]]:
        """
        Backup state of this backup item.
        """
        return pulumi.get(self, "protection_state")

    @protection_state.setter
    def protection_state(self, value: Optional[pulumi.Input[Union[str, 'ProtectionStatus']]]):
        pulumi.set(self, "protection_state", value)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM ID of the resource to be backed up.
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_id", value)


@pulumi.input_type
class AzureWorkloadAutoProtectionIntentArgs:
    def __init__(__self__, *,
                 backup_management_type: Optional[pulumi.Input[Union[str, 'BackupManagementType']]] = None,
                 item_id: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 protection_intent_item_type: Optional[pulumi.Input[str]] = None,
                 protection_state: Optional[pulumi.Input[Union[str, 'ProtectionStatus']]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None):
        """
        Azure Recovery Services Vault specific protection intent item.
        :param pulumi.Input[Union[str, 'BackupManagementType']] backup_management_type: Type of backup management for the backed up item.
        :param pulumi.Input[str] item_id: ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId
        :param pulumi.Input[str] policy_id: ID of the backup policy with which this item is backed up.
        :param pulumi.Input[str] protection_intent_item_type: backup protectionIntent type.
               Expected value is 'AzureWorkloadAutoProtectionIntent'.
        :param pulumi.Input[Union[str, 'ProtectionStatus']] protection_state: Backup state of this backup item.
        :param pulumi.Input[str] source_resource_id: ARM ID of the resource to be backed up.
        """
        if backup_management_type is not None:
            pulumi.set(__self__, "backup_management_type", backup_management_type)
        if item_id is not None:
            pulumi.set(__self__, "item_id", item_id)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if protection_intent_item_type is not None:
            pulumi.set(__self__, "protection_intent_item_type", 'AzureWorkloadAutoProtectionIntent')
        if protection_state is not None:
            pulumi.set(__self__, "protection_state", protection_state)
        if source_resource_id is not None:
            pulumi.set(__self__, "source_resource_id", source_resource_id)

    @property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[pulumi.Input[Union[str, 'BackupManagementType']]]:
        """
        Type of backup management for the backed up item.
        """
        return pulumi.get(self, "backup_management_type")

    @backup_management_type.setter
    def backup_management_type(self, value: Optional[pulumi.Input[Union[str, 'BackupManagementType']]]):
        pulumi.set(self, "backup_management_type", value)

    @property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId
        """
        return pulumi.get(self, "item_id")

    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "item_id", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the backup policy with which this item is backed up.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> Optional[pulumi.Input[str]]:
        """
        backup protectionIntent type.
        Expected value is 'AzureWorkloadAutoProtectionIntent'.
        """
        return pulumi.get(self, "protection_intent_item_type")

    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protection_intent_item_type", value)

    @property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[pulumi.Input[Union[str, 'ProtectionStatus']]]:
        """
        Backup state of this backup item.
        """
        return pulumi.get(self, "protection_state")

    @protection_state.setter
    def protection_state(self, value: Optional[pulumi.Input[Union[str, 'ProtectionStatus']]]):
        pulumi.set(self, "protection_state", value)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM ID of the resource to be backed up.
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_id", value)


@pulumi.input_type
class AzureWorkloadSQLAutoProtectionIntentArgs:
    def __init__(__self__, *,
                 backup_management_type: Optional[pulumi.Input[Union[str, 'BackupManagementType']]] = None,
                 item_id: Optional[pulumi.Input[str]] = None,
                 policy_id: Optional[pulumi.Input[str]] = None,
                 protection_intent_item_type: Optional[pulumi.Input[str]] = None,
                 protection_state: Optional[pulumi.Input[Union[str, 'ProtectionStatus']]] = None,
                 source_resource_id: Optional[pulumi.Input[str]] = None,
                 workload_item_type: Optional[pulumi.Input[Union[str, 'WorkloadItemType']]] = None):
        """
        Azure Workload SQL Auto Protection intent item.
        :param pulumi.Input[Union[str, 'BackupManagementType']] backup_management_type: Type of backup management for the backed up item.
        :param pulumi.Input[str] item_id: ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId
        :param pulumi.Input[str] policy_id: ID of the backup policy with which this item is backed up.
        :param pulumi.Input[str] protection_intent_item_type: backup protectionIntent type.
               Expected value is 'AzureWorkloadSQLAutoProtectionIntent'.
        :param pulumi.Input[Union[str, 'ProtectionStatus']] protection_state: Backup state of this backup item.
        :param pulumi.Input[str] source_resource_id: ARM ID of the resource to be backed up.
        :param pulumi.Input[Union[str, 'WorkloadItemType']] workload_item_type: Workload item type of the item for which intent is to be set
        """
        if backup_management_type is not None:
            pulumi.set(__self__, "backup_management_type", backup_management_type)
        if item_id is not None:
            pulumi.set(__self__, "item_id", item_id)
        if policy_id is not None:
            pulumi.set(__self__, "policy_id", policy_id)
        if protection_intent_item_type is not None:
            pulumi.set(__self__, "protection_intent_item_type", 'AzureWorkloadSQLAutoProtectionIntent')
        if protection_state is not None:
            pulumi.set(__self__, "protection_state", protection_state)
        if source_resource_id is not None:
            pulumi.set(__self__, "source_resource_id", source_resource_id)
        if workload_item_type is not None:
            pulumi.set(__self__, "workload_item_type", workload_item_type)

    @property
    @pulumi.getter(name="backupManagementType")
    def backup_management_type(self) -> Optional[pulumi.Input[Union[str, 'BackupManagementType']]]:
        """
        Type of backup management for the backed up item.
        """
        return pulumi.get(self, "backup_management_type")

    @backup_management_type.setter
    def backup_management_type(self, value: Optional[pulumi.Input[Union[str, 'BackupManagementType']]]):
        pulumi.set(self, "backup_management_type", value)

    @property
    @pulumi.getter(name="itemId")
    def item_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the item which is getting protected, In case of Azure Vm , it is ProtectedItemId
        """
        return pulumi.get(self, "item_id")

    @item_id.setter
    def item_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "item_id", value)

    @property
    @pulumi.getter(name="policyId")
    def policy_id(self) -> Optional[pulumi.Input[str]]:
        """
        ID of the backup policy with which this item is backed up.
        """
        return pulumi.get(self, "policy_id")

    @policy_id.setter
    def policy_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "policy_id", value)

    @property
    @pulumi.getter(name="protectionIntentItemType")
    def protection_intent_item_type(self) -> Optional[pulumi.Input[str]]:
        """
        backup protectionIntent type.
        Expected value is 'AzureWorkloadSQLAutoProtectionIntent'.
        """
        return pulumi.get(self, "protection_intent_item_type")

    @protection_intent_item_type.setter
    def protection_intent_item_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "protection_intent_item_type", value)

    @property
    @pulumi.getter(name="protectionState")
    def protection_state(self) -> Optional[pulumi.Input[Union[str, 'ProtectionStatus']]]:
        """
        Backup state of this backup item.
        """
        return pulumi.get(self, "protection_state")

    @protection_state.setter
    def protection_state(self, value: Optional[pulumi.Input[Union[str, 'ProtectionStatus']]]):
        pulumi.set(self, "protection_state", value)

    @property
    @pulumi.getter(name="sourceResourceId")
    def source_resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM ID of the resource to be backed up.
        """
        return pulumi.get(self, "source_resource_id")

    @source_resource_id.setter
    def source_resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "source_resource_id", value)

    @property
    @pulumi.getter(name="workloadItemType")
    def workload_item_type(self) -> Optional[pulumi.Input[Union[str, 'WorkloadItemType']]]:
        """
        Workload item type of the item for which intent is to be set
        """
        return pulumi.get(self, "workload_item_type")

    @workload_item_type.setter
    def workload_item_type(self, value: Optional[pulumi.Input[Union[str, 'WorkloadItemType']]]):
        pulumi.set(self, "workload_item_type", value)


