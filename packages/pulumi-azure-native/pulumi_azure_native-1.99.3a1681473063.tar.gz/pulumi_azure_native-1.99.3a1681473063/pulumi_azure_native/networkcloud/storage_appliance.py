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
from ._inputs import *

__all__ = ['StorageApplianceArgs', 'StorageAppliance']

@pulumi.input_type
class StorageApplianceArgs:
    def __init__(__self__, *,
                 administrator_credentials: pulumi.Input['AdministrativeCredentialsArgs'],
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 rack_id: pulumi.Input[str],
                 rack_slot: pulumi.Input[float],
                 resource_group_name: pulumi.Input[str],
                 serial_number: pulumi.Input[str],
                 storage_appliance_sku_id: pulumi.Input[str],
                 location: Optional[pulumi.Input[str]] = None,
                 storage_appliance_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a StorageAppliance resource.
        :param pulumi.Input['AdministrativeCredentialsArgs'] administrator_credentials: The credentials of the administrative interface on this storage appliance.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[str] rack_id: The resource ID of the rack where this storage appliance resides.
        :param pulumi.Input[float] rack_slot: The slot the storage appliance is in the rack based on the BOM configuration.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] serial_number: The serial number for the storage appliance.
        :param pulumi.Input[str] storage_appliance_sku_id: The SKU for the storage appliance.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] storage_appliance_name: The name of the storage appliance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "administrator_credentials", administrator_credentials)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "rack_id", rack_id)
        pulumi.set(__self__, "rack_slot", rack_slot)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "serial_number", serial_number)
        pulumi.set(__self__, "storage_appliance_sku_id", storage_appliance_sku_id)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if storage_appliance_name is not None:
            pulumi.set(__self__, "storage_appliance_name", storage_appliance_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter(name="administratorCredentials")
    def administrator_credentials(self) -> pulumi.Input['AdministrativeCredentialsArgs']:
        """
        The credentials of the administrative interface on this storage appliance.
        """
        return pulumi.get(self, "administrator_credentials")

    @administrator_credentials.setter
    def administrator_credentials(self, value: pulumi.Input['AdministrativeCredentialsArgs']):
        pulumi.set(self, "administrator_credentials", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

    @property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> pulumi.Input[str]:
        """
        The resource ID of the rack where this storage appliance resides.
        """
        return pulumi.get(self, "rack_id")

    @rack_id.setter
    def rack_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "rack_id", value)

    @property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> pulumi.Input[float]:
        """
        The slot the storage appliance is in the rack based on the BOM configuration.
        """
        return pulumi.get(self, "rack_slot")

    @rack_slot.setter
    def rack_slot(self, value: pulumi.Input[float]):
        pulumi.set(self, "rack_slot", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Input[str]:
        """
        The serial number for the storage appliance.
        """
        return pulumi.get(self, "serial_number")

    @serial_number.setter
    def serial_number(self, value: pulumi.Input[str]):
        pulumi.set(self, "serial_number", value)

    @property
    @pulumi.getter(name="storageApplianceSkuId")
    def storage_appliance_sku_id(self) -> pulumi.Input[str]:
        """
        The SKU for the storage appliance.
        """
        return pulumi.get(self, "storage_appliance_sku_id")

    @storage_appliance_sku_id.setter
    def storage_appliance_sku_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "storage_appliance_sku_id", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter(name="storageApplianceName")
    def storage_appliance_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the storage appliance.
        """
        return pulumi.get(self, "storage_appliance_name")

    @storage_appliance_name.setter
    def storage_appliance_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "storage_appliance_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class StorageAppliance(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_credentials: Optional[pulumi.Input[pulumi.InputType['AdministrativeCredentialsArgs']]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 rack_id: Optional[pulumi.Input[str]] = None,
                 rack_slot: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 storage_appliance_name: Optional[pulumi.Input[str]] = None,
                 storage_appliance_sku_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        """
        API Version: 2022-12-12-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[pulumi.InputType['AdministrativeCredentialsArgs']] administrator_credentials: The credentials of the administrative interface on this storage appliance.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the cluster associated with the resource.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] rack_id: The resource ID of the rack where this storage appliance resides.
        :param pulumi.Input[float] rack_slot: The slot the storage appliance is in the rack based on the BOM configuration.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] serial_number: The serial number for the storage appliance.
        :param pulumi.Input[str] storage_appliance_name: The name of the storage appliance.
        :param pulumi.Input[str] storage_appliance_sku_id: The SKU for the storage appliance.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: StorageApplianceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        API Version: 2022-12-12-preview.

        :param str resource_name: The name of the resource.
        :param StorageApplianceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(StorageApplianceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 administrator_credentials: Optional[pulumi.Input[pulumi.InputType['AdministrativeCredentialsArgs']]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 rack_id: Optional[pulumi.Input[str]] = None,
                 rack_slot: Optional[pulumi.Input[float]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 serial_number: Optional[pulumi.Input[str]] = None,
                 storage_appliance_name: Optional[pulumi.Input[str]] = None,
                 storage_appliance_sku_id: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = StorageApplianceArgs.__new__(StorageApplianceArgs)

            if administrator_credentials is None and not opts.urn:
                raise TypeError("Missing required property 'administrator_credentials'")
            __props__.__dict__["administrator_credentials"] = administrator_credentials
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            if rack_id is None and not opts.urn:
                raise TypeError("Missing required property 'rack_id'")
            __props__.__dict__["rack_id"] = rack_id
            if rack_slot is None and not opts.urn:
                raise TypeError("Missing required property 'rack_slot'")
            __props__.__dict__["rack_slot"] = rack_slot
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if serial_number is None and not opts.urn:
                raise TypeError("Missing required property 'serial_number'")
            __props__.__dict__["serial_number"] = serial_number
            __props__.__dict__["storage_appliance_name"] = storage_appliance_name
            if storage_appliance_sku_id is None and not opts.urn:
                raise TypeError("Missing required property 'storage_appliance_sku_id'")
            __props__.__dict__["storage_appliance_sku_id"] = storage_appliance_sku_id
            __props__.__dict__["tags"] = tags
            __props__.__dict__["capacity"] = None
            __props__.__dict__["capacity_used"] = None
            __props__.__dict__["cluster_id"] = None
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["management_ipv4_address"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["remote_vendor_management_feature"] = None
            __props__.__dict__["remote_vendor_management_status"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud/v20221212preview:StorageAppliance")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(StorageAppliance, __self__).__init__(
            'azure-native:networkcloud:StorageAppliance',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'StorageAppliance':
        """
        Get an existing StorageAppliance resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = StorageApplianceArgs.__new__(StorageApplianceArgs)

        __props__.__dict__["administrator_credentials"] = None
        __props__.__dict__["capacity"] = None
        __props__.__dict__["capacity_used"] = None
        __props__.__dict__["cluster_id"] = None
        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["management_ipv4_address"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["rack_id"] = None
        __props__.__dict__["rack_slot"] = None
        __props__.__dict__["remote_vendor_management_feature"] = None
        __props__.__dict__["remote_vendor_management_status"] = None
        __props__.__dict__["serial_number"] = None
        __props__.__dict__["storage_appliance_sku_id"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        return StorageAppliance(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="administratorCredentials")
    def administrator_credentials(self) -> pulumi.Output['outputs.AdministrativeCredentialsResponse']:
        """
        The credentials of the administrative interface on this storage appliance.
        """
        return pulumi.get(self, "administrator_credentials")

    @property
    @pulumi.getter
    def capacity(self) -> pulumi.Output[float]:
        """
        The total capacity of the storage appliance.
        """
        return pulumi.get(self, "capacity")

    @property
    @pulumi.getter(name="capacityUsed")
    def capacity_used(self) -> pulumi.Output[float]:
        """
        The amount of storage consumed.
        """
        return pulumi.get(self, "capacity_used")

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the cluster this storage appliance is associated with.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The detailed status of the storage appliance.
        """
        return pulumi.get(self, "detailed_status")

    @property
    @pulumi.getter(name="detailedStatusMessage")
    def detailed_status_message(self) -> pulumi.Output[str]:
        """
        The descriptive message about the current detailed status.
        """
        return pulumi.get(self, "detailed_status_message")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster associated with the resource.
        """
        return pulumi.get(self, "extended_location")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter(name="managementIpv4Address")
    def management_ipv4_address(self) -> pulumi.Output[str]:
        """
        The endpoint for the management interface of the storage appliance.
        """
        return pulumi.get(self, "management_ipv4_address")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the storage appliance.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="rackId")
    def rack_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the rack where this storage appliance resides.
        """
        return pulumi.get(self, "rack_id")

    @property
    @pulumi.getter(name="rackSlot")
    def rack_slot(self) -> pulumi.Output[float]:
        """
        The slot the storage appliance is in the rack based on the BOM configuration.
        """
        return pulumi.get(self, "rack_slot")

    @property
    @pulumi.getter(name="remoteVendorManagementFeature")
    def remote_vendor_management_feature(self) -> pulumi.Output[str]:
        """
        The indicator of whether the storage appliance supports remote vendor management.
        """
        return pulumi.get(self, "remote_vendor_management_feature")

    @property
    @pulumi.getter(name="remoteVendorManagementStatus")
    def remote_vendor_management_status(self) -> pulumi.Output[str]:
        """
        The indicator of whether the remote vendor management feature is enabled or disabled, or unsupported if it is an unsupported feature.
        """
        return pulumi.get(self, "remote_vendor_management_status")

    @property
    @pulumi.getter(name="serialNumber")
    def serial_number(self) -> pulumi.Output[str]:
        """
        The serial number for the storage appliance.
        """
        return pulumi.get(self, "serial_number")

    @property
    @pulumi.getter(name="storageApplianceSkuId")
    def storage_appliance_sku_id(self) -> pulumi.Output[str]:
        """
        The SKU for the storage appliance.
        """
        return pulumi.get(self, "storage_appliance_sku_id")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

