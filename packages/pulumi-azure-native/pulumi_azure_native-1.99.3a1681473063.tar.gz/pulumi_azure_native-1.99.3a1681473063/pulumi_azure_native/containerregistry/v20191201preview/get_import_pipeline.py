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
    'GetImportPipelineResult',
    'AwaitableGetImportPipelineResult',
    'get_import_pipeline',
    'get_import_pipeline_output',
]

@pulumi.output_type
class GetImportPipelineResult:
    """
    An object that represents an import pipeline for a container registry.
    """
    def __init__(__self__, id=None, identity=None, location=None, name=None, options=None, provisioning_state=None, source=None, system_data=None, trigger=None, type=None):
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identity and not isinstance(identity, dict):
            raise TypeError("Expected argument 'identity' to be a dict")
        pulumi.set(__self__, "identity", identity)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if options and not isinstance(options, list):
            raise TypeError("Expected argument 'options' to be a list")
        pulumi.set(__self__, "options", options)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if source and not isinstance(source, dict):
            raise TypeError("Expected argument 'source' to be a dict")
        pulumi.set(__self__, "source", source)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if trigger and not isinstance(trigger, dict):
            raise TypeError("Expected argument 'trigger' to be a dict")
        pulumi.set(__self__, "trigger", trigger)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identity(self) -> Optional['outputs.IdentityPropertiesResponse']:
        """
        The identity of the import pipeline.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the import pipeline.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def options(self) -> Optional[Sequence[str]]:
        """
        The list of all options configured for the pipeline.
        """
        return pulumi.get(self, "options")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state of the pipeline at the time the operation was called.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def source(self) -> 'outputs.ImportPipelineSourcePropertiesResponse':
        """
        The source properties of the import pipeline.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def trigger(self) -> Optional['outputs.PipelineTriggerPropertiesResponse']:
        """
        The properties that describe the trigger of the import pipeline.
        """
        return pulumi.get(self, "trigger")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")


class AwaitableGetImportPipelineResult(GetImportPipelineResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetImportPipelineResult(
            id=self.id,
            identity=self.identity,
            location=self.location,
            name=self.name,
            options=self.options,
            provisioning_state=self.provisioning_state,
            source=self.source,
            system_data=self.system_data,
            trigger=self.trigger,
            type=self.type)


def get_import_pipeline(import_pipeline_name: Optional[str] = None,
                        registry_name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetImportPipelineResult:
    """
    Gets the properties of the import pipeline.


    :param str import_pipeline_name: The name of the import pipeline.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    __args__ = dict()
    __args__['importPipelineName'] = import_pipeline_name
    __args__['registryName'] = registry_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:containerregistry/v20191201preview:getImportPipeline', __args__, opts=opts, typ=GetImportPipelineResult).value

    return AwaitableGetImportPipelineResult(
        id=__ret__.id,
        identity=__ret__.identity,
        location=__ret__.location,
        name=__ret__.name,
        options=__ret__.options,
        provisioning_state=__ret__.provisioning_state,
        source=__ret__.source,
        system_data=__ret__.system_data,
        trigger=__ret__.trigger,
        type=__ret__.type)


@_utilities.lift_output_func(get_import_pipeline)
def get_import_pipeline_output(import_pipeline_name: Optional[pulumi.Input[str]] = None,
                               registry_name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetImportPipelineResult]:
    """
    Gets the properties of the import pipeline.


    :param str import_pipeline_name: The name of the import pipeline.
    :param str registry_name: The name of the container registry.
    :param str resource_group_name: The name of the resource group to which the container registry belongs.
    """
    ...
