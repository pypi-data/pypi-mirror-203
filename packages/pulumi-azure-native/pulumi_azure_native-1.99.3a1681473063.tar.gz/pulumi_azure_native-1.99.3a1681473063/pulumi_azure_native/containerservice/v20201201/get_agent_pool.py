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
    'GetAgentPoolResult',
    'AwaitableGetAgentPoolResult',
    'get_agent_pool',
    'get_agent_pool_output',
]

@pulumi.output_type
class GetAgentPoolResult:
    """
    Agent Pool.
    """
    def __init__(__self__, availability_zones=None, count=None, enable_auto_scaling=None, enable_encryption_at_host=None, enable_node_public_ip=None, id=None, kubelet_config=None, kubelet_disk_type=None, linux_os_config=None, max_count=None, max_pods=None, min_count=None, mode=None, name=None, node_image_version=None, node_labels=None, node_taints=None, orchestrator_version=None, os_disk_size_gb=None, os_disk_type=None, os_type=None, pod_subnet_id=None, power_state=None, provisioning_state=None, proximity_placement_group_id=None, scale_set_eviction_policy=None, scale_set_priority=None, spot_max_price=None, tags=None, type=None, upgrade_settings=None, vm_size=None, vnet_subnet_id=None):
        if availability_zones and not isinstance(availability_zones, list):
            raise TypeError("Expected argument 'availability_zones' to be a list")
        pulumi.set(__self__, "availability_zones", availability_zones)
        if count and not isinstance(count, int):
            raise TypeError("Expected argument 'count' to be a int")
        pulumi.set(__self__, "count", count)
        if enable_auto_scaling and not isinstance(enable_auto_scaling, bool):
            raise TypeError("Expected argument 'enable_auto_scaling' to be a bool")
        pulumi.set(__self__, "enable_auto_scaling", enable_auto_scaling)
        if enable_encryption_at_host and not isinstance(enable_encryption_at_host, bool):
            raise TypeError("Expected argument 'enable_encryption_at_host' to be a bool")
        pulumi.set(__self__, "enable_encryption_at_host", enable_encryption_at_host)
        if enable_node_public_ip and not isinstance(enable_node_public_ip, bool):
            raise TypeError("Expected argument 'enable_node_public_ip' to be a bool")
        pulumi.set(__self__, "enable_node_public_ip", enable_node_public_ip)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if kubelet_config and not isinstance(kubelet_config, dict):
            raise TypeError("Expected argument 'kubelet_config' to be a dict")
        pulumi.set(__self__, "kubelet_config", kubelet_config)
        if kubelet_disk_type and not isinstance(kubelet_disk_type, str):
            raise TypeError("Expected argument 'kubelet_disk_type' to be a str")
        pulumi.set(__self__, "kubelet_disk_type", kubelet_disk_type)
        if linux_os_config and not isinstance(linux_os_config, dict):
            raise TypeError("Expected argument 'linux_os_config' to be a dict")
        pulumi.set(__self__, "linux_os_config", linux_os_config)
        if max_count and not isinstance(max_count, int):
            raise TypeError("Expected argument 'max_count' to be a int")
        pulumi.set(__self__, "max_count", max_count)
        if max_pods and not isinstance(max_pods, int):
            raise TypeError("Expected argument 'max_pods' to be a int")
        pulumi.set(__self__, "max_pods", max_pods)
        if min_count and not isinstance(min_count, int):
            raise TypeError("Expected argument 'min_count' to be a int")
        pulumi.set(__self__, "min_count", min_count)
        if mode and not isinstance(mode, str):
            raise TypeError("Expected argument 'mode' to be a str")
        pulumi.set(__self__, "mode", mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if node_image_version and not isinstance(node_image_version, str):
            raise TypeError("Expected argument 'node_image_version' to be a str")
        pulumi.set(__self__, "node_image_version", node_image_version)
        if node_labels and not isinstance(node_labels, dict):
            raise TypeError("Expected argument 'node_labels' to be a dict")
        pulumi.set(__self__, "node_labels", node_labels)
        if node_taints and not isinstance(node_taints, list):
            raise TypeError("Expected argument 'node_taints' to be a list")
        pulumi.set(__self__, "node_taints", node_taints)
        if orchestrator_version and not isinstance(orchestrator_version, str):
            raise TypeError("Expected argument 'orchestrator_version' to be a str")
        pulumi.set(__self__, "orchestrator_version", orchestrator_version)
        if os_disk_size_gb and not isinstance(os_disk_size_gb, int):
            raise TypeError("Expected argument 'os_disk_size_gb' to be a int")
        pulumi.set(__self__, "os_disk_size_gb", os_disk_size_gb)
        if os_disk_type and not isinstance(os_disk_type, str):
            raise TypeError("Expected argument 'os_disk_type' to be a str")
        pulumi.set(__self__, "os_disk_type", os_disk_type)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if pod_subnet_id and not isinstance(pod_subnet_id, str):
            raise TypeError("Expected argument 'pod_subnet_id' to be a str")
        pulumi.set(__self__, "pod_subnet_id", pod_subnet_id)
        if power_state and not isinstance(power_state, dict):
            raise TypeError("Expected argument 'power_state' to be a dict")
        pulumi.set(__self__, "power_state", power_state)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if proximity_placement_group_id and not isinstance(proximity_placement_group_id, str):
            raise TypeError("Expected argument 'proximity_placement_group_id' to be a str")
        pulumi.set(__self__, "proximity_placement_group_id", proximity_placement_group_id)
        if scale_set_eviction_policy and not isinstance(scale_set_eviction_policy, str):
            raise TypeError("Expected argument 'scale_set_eviction_policy' to be a str")
        pulumi.set(__self__, "scale_set_eviction_policy", scale_set_eviction_policy)
        if scale_set_priority and not isinstance(scale_set_priority, str):
            raise TypeError("Expected argument 'scale_set_priority' to be a str")
        pulumi.set(__self__, "scale_set_priority", scale_set_priority)
        if spot_max_price and not isinstance(spot_max_price, float):
            raise TypeError("Expected argument 'spot_max_price' to be a float")
        pulumi.set(__self__, "spot_max_price", spot_max_price)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if upgrade_settings and not isinstance(upgrade_settings, dict):
            raise TypeError("Expected argument 'upgrade_settings' to be a dict")
        pulumi.set(__self__, "upgrade_settings", upgrade_settings)
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        pulumi.set(__self__, "vm_size", vm_size)
        if vnet_subnet_id and not isinstance(vnet_subnet_id, str):
            raise TypeError("Expected argument 'vnet_subnet_id' to be a str")
        pulumi.set(__self__, "vnet_subnet_id", vnet_subnet_id)

    @property
    @pulumi.getter(name="availabilityZones")
    def availability_zones(self) -> Optional[Sequence[str]]:
        """
        Availability zones for nodes. Must use VirtualMachineScaleSets AgentPoolType.
        """
        return pulumi.get(self, "availability_zones")

    @property
    @pulumi.getter
    def count(self) -> Optional[int]:
        """
        Number of agents (VMs) to host docker containers. Allowed values must be in the range of 0 to 100 (inclusive) for user pools and in the range of 1 to 100 (inclusive) for system pools. The default value is 1.
        """
        return pulumi.get(self, "count")

    @property
    @pulumi.getter(name="enableAutoScaling")
    def enable_auto_scaling(self) -> Optional[bool]:
        """
        Whether to enable auto-scaler
        """
        return pulumi.get(self, "enable_auto_scaling")

    @property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> Optional[bool]:
        """
        Whether to enable EncryptionAtHost
        """
        return pulumi.get(self, "enable_encryption_at_host")

    @property
    @pulumi.getter(name="enableNodePublicIP")
    def enable_node_public_ip(self) -> Optional[bool]:
        """
        Enable public IP for nodes
        """
        return pulumi.get(self, "enable_node_public_ip")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="kubeletConfig")
    def kubelet_config(self) -> Optional['outputs.KubeletConfigResponse']:
        """
        KubeletConfig specifies the configuration of kubelet on agent nodes.
        """
        return pulumi.get(self, "kubelet_config")

    @property
    @pulumi.getter(name="kubeletDiskType")
    def kubelet_disk_type(self) -> Optional[str]:
        """
        KubeletDiskType determines the placement of emptyDir volumes, container runtime data root, and Kubelet ephemeral storage. Currently allows one value, OS, resulting in Kubelet using the OS disk for data.
        """
        return pulumi.get(self, "kubelet_disk_type")

    @property
    @pulumi.getter(name="linuxOSConfig")
    def linux_os_config(self) -> Optional['outputs.LinuxOSConfigResponse']:
        """
        LinuxOSConfig specifies the OS configuration of linux agent nodes.
        """
        return pulumi.get(self, "linux_os_config")

    @property
    @pulumi.getter(name="maxCount")
    def max_count(self) -> Optional[int]:
        """
        Maximum number of nodes for auto-scaling
        """
        return pulumi.get(self, "max_count")

    @property
    @pulumi.getter(name="maxPods")
    def max_pods(self) -> Optional[int]:
        """
        Maximum number of pods that can run on a node.
        """
        return pulumi.get(self, "max_pods")

    @property
    @pulumi.getter(name="minCount")
    def min_count(self) -> Optional[int]:
        """
        Minimum number of nodes for auto-scaling
        """
        return pulumi.get(self, "min_count")

    @property
    @pulumi.getter
    def mode(self) -> Optional[str]:
        """
        AgentPoolMode represents mode of an agent pool
        """
        return pulumi.get(self, "mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource that is unique within a resource group. This name can be used to access the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="nodeImageVersion")
    def node_image_version(self) -> str:
        """
        Version of node image
        """
        return pulumi.get(self, "node_image_version")

    @property
    @pulumi.getter(name="nodeLabels")
    def node_labels(self) -> Optional[Mapping[str, str]]:
        """
        Agent pool node labels to be persisted across all nodes in agent pool.
        """
        return pulumi.get(self, "node_labels")

    @property
    @pulumi.getter(name="nodeTaints")
    def node_taints(self) -> Optional[Sequence[str]]:
        """
        Taints added to new nodes during node pool create and scale. For example, key=value:NoSchedule.
        """
        return pulumi.get(self, "node_taints")

    @property
    @pulumi.getter(name="orchestratorVersion")
    def orchestrator_version(self) -> Optional[str]:
        """
        Version of orchestrator specified when creating the managed cluster.
        """
        return pulumi.get(self, "orchestrator_version")

    @property
    @pulumi.getter(name="osDiskSizeGB")
    def os_disk_size_gb(self) -> Optional[int]:
        """
        OS Disk Size in GB to be used to specify the disk size for every machine in this master/agent pool. If you specify 0, it will apply the default osDisk size according to the vmSize specified.
        """
        return pulumi.get(self, "os_disk_size_gb")

    @property
    @pulumi.getter(name="osDiskType")
    def os_disk_type(self) -> Optional[str]:
        """
        OS disk type to be used for machines in a given agent pool. Allowed values are 'Ephemeral' and 'Managed'. If unspecified, defaults to 'Ephemeral' when the VM supports ephemeral OS and has a cache disk larger than the requested OSDiskSizeGB. Otherwise, defaults to 'Managed'. May not be changed after creation.
        """
        return pulumi.get(self, "os_disk_type")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> Optional[str]:
        """
        OsType to be used to specify os type. Choose from Linux and Windows. Default to Linux.
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="podSubnetID")
    def pod_subnet_id(self) -> Optional[str]:
        """
        Pod SubnetID specifies the VNet's subnet identifier for pods.
        """
        return pulumi.get(self, "pod_subnet_id")

    @property
    @pulumi.getter(name="powerState")
    def power_state(self) -> 'outputs.PowerStateResponse':
        """
        Describes whether the Agent Pool is Running or Stopped
        """
        return pulumi.get(self, "power_state")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The current deployment or provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="proximityPlacementGroupID")
    def proximity_placement_group_id(self) -> Optional[str]:
        """
        The ID for Proximity Placement Group.
        """
        return pulumi.get(self, "proximity_placement_group_id")

    @property
    @pulumi.getter(name="scaleSetEvictionPolicy")
    def scale_set_eviction_policy(self) -> Optional[str]:
        """
        ScaleSetEvictionPolicy to be used to specify eviction policy for Spot virtual machine scale set. Default to Delete.
        """
        return pulumi.get(self, "scale_set_eviction_policy")

    @property
    @pulumi.getter(name="scaleSetPriority")
    def scale_set_priority(self) -> Optional[str]:
        """
        ScaleSetPriority to be used to specify virtual machine scale set priority. Default to regular.
        """
        return pulumi.get(self, "scale_set_priority")

    @property
    @pulumi.getter(name="spotMaxPrice")
    def spot_max_price(self) -> Optional[float]:
        """
        SpotMaxPrice to be used to specify the maximum price you are willing to pay in US Dollars. Possible values are any decimal value greater than zero or -1 which indicates default price to be up-to on-demand.
        """
        return pulumi.get(self, "spot_max_price")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Agent pool tags to be persisted on the agent pool virtual machine scale set.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        AgentPoolType represents types of an agent pool
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="upgradeSettings")
    def upgrade_settings(self) -> Optional['outputs.AgentPoolUpgradeSettingsResponse']:
        """
        Settings for upgrading the agentpool
        """
        return pulumi.get(self, "upgrade_settings")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        Size of agent VMs.
        """
        return pulumi.get(self, "vm_size")

    @property
    @pulumi.getter(name="vnetSubnetID")
    def vnet_subnet_id(self) -> Optional[str]:
        """
        VNet SubnetID specifies the VNet's subnet identifier for nodes and maybe pods
        """
        return pulumi.get(self, "vnet_subnet_id")


class AwaitableGetAgentPoolResult(GetAgentPoolResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAgentPoolResult(
            availability_zones=self.availability_zones,
            count=self.count,
            enable_auto_scaling=self.enable_auto_scaling,
            enable_encryption_at_host=self.enable_encryption_at_host,
            enable_node_public_ip=self.enable_node_public_ip,
            id=self.id,
            kubelet_config=self.kubelet_config,
            kubelet_disk_type=self.kubelet_disk_type,
            linux_os_config=self.linux_os_config,
            max_count=self.max_count,
            max_pods=self.max_pods,
            min_count=self.min_count,
            mode=self.mode,
            name=self.name,
            node_image_version=self.node_image_version,
            node_labels=self.node_labels,
            node_taints=self.node_taints,
            orchestrator_version=self.orchestrator_version,
            os_disk_size_gb=self.os_disk_size_gb,
            os_disk_type=self.os_disk_type,
            os_type=self.os_type,
            pod_subnet_id=self.pod_subnet_id,
            power_state=self.power_state,
            provisioning_state=self.provisioning_state,
            proximity_placement_group_id=self.proximity_placement_group_id,
            scale_set_eviction_policy=self.scale_set_eviction_policy,
            scale_set_priority=self.scale_set_priority,
            spot_max_price=self.spot_max_price,
            tags=self.tags,
            type=self.type,
            upgrade_settings=self.upgrade_settings,
            vm_size=self.vm_size,
            vnet_subnet_id=self.vnet_subnet_id)


def get_agent_pool(agent_pool_name: Optional[str] = None,
                   resource_group_name: Optional[str] = None,
                   resource_name: Optional[str] = None,
                   opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAgentPoolResult:
    """
    Gets the details of the agent pool by managed cluster and resource group.


    :param str agent_pool_name: The name of the agent pool.
    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The name of the managed cluster resource.
    """
    __args__ = dict()
    __args__['agentPoolName'] = agent_pool_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerservice/v20201201:getAgentPool', __args__, opts=opts, typ=GetAgentPoolResult).value

    return AwaitableGetAgentPoolResult(
        availability_zones=__ret__.availability_zones,
        count=__ret__.count,
        enable_auto_scaling=__ret__.enable_auto_scaling,
        enable_encryption_at_host=__ret__.enable_encryption_at_host,
        enable_node_public_ip=__ret__.enable_node_public_ip,
        id=__ret__.id,
        kubelet_config=__ret__.kubelet_config,
        kubelet_disk_type=__ret__.kubelet_disk_type,
        linux_os_config=__ret__.linux_os_config,
        max_count=__ret__.max_count,
        max_pods=__ret__.max_pods,
        min_count=__ret__.min_count,
        mode=__ret__.mode,
        name=__ret__.name,
        node_image_version=__ret__.node_image_version,
        node_labels=__ret__.node_labels,
        node_taints=__ret__.node_taints,
        orchestrator_version=__ret__.orchestrator_version,
        os_disk_size_gb=__ret__.os_disk_size_gb,
        os_disk_type=__ret__.os_disk_type,
        os_type=__ret__.os_type,
        pod_subnet_id=__ret__.pod_subnet_id,
        power_state=__ret__.power_state,
        provisioning_state=__ret__.provisioning_state,
        proximity_placement_group_id=__ret__.proximity_placement_group_id,
        scale_set_eviction_policy=__ret__.scale_set_eviction_policy,
        scale_set_priority=__ret__.scale_set_priority,
        spot_max_price=__ret__.spot_max_price,
        tags=__ret__.tags,
        type=__ret__.type,
        upgrade_settings=__ret__.upgrade_settings,
        vm_size=__ret__.vm_size,
        vnet_subnet_id=__ret__.vnet_subnet_id)


@_utilities.lift_output_func(get_agent_pool)
def get_agent_pool_output(agent_pool_name: Optional[pulumi.Input[str]] = None,
                          resource_group_name: Optional[pulumi.Input[str]] = None,
                          resource_name: Optional[pulumi.Input[str]] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAgentPoolResult]:
    """
    Gets the details of the agent pool by managed cluster and resource group.


    :param str agent_pool_name: The name of the agent pool.
    :param str resource_group_name: The name of the resource group.
    :param str resource_name: The name of the managed cluster resource.
    """
    ...
