# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from ._enums import *

__all__ = [
    'AcsClusterPropertiesArgs',
    'AppInsightsPropertiesArgs',
    'AutoScaleConfigurationArgs',
    'ContainerRegistryPropertiesArgs',
    'GlobalServiceConfigurationArgs',
    'KubernetesClusterPropertiesArgs',
    'ServiceAuthConfigurationArgs',
    'ServicePrincipalPropertiesArgs',
    'SslConfigurationArgs',
    'StorageAccountPropertiesArgs',
    'SystemServiceArgs',
]

@pulumi.input_type
class AcsClusterPropertiesArgs:
    def __init__(__self__, *,
                 orchestrator_type: pulumi.Input[Union[str, 'OrchestratorType']],
                 agent_count: Optional[pulumi.Input[int]] = None,
                 agent_vm_size: Optional[pulumi.Input[Union[str, 'AgentVMSizeTypes']]] = None,
                 master_count: Optional[pulumi.Input[int]] = None,
                 orchestrator_properties: Optional[pulumi.Input['KubernetesClusterPropertiesArgs']] = None,
                 system_services: Optional[pulumi.Input[Sequence[pulumi.Input['SystemServiceArgs']]]] = None):
        """
        Information about the container service backing the cluster
        :param pulumi.Input[Union[str, 'OrchestratorType']] orchestrator_type: Type of orchestrator. It cannot be changed once the cluster is created.
        :param pulumi.Input[int] agent_count: The number of agent nodes in the Container Service. This can be changed to scale the cluster.
        :param pulumi.Input[Union[str, 'AgentVMSizeTypes']] agent_vm_size: The Azure VM size of the agent VM nodes. This cannot be changed once the cluster is created. This list is non exhaustive; refer to https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes for the possible VM sizes.
        :param pulumi.Input[int] master_count: The number of master nodes in the container service.
        :param pulumi.Input['KubernetesClusterPropertiesArgs'] orchestrator_properties: Orchestrator specific properties
        :param pulumi.Input[Sequence[pulumi.Input['SystemServiceArgs']]] system_services: The system services deployed to the cluster
        """
        pulumi.set(__self__, "orchestrator_type", orchestrator_type)
        if agent_count is None:
            agent_count = 2
        if agent_count is not None:
            pulumi.set(__self__, "agent_count", agent_count)
        if agent_vm_size is None:
            agent_vm_size = 'Standard_D3_v2'
        if agent_vm_size is not None:
            pulumi.set(__self__, "agent_vm_size", agent_vm_size)
        if master_count is None:
            master_count = 1
        if master_count is not None:
            pulumi.set(__self__, "master_count", master_count)
        if orchestrator_properties is not None:
            pulumi.set(__self__, "orchestrator_properties", orchestrator_properties)
        if system_services is not None:
            pulumi.set(__self__, "system_services", system_services)

    @property
    @pulumi.getter(name="orchestratorType")
    def orchestrator_type(self) -> pulumi.Input[Union[str, 'OrchestratorType']]:
        """
        Type of orchestrator. It cannot be changed once the cluster is created.
        """
        return pulumi.get(self, "orchestrator_type")

    @orchestrator_type.setter
    def orchestrator_type(self, value: pulumi.Input[Union[str, 'OrchestratorType']]):
        pulumi.set(self, "orchestrator_type", value)

    @property
    @pulumi.getter(name="agentCount")
    def agent_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of agent nodes in the Container Service. This can be changed to scale the cluster.
        """
        return pulumi.get(self, "agent_count")

    @agent_count.setter
    def agent_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "agent_count", value)

    @property
    @pulumi.getter(name="agentVmSize")
    def agent_vm_size(self) -> Optional[pulumi.Input[Union[str, 'AgentVMSizeTypes']]]:
        """
        The Azure VM size of the agent VM nodes. This cannot be changed once the cluster is created. This list is non exhaustive; refer to https://docs.microsoft.com/en-us/azure/virtual-machines/windows/sizes for the possible VM sizes.
        """
        return pulumi.get(self, "agent_vm_size")

    @agent_vm_size.setter
    def agent_vm_size(self, value: Optional[pulumi.Input[Union[str, 'AgentVMSizeTypes']]]):
        pulumi.set(self, "agent_vm_size", value)

    @property
    @pulumi.getter(name="masterCount")
    def master_count(self) -> Optional[pulumi.Input[int]]:
        """
        The number of master nodes in the container service.
        """
        return pulumi.get(self, "master_count")

    @master_count.setter
    def master_count(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "master_count", value)

    @property
    @pulumi.getter(name="orchestratorProperties")
    def orchestrator_properties(self) -> Optional[pulumi.Input['KubernetesClusterPropertiesArgs']]:
        """
        Orchestrator specific properties
        """
        return pulumi.get(self, "orchestrator_properties")

    @orchestrator_properties.setter
    def orchestrator_properties(self, value: Optional[pulumi.Input['KubernetesClusterPropertiesArgs']]):
        pulumi.set(self, "orchestrator_properties", value)

    @property
    @pulumi.getter(name="systemServices")
    def system_services(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['SystemServiceArgs']]]]:
        """
        The system services deployed to the cluster
        """
        return pulumi.get(self, "system_services")

    @system_services.setter
    def system_services(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['SystemServiceArgs']]]]):
        pulumi.set(self, "system_services", value)


@pulumi.input_type
class AppInsightsPropertiesArgs:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        Properties of App Insights.
        :param pulumi.Input[str] resource_id: ARM resource ID of the App Insights.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource ID of the App Insights.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


@pulumi.input_type
class AutoScaleConfigurationArgs:
    def __init__(__self__, *,
                 max_replicas: Optional[pulumi.Input[int]] = None,
                 min_replicas: Optional[pulumi.Input[int]] = None,
                 refresh_period_in_seconds: Optional[pulumi.Input[int]] = None,
                 status: Optional[pulumi.Input[Union[str, 'Status']]] = None,
                 target_utilization: Optional[pulumi.Input[float]] = None):
        """
        AutoScale configuration properties.
        :param pulumi.Input[int] max_replicas: The maximum number of replicas for each service.
        :param pulumi.Input[int] min_replicas: The minimum number of replicas for each service.
        :param pulumi.Input[int] refresh_period_in_seconds: Refresh period in seconds.
        :param pulumi.Input[Union[str, 'Status']] status: If auto-scale is enabled for all services. Each service can turn it off individually.
        :param pulumi.Input[float] target_utilization: The target utilization.
        """
        if max_replicas is None:
            max_replicas = 100
        if max_replicas is not None:
            pulumi.set(__self__, "max_replicas", max_replicas)
        if min_replicas is None:
            min_replicas = 1
        if min_replicas is not None:
            pulumi.set(__self__, "min_replicas", min_replicas)
        if refresh_period_in_seconds is not None:
            pulumi.set(__self__, "refresh_period_in_seconds", refresh_period_in_seconds)
        if status is None:
            status = 'Disabled'
        if status is not None:
            pulumi.set(__self__, "status", status)
        if target_utilization is not None:
            pulumi.set(__self__, "target_utilization", target_utilization)

    @property
    @pulumi.getter(name="maxReplicas")
    def max_replicas(self) -> Optional[pulumi.Input[int]]:
        """
        The maximum number of replicas for each service.
        """
        return pulumi.get(self, "max_replicas")

    @max_replicas.setter
    def max_replicas(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "max_replicas", value)

    @property
    @pulumi.getter(name="minReplicas")
    def min_replicas(self) -> Optional[pulumi.Input[int]]:
        """
        The minimum number of replicas for each service.
        """
        return pulumi.get(self, "min_replicas")

    @min_replicas.setter
    def min_replicas(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "min_replicas", value)

    @property
    @pulumi.getter(name="refreshPeriodInSeconds")
    def refresh_period_in_seconds(self) -> Optional[pulumi.Input[int]]:
        """
        Refresh period in seconds.
        """
        return pulumi.get(self, "refresh_period_in_seconds")

    @refresh_period_in_seconds.setter
    def refresh_period_in_seconds(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "refresh_period_in_seconds", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'Status']]]:
        """
        If auto-scale is enabled for all services. Each service can turn it off individually.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'Status']]]):
        pulumi.set(self, "status", value)

    @property
    @pulumi.getter(name="targetUtilization")
    def target_utilization(self) -> Optional[pulumi.Input[float]]:
        """
        The target utilization.
        """
        return pulumi.get(self, "target_utilization")

    @target_utilization.setter
    def target_utilization(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "target_utilization", value)


