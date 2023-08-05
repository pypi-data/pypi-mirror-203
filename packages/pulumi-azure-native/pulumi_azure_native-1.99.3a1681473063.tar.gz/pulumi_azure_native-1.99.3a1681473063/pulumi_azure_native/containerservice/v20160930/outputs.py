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
from ._enums import *

__all__ = [
    'ContainerServiceAgentPoolProfileResponse',
    'ContainerServiceCustomProfileResponse',
    'ContainerServiceDiagnosticsProfileResponse',
    'ContainerServiceLinuxProfileResponse',
    'ContainerServiceMasterProfileResponse',
    'ContainerServiceOrchestratorProfileResponse',
    'ContainerServiceServicePrincipalProfileResponse',
    'ContainerServiceSshConfigurationResponse',
    'ContainerServiceSshPublicKeyResponse',
    'ContainerServiceVMDiagnosticsResponse',
    'ContainerServiceWindowsProfileResponse',
]

@pulumi.output_type
class ContainerServiceAgentPoolProfileResponse(dict):
    """
    Profile for the container service agent pool.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dnsPrefix":
            suggest = "dns_prefix"
        elif key == "vmSize":
            suggest = "vm_size"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceAgentPoolProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceAgentPoolProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceAgentPoolProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 count: int,
                 dns_prefix: str,
                 fqdn: str,
                 name: str,
                 vm_size: str):
        """
        Profile for the container service agent pool.
        :param int count: Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1. 
        :param str dns_prefix: DNS prefix to be used to create the FQDN for the agent pool.
        :param str fqdn: FQDN for the agent pool.
        :param str name: Unique name of the agent pool profile in the context of the subscription and resource group.
        :param str vm_size: Size of agent VMs.
        """
        if count is None:
            count = 1
        pulumi.set(__self__, "count", count)
        pulumi.set(__self__, "dns_prefix", dns_prefix)
        pulumi.set(__self__, "fqdn", fqdn)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter
    def count(self) -> int:
        """
        Number of agents (VMs) to host docker containers. Allowed values must be in the range of 1 to 100 (inclusive). The default value is 1. 
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> str:
        """
        DNS prefix to be used to create the FQDN for the agent pool.
        """
        return pulumi.get(self, "dns_prefix")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        FQDN for the agent pool.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Unique name of the agent pool profile in the context of the subscription and resource group.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> str:
        """
        Size of agent VMs.
        """
        return pulumi.get(self, "vm_size")


@pulumi.output_type
class ContainerServiceCustomProfileResponse(dict):
    """
    Properties to configure a custom container service cluster.
    """
    def __init__(__self__, *,
                 orchestrator: str):
        """
        Properties to configure a custom container service cluster.
        :param str orchestrator: The name of the custom orchestrator to use.
        """
        pulumi.set(__self__, "orchestrator", orchestrator)

    @property
    @pulumi.getter
    def orchestrator(self) -> str:
        """
        The name of the custom orchestrator to use.
        """
        return pulumi.get(self, "orchestrator")


@pulumi.output_type
class ContainerServiceDiagnosticsProfileResponse(dict):
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "vmDiagnostics":
            suggest = "vm_diagnostics"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceDiagnosticsProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceDiagnosticsProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceDiagnosticsProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 vm_diagnostics: 'outputs.ContainerServiceVMDiagnosticsResponse'):
        """
        :param 'ContainerServiceVMDiagnosticsResponse' vm_diagnostics: Profile for the container service VM diagnostic agent.
        """
        pulumi.set(__self__, "vm_diagnostics", vm_diagnostics)

    @property
    @pulumi.getter(name="vmDiagnostics")
    def vm_diagnostics(self) -> 'outputs.ContainerServiceVMDiagnosticsResponse':
        """
        Profile for the container service VM diagnostic agent.
        """
        return pulumi.get(self, "vm_diagnostics")


@pulumi.output_type
class ContainerServiceLinuxProfileResponse(dict):
    """
    Profile for Linux VMs in the container service cluster.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "adminUsername":
            suggest = "admin_username"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceLinuxProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceLinuxProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceLinuxProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 admin_username: str,
                 ssh: 'outputs.ContainerServiceSshConfigurationResponse'):
        """
        Profile for Linux VMs in the container service cluster.
        :param str admin_username: The administrator username to use for Linux VMs.
        :param 'ContainerServiceSshConfigurationResponse' ssh: The ssh key configuration for Linux VMs.
        """
        pulumi.set(__self__, "admin_username", admin_username)
        pulumi.set(__self__, "ssh", ssh)

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> str:
        """
        The administrator username to use for Linux VMs.
        """
        return pulumi.get(self, "admin_username")

    @property
    @pulumi.getter
    def ssh(self) -> 'outputs.ContainerServiceSshConfigurationResponse':
        """
        The ssh key configuration for Linux VMs.
        """
        return pulumi.get(self, "ssh")


@pulumi.output_type
class ContainerServiceMasterProfileResponse(dict):
    """
    Profile for the container service master.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "dnsPrefix":
            suggest = "dns_prefix"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceMasterProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceMasterProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceMasterProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 dns_prefix: str,
                 fqdn: str,
                 count: Optional[int] = None):
        """
        Profile for the container service master.
        :param str dns_prefix: DNS prefix to be used to create the FQDN for master.
        :param str fqdn: FQDN for the master.
        :param int count: Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The default value is 1.
        """
        pulumi.set(__self__, "dns_prefix", dns_prefix)
        pulumi.set(__self__, "fqdn", fqdn)
        if count is None:
            count = 1
        if count is not None:
            pulumi.set(__self__, "count", count)

    @property
    @pulumi.getter(name="dnsPrefix")
    def dns_prefix(self) -> str:
        """
        DNS prefix to be used to create the FQDN for master.
        """
        return pulumi.get(self, "dns_prefix")

    @property
    @pulumi.getter
    def fqdn(self) -> str:
        """
        FQDN for the master.
        """
        return pulumi.get(self, "fqdn")

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        Number of masters (VMs) in the container service cluster. Allowed values are 1, 3, and 5. The default value is 1.
        """
        return pulumi.get(self, "count")


@pulumi.output_type
class ContainerServiceOrchestratorProfileResponse(dict):
    """
    Profile for the container service orchestrator.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "orchestratorType":
            suggest = "orchestrator_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceOrchestratorProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceOrchestratorProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceOrchestratorProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 orchestrator_type: str):
        """
        Profile for the container service orchestrator.
        :param str orchestrator_type: The orchestrator to use to manage container service cluster resources. Valid values are Swarm, DCOS, and Custom.
        """
        pulumi.set(__self__, "orchestrator_type", orchestrator_type)

    @property
    @pulumi.getter(name="orchestratorType")
    def orchestrator_type(self) -> str:
        """
        The orchestrator to use to manage container service cluster resources. Valid values are Swarm, DCOS, and Custom.
        """
        return pulumi.get(self, "orchestrator_type")


