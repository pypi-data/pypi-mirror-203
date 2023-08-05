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
from ._inputs import *

__all__ = ['IoTAddonArgs', 'IoTAddon']

@pulumi.input_type
class IoTAddonArgs:
    def __init__(__self__, *,
                 device_name: pulumi.Input[str],
                 io_t_device_details: pulumi.Input['IoTDeviceInfoArgs'],
                 io_t_edge_device_details: pulumi.Input['IoTDeviceInfoArgs'],
                 kind: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 role_name: pulumi.Input[str],
                 addon_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a IoTAddon resource.
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input['IoTDeviceInfoArgs'] io_t_device_details: IoT device metadata to which appliance needs to be connected.
        :param pulumi.Input['IoTDeviceInfoArgs'] io_t_edge_device_details: IoT edge device to which the IoT Addon needs to be configured.
        :param pulumi.Input[str] kind: Addon type.
               Expected value is 'IotEdge'.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] role_name: The role name.
        :param pulumi.Input[str] addon_name: The addon name.
        """
        pulumi.set(__self__, "device_name", device_name)
        pulumi.set(__self__, "io_t_device_details", io_t_device_details)
        pulumi.set(__self__, "io_t_edge_device_details", io_t_edge_device_details)
        pulumi.set(__self__, "kind", 'IotEdge')
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "role_name", role_name)
        if addon_name is not None:
            pulumi.set(__self__, "addon_name", addon_name)

    @property
    @pulumi.getter(name="deviceName")
    def device_name(self) -> pulumi.Input[str]:
        """
        The device name.
        """
        return pulumi.get(self, "device_name")

    @device_name.setter
    def device_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "device_name", value)

    @property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> pulumi.Input['IoTDeviceInfoArgs']:
        """
        IoT device metadata to which appliance needs to be connected.
        """
        return pulumi.get(self, "io_t_device_details")

    @io_t_device_details.setter
    def io_t_device_details(self, value: pulumi.Input['IoTDeviceInfoArgs']):
        pulumi.set(self, "io_t_device_details", value)

    @property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> pulumi.Input['IoTDeviceInfoArgs']:
        """
        IoT edge device to which the IoT Addon needs to be configured.
        """
        return pulumi.get(self, "io_t_edge_device_details")

    @io_t_edge_device_details.setter
    def io_t_edge_device_details(self, value: pulumi.Input['IoTDeviceInfoArgs']):
        pulumi.set(self, "io_t_edge_device_details", value)

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Input[str]:
        """
        Addon type.
        Expected value is 'IotEdge'.
        """
        return pulumi.get(self, "kind")

    @kind.setter
    def kind(self, value: pulumi.Input[str]):
        pulumi.set(self, "kind", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The resource group name.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="roleName")
    def role_name(self) -> pulumi.Input[str]:
        """
        The role name.
        """
        return pulumi.get(self, "role_name")

    @role_name.setter
    def role_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "role_name", value)

    @property
    @pulumi.getter(name="addonName")
    def addon_name(self) -> Optional[pulumi.Input[str]]:
        """
        The addon name.
        """
        return pulumi.get(self, "addon_name")

    @addon_name.setter
    def addon_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "addon_name", value)


class IoTAddon(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addon_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 io_t_device_details: Optional[pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']]] = None,
                 io_t_edge_device_details: Optional[pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        IoT Addon.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] addon_name: The addon name.
        :param pulumi.Input[str] device_name: The device name.
        :param pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']] io_t_device_details: IoT device metadata to which appliance needs to be connected.
        :param pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']] io_t_edge_device_details: IoT edge device to which the IoT Addon needs to be configured.
        :param pulumi.Input[str] kind: Addon type.
               Expected value is 'IotEdge'.
        :param pulumi.Input[str] resource_group_name: The resource group name.
        :param pulumi.Input[str] role_name: The role name.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: IoTAddonArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        IoT Addon.

        :param str resource_name: The name of the resource.
        :param IoTAddonArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(IoTAddonArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 addon_name: Optional[pulumi.Input[str]] = None,
                 device_name: Optional[pulumi.Input[str]] = None,
                 io_t_device_details: Optional[pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']]] = None,
                 io_t_edge_device_details: Optional[pulumi.Input[pulumi.InputType['IoTDeviceInfoArgs']]] = None,
                 kind: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 role_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = IoTAddonArgs.__new__(IoTAddonArgs)

            __props__.__dict__["addon_name"] = addon_name
            if device_name is None and not opts.urn:
                raise TypeError("Missing required property 'device_name'")
            __props__.__dict__["device_name"] = device_name
            if io_t_device_details is None and not opts.urn:
                raise TypeError("Missing required property 'io_t_device_details'")
            __props__.__dict__["io_t_device_details"] = io_t_device_details
            if io_t_edge_device_details is None and not opts.urn:
                raise TypeError("Missing required property 'io_t_edge_device_details'")
            __props__.__dict__["io_t_edge_device_details"] = io_t_edge_device_details
            if kind is None and not opts.urn:
                raise TypeError("Missing required property 'kind'")
            __props__.__dict__["kind"] = 'IotEdge'
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if role_name is None and not opts.urn:
                raise TypeError("Missing required property 'role_name'")
            __props__.__dict__["role_name"] = role_name
            __props__.__dict__["host_platform"] = None
            __props__.__dict__["host_platform_type"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["version"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:databoxedge:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20200901preview:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20201201:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20210201:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20210201preview:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20210601:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20210601preview:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20220301:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20220401preview:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20221201preview:IoTAddon"), pulumi.Alias(type_="azure-native:databoxedge/v20230101preview:IoTAddon")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(IoTAddon, __self__).__init__(
            'azure-native:databoxedge/v20200901:IoTAddon',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'IoTAddon':
        """
        Get an existing IoTAddon resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = IoTAddonArgs.__new__(IoTAddonArgs)

        __props__.__dict__["host_platform"] = None
        __props__.__dict__["host_platform_type"] = None
        __props__.__dict__["io_t_device_details"] = None
        __props__.__dict__["io_t_edge_device_details"] = None
        __props__.__dict__["kind"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["version"] = None
        return IoTAddon(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="hostPlatform")
    def host_platform(self) -> pulumi.Output[str]:
        """
        Host OS supported by the IoT addon.
        """
        return pulumi.get(self, "host_platform")

    @property
    @pulumi.getter(name="hostPlatformType")
    def host_platform_type(self) -> pulumi.Output[str]:
        """
        Platform where the runtime is hosted.
        """
        return pulumi.get(self, "host_platform_type")

    @property
    @pulumi.getter(name="ioTDeviceDetails")
    def io_t_device_details(self) -> pulumi.Output['outputs.IoTDeviceInfoResponse']:
        """
        IoT device metadata to which appliance needs to be connected.
        """
        return pulumi.get(self, "io_t_device_details")

    @property
    @pulumi.getter(name="ioTEdgeDeviceDetails")
    def io_t_edge_device_details(self) -> pulumi.Output['outputs.IoTDeviceInfoResponse']:
        """
        IoT edge device to which the IoT Addon needs to be configured.
        """
        return pulumi.get(self, "io_t_edge_device_details")

    @property
    @pulumi.getter
    def kind(self) -> pulumi.Output[str]:
        """
        Addon type.
        Expected value is 'IotEdge'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The object name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        Addon Provisioning State
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Addon type
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The hierarchical type of the object.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def version(self) -> pulumi.Output[str]:
        """
        Version of IoT running on the appliance.
        """
        return pulumi.get(self, "version")