@pulumi.input_type
class ContainerRegistryPropertiesArgs:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        Properties of Azure Container Registry.
        :param pulumi.Input[str] resource_id: ARM resource ID of the Azure Container Registry used to store Docker images for web services in the cluster. If not provided one will be created. This cannot be changed once the cluster is created.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource ID of the Azure Container Registry used to store Docker images for web services in the cluster. If not provided one will be created. This cannot be changed once the cluster is created.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


@pulumi.input_type
class GlobalServiceConfigurationArgs:
    def __init__(__self__, *,
                 auto_scale: Optional[pulumi.Input['AutoScaleConfigurationArgs']] = None,
                 etag: Optional[pulumi.Input[str]] = None,
                 service_auth: Optional[pulumi.Input['ServiceAuthConfigurationArgs']] = None,
                 ssl: Optional[pulumi.Input['SslConfigurationArgs']] = None):
        """
        Global configuration for services in the cluster.
        :param pulumi.Input['AutoScaleConfigurationArgs'] auto_scale: The auto-scale configuration
        :param pulumi.Input[str] etag: The configuration ETag for updates.
        :param pulumi.Input['ServiceAuthConfigurationArgs'] service_auth: Optional global authorization keys for all user services deployed in cluster. These are used if the service does not have auth keys.
        :param pulumi.Input['SslConfigurationArgs'] ssl: The SSL configuration properties
        """
        if auto_scale is not None:
            pulumi.set(__self__, "auto_scale", auto_scale)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if service_auth is not None:
            pulumi.set(__self__, "service_auth", service_auth)
        if ssl is not None:
            pulumi.set(__self__, "ssl", ssl)

    @property
    @pulumi.getter(name="autoScale")
    def auto_scale(self) -> Optional[pulumi.Input['AutoScaleConfigurationArgs']]:
        """
        The auto-scale configuration
        """
        return pulumi.get(self, "auto_scale")

    @auto_scale.setter
    def auto_scale(self, value: Optional[pulumi.Input['AutoScaleConfigurationArgs']]):
        pulumi.set(self, "auto_scale", value)

    @property
    @pulumi.getter
    def etag(self) -> Optional[pulumi.Input[str]]:
        """
        The configuration ETag for updates.
        """
        return pulumi.get(self, "etag")

    @etag.setter
    def etag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "etag", value)

    @property
    @pulumi.getter(name="serviceAuth")
    def service_auth(self) -> Optional[pulumi.Input['ServiceAuthConfigurationArgs']]:
        """
        Optional global authorization keys for all user services deployed in cluster. These are used if the service does not have auth keys.
        """
        return pulumi.get(self, "service_auth")

    @service_auth.setter
    def service_auth(self, value: Optional[pulumi.Input['ServiceAuthConfigurationArgs']]):
        pulumi.set(self, "service_auth", value)

    @property
    @pulumi.getter
    def ssl(self) -> Optional[pulumi.Input['SslConfigurationArgs']]:
        """
        The SSL configuration properties
        """
        return pulumi.get(self, "ssl")

    @ssl.setter
    def ssl(self, value: Optional[pulumi.Input['SslConfigurationArgs']]):
        pulumi.set(self, "ssl", value)


