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

__all__ = ['ConsoleArgs', 'Console']

@pulumi.input_type
class ConsoleArgs:
    def __init__(__self__, *,
                 enabled: pulumi.Input[Union[str, 'ConsoleEnabled']],
                 extended_location: pulumi.Input['ExtendedLocationArgs'],
                 resource_group_name: pulumi.Input[str],
                 ssh_public_key: pulumi.Input['SshPublicKeyArgs'],
                 virtual_machine_name: pulumi.Input[str],
                 console_name: Optional[pulumi.Input[str]] = None,
                 expiration: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None):
        """
        The set of arguments for constructing a Console resource.
        :param pulumi.Input[Union[str, 'ConsoleEnabled']] enabled: The indicator of whether the console access is enabled.
        :param pulumi.Input['ExtendedLocationArgs'] extended_location: The extended location of the cluster manager associated with the cluster this virtual machine is created on.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input['SshPublicKeyArgs'] ssh_public_key: The SSH public key that will be provisioned for user access. The user is expected to have the corresponding SSH private key for logging in.
        :param pulumi.Input[str] virtual_machine_name: The name of the virtual machine.
        :param pulumi.Input[str] console_name: The name of the virtual machine console.
        :param pulumi.Input[str] expiration: The date and time after which the key will be disallowed access.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        """
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "extended_location", extended_location)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "ssh_public_key", ssh_public_key)
        pulumi.set(__self__, "virtual_machine_name", virtual_machine_name)
        if console_name is not None:
            pulumi.set(__self__, "console_name", console_name)
        if expiration is not None:
            pulumi.set(__self__, "expiration", expiration)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)

    @property
    @pulumi.getter
    def enabled(self) -> pulumi.Input[Union[str, 'ConsoleEnabled']]:
        """
        The indicator of whether the console access is enabled.
        """
        return pulumi.get(self, "enabled")

    @enabled.setter
    def enabled(self, value: pulumi.Input[Union[str, 'ConsoleEnabled']]):
        pulumi.set(self, "enabled", value)

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Input['ExtendedLocationArgs']:
        """
        The extended location of the cluster manager associated with the cluster this virtual machine is created on.
        """
        return pulumi.get(self, "extended_location")

    @extended_location.setter
    def extended_location(self, value: pulumi.Input['ExtendedLocationArgs']):
        pulumi.set(self, "extended_location", value)

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
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> pulumi.Input['SshPublicKeyArgs']:
        """
        The SSH public key that will be provisioned for user access. The user is expected to have the corresponding SSH private key for logging in.
        """
        return pulumi.get(self, "ssh_public_key")

    @ssh_public_key.setter
    def ssh_public_key(self, value: pulumi.Input['SshPublicKeyArgs']):
        pulumi.set(self, "ssh_public_key", value)

    @property
    @pulumi.getter(name="virtualMachineName")
    def virtual_machine_name(self) -> pulumi.Input[str]:
        """
        The name of the virtual machine.
        """
        return pulumi.get(self, "virtual_machine_name")

    @virtual_machine_name.setter
    def virtual_machine_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "virtual_machine_name", value)

    @property
    @pulumi.getter(name="consoleName")
    def console_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the virtual machine console.
        """
        return pulumi.get(self, "console_name")

    @console_name.setter
    def console_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "console_name", value)

    @property
    @pulumi.getter
    def expiration(self) -> Optional[pulumi.Input[str]]:
        """
        The date and time after which the key will be disallowed access.
        """
        return pulumi.get(self, "expiration")

    @expiration.setter
    def expiration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expiration", value)

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
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)


class Console(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 console_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[Union[str, 'ConsoleEnabled']]] = None,
                 expiration: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[pulumi.InputType['SshPublicKeyArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Create a Console resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] console_name: The name of the virtual machine console.
        :param pulumi.Input[Union[str, 'ConsoleEnabled']] enabled: The indicator of whether the console access is enabled.
        :param pulumi.Input[str] expiration: The date and time after which the key will be disallowed access.
        :param pulumi.Input[pulumi.InputType['ExtendedLocationArgs']] extended_location: The extended location of the cluster manager associated with the cluster this virtual machine is created on.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[pulumi.InputType['SshPublicKeyArgs']] ssh_public_key: The SSH public key that will be provisioned for user access. The user is expected to have the corresponding SSH private key for logging in.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[str] virtual_machine_name: The name of the virtual machine.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConsoleArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Create a Console resource with the given unique name, props, and options.
        :param str resource_name: The name of the resource.
        :param ConsoleArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConsoleArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 console_name: Optional[pulumi.Input[str]] = None,
                 enabled: Optional[pulumi.Input[Union[str, 'ConsoleEnabled']]] = None,
                 expiration: Optional[pulumi.Input[str]] = None,
                 extended_location: Optional[pulumi.Input[pulumi.InputType['ExtendedLocationArgs']]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 ssh_public_key: Optional[pulumi.Input[pulumi.InputType['SshPublicKeyArgs']]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 virtual_machine_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ConsoleArgs.__new__(ConsoleArgs)

            __props__.__dict__["console_name"] = console_name
            if enabled is None and not opts.urn:
                raise TypeError("Missing required property 'enabled'")
            __props__.__dict__["enabled"] = enabled
            __props__.__dict__["expiration"] = expiration
            if extended_location is None and not opts.urn:
                raise TypeError("Missing required property 'extended_location'")
            __props__.__dict__["extended_location"] = extended_location
            __props__.__dict__["location"] = location
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if ssh_public_key is None and not opts.urn:
                raise TypeError("Missing required property 'ssh_public_key'")
            __props__.__dict__["ssh_public_key"] = ssh_public_key
            __props__.__dict__["tags"] = tags
            if virtual_machine_name is None and not opts.urn:
                raise TypeError("Missing required property 'virtual_machine_name'")
            __props__.__dict__["virtual_machine_name"] = virtual_machine_name
            __props__.__dict__["detailed_status"] = None
            __props__.__dict__["detailed_status_message"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["private_link_service_id"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
            __props__.__dict__["virtual_machine_access_id"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:networkcloud:Console")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Console, __self__).__init__(
            'azure-native:networkcloud/v20221212preview:Console',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Console':
        """
        Get an existing Console resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ConsoleArgs.__new__(ConsoleArgs)

        __props__.__dict__["detailed_status"] = None
        __props__.__dict__["detailed_status_message"] = None
        __props__.__dict__["enabled"] = None
        __props__.__dict__["expiration"] = None
        __props__.__dict__["extended_location"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["private_link_service_id"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["ssh_public_key"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["virtual_machine_access_id"] = None
        return Console(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="detailedStatus")
    def detailed_status(self) -> pulumi.Output[str]:
        """
        The more detailed status of the console.
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
    @pulumi.getter
    def enabled(self) -> pulumi.Output[str]:
        """
        The indicator of whether the console access is enabled.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def expiration(self) -> pulumi.Output[Optional[str]]:
        """
        The date and time after which the key will be disallowed access.
        """
        return pulumi.get(self, "expiration")

    @property
    @pulumi.getter(name="extendedLocation")
    def extended_location(self) -> pulumi.Output['outputs.ExtendedLocationResponse']:
        """
        The extended location of the cluster manager associated with the cluster this virtual machine is created on.
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
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="privateLinkServiceId")
    def private_link_service_id(self) -> pulumi.Output[str]:
        """
        The resource ID of the private link service that is used to provide virtual machine console access.
        """
        return pulumi.get(self, "private_link_service_id")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the virtual machine console.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="sshPublicKey")
    def ssh_public_key(self) -> pulumi.Output['outputs.SshPublicKeyResponse']:
        """
        The SSH public key that will be provisioned for user access. The user is expected to have the corresponding SSH private key for logging in.
        """
        return pulumi.get(self, "ssh_public_key")

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

    @property
    @pulumi.getter(name="virtualMachineAccessId")
    def virtual_machine_access_id(self) -> pulumi.Output[str]:
        """
        The unique identifier for the virtual machine that is used to access the console.
        """
        return pulumi.get(self, "virtual_machine_access_id")

