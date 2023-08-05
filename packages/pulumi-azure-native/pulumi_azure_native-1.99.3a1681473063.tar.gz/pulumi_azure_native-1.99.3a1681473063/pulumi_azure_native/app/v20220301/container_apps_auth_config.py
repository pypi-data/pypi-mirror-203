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

__all__ = ['ContainerAppsAuthConfigArgs', 'ContainerAppsAuthConfig']

@pulumi.input_type
class ContainerAppsAuthConfigArgs:
    def __init__(__self__, *,
                 container_app_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 auth_config_name: Optional[pulumi.Input[str]] = None,
                 global_validation: Optional[pulumi.Input['GlobalValidationArgs']] = None,
                 http_settings: Optional[pulumi.Input['HttpSettingsArgs']] = None,
                 identity_providers: Optional[pulumi.Input['IdentityProvidersArgs']] = None,
                 login: Optional[pulumi.Input['LoginArgs']] = None,
                 platform: Optional[pulumi.Input['AuthPlatformArgs']] = None):
        """
        The set of arguments for constructing a ContainerAppsAuthConfig resource.
        :param pulumi.Input[str] container_app_name: Name of the Container App.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] auth_config_name: Name of the Container App AuthConfig.
        :param pulumi.Input['GlobalValidationArgs'] global_validation: The configuration settings that determines the validation flow of users using  Service Authentication/Authorization.
        :param pulumi.Input['HttpSettingsArgs'] http_settings: The configuration settings of the HTTP requests for authentication and authorization requests made against ContainerApp Service Authentication/Authorization.
        :param pulumi.Input['IdentityProvidersArgs'] identity_providers: The configuration settings of each of the identity providers used to configure ContainerApp Service Authentication/Authorization.
        :param pulumi.Input['LoginArgs'] login: The configuration settings of the login flow of users using ContainerApp Service Authentication/Authorization.
        :param pulumi.Input['AuthPlatformArgs'] platform: The configuration settings of the platform of ContainerApp Service Authentication/Authorization.
        """
        pulumi.set(__self__, "container_app_name", container_app_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auth_config_name is not None:
            pulumi.set(__self__, "auth_config_name", auth_config_name)
        if global_validation is not None:
            pulumi.set(__self__, "global_validation", global_validation)
        if http_settings is not None:
            pulumi.set(__self__, "http_settings", http_settings)
        if identity_providers is not None:
            pulumi.set(__self__, "identity_providers", identity_providers)
        if login is not None:
            pulumi.set(__self__, "login", login)
        if platform is not None:
            pulumi.set(__self__, "platform", platform)

    @property
    @pulumi.getter(name="containerAppName")
    def container_app_name(self) -> pulumi.Input[str]:
        """
        Name of the Container App.
        """
        return pulumi.get(self, "container_app_name")

    @container_app_name.setter
    def container_app_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "container_app_name", value)

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
    @pulumi.getter(name="authConfigName")
    def auth_config_name(self) -> Optional[pulumi.Input[str]]:
        """
        Name of the Container App AuthConfig.
        """
        return pulumi.get(self, "auth_config_name")

    @auth_config_name.setter
    def auth_config_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "auth_config_name", value)

    @property
    @pulumi.getter(name="globalValidation")
    def global_validation(self) -> Optional[pulumi.Input['GlobalValidationArgs']]:
        """
        The configuration settings that determines the validation flow of users using  Service Authentication/Authorization.
        """
        return pulumi.get(self, "global_validation")

    @global_validation.setter
    def global_validation(self, value: Optional[pulumi.Input['GlobalValidationArgs']]):
        pulumi.set(self, "global_validation", value)

    @property
    @pulumi.getter(name="httpSettings")
    def http_settings(self) -> Optional[pulumi.Input['HttpSettingsArgs']]:
        """
        The configuration settings of the HTTP requests for authentication and authorization requests made against ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "http_settings")

    @http_settings.setter
    def http_settings(self, value: Optional[pulumi.Input['HttpSettingsArgs']]):
        pulumi.set(self, "http_settings", value)

    @property
    @pulumi.getter(name="identityProviders")
    def identity_providers(self) -> Optional[pulumi.Input['IdentityProvidersArgs']]:
        """
        The configuration settings of each of the identity providers used to configure ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "identity_providers")

    @identity_providers.setter
    def identity_providers(self, value: Optional[pulumi.Input['IdentityProvidersArgs']]):
        pulumi.set(self, "identity_providers", value)

    @property
    @pulumi.getter
    def login(self) -> Optional[pulumi.Input['LoginArgs']]:
        """
        The configuration settings of the login flow of users using ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "login")

    @login.setter
    def login(self, value: Optional[pulumi.Input['LoginArgs']]):
        pulumi.set(self, "login", value)

    @property
    @pulumi.getter
    def platform(self) -> Optional[pulumi.Input['AuthPlatformArgs']]:
        """
        The configuration settings of the platform of ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "platform")

    @platform.setter
    def platform(self, value: Optional[pulumi.Input['AuthPlatformArgs']]):
        pulumi.set(self, "platform", value)


