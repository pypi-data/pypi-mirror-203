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
    'ListApplianceClusterUserCredentialResult',
    'AwaitableListApplianceClusterUserCredentialResult',
    'list_appliance_cluster_user_credential',
    'list_appliance_cluster_user_credential_output',
]

@pulumi.output_type
class ListApplianceClusterUserCredentialResult:
    """
    The List Cluster User Credential appliance.
    """
    def __init__(__self__, hybrid_connection_config=None, kubeconfigs=None):
        if hybrid_connection_config and not isinstance(hybrid_connection_config, dict):
            raise TypeError("Expected argument 'hybrid_connection_config' to be a dict")
        pulumi.set(__self__, "hybrid_connection_config", hybrid_connection_config)
        if kubeconfigs and not isinstance(kubeconfigs, list):
            raise TypeError("Expected argument 'kubeconfigs' to be a list")
        pulumi.set(__self__, "kubeconfigs", kubeconfigs)

    @property
    @pulumi.getter(name="hybridConnectionConfig")
    def hybrid_connection_config(self) -> 'outputs.HybridConnectionConfigResponse':
        """
        Contains the REP (rendezvous endpoint) and “Listener” access token from notification service (NS).
        """
        return pulumi.get(self, "hybrid_connection_config")

    @property
    @pulumi.getter
    def kubeconfigs(self) -> Sequence['outputs.ApplianceCredentialKubeconfigResponse']:
        """
        The list of appliance kubeconfigs.
        """
        return pulumi.get(self, "kubeconfigs")


class AwaitableListApplianceClusterUserCredentialResult(ListApplianceClusterUserCredentialResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListApplianceClusterUserCredentialResult(
            hybrid_connection_config=self.hybrid_connection_config,
            kubeconfigs=self.kubeconfigs)


def list_appliance_cluster_user_credential(resource_group_name: Optional[str] = None,
                                           resource_name: Optional[str] = None,
                                           opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListApplianceClusterUserCredentialResult:
    """
    Returns the cluster user credentials for the dedicated appliance.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: Appliances name.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['resourceName'] = resource_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:resourceconnector/v20221027:listApplianceClusterUserCredential', __args__, opts=opts, typ=ListApplianceClusterUserCredentialResult).value

    return AwaitableListApplianceClusterUserCredentialResult(
        hybrid_connection_config=__ret__.hybrid_connection_config,
        kubeconfigs=__ret__.kubeconfigs)


@_utilities.lift_output_func(list_appliance_cluster_user_credential)
def list_appliance_cluster_user_credential_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                                  resource_name: Optional[pulumi.Input[str]] = None,
                                                  opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListApplianceClusterUserCredentialResult]:
    """
    Returns the cluster user credentials for the dedicated appliance.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str resource_name: Appliances name.
    """
    ...