@pulumi.output_type
class ContainerServiceServicePrincipalProfileResponse(dict):
    """
    Information about a service principal identity for the cluster to use for manipulating Azure APIs.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "clientId":
            suggest = "client_id"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceServicePrincipalProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceServicePrincipalProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceServicePrincipalProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 client_id: str,
                 secret: str):
        """
        Information about a service principal identity for the cluster to use for manipulating Azure APIs.
        :param str client_id: The ID for the service principal.
        :param str secret: The secret password associated with the service principal.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> str:
        """
        The ID for the service principal.
        """
        return pulumi.get(self, "client_id")

    @property
    @pulumi.getter
    def secret(self) -> str:
        """
        The secret password associated with the service principal.
        """
        return pulumi.get(self, "secret")


@pulumi.output_type
class ContainerServiceSshConfigurationResponse(dict):
    """
    SSH configuration for Linux-based VMs running on Azure.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "publicKeys":
            suggest = "public_keys"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceSshConfigurationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceSshConfigurationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceSshConfigurationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 public_keys: Sequence['outputs.ContainerServiceSshPublicKeyResponse']):
        """
        SSH configuration for Linux-based VMs running on Azure.
        :param Sequence['ContainerServiceSshPublicKeyResponse'] public_keys: the list of SSH public keys used to authenticate with Linux-based VMs.
        """
        pulumi.set(__self__, "public_keys", public_keys)

    @property
    @pulumi.getter(name="publicKeys")
    def public_keys(self) -> Sequence['outputs.ContainerServiceSshPublicKeyResponse']:
        """
        the list of SSH public keys used to authenticate with Linux-based VMs.
        """
        return pulumi.get(self, "public_keys")


@pulumi.output_type
class ContainerServiceSshPublicKeyResponse(dict):
    """
    Contains information about SSH certificate public key data.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "keyData":
            suggest = "key_data"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceSshPublicKeyResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceSshPublicKeyResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceSshPublicKeyResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 key_data: str):
        """
        Contains information about SSH certificate public key data.
        :param str key_data: Certificate public key used to authenticate with VMs through SSH. The certificate must be in PEM format with or without headers.
        """
        pulumi.set(__self__, "key_data", key_data)

    @property
    @pulumi.getter(name="keyData")
    def key_data(self) -> str:
        """
        Certificate public key used to authenticate with VMs through SSH. The certificate must be in PEM format with or without headers.
        """
        return pulumi.get(self, "key_data")


@pulumi.output_type
class ContainerServiceVMDiagnosticsResponse(dict):
    """
    Profile for diagnostics on the container service VMs.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "storageUri":
            suggest = "storage_uri"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceVMDiagnosticsResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceVMDiagnosticsResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceVMDiagnosticsResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 enabled: bool,
                 storage_uri: str):
        """
        Profile for diagnostics on the container service VMs.
        :param bool enabled: Whether the VM diagnostic agent is provisioned on the VM.
        :param str storage_uri: The URI of the storage account where diagnostics are stored.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "storage_uri", storage_uri)

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        Whether the VM diagnostic agent is provisioned on the VM.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter(name="storageUri")
    def storage_uri(self) -> str:
        """
        The URI of the storage account where diagnostics are stored.
        """
        return pulumi.get(self, "storage_uri")


@pulumi.output_type
class ContainerServiceWindowsProfileResponse(dict):
    """
    Profile for Windows VMs in the container service cluster.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "adminPassword":
            suggest = "admin_password"
        elif key == "adminUsername":
            suggest = "admin_username"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ContainerServiceWindowsProfileResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ContainerServiceWindowsProfileResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ContainerServiceWindowsProfileResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 admin_password: str,
                 admin_username: str):
        """
        Profile for Windows VMs in the container service cluster.
        :param str admin_password: The administrator password to use for Windows VMs.
        :param str admin_username: The administrator username to use for Windows VMs.
        """
        pulumi.set(__self__, "admin_password", admin_password)
        pulumi.set(__self__, "admin_username", admin_username)

    @property
    @pulumi.getter(name="adminPassword")
    def admin_password(self) -> str:
        """
        The administrator password to use for Windows VMs.
        """
        return pulumi.get(self, "admin_password")

    @property
    @pulumi.getter(name="adminUsername")
    def admin_username(self) -> str:
        """
        The administrator username to use for Windows VMs.
        """
        return pulumi.get(self, "admin_username")


