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
    'AuthorizationInfoArgs',
    'AzureDevOpsConnectorPropertiesArgs',
    'AzureDevOpsOrgMetadataArgs',
    'AzureDevOpsProjectMetadataArgs',
    'GitHubConnectorPropertiesArgs',
]

@pulumi.input_type
class AuthorizationInfoArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] code: Gets or sets one-time OAuth code to exchange for refresh and access tokens.
               
               Only used during PUT operations. The secret is cleared during GET.
               In general, RPaaS does not return any property marked as a secret.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets one-time OAuth code to exchange for refresh and access tokens.
        
        Only used during PUT operations. The secret is cleared during GET.
        In general, RPaaS does not return any property marked as a secret.
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code", value)


@pulumi.input_type
class AzureDevOpsConnectorPropertiesArgs:
    def __init__(__self__, *,
                 authorization: Optional[pulumi.Input['AuthorizationInfoArgs']] = None,
                 orgs: Optional[pulumi.Input[Sequence[pulumi.Input['AzureDevOpsOrgMetadataArgs']]]] = None):
        """
        :param pulumi.Input[Sequence[pulumi.Input['AzureDevOpsOrgMetadataArgs']]] orgs: Gets or sets org onboarding information.
        """
        if authorization is not None:
            pulumi.set(__self__, "authorization", authorization)
        if orgs is not None:
            pulumi.set(__self__, "orgs", orgs)

    @property
    @pulumi.getter
    def authorization(self) -> Optional[pulumi.Input['AuthorizationInfoArgs']]:
        return pulumi.get(self, "authorization")

    @authorization.setter
    def authorization(self, value: Optional[pulumi.Input['AuthorizationInfoArgs']]):
        pulumi.set(self, "authorization", value)

    @property
    @pulumi.getter
    def orgs(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureDevOpsOrgMetadataArgs']]]]:
        """
        Gets or sets org onboarding information.
        """
        return pulumi.get(self, "orgs")

    @orgs.setter
    def orgs(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureDevOpsOrgMetadataArgs']]]]):
        pulumi.set(self, "orgs", value)


@pulumi.input_type
class AzureDevOpsOrgMetadataArgs:
    def __init__(__self__, *,
                 auto_discovery: Optional[pulumi.Input[Union[str, 'AutoDiscovery']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 projects: Optional[pulumi.Input[Sequence[pulumi.Input['AzureDevOpsProjectMetadataArgs']]]] = None):
        """
        Org onboarding info.
        :param pulumi.Input[str] name: Gets or sets name of the AzureDevOps Org.
        """
        if auto_discovery is not None:
            pulumi.set(__self__, "auto_discovery", auto_discovery)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if projects is not None:
            pulumi.set(__self__, "projects", projects)

    @property
    @pulumi.getter(name="autoDiscovery")
    def auto_discovery(self) -> Optional[pulumi.Input[Union[str, 'AutoDiscovery']]]:
        return pulumi.get(self, "auto_discovery")

    @auto_discovery.setter
    def auto_discovery(self, value: Optional[pulumi.Input[Union[str, 'AutoDiscovery']]]):
        pulumi.set(self, "auto_discovery", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets name of the AzureDevOps Org.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def projects(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['AzureDevOpsProjectMetadataArgs']]]]:
        return pulumi.get(self, "projects")

    @projects.setter
    def projects(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['AzureDevOpsProjectMetadataArgs']]]]):
        pulumi.set(self, "projects", value)


@pulumi.input_type
class AzureDevOpsProjectMetadataArgs:
    def __init__(__self__, *,
                 auto_discovery: Optional[pulumi.Input[Union[str, 'AutoDiscovery']]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 repos: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Project onboarding info.
        :param pulumi.Input[str] name: Gets or sets name of the AzureDevOps Project.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] repos: Gets or sets repositories.
        """
        if auto_discovery is not None:
            pulumi.set(__self__, "auto_discovery", auto_discovery)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if repos is not None:
            pulumi.set(__self__, "repos", repos)

    @property
    @pulumi.getter(name="autoDiscovery")
    def auto_discovery(self) -> Optional[pulumi.Input[Union[str, 'AutoDiscovery']]]:
        return pulumi.get(self, "auto_discovery")

    @auto_discovery.setter
    def auto_discovery(self, value: Optional[pulumi.Input[Union[str, 'AutoDiscovery']]]):
        pulumi.set(self, "auto_discovery", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets name of the AzureDevOps Project.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def repos(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        Gets or sets repositories.
        """
        return pulumi.get(self, "repos")

    @repos.setter
    def repos(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "repos", value)


@pulumi.input_type
class GitHubConnectorPropertiesArgs:
    def __init__(__self__, *,
                 code: Optional[pulumi.Input[str]] = None):
        """
        Properties of the ARM resource for /subscriptions/xxx/resourceGroups/xxx/providers/Microsoft.SecurityDevOps/gitHubConnectors.
        :param pulumi.Input[str] code: Gets or sets one-time OAuth code to exchange for refresh and access tokens.
               
               Only used during PUT operations. The secret is cleared during GET.
               In general, RPaaS does not return any property marked as a secret.
        """
        if code is not None:
            pulumi.set(__self__, "code", code)

    @property
    @pulumi.getter
    def code(self) -> Optional[pulumi.Input[str]]:
        """
        Gets or sets one-time OAuth code to exchange for refresh and access tokens.
        
        Only used during PUT operations. The secret is cleared during GET.
        In general, RPaaS does not return any property marked as a secret.
        """
        return pulumi.get(self, "code")

    @code.setter
    def code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "code", value)


