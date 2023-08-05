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

__all__ = ['WorkloadNetworkDnsServiceArgs', 'WorkloadNetworkDnsService']

@pulumi.input_type
class WorkloadNetworkDnsServiceArgs:
    def __init__(__self__, *,
                 private_cloud_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 default_dns_zone: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_service_id: Optional[pulumi.Input[str]] = None,
                 dns_service_ip: Optional[pulumi.Input[str]] = None,
                 fqdn_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 log_level: Optional[pulumi.Input[Union[str, 'DnsServiceLogLevelEnum']]] = None,
                 revision: Optional[pulumi.Input[float]] = None):
        """
        The set of arguments for constructing a WorkloadNetworkDnsService resource.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] default_dns_zone: Default DNS zone of the DNS Service.
        :param pulumi.Input[str] display_name: Display name of the DNS Service.
        :param pulumi.Input[str] dns_service_id: NSX DNS Service identifier. Generally the same as the DNS Service's display name
        :param pulumi.Input[str] dns_service_ip: DNS service IP of the DNS Service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fqdn_zones: FQDN zones of the DNS Service.
        :param pulumi.Input[Union[str, 'DnsServiceLogLevelEnum']] log_level: DNS Service log level.
        :param pulumi.Input[float] revision: NSX revision number.
        """
        pulumi.set(__self__, "private_cloud_name", private_cloud_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if default_dns_zone is not None:
            pulumi.set(__self__, "default_dns_zone", default_dns_zone)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if dns_service_id is not None:
            pulumi.set(__self__, "dns_service_id", dns_service_id)
        if dns_service_ip is not None:
            pulumi.set(__self__, "dns_service_ip", dns_service_ip)
        if fqdn_zones is not None:
            pulumi.set(__self__, "fqdn_zones", fqdn_zones)
        if log_level is not None:
            pulumi.set(__self__, "log_level", log_level)
        if revision is not None:
            pulumi.set(__self__, "revision", revision)

    @property
    @pulumi.getter(name="privateCloudName")
    def private_cloud_name(self) -> pulumi.Input[str]:
        """
        Name of the private cloud
        """
        return pulumi.get(self, "private_cloud_name")

    @private_cloud_name.setter
    def private_cloud_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "private_cloud_name", value)

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
    @pulumi.getter(name="defaultDnsZone")
    def default_dns_zone(self) -> Optional[pulumi.Input[str]]:
        """
        Default DNS zone of the DNS Service.
        """
        return pulumi.get(self, "default_dns_zone")

    @default_dns_zone.setter
    def default_dns_zone(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "default_dns_zone", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        Display name of the DNS Service.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)

    @property
    @pulumi.getter(name="dnsServiceId")
    def dns_service_id(self) -> Optional[pulumi.Input[str]]:
        """
        NSX DNS Service identifier. Generally the same as the DNS Service's display name
        """
        return pulumi.get(self, "dns_service_id")

    @dns_service_id.setter
    def dns_service_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_service_id", value)

    @property
    @pulumi.getter(name="dnsServiceIp")
    def dns_service_ip(self) -> Optional[pulumi.Input[str]]:
        """
        DNS service IP of the DNS Service.
        """
        return pulumi.get(self, "dns_service_ip")

    @dns_service_ip.setter
    def dns_service_ip(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "dns_service_ip", value)

    @property
    @pulumi.getter(name="fqdnZones")
    def fqdn_zones(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        FQDN zones of the DNS Service.
        """
        return pulumi.get(self, "fqdn_zones")

    @fqdn_zones.setter
    def fqdn_zones(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "fqdn_zones", value)

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> Optional[pulumi.Input[Union[str, 'DnsServiceLogLevelEnum']]]:
        """
        DNS Service log level.
        """
        return pulumi.get(self, "log_level")

    @log_level.setter
    def log_level(self, value: Optional[pulumi.Input[Union[str, 'DnsServiceLogLevelEnum']]]):
        pulumi.set(self, "log_level", value)

    @property
    @pulumi.getter
    def revision(self) -> Optional[pulumi.Input[float]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @revision.setter
    def revision(self, value: Optional[pulumi.Input[float]]):
        pulumi.set(self, "revision", value)


class WorkloadNetworkDnsService(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_dns_zone: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_service_id: Optional[pulumi.Input[str]] = None,
                 dns_service_ip: Optional[pulumi.Input[str]] = None,
                 fqdn_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 log_level: Optional[pulumi.Input[Union[str, 'DnsServiceLogLevelEnum']]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        """
        NSX DNS Service
        API Version: 2020-07-17-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] default_dns_zone: Default DNS zone of the DNS Service.
        :param pulumi.Input[str] display_name: Display name of the DNS Service.
        :param pulumi.Input[str] dns_service_id: NSX DNS Service identifier. Generally the same as the DNS Service's display name
        :param pulumi.Input[str] dns_service_ip: DNS service IP of the DNS Service.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] fqdn_zones: FQDN zones of the DNS Service.
        :param pulumi.Input[Union[str, 'DnsServiceLogLevelEnum']] log_level: DNS Service log level.
        :param pulumi.Input[str] private_cloud_name: Name of the private cloud
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[float] revision: NSX revision number.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: WorkloadNetworkDnsServiceArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        NSX DNS Service
        API Version: 2020-07-17-preview.

        :param str resource_name: The name of the resource.
        :param WorkloadNetworkDnsServiceArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(WorkloadNetworkDnsServiceArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 default_dns_zone: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None,
                 dns_service_id: Optional[pulumi.Input[str]] = None,
                 dns_service_ip: Optional[pulumi.Input[str]] = None,
                 fqdn_zones: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 log_level: Optional[pulumi.Input[Union[str, 'DnsServiceLogLevelEnum']]] = None,
                 private_cloud_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 revision: Optional[pulumi.Input[float]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = WorkloadNetworkDnsServiceArgs.__new__(WorkloadNetworkDnsServiceArgs)

            __props__.__dict__["default_dns_zone"] = default_dns_zone
            __props__.__dict__["display_name"] = display_name
            __props__.__dict__["dns_service_id"] = dns_service_id
            __props__.__dict__["dns_service_ip"] = dns_service_ip
            __props__.__dict__["fqdn_zones"] = fqdn_zones
            __props__.__dict__["log_level"] = log_level
            if private_cloud_name is None and not opts.urn:
                raise TypeError("Missing required property 'private_cloud_name'")
            __props__.__dict__["private_cloud_name"] = private_cloud_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["revision"] = revision
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["status"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:avs/v20200717preview:WorkloadNetworkDnsService"), pulumi.Alias(type_="azure-native:avs/v20210101preview:WorkloadNetworkDnsService"), pulumi.Alias(type_="azure-native:avs/v20210601:WorkloadNetworkDnsService"), pulumi.Alias(type_="azure-native:avs/v20211201:WorkloadNetworkDnsService"), pulumi.Alias(type_="azure-native:avs/v20220501:WorkloadNetworkDnsService")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(WorkloadNetworkDnsService, __self__).__init__(
            'azure-native:avs:WorkloadNetworkDnsService',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'WorkloadNetworkDnsService':
        """
        Get an existing WorkloadNetworkDnsService resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = WorkloadNetworkDnsServiceArgs.__new__(WorkloadNetworkDnsServiceArgs)

        __props__.__dict__["default_dns_zone"] = None
        __props__.__dict__["display_name"] = None
        __props__.__dict__["dns_service_ip"] = None
        __props__.__dict__["fqdn_zones"] = None
        __props__.__dict__["log_level"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["revision"] = None
        __props__.__dict__["status"] = None
        __props__.__dict__["type"] = None
        return WorkloadNetworkDnsService(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="defaultDnsZone")
    def default_dns_zone(self) -> pulumi.Output[Optional[str]]:
        """
        Default DNS zone of the DNS Service.
        """
        return pulumi.get(self, "default_dns_zone")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> pulumi.Output[Optional[str]]:
        """
        Display name of the DNS Service.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="dnsServiceIp")
    def dns_service_ip(self) -> pulumi.Output[Optional[str]]:
        """
        DNS service IP of the DNS Service.
        """
        return pulumi.get(self, "dns_service_ip")

    @property
    @pulumi.getter(name="fqdnZones")
    def fqdn_zones(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        FQDN zones of the DNS Service.
        """
        return pulumi.get(self, "fqdn_zones")

    @property
    @pulumi.getter(name="logLevel")
    def log_level(self) -> pulumi.Output[Optional[str]]:
        """
        DNS Service log level.
        """
        return pulumi.get(self, "log_level")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def revision(self) -> pulumi.Output[Optional[float]]:
        """
        NSX revision number.
        """
        return pulumi.get(self, "revision")

    @property
    @pulumi.getter
    def status(self) -> pulumi.Output[str]:
        """
        DNS Service status.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

