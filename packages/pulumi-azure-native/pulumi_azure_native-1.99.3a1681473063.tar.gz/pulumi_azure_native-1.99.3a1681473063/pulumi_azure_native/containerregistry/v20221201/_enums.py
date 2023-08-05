# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from enum import Enum

__all__ = [
    'Action',
    'ActionsRequired',
    'ConnectionStatus',
    'DefaultAction',
    'EncryptionStatus',
    'ExportPolicyStatus',
    'NetworkRuleBypassOptions',
    'PolicyStatus',
    'PublicNetworkAccess',
    'ResourceIdentityType',
    'SkuName',
    'TokenCertificateName',
    'TokenPasswordName',
    'TokenStatus',
    'TrustPolicyType',
    'WebhookAction',
    'WebhookStatus',
    'ZoneRedundancy',
]


class Action(str, Enum):
    """
    The action of IP ACL rule.
    """
    ALLOW = "Allow"


class ActionsRequired(str, Enum):
    """
    A message indicating if changes on the service provider require any updates on the consumer.
    """
    NONE = "None"
    RECREATE = "Recreate"


class ConnectionStatus(str, Enum):
    """
    The private link service connection status.
    """
    APPROVED = "Approved"
    PENDING = "Pending"
    REJECTED = "Rejected"
    DISCONNECTED = "Disconnected"


class DefaultAction(str, Enum):
    """
    The default action of allow or deny when no other rules match.
    """
    ALLOW = "Allow"
    DENY = "Deny"


class EncryptionStatus(str, Enum):
    """
    Indicates whether or not the encryption is enabled for container registry.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class ExportPolicyStatus(str, Enum):
    """
    The value that indicates whether the policy is enabled or not.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class NetworkRuleBypassOptions(str, Enum):
    """
    Whether to allow trusted Azure services to access a network restricted registry.
    """
    AZURE_SERVICES = "AzureServices"
    NONE = "None"


class PolicyStatus(str, Enum):
    """
    The value that indicates whether the policy is enabled or not.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class PublicNetworkAccess(str, Enum):
    """
    Whether or not public network access is allowed for the container registry.
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"


class ResourceIdentityType(str, Enum):
    """
    The identity type.
    """
    SYSTEM_ASSIGNED = "SystemAssigned"
    USER_ASSIGNED = "UserAssigned"
    SYSTEM_ASSIGNED_USER_ASSIGNED = "SystemAssigned, UserAssigned"
    NONE = "None"


class SkuName(str, Enum):
    """
    The SKU name of the container registry. Required for registry creation.
    """
    CLASSIC = "Classic"
    BASIC = "Basic"
    STANDARD = "Standard"
    PREMIUM = "Premium"


class TokenCertificateName(str, Enum):
    CERTIFICATE1 = "certificate1"
    CERTIFICATE2 = "certificate2"


class TokenPasswordName(str, Enum):
    """
    The password name "password1" or "password2"
    """
    PASSWORD1 = "password1"
    PASSWORD2 = "password2"


class TokenStatus(str, Enum):
    """
    The status of the token example enabled or disabled.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class TrustPolicyType(str, Enum):
    """
    The type of trust policy.
    """
    NOTARY = "Notary"


class WebhookAction(str, Enum):
    PUSH = "push"
    DELETE = "delete"
    QUARANTINE = "quarantine"
    CHART_PUSH = "chart_push"
    CHART_DELETE = "chart_delete"


class WebhookStatus(str, Enum):
    """
    The status of the webhook at the time the operation was called.
    """
    ENABLED = "enabled"
    DISABLED = "disabled"


class ZoneRedundancy(str, Enum):
    """
    Whether or not zone redundancy is enabled for this container registry replication
    """
    ENABLED = "Enabled"
    DISABLED = "Disabled"