class ContainerAppsAuthConfig(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_config_name: Optional[pulumi.Input[str]] = None,
                 container_app_name: Optional[pulumi.Input[str]] = None,
                 global_validation: Optional[pulumi.Input[pulumi.InputType['GlobalValidationArgs']]] = None,
                 http_settings: Optional[pulumi.Input[pulumi.InputType['HttpSettingsArgs']]] = None,
                 identity_providers: Optional[pulumi.Input[pulumi.InputType['IdentityProvidersArgs']]] = None,
                 login: Optional[pulumi.Input[pulumi.InputType['LoginArgs']]] = None,
                 platform: Optional[pulumi.Input[pulumi.InputType['AuthPlatformArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Configuration settings for the Azure ContainerApp Service Authentication / Authorization feature.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] auth_config_name: Name of the Container App AuthConfig.
        :param pulumi.Input[str] container_app_name: Name of the Container App.
        :param pulumi.Input[pulumi.InputType['GlobalValidationArgs']] global_validation: The configuration settings that determines the validation flow of users using  Service Authentication/Authorization.
        :param pulumi.Input[pulumi.InputType['HttpSettingsArgs']] http_settings: The configuration settings of the HTTP requests for authentication and authorization requests made against ContainerApp Service Authentication/Authorization.
        :param pulumi.Input[pulumi.InputType['IdentityProvidersArgs']] identity_providers: The configuration settings of each of the identity providers used to configure ContainerApp Service Authentication/Authorization.
        :param pulumi.Input[pulumi.InputType['LoginArgs']] login: The configuration settings of the login flow of users using ContainerApp Service Authentication/Authorization.
        :param pulumi.Input[pulumi.InputType['AuthPlatformArgs']] platform: The configuration settings of the platform of ContainerApp Service Authentication/Authorization.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ContainerAppsAuthConfigArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Configuration settings for the Azure ContainerApp Service Authentication / Authorization feature.

        :param str resource_name: The name of the resource.
        :param ContainerAppsAuthConfigArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ContainerAppsAuthConfigArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 auth_config_name: Optional[pulumi.Input[str]] = None,
                 container_app_name: Optional[pulumi.Input[str]] = None,
                 global_validation: Optional[pulumi.Input[pulumi.InputType['GlobalValidationArgs']]] = None,
                 http_settings: Optional[pulumi.Input[pulumi.InputType['HttpSettingsArgs']]] = None,
                 identity_providers: Optional[pulumi.Input[pulumi.InputType['IdentityProvidersArgs']]] = None,
                 login: Optional[pulumi.Input[pulumi.InputType['LoginArgs']]] = None,
                 platform: Optional[pulumi.Input[pulumi.InputType['AuthPlatformArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ContainerAppsAuthConfigArgs.__new__(ContainerAppsAuthConfigArgs)

            __props__.__dict__["auth_config_name"] = auth_config_name
            if container_app_name is None and not opts.urn:
                raise TypeError("Missing required property 'container_app_name'")
            __props__.__dict__["container_app_name"] = container_app_name
            __props__.__dict__["global_validation"] = global_validation
            __props__.__dict__["http_settings"] = http_settings
            __props__.__dict__["identity_providers"] = identity_providers
            __props__.__dict__["login"] = login
            __props__.__dict__["platform"] = platform
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:app:ContainerAppsAuthConfig"), pulumi.Alias(type_="azure-native:app/v20220101preview:ContainerAppsAuthConfig"), pulumi.Alias(type_="azure-native:app/v20220601preview:ContainerAppsAuthConfig"), pulumi.Alias(type_="azure-native:app/v20221001:ContainerAppsAuthConfig")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ContainerAppsAuthConfig, __self__).__init__(
            'azure-native:app/v20220301:ContainerAppsAuthConfig',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ContainerAppsAuthConfig':
        """
        Get an existing ContainerAppsAuthConfig resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ContainerAppsAuthConfigArgs.__new__(ContainerAppsAuthConfigArgs)

        __props__.__dict__["global_validation"] = None
        __props__.__dict__["http_settings"] = None
        __props__.__dict__["identity_providers"] = None
        __props__.__dict__["login"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["platform"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return ContainerAppsAuthConfig(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="globalValidation")
    def global_validation(self) -> pulumi.Output[Optional['outputs.GlobalValidationResponse']]:
        """
        The configuration settings that determines the validation flow of users using  Service Authentication/Authorization.
        """
        return pulumi.get(self, "global_validation")

    @property
    @pulumi.getter(name="httpSettings")
    def http_settings(self) -> pulumi.Output[Optional['outputs.HttpSettingsResponse']]:
        """
        The configuration settings of the HTTP requests for authentication and authorization requests made against ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "http_settings")

    @property
    @pulumi.getter(name="identityProviders")
    def identity_providers(self) -> pulumi.Output[Optional['outputs.IdentityProvidersResponse']]:
        """
        The configuration settings of each of the identity providers used to configure ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "identity_providers")

    @property
    @pulumi.getter
    def login(self) -> pulumi.Output[Optional['outputs.LoginResponse']]:
        """
        The configuration settings of the login flow of users using ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "login")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def platform(self) -> pulumi.Output[Optional['outputs.AuthPlatformResponse']]:
        """
        The configuration settings of the platform of ContainerApp Service Authentication/Authorization.
        """
        return pulumi.get(self, "platform")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

