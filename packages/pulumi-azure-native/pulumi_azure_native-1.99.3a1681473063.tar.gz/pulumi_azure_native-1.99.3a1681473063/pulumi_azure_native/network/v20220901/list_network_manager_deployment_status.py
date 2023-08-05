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

__all__ = [
    'ListNetworkManagerDeploymentStatusResult',
    'AwaitableListNetworkManagerDeploymentStatusResult',
    'list_network_manager_deployment_status',
    'list_network_manager_deployment_status_output',
]

@pulumi.output_type
class ListNetworkManagerDeploymentStatusResult:
    """
    A list of Network Manager Deployment Status
    """
    def __init__(__self__, skip_token=None, value=None):
        if skip_token and not isinstance(skip_token, str):
            raise TypeError("Expected argument 'skip_token' to be a str")
        pulumi.set(__self__, "skip_token", skip_token)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="skipToken")
    def skip_token(self) -> Optional[str]:
        """
        When present, the value can be passed to a subsequent query call (together with the same query and scopes used in the current request) to retrieve the next page of data.
        """
        return pulumi.get(self, "skip_token")

    @property
    @pulumi.getter
    def value(self) -> Optional[Sequence['outputs.NetworkManagerDeploymentStatusResponse']]:
        """
        Gets a page of Network Manager Deployment Status
        """
        return pulumi.get(self, "value")


class AwaitableListNetworkManagerDeploymentStatusResult(ListNetworkManagerDeploymentStatusResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListNetworkManagerDeploymentStatusResult(
            skip_token=self.skip_token,
            value=self.value)


def list_network_manager_deployment_status(deployment_types: Optional[Sequence[Union[str, 'ConfigurationType']]] = None,
                                           network_manager_name: Optional[str] = None,
                                           regions: Optional[Sequence[str]] = None,
                                           resource_group_name: Optional[str] = None,
                                           skip_token: Optional[str] = None,
                                           top: Optional[int] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListNetworkManagerDeploymentStatusResult:
    """
    Post to List of Network Manager Deployment Status.


    :param Sequence[Union[str, 'ConfigurationType']] deployment_types: List of deployment types.
    :param str network_manager_name: The name of the network manager.
    :param Sequence[str] regions: List of locations.
    :param str resource_group_name: The name of the resource group.
    :param str skip_token: Continuation token for pagination, capturing the next page size and offset, as well as the context of the query.
    :param int top: An optional query parameter which specifies the maximum number of records to be returned by the server.
    """
    __args__ = dict()
    __args__['deploymentTypes'] = deployment_types
    __args__['networkManagerName'] = network_manager_name
    __args__['regions'] = regions
    __args__['resourceGroupName'] = resource_group_name
    __args__['skipToken'] = skip_token
    __args__['top'] = top
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:network/v20220901:listNetworkManagerDeploymentStatus', __args__, opts=opts, typ=ListNetworkManagerDeploymentStatusResult).value

    return AwaitableListNetworkManagerDeploymentStatusResult(
        skip_token=__ret__.skip_token,
        value=__ret__.value)


@_utilities.lift_output_func(list_network_manager_deployment_status)
def list_network_manager_deployment_status_output(deployment_types: Optional[pulumi.Input[Optional[Sequence[Union[str, 'ConfigurationType']]]]] = None,
                                                  network_manager_name: Optional[pulumi.Input[str]] = None,
                                                  regions: Optional[pulumi.Input[Optional[Sequence[str]]]] = None,
                                                  resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  skip_token: Optional[pulumi.Input[Optional[str]]] = None,
                                                  top: Optional[pulumi.Input[Optional[int]]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListNetworkManagerDeploymentStatusResult]:
    """
    Post to List of Network Manager Deployment Status.


    :param Sequence[Union[str, 'ConfigurationType']] deployment_types: List of deployment types.
    :param str network_manager_name: The name of the network manager.
    :param Sequence[str] regions: List of locations.
    :param str resource_group_name: The name of the resource group.
    :param str skip_token: Continuation token for pagination, capturing the next page size and offset, as well as the context of the query.
    :param int top: An optional query parameter which specifies the maximum number of records to be returned by the server.
    """
    ...
