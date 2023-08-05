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
    'GetAzurePowerShellScriptResult',
    'AwaitableGetAzurePowerShellScriptResult',
    'get_azure_power_shell_script',
    'get_azure_power_shell_script_output',
]

@pulumi.output_type
class GetAzurePowerShellScriptResult:
    """
    Object model for the Azure PowerShell script.
    """
    def __init__(__self__, arguments=None, az_power_shell_version=None, cleanup_preference=None, container_settings=None, environment_variables=None, force_update_tag=None, id=None, identity=None, kind=None, location=None, name=None, outputs=None, primary_script_uri=None, provisioning_state=None, retention_interval=None, script_content=None, status=None, storage_account_settings=None, supporting_script_uris=None, system_data=None, tags=None, timeout=None, type=None):
        if arguments and not isinstance(arguments, str):
            raise TypeError("Expected argument 'arguments' to be a str")
        pulumi.set(__self__, "arguments", arguments)
        if az_power_shell_version and not isinstance(az_power_shell_version, str):
            raise TypeError("Expected argument 'az_power_shell_version' to be a str")
        pulumi.set(__self__, "az_power_shell_version", az_power_shell_version)
        if cleanup_preference and not isinstance(cleanup_preference, str):
            raise TypeError("Expected argument 'cleanup_preference' to be a str")
        pulumi.set(__self__, "cleanup_preference", cleanup_preference)
        if container_settings and not isinstance(container_settings, dict):
            raise TypeError("Expected argument 'container_settings' to be a dict")
        pulumi.set(__self__, "container_settings", container_settings)
        if environment_variables and not isinstance(environment_variables, list):
            raise TypeError("Expected argument 'environment_variables' to be a list")
        pulumi.set(__self__, "environment_variables", environment_variables)
        if force_update_tag and not isinstance(force_update_tag, str):
            raise TypeError("Expected argument 'force_update_tag' to be a str")
        pulumi.set(__self__, "force_update_tag", force_update_tag)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if kind and not isinstance(kind, str):
            raise TypeError("Expected argument 'kind' to be a str")
        pulumi.set(__self__, "kind", kind)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if outputs and not isinstance(outputs, dict):
            raise TypeError("Expected argument 'outputs' to be a dict")
        pulumi.set(__self__, "outputs", outputs)
        if primary_script_uri and not isinstance(primary_script_uri, str):
            raise TypeError("Expected argument 'primary_script_uri' to be a str")
        pulumi.set(__self__, "primary_script_uri", primary_script_uri)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if retention_interval and not isinstance(retention_interval, str):
            raise TypeError("Expected argument 'retention_interval' to be a str")
        pulumi.set(__self__, "retention_interval", retention_interval)
        if script_content and not isinstance(script_content, str):
            raise TypeError("Expected argument 'script_content' to be a str")
        pulumi.set(__self__, "script_content", script_content)
        if status and not isinstance(status, dict):
            raise TypeError("Expected argument 'status' to be a dict")
        pulumi.set(__self__, "status", status)
        if storage_account_settings and not isinstance(storage_account_settings, dict):
            raise TypeError("Expected argument 'storage_account_settings' to be a dict")
        pulumi.set(__self__, "storage_account_settings", storage_account_settings)
        if supporting_script_uris and not isinstance(supporting_script_uris, list):
            raise TypeError("Expected argument 'supporting_script_uris' to be a list")
        pulumi.set(__self__, "supporting_script_uris", supporting_script_uris)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if timeout and not isinstance(timeout, str):
            raise TypeError("Expected argument 'timeout' to be a str")
        pulumi.set(__self__, "timeout", timeout)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def arguments(self) -> Optional[str]:
        """
        Command line arguments to pass to the script. Arguments are separated by spaces. ex: -Name blue* -Location 'West US 2' 
        """
        return pulumi.get(self, "arguments")

    @property
    @pulumi.getter(name="azPowerShellVersion")
    def az_power_shell_version(self) -> str:
        """
        Azure PowerShell module version to be used.
        """
        return pulumi.get(self, "az_power_shell_version")

    @property
    @pulumi.getter(name="cleanupPreference")
    def cleanup_preference(self) -> Optional[str]:
        """
        The clean up preference when the script execution gets in a terminal state. Default setting is 'Always'.
        """
        return pulumi.get(self, "cleanup_preference")

    @property
    @pulumi.getter(name="containerSettings")
    def container_settings(self) -> Optional['outputs.ContainerConfigurationResponse']:
        """
        Container settings.
        """
        return pulumi.get(self, "container_settings")

    @property
    @pulumi.getter(name="environmentVariables")
    def environment_variables(self) -> Optional[Sequence['outputs.EnvironmentVariableResponse']]:
        """
        The environment variables to pass over to the script.
        """
        return pulumi.get(self, "environment_variables")

    @property
    @pulumi.getter(name="forceUpdateTag")
    def force_update_tag(self) -> Optional[str]:
        """
        Gets or sets how the deployment script should be forced to execute even if the script resource has not changed. Can be current time stamp or a GUID.
        """
        return pulumi.get(self, "force_update_tag")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        String Id used to locate any resource on Azure.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.ManagedServiceIdentityResponse']:
        """
        Optional property. Managed identity to be used for this deployment script. Currently, only user-assigned MSI is supported.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def kind(self) -> str:
        """
        Type of the script.
        Expected value is 'AzurePowerShell'.
        """
        return pulumi.get(self, "kind")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        The location of the ACI and the storage account for the deployment script.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of this resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def outputs(self) -> Mapping[str, Any]:
        """
        List of script outputs.
        """
        return pulumi.get(self, "outputs")

    @property
    @pulumi.getter(name="primaryScriptUri")
    def primary_script_uri(self) -> Optional[str]:
        """
        Uri for the script. This is the entry point for the external script.
        """
        return pulumi.get(self, "primary_script_uri")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the script execution. This only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="retentionInterval")
    def retention_interval(self) -> str:
        """
        Interval for which the service retains the script resource after it reaches a terminal state. Resource will be deleted when this duration expires. Duration is based on ISO 8601 pattern (for example P1D means one day).
        """
        return pulumi.get(self, "retention_interval")

    @property
    @pulumi.getter(name="scriptContent")
    def script_content(self) -> Optional[str]:
        """
        Script body.
        """
        return pulumi.get(self, "script_content")

    @property
    @pulumi.getter
    def status(self) -> 'outputs.ScriptStatusResponse':
        """
        Contains the results of script execution.
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter(name="storageAccountSettings")
    def storage_account_settings(self) -> Optional['outputs.StorageAccountConfigurationResponse']:
        """
        Storage Account settings.
        """
        return pulumi.get(self, "storage_account_settings")

    @property
    @pulumi.getter(name="supportingScriptUris")
    def supporting_script_uris(self) -> Optional[Sequence[str]]:
        """
        Supporting files for the external script.
        """
        return pulumi.get(self, "supporting_script_uris")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata related to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def timeout(self) -> Optional[str]:
        """
        Maximum allowed script execution time specified in ISO 8601 format. Default value is P1D
        """
        return pulumi.get(self, "timeout")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of this resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetAzurePowerShellScriptResult(GetAzurePowerShellScriptResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAzurePowerShellScriptResult(
            arguments=self.arguments,
            az_power_shell_version=self.az_power_shell_version,
            cleanup_preference=self.cleanup_preference,
            container_settings=self.container_settings,
            environment_variables=self.environment_variables,
            force_update_tag=self.force_update_tag,
            id=self.id,
            identity=self.identity,
            kind=self.kind,
            location=self.location,
            name=self.name,
            outputs=self.outputs,
            primary_script_uri=self.primary_script_uri,
            provisioning_state=self.provisioning_state,
            retention_interval=self.retention_interval,
            script_content=self.script_content,
            status=self.status,
            storage_account_settings=self.storage_account_settings,
            supporting_script_uris=self.supporting_script_uris,
            system_data=self.system_data,
            tags=self.tags,
            timeout=self.timeout,
            type=self.type)


def get_azure_power_shell_script(resource_group_name: Optional[str] = None,
                                 script_name: Optional[str] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAzurePowerShellScriptResult:
    """
    Gets a deployment script with a given name.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str script_name: Name of the deployment script.
    """
    __args__ = dict()
    __args__['resourceGroupName'] = resource_group_name
    __args__['scriptName'] = script_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:resources/v20201001:getAzurePowerShellScript', __args__, opts=opts, typ=GetAzurePowerShellScriptResult).value

    return AwaitableGetAzurePowerShellScriptResult(
        arguments=__ret__.arguments,
        az_power_shell_version=__ret__.az_power_shell_version,
        cleanup_preference=__ret__.cleanup_preference,
        container_settings=__ret__.container_settings,
        environment_variables=__ret__.environment_variables,
        force_update_tag=__ret__.force_update_tag,
        id=__ret__.id,
        identity=__ret__.identity,
        kind=__ret__.kind,
        location=__ret__.location,
        name=__ret__.name,
        outputs=__ret__.outputs,
        primary_script_uri=__ret__.primary_script_uri,
        provisioning_state=__ret__.provisioning_state,
        retention_interval=__ret__.retention_interval,
        script_content=__ret__.script_content,
        status=__ret__.status,
        storage_account_settings=__ret__.storage_account_settings,
        supporting_script_uris=__ret__.supporting_script_uris,
        system_data=__ret__.system_data,
        tags=__ret__.tags,
        timeout=__ret__.timeout,
        type=__ret__.type)


@_utilities.lift_output_func(get_azure_power_shell_script)
def get_azure_power_shell_script_output(resource_group_name: Optional[pulumi.Input[str]] = None,
                                        script_name: Optional[pulumi.Input[str]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAzurePowerShellScriptResult]:
    """
    Gets a deployment script with a given name.


    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str script_name: Name of the deployment script.
    """
    ...
