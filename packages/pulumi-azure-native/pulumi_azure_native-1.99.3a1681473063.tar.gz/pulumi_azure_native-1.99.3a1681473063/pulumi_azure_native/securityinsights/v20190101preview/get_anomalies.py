# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = [
    'GetAnomaliesResult',
    'AwaitableGetAnomaliesResult',
    'get_anomalies',
    'get_anomalies_output',
]

@pulumi.output_type
class GetAnomaliesResult:
    """
    Settings with single toggle.
    """
    def __init__(__self__, etag=None, id=None, is_enabled=None, kind=None, name=None, type=None):
        if etag and not isinstance(etag, str):
            raise TypeError("Expected argument 'etag' to be a str")
        pulumi.set(__self__, "etag", etag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if is_enabled and not isinstance(is_enabled, bool):
            raise TypeError("Expected argument 'is_enabled' to be a bool")
        pulumi.set(__self__, "is_enabled", is_enabled)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        Etag of the azure resource
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="isEnabled")
    def is_enabled(self) -> bool:
        """
        Determines whether the setting is enable or disabled.
        """
        return pulumi.get(self, "is_enabled")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """

        Expected value is 'Anomalies'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetAnomaliesResult(GetAnomaliesResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAnomaliesResult(
            etag=self.etag,
            id=self.id,
            is_enabled=self.is_enabled,
            kind=self.kind,
            name=self.name,
            type=self.type)


def get_anomalies(operational_insights_resource_provider: Optional[str] = None,
                  resource_group_name: Optional[str] = None,
                  settings_name: Optional[str] = None,
                  workspace_name: Optional[str] = None,
                  opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAnomaliesResult:
    """
    Gets a setting.


    :param str operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str settings_name: The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['operationalInsightsResourceProvider'] = operational_insights_resource_provider
    __args__['resourceGroupName'] = resource_group_name
    __args__['settingsName'] = settings_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20190101preview:getAnomalies', __args__, opts=opts, typ=GetAnomaliesResult).value

    return AwaitableGetAnomaliesResult(
        etag=__ret__.etag,
        id=__ret__.id,
        is_enabled=__ret__.is_enabled,
        kind=__ret__.kind,
        name=__ret__.name,
        type=__ret__.type)


@_utilities.lift_output_func(get_anomalies)
def get_anomalies_output(operational_insights_resource_provider: Optional[pulumi.Input[str]] = None,
                         resource_group_name: Optional[pulumi.Input[str]] = None,
                         settings_name: Optional[pulumi.Input[str]] = None,
                         workspace_name: Optional[pulumi.Input[str]] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAnomaliesResult]:
    """
    Gets a setting.


    :param str operational_insights_resource_provider: The namespace of workspaces resource provider- Microsoft.OperationalInsights.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    :param str settings_name: The setting name. Supports - Anomalies, EyesOn, EntityAnalytics, Ueba
    :param str workspace_name: The name of the workspace.
    """
    ...
