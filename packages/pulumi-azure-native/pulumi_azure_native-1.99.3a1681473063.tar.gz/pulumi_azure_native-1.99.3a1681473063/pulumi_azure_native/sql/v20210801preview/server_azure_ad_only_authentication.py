# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['ServerAzureADOnlyAuthenticationArgs', 'ServerAzureADOnlyAuthentication']

@pulumi.input_type
class ServerAzureADOnlyAuthenticationArgs:
    def __init__(__self__, *,
                 azure_ad_only_authentication: pulumi.Input[bool],
                 resource_group_name: pulumi.Input[str],
                 server_name: pulumi.Input[str],
                 authentication_name: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a ServerAzureADOnlyAuthentication resource.
        :param pulumi.Input[bool] azure_ad_only_authentication: Azure Active Directory only Authentication enabled.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        :param pulumi.Input[str] authentication_name: The name of server azure active directory only authentication.
        """
        pulumi.set(__self__, "azure_ad_only_authentication", azure_ad_only_authentication)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "server_name", server_name)
        if authentication_name is not None:
            pulumi.set(__self__, "authentication_name", authentication_name)

    @property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> pulumi.Input[bool]:
        """
        Azure Active Directory only Authentication enabled.
        """
        return pulumi.get(self, "azure_ad_only_authentication")

    @azure_ad_only_authentication.setter
    def azure_ad_only_authentication(self, value: pulumi.Input[bool]):
        pulumi.set(self, "azure_ad_only_authentication", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serverName")
    def server_name(self) -> pulumi.Input[str]:
        """
        The name of the server.
        """
        return pulumi.get(self, "server_name")

    @server_name.setter
    def server_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "server_name", value)

    @property
    @pulumi.getter(name="authenticationName")
    def authentication_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of server azure active directory only authentication.
        """
        return pulumi.get(self, "authentication_name")

    @authentication_name.setter
    def authentication_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "authentication_name", value)


class ServerAzureADOnlyAuthentication(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_name: Optional[pulumi.Input[str]] = None,
                 azure_ad_only_authentication: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Azure Active Directory only authentication.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] authentication_name: The name of server azure active directory only authentication.
        :param pulumi.Input[bool] azure_ad_only_authentication: Azure Active Directory only Authentication enabled.
        :param pulumi.Input[str] resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
        :param pulumi.Input[str] server_name: The name of the server.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ServerAzureADOnlyAuthenticationArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Azure Active Directory only authentication.

        :param str resource_name: The name of the resource.
        :param ServerAzureADOnlyAuthenticationArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ServerAzureADOnlyAuthenticationArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 authentication_name: Optional[pulumi.Input[str]] = None,
                 azure_ad_only_authentication: Optional[pulumi.Input[bool]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 server_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ServerAzureADOnlyAuthenticationArgs.__new__(ServerAzureADOnlyAuthenticationArgs)

            __props__.__dict__["authentication_name"] = authentication_name
            if azure_ad_only_authentication is None and not opts.urn:
                raise TypeError("Missing required property 'azure_ad_only_authentication'")
            __props__.__dict__["azure_ad_only_authentication"] = azure_ad_only_authentication
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if server_name is None and not opts.urn:
                raise TypeError("Missing required property 'server_name'")
            __props__.__dict__["server_name"] = server_name
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:sql:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20200202preview:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20200801preview:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20201101preview:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20210201preview:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20210501preview:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20211101:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20211101preview:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20220201preview:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20220501preview:ServerAzureADOnlyAuthentication"), pulumi.Alias(type_="azure-native:sql/v20220801preview:ServerAzureADOnlyAuthentication")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ServerAzureADOnlyAuthentication, __self__).__init__(
            'azure-native:sql/v20210801preview:ServerAzureADOnlyAuthentication',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ServerAzureADOnlyAuthentication':
        """
        Get an existing ServerAzureADOnlyAuthentication resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ServerAzureADOnlyAuthenticationArgs.__new__(ServerAzureADOnlyAuthenticationArgs)

        __props__.__dict__["azure_ad_only_authentication"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["type"] = None
        return ServerAzureADOnlyAuthentication(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="azureADOnlyAuthentication")
    def azure_ad_only_authentication(self) -> pulumi.Output[bool]:
        """
        Azure Active Directory only Authentication enabled.
        """
        return pulumi.get(self, "azure_ad_only_authentication")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

