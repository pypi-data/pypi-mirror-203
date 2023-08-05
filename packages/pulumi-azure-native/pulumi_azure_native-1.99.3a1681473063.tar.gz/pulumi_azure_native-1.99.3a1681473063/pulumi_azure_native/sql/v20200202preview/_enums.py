# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'AdministratorType',
    'AutoExecuteStatus',
    'BlobAuditingPolicyState',
    'CatalogCollationType',
    'CreateMode',
    'DatabaseLicenseType',
    'DatabaseReadScale',
    'ElasticPoolLicenseType',
    'IdentityType',
    'InstancePoolLicenseType',
    'JobScheduleType',
    'JobStepActionSource',
    'JobStepActionType',
    'JobStepOutputType',
    'JobTargetGroupMembershipType',
    'JobTargetType',
    'ManagedDatabaseCreateMode',
    'ManagedInstanceAdministratorType',
    'ManagedInstanceLicenseType',
    'ManagedInstanceProxyOverride',
    'ManagedServerCreateMode',
    'PrivateLinkServiceConnectionStateStatus',
    'ReadOnlyEndpointFailoverPolicy',
    'ReadWriteEndpointFailoverPolicy',
    'SampleName',
    'SecurityAlertsPolicyState',
    'SensitivityLabelRank',
    'ServerKeyType',
    'ServerPublicNetworkAccess',
    'StorageAccountType',
    'SyncConflictResolutionPolicy',
    'SyncDirection',
    'SyncMemberDbType',
    'TransparentDataEncryptionState',
]


class AdministratorType(str, Enum):
    """
    Type of the sever administrator.
    """
    ACTIVE_DIRECTORY = "ActiveDirectory"


class AutoExecuteStatus(str, Enum):
    """
    Gets the auto-execute status (whether to let the system execute the recommendations) of this advisor. Possible values are 'Enabled' and 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    DEFAULT = "Default"


class BlobAuditingPolicyState(str, Enum):
    """
    Specifies the state of the audit. If state is Enabled, storageEndpoint or isAzureMonitorTargetEnabled are required.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class CatalogCollationType(str, Enum):
    """
    Collation of the metadata catalog.
    """
    DATABAS_E_DEFAULT = "DATABASE_DEFAULT"
    SQ_L_LATIN1_GENERAL_CP1_C_I_AS = "SQL_Latin1_General_CP1_CI_AS"


class CreateMode(str, Enum):
    """
    Specifies the mode of database creation.
    
    Default: regular database creation.
    
    Copy: creates a database as a copy of an existing database. sourceDatabaseId must be specified as the resource ID of the source database.
    
    Secondary: creates a database as a secondary replica of an existing database. sourceDatabaseId must be specified as the resource ID of the existing primary database.
    
    PointInTimeRestore: Creates a database by restoring a point in time backup of an existing database. sourceDatabaseId must be specified as the resource ID of the existing database, and restorePointInTime must be specified.
    
    Recovery: Creates a database by restoring a geo-replicated backup. sourceDatabaseId must be specified as the recoverable database resource ID to restore.
    
    Restore: Creates a database by restoring a backup of a deleted database. sourceDatabaseId must be specified. If sourceDatabaseId is the database's original resource ID, then sourceDatabaseDeletionDate must be specified. Otherwise sourceDatabaseId must be the restorable dropped database resource ID and sourceDatabaseDeletionDate is ignored. restorePointInTime may also be specified to restore from an earlier point in time.
    
    RestoreLongTermRetentionBackup: Creates a database by restoring from a long term retention vault. recoveryServicesRecoveryPointResourceId must be specified as the recovery point resource ID.
    
    Copy, Secondary, and RestoreLongTermRetentionBackup are not supported for DataWarehouse edition.
    """
    DEFAULT = "Default"
    COPY = "Copy"
    SECONDARY = "Secondary"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RESTORE = "Restore"
    RECOVERY = "Recovery"
    RESTORE_EXTERNAL_BACKUP = "RestoreExternalBackup"
    RESTORE_EXTERNAL_BACKUP_SECONDARY = "RestoreExternalBackupSecondary"
    RESTORE_LONG_TERM_RETENTION_BACKUP = "RestoreLongTermRetentionBackup"
    ONLINE_SECONDARY = "OnlineSecondary"


class DatabaseLicenseType(str, Enum):
    """
    The license type to apply for this database. `LicenseIncluded` if you need a license, or `BasePrice` if you have a license and are eligible for the Azure Hybrid Benefit.
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class DatabaseReadScale(str, Enum):
    """
    The state of read-only routing. If enabled, connections that have application intent set to readonly in their connection string may be routed to a readonly secondary replica in the same region.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ElasticPoolLicenseType(str, Enum):
    """
    The license type to apply for this elastic pool.
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class IdentityType(str, Enum):
    """
    The identity type. Set this to 'SystemAssigned' in order to automatically create and assign an Azure Active Directory principal for the resource.
    """
    NONE = "None"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned,UserAssigned"


class InstancePoolLicenseType(str, Enum):
    """
    The license type. Possible values are 'LicenseIncluded' (price for SQL license is included) and 'BasePrice' (without SQL license price).
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class JobScheduleType(str, Enum):
    """
    Schedule interval type
    """
    ONCE = "Once"
    RECURRING = "Recurring"


class JobStepActionSource(str, Enum):
    """
    The source of the action to execute.
    """
    INLINE = "Inline"


class JobStepActionType(str, Enum):
    """
    Type of action being executed by the job step.
    """
    T_SQL = "TSql"