@pulumi.input_type
class KubernetesClusterPropertiesArgs:
    def __init__(__self__, *,
                 service_principal: Optional[pulumi.Input['ServicePrincipalPropertiesArgs']] = None):
        """
        Kubernetes cluster specific properties
        :param pulumi.Input['ServicePrincipalPropertiesArgs'] service_principal: The Azure Service Principal used by Kubernetes
        """
        if service_principal is not None:
            pulumi.set(__self__, "service_principal", service_principal)

    @property
    @pulumi.getter(name="servicePrincipal")
    def service_principal(self) -> Optional[pulumi.Input['ServicePrincipalPropertiesArgs']]:
        """
        The Azure Service Principal used by Kubernetes
        """
        return pulumi.get(self, "service_principal")

    @service_principal.setter
    def service_principal(self, value: Optional[pulumi.Input['ServicePrincipalPropertiesArgs']]):
        pulumi.set(self, "service_principal", value)


@pulumi.input_type
class ServiceAuthConfigurationArgs:
    def __init__(__self__, *,
                 primary_auth_key_hash: pulumi.Input[str],
                 secondary_auth_key_hash: pulumi.Input[str]):
        """
        Global service auth configuration properties. These are the data-plane authorization keys and are used if a service doesn't define it's own.
        :param pulumi.Input[str] primary_auth_key_hash: The primary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API.
        :param pulumi.Input[str] secondary_auth_key_hash: The secondary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API.
        """
        pulumi.set(__self__, "primary_auth_key_hash", primary_auth_key_hash)
        pulumi.set(__self__, "secondary_auth_key_hash", secondary_auth_key_hash)

    @property
    @pulumi.getter(name="primaryAuthKeyHash")
    def primary_auth_key_hash(self) -> pulumi.Input[str]:
        """
        The primary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API.
        """
        return pulumi.get(self, "primary_auth_key_hash")

    @primary_auth_key_hash.setter
    def primary_auth_key_hash(self, value: pulumi.Input[str]):
        pulumi.set(self, "primary_auth_key_hash", value)

    @property
    @pulumi.getter(name="secondaryAuthKeyHash")
    def secondary_auth_key_hash(self) -> pulumi.Input[str]:
        """
        The secondary auth key hash. This is not returned in response of GET/PUT on the resource.. To see this please call listKeys API.
        """
        return pulumi.get(self, "secondary_auth_key_hash")

    @secondary_auth_key_hash.setter
    def secondary_auth_key_hash(self, value: pulumi.Input[str]):
        pulumi.set(self, "secondary_auth_key_hash", value)


