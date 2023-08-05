# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'GetExtendedServerBlobAuditingPolicyResult',
    'AwaitableGetExtendedServerBlobAuditingPolicyResult',
    'get_extended_server_blob_auditing_policy',
    'get_extended_server_blob_auditing_policy_output',
]

@pulumi.output_type
class GetExtendedServerBlobAuditingPolicyResult:
    """
    An extended server blob auditing policy.
    """
    def __init__(__self__, audit_actions_and_groups=None, id=None, is_azure_monitor_target_enabled=None, is_devops_audit_enabled=None, is_storage_secondary_key_in_use=None, name=None, predicate_expression=None, queue_delay_ms=None, retention_days=None, state=None, storage_account_subscription_id=None, storage_endpoint=None, type=None):
        if audit_actions_and_groups and not isinstance(audit_actions_and_groups, list):
            raise TypeError("Expected argument 'audit_actions_and_groups' to be a list")
        pulumi.set(__self__, "audit_actions_and_groups", audit_actions_and_groups)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_azure_monitor_target_enabled and not isinstance(is_azure_monitor_target_enabled, bool):
            raise TypeError("Expected argument 'is_azure_monitor_target_enabled' to be a bool")
        pulumi.set(__self__, "is_azure_monitor_target_enabled", is_azure_monitor_target_enabled)
        if is_devops_audit_enabled and not isinstance(is_devops_audit_enabled, bool):
            raise TypeError("Expected argument 'is_devops_audit_enabled' to be a bool")
        pulumi.set(__self__, "is_devops_audit_enabled", is_devops_audit_enabled)
        if is_storage_secondary_key_in_use and not isinstance(is_storage_secondary_key_in_use, bool):
            raise TypeError("Expected argument 'is_storage_secondary_key_in_use' to be a bool")
        pulumi.set(__self__, "is_storage_secondary_key_in_use", is_storage_secondary_key_in_use)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if predicate_expression and not isinstance(predicate_expression, str):
            raise TypeError("Expected argument 'predicate_expression' to be a str")
        pulumi.set(__self__, "predicate_expression", predicate_expression)
        if queue_delay_ms and not isinstance(queue_delay_ms, int):
            raise TypeError("Expected argument 'queue_delay_ms' to be a int")
        pulumi.set(__self__, "queue_delay_ms", queue_delay_ms)
        if retention_days and not isinstance(retention_days, int):
            raise TypeError("Expected argument 'retention_days' to be a int")
        pulumi.set(__self__, "retention_days", retention_days)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if storage_account_subscription_id and not isinstance(storage_account_subscription_id, str):
            raise TypeError("Expected argument 'storage_account_subscription_id' to be a str")
        pulumi.set(__self__, "storage_account_subscription_id", storage_account_subscription_id)
        if storage_endpoint and not isinstance(storage_endpoint, str):
            raise TypeError("Expected argument 'storage_endpoint' to be a str")
        pulumi.set(__self__, "storage_endpoint", storage_endpoint)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="auditActionsAndGroups")
    def audit_actions_and_groups(self) -> Optional[Sequence[str]]:
        """
        Specifies the Actions-Groups and Actions to audit.
        
        The recommended set of action groups to use is the following combination - this will audit all the queries and stored procedures executed against the database, as well as successful and failed logins:
        
        BATCH_COMPLETED_GROUP,
        SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP,
        FAILED_DATABASE_AUTHENTICATION_GROUP.
        
        This above combination is also the set that is configured by default when enabling auditing from the Azure portal.
        
        The supported action groups to audit are (note: choose only specific groups that cover your auditing needs. Using unnecessary groups could lead to very large quantities of audit records):
        
        APPLICATION_ROLE_CHANGE_PASSWORD_GROUP
        BACKUP_RESTORE_GROUP
        DATABASE_LOGOUT_GROUP
        DATABASE_OBJECT_CHANGE_GROUP
        DATABASE_OBJECT_OWNERSHIP_CHANGE_GROUP
        DATABASE_OBJECT_PERMISSION_CHANGE_GROUP
        DATABASE_OPERATION_GROUP
        DATABASE_PERMISSION_CHANGE_GROUP
        DATABASE_PRINCIPAL_CHANGE_GROUP
        DATABASE_PRINCIPAL_IMPERSONATION_GROUP
        DATABASE_ROLE_MEMBER_CHANGE_GROUP
        FAILED_DATABASE_AUTHENTICATION_GROUP
        SCHEMA_OBJECT_ACCESS_GROUP
        SCHEMA_OBJECT_CHANGE_GROUP
        SCHEMA_OBJECT_OWNERSHIP_CHANGE_GROUP
        SCHEMA_OBJECT_PERMISSION_CHANGE_GROUP
        SUCCESSFUL_DATABASE_AUTHENTICATION_GROUP
        USER_CHANGE_PASSWORD_GROUP
        BATCH_STARTED_GROUP
        BATCH_COMPLETED_GROUP
        
        These are groups that cover all sql statements and stored procedures executed against the database, and should not be used in combination with other groups as this will result in duplicate audit logs.
        
        For more information, see [Database-Level Audit Action Groups](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-action-groups).
        
        For Database auditing policy, specific Actions can also be specified (note that Actions cannot be specified for Server auditing policy). The supported actions to audit are:
        SELECT
        UPDATE
        INSERT
        DELETE
        EXECUTE
        RECEIVE
        REFERENCES
        
        The general form for defining an action to be audited is:
        {action} ON {object} BY {principal}
        
        Note that <object> in the above format can refer to an object like a table, view, or stored procedure, or an entire database or schema. For the latter cases, the forms DATABASE::{db_name} and SCHEMA::{schema_name} are used, respectively.
        
        For example:
        SELECT on dbo.myTable by public
        SELECT on DATABASE::myDatabase by public
        SELECT on SCHEMA::mySchema by public
        
        For more information, see [Database-Level Audit Actions](https://docs.microsoft.com/en-us/sql/relational-databases/security/auditing/sql-server-audit-action-groups-and-actions#database-level-audit-actions)
        """
        return pulumi.get(self, "audit_actions_and_groups")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isAzureMonitorTargetEnabled")
    def is_azure_monitor_target_enabled(self) -> Optional[bool]:
        """
        Specifies whether audit events are sent to Azure Monitor. 
        In order to send the events to Azure Monitor, specify 'State' as 'Enabled' and 'IsAzureMonitorTargetEnabled' as true.
        
        When using REST API to configure auditing, Diagnostic Settings with 'SQLSecurityAuditEvents' diagnostic logs category on the database should be also created.
        Note that for server level audit you should use the 'master' database as {databaseName}.
        
        Diagnostic Settings URI format:
        PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Sql/servers/{serverName}/databases/{databaseName}/providers/microsoft.insights/diagnosticSettings/{settingsName}?api-version=2017-05-01-preview
        
        For more information, see [Diagnostic Settings REST API](https://go.microsoft.com/fwlink/?linkid=2033207)
        or [Diagnostic Settings PowerShell](https://go.microsoft.com/fwlink/?linkid=2033043)
        """
        return pulumi.get(self, "is_azure_monitor_target_enabled")

    @property
    @pulumi.getter(name="isDevopsAuditEnabled")
    def is_devops_audit_enabled(self) -> Optional[bool]:
        """
        Specifies the state of devops audit. If state is Enabled, devops logs will be sent to Azure Monitor.
        In order to send the events to Azure Monitor, specify 'State' as 'Enabled', 'IsAzureMonitorTargetEnabled' as true and 'IsDevopsAuditEnabled' as true
        
        When using REST API to configure auditing, Diagnostic Settings with 'DevOpsOperationsAudit' diagnostic logs category on the master database should also be created.
        
        Diagnostic Settings URI format:
        PUT https://management.azure.com/subscriptions/{subscriptionId}/resourceGroups/{resourceGroup}/providers/Microsoft.Sql/servers/{serverName}/databases/master/providers/microsoft.insights/diagnosticSettings/{settingsName}?api-version=2017-05-01-preview
        
        For more information, see [Diagnostic Settings REST API](https://go.microsoft.com/fwlink/?linkid=2033207)
        or [Diagnostic Settings PowerShell](https://go.microsoft.com/fwlink/?linkid=2033043)
        """
        return pulumi.get(self, "is_devops_audit_enabled")

    @property
    @pulumi.getter(name="isStorageSecondaryKeyInUse")
    def is_storage_secondary_key_in_use(self) -> Optional[bool]:
        """
        Specifies whether storageAccountAccessKey value is the storage's secondary key.
        """
        return pulumi.get(self, "is_storage_secondary_key_in_use")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="predicateExpression")
    def predicate_expression(self) -> Optional[str]:
        """
        Specifies condition of where clause when creating an audit.
        """
        return pulumi.get(self, "predicate_expression")

    @property
    @pulumi.getter(name="queueDelayMs")
    def queue_delay_ms(self) -> Optional[int]:
        """
        Specifies the amount of time in milliseconds that can elapse before audit actions are forced to be processed.
        The default minimum value is 1000 (1 second). The maximum is 2,147,483,647.
        """
        return pulumi.get(self, "queue_delay_ms")

    @property
    @pulumi.getter(name="retentionDays")
    def retention_days(self) -> Optional[int]:
        """
        Specifies the number of days to keep in the audit logs in the storage account.
        """
        return pulumi.get(self, "retention_days")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="storageAccountSubscriptionId")
    def storage_account_subscription_id(self) -> Optional[str]:
        """
        Specifies the blob storage subscription Id.
        """
        return pulumi.get(self, "storage_account_subscription_id")

    @property
    @pulumi.getter(name="storageEndpoint")
    def storage_endpoint(self) -> Optional[str]:
        """
        Specifies the blob storage endpoint (e.g. https://MyAccount.blob.core.windows.net). If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled is required.
        """
        return pulumi.get(self, "storage_endpoint")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetExtendedServerBlobAuditingPolicyResult(GetExtendedServerBlobAuditingPolicyResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetExtendedServerBlobAuditingPolicyResult(
            audit_actions_and_groups=self.audit_actions_and_groups,
            id=self.id,
            is_azure_monitor_target_enabled=self.is_azure_monitor_target_enabled,
            is_devops_audit_enabled=self.is_devops_audit_enabled,
            is_storage_secondary_key_in_use=self.is_storage_secondary_key_in_use,
            name=self.name,
            predicate_expression=self.predicate_expression,
            queue_delay_ms=self.queue_delay_ms,
            retention_days=self.retention_days,
            state=self.state,
            storage_account_subscription_id=self.storage_account_subscription_id,
            storage_endpoint=self.storage_endpoint,
            type=self.type)


def get_extended_server_blob_auditing_policy(blob_auditing_policy_name: Optional[str] = None,
                                             resource_group_name: Optional[str] = None,
                                             server_name: Optional[str] = None,
                                             opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetExtendedServerBlobAuditingPolicyResult:
    """
    Gets an extended server's blob auditing policy.
    API Version: 2020-11-01-preview.


    :param str blob_auditing_policy_name: The name of the blob auditing policy.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    __args__ = dict()
    __args__['blobAuditingPolicyName'] = blob_auditing_policy_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['serverName'] = server_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:sql:getExtendedServerBlobAuditingPolicy', __args__, opts=opts, typ=GetExtendedServerBlobAuditingPolicyResult).value

    return AwaitableGetExtendedServerBlobAuditingPolicyResult(
        audit_actions_and_groups=__ret__.audit_actions_and_groups,
        id=__ret__.id,
        is_azure_monitor_target_enabled=__ret__.is_azure_monitor_target_enabled,
        is_devops_audit_enabled=__ret__.is_devops_audit_enabled,
        is_storage_secondary_key_in_use=__ret__.is_storage_secondary_key_in_use,
        name=__ret__.name,
        predicate_expression=__ret__.predicate_expression,
        queue_delay_ms=__ret__.queue_delay_ms,
        retention_days=__ret__.retention_days,
        state=__ret__.state,
        storage_account_subscription_id=__ret__.storage_account_subscription_id,
        storage_endpoint=__ret__.storage_endpoint,
        type=__ret__.type)


@_utilities.lift_output_func(get_extended_server_blob_auditing_policy)
def get_extended_server_blob_auditing_policy_output(blob_auditing_policy_name: Optional[pulumi.Input[str]] = None,
                                                    resource_group_name: Optional[pulumi.Input[str]] = None,
                                                    server_name: Optional[pulumi.Input[str]] = None,
                                                    opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetExtendedServerBlobAuditingPolicyResult]:
    """
    Gets an extended server's blob auditing policy.
    API Version: 2020-11-01-preview.


    :param str blob_auditing_policy_name: The name of the blob auditing policy.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str server_name: The name of the server.
    """
    ...