class JobStepOutputType(str, Enum):
    """
    The output destination type.
    """
    SQL_DATABASE = "SqlDatabase"


class JobTargetGroupMembershipType(str, Enum):
    """
    Whether the target is included or excluded from the group.
    """
    INCLUDE = "Include"
    EXCLUDE = "Exclude"


class JobTargetType(str, Enum):
    """
    The target type.
    """
    TARGET_GROUP = "TargetGroup"
    SQL_DATABASE = "SqlDatabase"
    SQL_ELASTIC_POOL = "SqlElasticPool"
    SQL_SHARD_MAP = "SqlShardMap"
    SQL_SERVER = "SqlServer"


class ManagedDatabaseCreateMode(str, Enum):
    """
    Managed database create mode. PointInTimeRestore: Create a database by restoring a point in time backup of an existing database. SourceDatabaseName, SourceManagedInstanceName and PointInTime must be specified. RestoreExternalBackup: Create a database by restoring from external backup files. Collation, StorageContainerUri and StorageContainerSasToken must be specified. Recovery: Creates a database by restoring a geo-replicated backup. RecoverableDatabaseId must be specified as the recoverable database resource ID to restore. RestoreLongTermRetentionBackup: Create a database by restoring from a long term retention backup (longTermRetentionBackupResourceId required).
    """
    DEFAULT = "Default"
    RESTORE_EXTERNAL_BACKUP = "RestoreExternalBackup"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"
    RECOVERY = "Recovery"
    RESTORE_LONG_TERM_RETENTION_BACKUP = "RestoreLongTermRetentionBackup"


class ManagedInstanceAdministratorType(str, Enum):
    """
    Type of the managed instance administrator.
    """
    ACTIVE_DIRECTORY = "ActiveDirectory"


class ManagedInstanceLicenseType(str, Enum):
    """
    The license type. Possible values are 'LicenseIncluded' (regular price inclusive of a new SQL license) and 'BasePrice' (discounted AHB price for bringing your own SQL licenses).
    """
    LICENSE_INCLUDED = "LicenseIncluded"
    BASE_PRICE = "BasePrice"


class ManagedInstanceProxyOverride(str, Enum):
    """
    Connection type used for connecting to the instance.
    """
    PROXY = "Proxy"
    REDIRECT = "Redirect"
    DEFAULT = "Default"


class ManagedServerCreateMode(str, Enum):
    """
    Specifies the mode of database creation.
    
    Default: Regular instance creation.
    
    Restore: Creates an instance by restoring a set of backups to specific point in time. RestorePointInTime and SourceManagedInstanceId must be specified.
    """
    DEFAULT = "Default"
    POINT_IN_TIME_RESTORE = "PointInTimeRestore"


class PrivateLinkServiceConnectionStateStatus(str, Enum):
    """
    The private link service connection status.
    """
    APPROVED = "Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class ReadOnlyEndpointFailoverPolicy(str, Enum):
    """
    Failover policy of the read-only endpoint for the failover group.
    """
    DISABLED = "Disabled"
    ENABLED = "Enabled"


class ReadWriteEndpointFailoverPolicy(str, Enum):
    """
    Failover policy of the read-write endpoint for the failover group. If failoverPolicy is Automatic then failoverWithDataLossGracePeriodMinutes is required.
    """
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class SampleName(str, Enum):
    """
    The name of the sample schema to apply when creating this database.
    """
    ADVENTURE_WORKS_LT = "AdventureWorksLT"
    WIDE_WORLD_IMPORTERS_STD = "WideWorldImportersStd"
    WIDE_WORLD_IMPORTERS_FULL = "WideWorldImportersFull"


class SecurityAlertsPolicyState(str, Enum):
    """
    Specifies the state of the policy, whether it is enabled or disabled or a policy has not been applied yet on the specific database.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class SensitivityLabelRank(str, Enum):
    NONE = "None"
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class ServerKeyType(str, Enum):
    """
    The server key type like 'ServiceManaged', 'AzureKeyVault'.
    """
    SERVICE_MANAGED = "ServiceManaged"
    AZURE_KEY_VAULT = "AzureKeyVault"


class ServerPublicNetworkAccess(str, Enum):
    """
    Whether or not public endpoint access is allowed for this server.  Value is optional but if passed in, must be 'Enabled' or 'Disabled'
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class StorageAccountType(str, Enum):
    """
    The storage account type used to store backups for this instance. The options are LRS (LocallyRedundantStorage), ZRS (ZoneRedundantStorage) and GRS (GeoRedundantStorage)
    """
    GRS = "GRS"
    LRS = "LRS"
    ZRS = "ZRS"


class SyncConflictResolutionPolicy(str, Enum):
    """
    Conflict resolution policy of the sync group.
    """
    HUB_WIN = "HubWin"
    MEMBER_WIN = "MemberWin"


class SyncDirection(str, Enum):
    """
    Sync direction of the sync member.
    """
    BIDIRECTIONAL = "Bidirectional"
    ONE_WAY_MEMBER_TO_HUB = "OneWayMemberToHub"
    ONE_WAY_HUB_TO_MEMBER = "OneWayHubToMember"


class SyncMemberDbType(str, Enum):
    """
    Database type of the sync member.
    """
    AZURE_SQL_DATABASE = "AzureSqlDatabase"
    SQL_SERVER_DATABASE = "SqlServerDatabase"


class TransparentDataEncryptionState(str, Enum):
    """
    Specifies the state of the transparent data encryption.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