@pulumi.input_type
class ServicePrincipalPropertiesArgs:
    def __init__(__self__, *,
                 client_id: pulumi.Input[str],
                 secret: pulumi.Input[str]):
        """
        The Azure service principal used by Kubernetes for configuring load balancers
        :param pulumi.Input[str] client_id: The service principal client ID
        :param pulumi.Input[str] secret: The service principal secret. This is not returned in response of GET/PUT on the resource. To see this please call listKeys.
        """
        pulumi.set(__self__, "client_id", client_id)
        pulumi.set(__self__, "secret", secret)

    @property
    @pulumi.getter(name="clientId")
    def client_id(self) -> pulumi.Input[str]:
        """
        The service principal client ID
        """
        return pulumi.get(self, "client_id")

    @client_id.setter
    def client_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "client_id", value)

    @property
    @pulumi.getter
    def secret(self) -> pulumi.Input[str]:
        """
        The service principal secret. This is not returned in response of GET/PUT on the resource. To see this please call listKeys.
        """
        return pulumi.get(self, "secret")

    @secret.setter
    def secret(self, value: pulumi.Input[str]):
        pulumi.set(self, "secret", value)


@pulumi.input_type
class SslConfigurationArgs:
    def __init__(__self__, *,
                 cert: Optional[pulumi.Input[str]] = None,
                 cname: Optional[pulumi.Input[str]] = None,
                 key: Optional[pulumi.Input[str]] = None,
                 status: Optional[pulumi.Input[Union[str, 'Status']]] = None):
        """
        SSL configuration. If configured data-plane calls to user services will be exposed over SSL only.
        :param pulumi.Input[str] cert: The SSL cert data in PEM format.
        :param pulumi.Input[str] cname: The CName of the certificate.
        :param pulumi.Input[str] key: The SSL key data in PEM format. This is not returned in response of GET/PUT on the resource. To see this please call listKeys API.
        :param pulumi.Input[Union[str, 'Status']] status: SSL status. Allowed values are Enabled and Disabled.
        """
        if cert is not None:
            pulumi.set(__self__, "cert", cert)
        if cname is not None:
            pulumi.set(__self__, "cname", cname)
        if key is not None:
            pulumi.set(__self__, "key", key)
        if status is None:
            status = 'Enabled'
        if status is not None:
            pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter
    def cert(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL cert data in PEM format.
        """
        return pulumi.get(self, "cert")

    @cert.setter
    def cert(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cert", value)

    @property
    @pulumi.getter
    def cname(self) -> Optional[pulumi.Input[str]]:
        """
        The CName of the certificate.
        """
        return pulumi.get(self, "cname")

    @cname.setter
    def cname(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cname", value)

    @property
    @pulumi.getter
    def key(self) -> Optional[pulumi.Input[str]]:
        """
        The SSL key data in PEM format. This is not returned in response of GET/PUT on the resource. To see this please call listKeys API.
        """
        return pulumi.get(self, "key")

    @key.setter
    def key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key", value)

    @property
    @pulumi.getter
    def status(self) -> Optional[pulumi.Input[Union[str, 'Status']]]:
        """
        SSL status. Allowed values are Enabled and Disabled.
        """
        return pulumi.get(self, "status")

    @status.setter
    def status(self, value: Optional[pulumi.Input[Union[str, 'Status']]]):
        pulumi.set(self, "status", value)


@pulumi.input_type
class StorageAccountPropertiesArgs:
    def __init__(__self__, *,
                 resource_id: Optional[pulumi.Input[str]] = None):
        """
        Properties of Storage Account.
        :param pulumi.Input[str] resource_id: ARM resource ID of the Azure Storage Account to store CLI specific files. If not provided one will be created. This cannot be changed once the cluster is created.
        """
        if resource_id is not None:
            pulumi.set(__self__, "resource_id", resource_id)

    @property
    @pulumi.getter(name="resourceId")
    def resource_id(self) -> Optional[pulumi.Input[str]]:
        """
        ARM resource ID of the Azure Storage Account to store CLI specific files. If not provided one will be created. This cannot be changed once the cluster is created.
        """
        return pulumi.get(self, "resource_id")

    @resource_id.setter
    def resource_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_id", value)


@pulumi.input_type
class SystemServiceArgs:
    def __init__(__self__, *,
                 system_service_type: pulumi.Input[Union[str, 'SystemServiceType']]):
        """
        Information about a system service deployed in the cluster
        :param pulumi.Input[Union[str, 'SystemServiceType']] system_service_type: The system service type
        """
        pulumi.set(__self__, "system_service_type", system_service_type)

    @property
    @pulumi.getter(name="systemServiceType")
    def system_service_type(self) -> pulumi.Input[Union[str, 'SystemServiceType']]:
        """
        The system service type
        """
        return pulumi.get(self, "system_service_type")

    @system_service_type.setter
    def system_service_type(self, value: pulumi.Input[Union[str, 'SystemServiceType']]):
        pulumi.set(self, "system_service_type", value)


