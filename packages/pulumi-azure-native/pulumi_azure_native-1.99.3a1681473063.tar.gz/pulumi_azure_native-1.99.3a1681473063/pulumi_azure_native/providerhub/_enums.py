# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'ExtendedLocationType',
    'ExtensionCategory',
    'ExtensionOptionType',
    'FeaturesPolicy',
    'IdentityManagementTypes',
    'LoggingDetails',
    'LoggingDirections',
    'MarketplaceType',
    'MessageScope',
    'NotificationMode',
    'OperationActionType',
    'OperationOrigins',
    'OptInHeaderType',
    'PreflightOption',
    'ProvisioningState',
    'Regionality',
    'ResourceAccessPolicy',
    'ResourceDeletionPolicy',
    'ResourceProviderCapabilitiesEffect',
    'ResourceProviderType',
    'RoutingType',
    'SkuScaleType',
    'SubscriptionNotificationOperation',
    'SubscriptionReregistrationResult',
    'SubscriptionState',
    'SubscriptionTransitioningState',
    'ThrottlingMetricType',
    'TrafficRegionCategory',
]


class ExtendedLocationType(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    EDGE_ZONE = "EdgeZone"
    ARC_ZONE = "ArcZone"


class ExtensionCategory(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    RESOURCE_CREATION_VALIDATE = "ResourceCreationValidate"
    RESOURCE_CREATION_BEGIN = "ResourceCreationBegin"
    RESOURCE_CREATION_COMPLETED = "ResourceCreationCompleted"
    RESOURCE_READ_VALIDATE = "ResourceReadValidate"
    RESOURCE_READ_BEGIN = "ResourceReadBegin"
    RESOURCE_PATCH_VALIDATE = "ResourcePatchValidate"
    RESOURCE_PATCH_COMPLETED = "ResourcePatchCompleted"
    RESOURCE_DELETION_VALIDATE = "ResourceDeletionValidate"
    RESOURCE_DELETION_BEGIN = "ResourceDeletionBegin"
    RESOURCE_DELETION_COMPLETED = "ResourceDeletionCompleted"
    RESOURCE_POST_ACTION = "ResourcePostAction"
    SUBSCRIPTION_LIFECYCLE_NOTIFICATION = "SubscriptionLifecycleNotification"
    RESOURCE_PATCH_BEGIN = "ResourcePatchBegin"
    RESOURCE_MOVE_BEGIN = "ResourceMoveBegin"
    RESOURCE_MOVE_COMPLETED = "ResourceMoveCompleted"


class ExtensionOptionType(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    DO_NOT_MERGE_EXISTING_READ_ONLY_AND_SECRET_PROPERTIES = "DoNotMergeExistingReadOnlyAndSecretProperties"
    INCLUDE_INTERNAL_METADATA = "IncludeInternalMetadata"


class FeaturesPolicy(str, Enum):
    ANY = "Any"
    ALL = "All"


class IdentityManagementTypes(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    ACTOR = "Actor"
    DELEGATED_RESOURCE_IDENTITY = "DelegatedResourceIdentity"


class LoggingDetails(str, Enum):
    NONE = "None"
    BODY = "Body"


class LoggingDirections(str, Enum):
    NONE = "None"
    REQUEST = "Request"
    RESPONSE = "Response"


class MarketplaceType(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    ADD_ON = "AddOn"
    BYPASS = "Bypass"
    STORE = "Store"


class MessageScope(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    REGISTERED_SUBSCRIPTIONS = "RegisteredSubscriptions"


class NotificationMode(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    EVENT_HUB = "EventHub"
    WEB_HOOK = "WebHook"


class OperationActionType(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    INTERNAL = "Internal"


class OperationOrigins(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    USER = "User"
    SYSTEM = "System"


class OptInHeaderType(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    SIGNED_USER_TOKEN = "SignedUserToken"
    CLIENT_GROUP_MEMBERSHIP = "ClientGroupMembership"
    SIGNED_AUXILIARY_TOKENS = "SignedAuxiliaryTokens"
    UNBOUNDED_CLIENT_GROUP_MEMBERSHIP = "UnboundedClientGroupMembership"


class PreflightOption(str, Enum):
    NONE = "None"
    CONTINUE_DEPLOYMENT_ON_FAILURE = "ContinueDeploymentOnFailure"
    DEFAULT_VALIDATION_ONLY = "DefaultValidationOnly"


class ProvisioningState(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    ACCEPTED = "Accepted"
    RUNNING = "Running"
    CREATING = "Creating"
    CREATED = "Created"
    DELETING = "Deleting"
    DELETED = "Deleted"
    CANCELED = "Canceled"
    FAILED = "Failed"
    SUCCEEDED = "Succeeded"
    MOVING_RESOURCES = "MovingResources"
    TRANSIENT_FAILURE = "TransientFailure"
    ROLLOUT_IN_PROGRESS = "RolloutInProgress"


class Regionality(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    GLOBAL_ = "Global"
    REGIONAL = "Regional"


class ResourceAccessPolicy(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    ACIS_READ_ALLOWED = "AcisReadAllowed"
    ACIS_ACTION_ALLOWED = "AcisActionAllowed"


class ResourceDeletionPolicy(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    CASCADE_DELETE_ALL = "CascadeDeleteAll"
    CASCADE_DELETE_PROXY_ONLY_CHILDREN = "CascadeDeleteProxyOnlyChildren"


class ResourceProviderCapabilitiesEffect(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    ALLOW = "Allow"
    DISALLOW = "Disallow"


class ResourceProviderType(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    INTERNAL = "Internal"
    EXTERNAL = "External"
    HIDDEN = "Hidden"
    REGISTRATION_FREE = "RegistrationFree"
    LEGACY_REGISTRATION_REQUIRED = "LegacyRegistrationRequired"
    TENANT_ONLY = "TenantOnly"
    AUTHORIZATION_FREE = "AuthorizationFree"


class RoutingType(str, Enum):
    DEFAULT = "Default"
    PROXY_ONLY = "ProxyOnly"
    HOST_BASED = "HostBased"
    EXTENSION = "Extension"
    TENANT = "Tenant"
    FANOUT = "Fanout"
    LOCATION_BASED = "LocationBased"
    FAILOVER = "Failover"
    CASCADE_EXTENSION = "CascadeExtension"


class SkuScaleType(str, Enum):
    NONE = "None"
    MANUAL = "Manual"
    AUTOMATIC = "Automatic"


class SubscriptionNotificationOperation(str, Enum):
    NOT_DEFINED = "NotDefined"
    DELETE_ALL_RESOURCES = "DeleteAllResources"
    SOFT_DELETE_ALL_RESOURCES = "SoftDeleteAllResources"
    NO_OP = "NoOp"
    BILLING_CANCELLATION = "BillingCancellation"
    UNDO_SOFT_DELETE = "UndoSoftDelete"


class SubscriptionReregistrationResult(str, Enum):
    NOT_APPLICABLE = "NotApplicable"
    CONDITIONAL_UPDATE = "ConditionalUpdate"
    FORCED_UPDATE = "ForcedUpdate"
    FAILED = "Failed"


class SubscriptionState(str, Enum):
    NOT_DEFINED = "NotDefined"
    ENABLED = "Enabled"
    WARNED = "Warned"
    PAST_DUE = "PastDue"
    DISABLED = "Disabled"
    DELETED = "Deleted"


class SubscriptionTransitioningState(str, Enum):
    REGISTERED = "Registered"
    UNREGISTERED = "Unregistered"
    WARNED = "Warned"
    SUSPENDED = "Suspended"
    DELETED = "Deleted"
    WARNED_TO_REGISTERED = "WarnedToRegistered"
    WARNED_TO_SUSPENDED = "WarnedToSuspended"
    WARNED_TO_DELETED = "WarnedToDeleted"
    WARNED_TO_UNREGISTERED = "WarnedToUnregistered"
    SUSPENDED_TO_REGISTERED = "SuspendedToRegistered"
    SUSPENDED_TO_WARNED = "SuspendedToWarned"
    SUSPENDED_TO_DELETED = "SuspendedToDeleted"
    SUSPENDED_TO_UNREGISTERED = "SuspendedToUnregistered"


class ThrottlingMetricType(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    NUMBER_OF_REQUESTS = "NumberOfRequests"
    NUMBER_OF_RESOURCES = "NumberOfResources"


class TrafficRegionCategory(str, Enum):
    NOT_SPECIFIED = "NotSpecified"
    CANARY = "Canary"
    LOW_TRAFFIC = "LowTraffic"
    MEDIUM_TRAFFIC = "MediumTraffic"
    HIGH_TRAFFIC = "HighTraffic"
    NONE = "None"
    REST_OF_THE_WORLD_GROUP_ONE = "RestOfTheWorldGroupOne"
    REST_OF_THE_WORLD_GROUP_TWO = "RestOfTheWorldGroupTwo"
