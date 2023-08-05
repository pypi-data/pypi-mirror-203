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
    'GetNodeTypeResult',
    'AwaitableGetNodeTypeResult',
    'get_node_type',
    'get_node_type_output',
]

@pulumi.output_type
class GetNodeTypeResult:
    """
    Describes a node type in the cluster, each node type represents sub set of nodes in the cluster.
    """
    def __init__(__self__, additional_data_disks=None, application_ports=None, capacities=None, data_disk_letter=None, data_disk_size_gb=None, data_disk_type=None, enable_accelerated_networking=None, enable_encryption_at_host=None, enable_over_provisioning=None, ephemeral_ports=None, frontend_configurations=None, id=None, is_primary=None, is_stateless=None, multiple_placement_groups=None, name=None, network_security_rules=None, placement_properties=None, provisioning_state=None, sku=None, system_data=None, tags=None, type=None, use_default_public_load_balancer=None, use_temp_data_disk=None, vm_extensions=None, vm_image_offer=None, vm_image_publisher=None, vm_image_sku=None, vm_image_version=None, vm_instance_count=None, vm_managed_identity=None, vm_secrets=None, vm_size=None):
        if additional_data_disks and not isinstance(additional_data_disks, list):
            raise TypeError("Expected argument 'additional_data_disks' to be a list")
        pulumi.set(__self__, "additional_data_disks", additional_data_disks)
        if application_ports and not isinstance(application_ports, dict):
            raise TypeError("Expected argument 'application_ports' to be a dict")
        pulumi.set(__self__, "application_ports", application_ports)
        if capacities and not isinstance(capacities, dict):
            raise TypeError("Expected argument 'capacities' to be a dict")
        pulumi.set(__self__, "capacities", capacities)
        if data_disk_letter and not isinstance(data_disk_letter, str):
            raise TypeError("Expected argument 'data_disk_letter' to be a str")
        pulumi.set(__self__, "data_disk_letter", data_disk_letter)
        if data_disk_size_gb and not isinstance(data_disk_size_gb, int):
            raise TypeError("Expected argument 'data_disk_size_gb' to be a int")
        pulumi.set(__self__, "data_disk_size_gb", data_disk_size_gb)
        if data_disk_type and not isinstance(data_disk_type, str):
            raise TypeError("Expected argument 'data_disk_type' to be a str")
        pulumi.set(__self__, "data_disk_type", data_disk_type)
        if enable_accelerated_networking and not isinstance(enable_accelerated_networking, bool):
            raise TypeError("Expected argument 'enable_accelerated_networking' to be a bool")
        pulumi.set(__self__, "enable_accelerated_networking", enable_accelerated_networking)
        if enable_encryption_at_host and not isinstance(enable_encryption_at_host, bool):
            raise TypeError("Expected argument 'enable_encryption_at_host' to be a bool")
        pulumi.set(__self__, "enable_encryption_at_host", enable_encryption_at_host)
        if enable_over_provisioning and not isinstance(enable_over_provisioning, bool):
            raise TypeError("Expected argument 'enable_over_provisioning' to be a bool")
        pulumi.set(__self__, "enable_over_provisioning", enable_over_provisioning)
        if ephemeral_ports and not isinstance(ephemeral_ports, dict):
            raise TypeError("Expected argument 'ephemeral_ports' to be a dict")
        pulumi.set(__self__, "ephemeral_ports", ephemeral_ports)
        if frontend_configurations and not isinstance(frontend_configurations, list):
            raise TypeError("Expected argument 'frontend_configurations' to be a list")
        pulumi.set(__self__, "frontend_configurations", frontend_configurations)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_primary and not isinstance(is_primary, bool):
            raise TypeError("Expected argument 'is_primary' to be a bool")
        pulumi.set(__self__, "is_primary", is_primary)
        if is_stateless and not isinstance(is_stateless, bool):
            raise TypeError("Expected argument 'is_stateless' to be a bool")
        pulumi.set(__self__, "is_stateless", is_stateless)
        if multiple_placement_groups and not isinstance(multiple_placement_groups, bool):
            raise TypeError("Expected argument 'multiple_placement_groups' to be a bool")
        pulumi.set(__self__, "multiple_placement_groups", multiple_placement_groups)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if network_security_rules and not isinstance(network_security_rules, list):
            raise TypeError("Expected argument 'network_security_rules' to be a list")
        pulumi.set(__self__, "network_security_rules", network_security_rules)
        if placement_properties and not isinstance(placement_properties, dict):
            raise TypeError("Expected argument 'placement_properties' to be a dict")
        pulumi.set(__self__, "placement_properties", placement_properties)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if sku and not isinstance(sku, dict):
            raise TypeError("Expected argument 'sku' to be a dict")
        pulumi.set(__self__, "sku", sku)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if use_default_public_load_balancer and not isinstance(use_default_public_load_balancer, bool):
            raise TypeError("Expected argument 'use_default_public_load_balancer' to be a bool")
        pulumi.set(__self__, "use_default_public_load_balancer", use_default_public_load_balancer)
        if use_temp_data_disk and not isinstance(use_temp_data_disk, bool):
            raise TypeError("Expected argument 'use_temp_data_disk' to be a bool")
        pulumi.set(__self__, "use_temp_data_disk", use_temp_data_disk)
        if vm_extensions and not isinstance(vm_extensions, list):
            raise TypeError("Expected argument 'vm_extensions' to be a list")
        pulumi.set(__self__, "vm_extensions", vm_extensions)
        if vm_image_offer and not isinstance(vm_image_offer, str):
            raise TypeError("Expected argument 'vm_image_offer' to be a str")
        pulumi.set(__self__, "vm_image_offer", vm_image_offer)
        if vm_image_publisher and not isinstance(vm_image_publisher, str):
            raise TypeError("Expected argument 'vm_image_publisher' to be a str")
        pulumi.set(__self__, "vm_image_publisher", vm_image_publisher)
        if vm_image_sku and not isinstance(vm_image_sku, str):
            raise TypeError("Expected argument 'vm_image_sku' to be a str")
        pulumi.set(__self__, "vm_image_sku", vm_image_sku)
        if vm_image_version and not isinstance(vm_image_version, str):
            raise TypeError("Expected argument 'vm_image_version' to be a str")
        pulumi.set(__self__, "vm_image_version", vm_image_version)
        if vm_instance_count and not isinstance(vm_instance_count, int):
            raise TypeError("Expected argument 'vm_instance_count' to be a int")
        pulumi.set(__self__, "vm_instance_count", vm_instance_count)
        if vm_managed_identity and not isinstance(vm_managed_identity, dict):
            raise TypeError("Expected argument 'vm_managed_identity' to be a dict")
        pulumi.set(__self__, "vm_managed_identity", vm_managed_identity)
        if vm_secrets and not isinstance(vm_secrets, list):
            raise TypeError("Expected argument 'vm_secrets' to be a list")
        pulumi.set(__self__, "vm_secrets", vm_secrets)
        if vm_size and not isinstance(vm_size, str):
            raise TypeError("Expected argument 'vm_size' to be a str")
        pulumi.set(__self__, "vm_size", vm_size)

    @property
    @pulumi.getter(name="additionalDataDisks")
    def additional_data_disks(self) -> Optional[Sequence['outputs.VmssDataDiskResponse']]:
        """
        Additional managed data disks.
        """
        return pulumi.get(self, "additional_data_disks")

    @property
    @pulumi.getter(name="applicationPorts")
    def application_ports(self) -> Optional['outputs.EndpointRangeDescriptionResponse']:
        """
        The range of ports from which cluster assigned port to Service Fabric applications.
        """
        return pulumi.get(self, "application_ports")

    @property
    @pulumi.getter
    def capacities(self) -> Optional[Mapping[str, str]]:
        """
        The capacity tags applied to the nodes in the node type, the cluster resource manager uses these tags to understand how much resource a node has.
        """
        return pulumi.get(self, "capacities")

    @property
    @pulumi.getter(name="dataDiskLetter")
    def data_disk_letter(self) -> Optional[str]:
        """
        Managed data disk letter. It can not use the reserved letter C or D and it can not change after created.
        """
        return pulumi.get(self, "data_disk_letter")

    @property
    @pulumi.getter(name="dataDiskSizeGB")
    def data_disk_size_gb(self) -> Optional[int]:
        """
        Disk size for the managed disk attached to the vms on the node type in GBs.
        """
        return pulumi.get(self, "data_disk_size_gb")

    @property
    @pulumi.getter(name="dataDiskType")
    def data_disk_type(self) -> Optional[str]:
        """
        Managed data disk type. Specifies the storage account type for the managed disk
        """
        return pulumi.get(self, "data_disk_type")

    @property
    @pulumi.getter(name="enableAcceleratedNetworking")
    def enable_accelerated_networking(self) -> Optional[bool]:
        """
        Specifies whether the network interface is accelerated networking-enabled.
        """
        return pulumi.get(self, "enable_accelerated_networking")

    @property
    @pulumi.getter(name="enableEncryptionAtHost")
    def enable_encryption_at_host(self) -> Optional[bool]:
        """
        Enable or disable the Host Encryption for the virtual machines on the node type. This will enable the encryption for all the disks including Resource/Temp disk at host itself. Default: The Encryption at host will be disabled unless this property is set to true for the resource.
        """
        return pulumi.get(self, "enable_encryption_at_host")

    @property
    @pulumi.getter(name="enableOverProvisioning")
    def enable_over_provisioning(self) -> Optional[bool]:
        """
        Specifies whether the node type should be overprovisioned. It is only allowed for stateless node types.
        """
        return pulumi.get(self, "enable_over_provisioning")

    @property
    @pulumi.getter(name="ephemeralPorts")
    def ephemeral_ports(self) -> Optional['outputs.EndpointRangeDescriptionResponse']:
        """
        The range of ephemeral ports that nodes in this node type should be configured with.
        """
        return pulumi.get(self, "ephemeral_ports")

    @property
    @pulumi.getter(name="frontendConfigurations")
    def frontend_configurations(self) -> Optional[Sequence['outputs.FrontendConfigurationResponse']]:
        """
        Indicates the node type uses its own frontend configurations instead of the default one for the cluster. This setting can only be specified for non-primary node types and can not be added or removed after the node type is created.
        """
        return pulumi.get(self, "frontend_configurations")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource identifier.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isPrimary")
    def is_primary(self) -> bool:
        """
        Indicates the Service Fabric system services for the cluster will run on this node type. This setting cannot be changed once the node type is created.
        """
        return pulumi.get(self, "is_primary")

    @property
    @pulumi.getter(name="isStateless")
    def is_stateless(self) -> Optional[bool]:
        """
        Indicates if the node type can only host Stateless workloads.
        """
        return pulumi.get(self, "is_stateless")

    @property
    @pulumi.getter(name="multiplePlacementGroups")
    def multiple_placement_groups(self) -> Optional[bool]:
        """
        Indicates if scale set associated with the node type can be composed of multiple placement groups.
        """
        return pulumi.get(self, "multiple_placement_groups")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="networkSecurityRules")
    def network_security_rules(self) -> Optional[Sequence['outputs.NetworkSecurityRuleResponse']]:
        """
        The Network Security Rules for this node type. This setting can only be specified for node types that are configured with frontend configurations.
        """
        return pulumi.get(self, "network_security_rules")

    @property
    @pulumi.getter(name="placementProperties")
    def placement_properties(self) -> Optional[Mapping[str, str]]:
        """
        The placement tags applied to nodes in the node type, which can be used to indicate where certain services (workload) should run.
        """
        return pulumi.get(self, "placement_properties")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the node type resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def sku(self) -> Optional['outputs.NodeTypeSkuResponse']:
        """
        The node type sku.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Azure resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="useDefaultPublicLoadBalancer")
    def use_default_public_load_balancer(self) -> Optional[bool]:
        """
        Specifies whether the use public load balancer. If not specified and the node type doesn't have its own frontend configuration, it will be attached to the default load balancer. If the node type uses its own Load balancer and useDefaultPublicLoadBalancer is true, then the frontend has to be an Internal Load Balancer. If the node type uses its own Load balancer and useDefaultPublicLoadBalancer is false or not set, then the custom load balancer must include a public load balancer to provide outbound connectivity.
        """
        return pulumi.get(self, "use_default_public_load_balancer")

    @property
    @pulumi.getter(name="useTempDataDisk")
    def use_temp_data_disk(self) -> Optional[bool]:
        """
        Specifies whether to use the temporary disk for the service fabric data root, in which case no managed data disk will be attached and the temporary disk will be used. It is only allowed for stateless node types.
        """
        return pulumi.get(self, "use_temp_data_disk")

    @property
    @pulumi.getter(name="vmExtensions")
    def vm_extensions(self) -> Optional[Sequence['outputs.VMSSExtensionResponse']]:
        """
        Set of extensions that should be installed onto the virtual machines.
        """
        return pulumi.get(self, "vm_extensions")

    @property
    @pulumi.getter(name="vmImageOffer")
    def vm_image_offer(self) -> Optional[str]:
        """
        The offer type of the Azure Virtual Machines Marketplace image. For example, UbuntuServer or WindowsServer.
        """
        return pulumi.get(self, "vm_image_offer")

    @property
    @pulumi.getter(name="vmImagePublisher")
    def vm_image_publisher(self) -> Optional[str]:
        """
        The publisher of the Azure Virtual Machines Marketplace image. For example, Canonical or MicrosoftWindowsServer.
        """
        return pulumi.get(self, "vm_image_publisher")

    @property
    @pulumi.getter(name="vmImageSku")
    def vm_image_sku(self) -> Optional[str]:
        """
        The SKU of the Azure Virtual Machines Marketplace image. For example, 14.04.0-LTS or 2012-R2-Datacenter.
        """
        return pulumi.get(self, "vm_image_sku")

    @property
    @pulumi.getter(name="vmImageVersion")
    def vm_image_version(self) -> Optional[str]:
        """
        The version of the Azure Virtual Machines Marketplace image. A value of 'latest' can be specified to select the latest version of an image. If omitted, the default is 'latest'.
        """
        return pulumi.get(self, "vm_image_version")

    @property
    @pulumi.getter(name="vmInstanceCount")
    def vm_instance_count(self) -> int:
        """
        The number of nodes in the node type. <br /><br />**Values:** <br />-1 - Use when auto scale rules are configured or sku.capacity is defined <br /> 0 - Not supported <br /> >0 - Use for manual scale.
        """
        return pulumi.get(self, "vm_instance_count")

    @property
    @pulumi.getter(name="vmManagedIdentity")
    def vm_managed_identity(self) -> Optional['outputs.VmManagedIdentityResponse']:
        """
        Identities to assign to the virtual machine scale set under the node type.
        """
        return pulumi.get(self, "vm_managed_identity")

    @property
    @pulumi.getter(name="vmSecrets")
    def vm_secrets(self) -> Optional[Sequence['outputs.VaultSecretGroupResponse']]:
        """
        The secrets to install in the virtual machines.
        """
        return pulumi.get(self, "vm_secrets")

    @property
    @pulumi.getter(name="vmSize")
    def vm_size(self) -> Optional[str]:
        """
        The size of virtual machines in the pool. All virtual machines in a pool are the same size. For example, Standard_D3.
        """
        return pulumi.get(self, "vm_size")


class AwaitableGetNodeTypeResult(GetNodeTypeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetNodeTypeResult(
            additional_data_disks=self.additional_data_disks,
            application_ports=self.application_ports,
            capacities=self.capacities,
            data_disk_letter=self.data_disk_letter,
            data_disk_size_gb=self.data_disk_size_gb,
            data_disk_type=self.data_disk_type,
            enable_accelerated_networking=self.enable_accelerated_networking,
            enable_encryption_at_host=self.enable_encryption_at_host,
            enable_over_provisioning=self.enable_over_provisioning,
            ephemeral_ports=self.ephemeral_ports,
            frontend_configurations=self.frontend_configurations,
            id=self.id,
            is_primary=self.is_primary,
            is_stateless=self.is_stateless,
            multiple_placement_groups=self.multiple_placement_groups,
            name=self.name,
            network_security_rules=self.network_security_rules,
            placement_properties=self.placement_properties,
            provisioning_state=self.provisioning_state,
            sku=self.sku,
            system_data=self.system_data,
            tags=self.tags,
            type=self.type,
            use_default_public_load_balancer=self.use_default_public_load_balancer,
            use_temp_data_disk=self.use_temp_data_disk,
            vm_extensions=self.vm_extensions,
            vm_image_offer=self.vm_image_offer,
            vm_image_publisher=self.vm_image_publisher,
            vm_image_sku=self.vm_image_sku,
            vm_image_version=self.vm_image_version,
            vm_instance_count=self.vm_instance_count,
            vm_managed_identity=self.vm_managed_identity,
            vm_secrets=self.vm_secrets,
            vm_size=self.vm_size)


def get_node_type(cluster_name: Optional[str] = None,
                  node_type_name: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetNodeTypeResult:
    """
    Get a Service Fabric node type of a given managed cluster.


    :param str cluster_name: The name of the cluster resource.
    :param str node_type_name: The name of the node type.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['clusterName'] = cluster_name
    __args__['nodeTypeName'] = node_type_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:servicefabric/v20220101:getNodeType', __args__, opts=opts, typ=GetNodeTypeResult).value

    return AwaitableGetNodeTypeResult(
        additional_data_disks=__ret__.additional_data_disks,
        application_ports=__ret__.application_ports,
        capacities=__ret__.capacities,
        data_disk_letter=__ret__.data_disk_letter,
        data_disk_size_gb=__ret__.data_disk_size_gb,
        data_disk_type=__ret__.data_disk_type,
        enable_accelerated_networking=__ret__.enable_accelerated_networking,
        enable_encryption_at_host=__ret__.enable_encryption_at_host,
        enable_over_provisioning=__ret__.enable_over_provisioning,
        ephemeral_ports=__ret__.ephemeral_ports,
        frontend_configurations=__ret__.frontend_configurations,
        id=__ret__.id,
        is_primary=__ret__.is_primary,
        is_stateless=__ret__.is_stateless,
        multiple_placement_groups=__ret__.multiple_placement_groups,
        name=__ret__.name,
        network_security_rules=__ret__.network_security_rules,
        placement_properties=__ret__.placement_properties,
        provisioning_state=__ret__.provisioning_state,
        sku=__ret__.sku,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        type=__ret__.type,
        use_default_public_load_balancer=__ret__.use_default_public_load_balancer,
        use_temp_data_disk=__ret__.use_temp_data_disk,
        vm_extensions=__ret__.vm_extensions,
        vm_image_offer=__ret__.vm_image_offer,
        vm_image_publisher=__ret__.vm_image_publisher,
        vm_image_sku=__ret__.vm_image_sku,
        vm_image_version=__ret__.vm_image_version,
        vm_instance_count=__ret__.vm_instance_count,
        vm_managed_identity=__ret__.vm_managed_identity,
        vm_secrets=__ret__.vm_secrets,
        vm_size=__ret__.vm_size)


@_utilities.lift_output_func(get_node_type)
def get_node_type_output(cluster_name: Optional[pulumi.Input[str]] = None,
                         node_type_name: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetNodeTypeResult]:
    """
    Get a Service Fabric node type of a given managed cluster.


    :param str cluster_name: The name of the cluster resource.
    :param str node_type_name: The name of the node type.
    :param str resource_group_name: The name of the resource group.
    """
    ...
