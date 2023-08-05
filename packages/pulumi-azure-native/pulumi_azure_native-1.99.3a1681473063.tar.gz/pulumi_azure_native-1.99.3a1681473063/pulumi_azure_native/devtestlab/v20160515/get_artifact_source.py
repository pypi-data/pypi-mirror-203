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
    'GetArtifactSourceResult',
    'AwaitableGetArtifactSourceResult',
    'get_artifact_source',
    'get_artifact_source_output',
]

warnings.warn("""Version 2016-05-15 will be removed in v2 of the provider.""", DeprecationWarning)

@pulumi.output_type
class GetArtifactSourceResult:
    """
    Properties of an artifact source.
    """
    def __init__(__self__, arm_template_folder_path=None, branch_ref=None, created_date=None, display_name=None, folder_path=None, id=None, location=None, name=None, provisioning_state=None, security_token=None, source_type=None, status=None, tags=None, type=None, unique_identifier=None, uri=None):
        if arm_template_folder_path and not isinstance(arm_template_folder_path, str):
            raise TypeError("Expected argument 'arm_template_folder_path' to be a str")
        pulumi.set(__self__, "arm_template_folder_path", arm_template_folder_path)
        if branch_ref and not isinstance(branch_ref, str):
            raise TypeError("Expected argument 'branch_ref' to be a str")
        pulumi.set(__self__, "branch_ref", branch_ref)
        if created_date and not isinstance(created_date, str):
            raise TypeError("Expected argument 'created_date' to be a str")
        pulumi.set(__self__, "created_date", created_date)
        if display_name and not isinstance(display_name, str):
            raise TypeError("Expected argument 'display_name' to be a str")
        pulumi.set(__self__, "display_name", display_name)
        if folder_path and not isinstance(folder_path, str):
            raise TypeError("Expected argument 'folder_path' to be a str")
        pulumi.set(__self__, "folder_path", folder_path)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if security_token and not isinstance(security_token, str):
            raise TypeError("Expected argument 'security_token' to be a str")
        pulumi.set(__self__, "security_token", security_token)
        if source_type and not isinstance(source_type, str):
            raise TypeError("Expected argument 'source_type' to be a str")
        pulumi.set(__self__, "source_type", source_type)
        if status and not isinstance(status, str):
            raise TypeError("Expected argument 'status' to be a str")
        pulumi.set(__self__, "status", status)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if unique_identifier and not isinstance(unique_identifier, str):
            raise TypeError("Expected argument 'unique_identifier' to be a str")
        pulumi.set(__self__, "unique_identifier", unique_identifier)
        if uri and not isinstance(uri, str):
            raise TypeError("Expected argument 'uri' to be a str")
        pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="armTemplateFolderPath")
    def arm_template_folder_path(self) -> Optional[str]:
        """
        The folder containing Azure Resource Manager templates.
        """
        return pulumi.get(self, "arm_template_folder_path")

    @property
    @pulumi.getter(name="branchRef")
    def branch_ref(self) -> Optional[str]:
        """
        The artifact source's branch reference.
        """
        return pulumi.get(self, "branch_ref")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> str:
        """
        The artifact source's creation date.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The artifact source's display name.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter(name="folderPath")
    def folder_path(self) -> Optional[str]:
        """
        The folder containing artifacts.
        """
        return pulumi.get(self, "folder_path")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The identifier of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        The location of the resource.
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
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> Optional[str]:
        """
        The provisioning status of the resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="securityToken")
    def security_token(self) -> Optional[str]:
        """
        The security token to authenticate to the artifact source.
        """
        return pulumi.get(self, "security_token")

    @property
    @pulumi.getter(name="sourceType")
    def source_type(self) -> Optional[str]:
        """
        The artifact source's type.
        """
        return pulumi.get(self, "source_type")

    @property
    @pulumi.getter
    def status(self) -> Optional[str]:
        """
        Indicates if the artifact source is enabled (values: Enabled, Disabled).
        """
        return pulumi.get(self, "status")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        The tags of the resource.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="uniqueIdentifier")
    def unique_identifier(self) -> Optional[str]:
        """
        The unique immutable identifier of a resource (Guid).
        """
        return pulumi.get(self, "unique_identifier")

    @property
    @pulumi.getter
    def uri(self) -> Optional[str]:
        """
        The artifact source's URI.
        """
        return pulumi.get(self, "uri")


class AwaitableGetArtifactSourceResult(GetArtifactSourceResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetArtifactSourceResult(
            arm_template_folder_path=self.arm_template_folder_path,
            branch_ref=self.branch_ref,
            created_date=self.created_date,
            display_name=self.display_name,
            folder_path=self.folder_path,
            id=self.id,
            location=self.location,
            name=self.name,
            provisioning_state=self.provisioning_state,
            security_token=self.security_token,
            source_type=self.source_type,
            status=self.status,
            tags=self.tags,
            type=self.type,
            unique_identifier=self.unique_identifier,
            uri=self.uri)


def get_artifact_source(expand: Optional[str] = None,
                        lab_name: Optional[str] = None,
                        name: Optional[str] = None,
                        resource_group_name: Optional[str] = None,
                        opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetArtifactSourceResult:
    """
    Get artifact source.


    :param str expand: Specify the $expand query. Example: 'properties($select=displayName)'
    :param str lab_name: The name of the lab.
    :param str name: The name of the artifact source.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_artifact_source is deprecated: Version 2016-05-15 will be removed in v2 of the provider.""")
    __args__ = dict()
    __args__['expand'] = expand
    __args__['labName'] = lab_name
    __args__['name'] = name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:devtestlab/v20160515:getArtifactSource', __args__, opts=opts, typ=GetArtifactSourceResult).value

    return AwaitableGetArtifactSourceResult(
        arm_template_folder_path=__ret__.arm_template_folder_path,
        branch_ref=__ret__.branch_ref,
        created_date=__ret__.created_date,
        display_name=__ret__.display_name,
        folder_path=__ret__.folder_path,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        provisioning_state=__ret__.provisioning_state,
        security_token=__ret__.security_token,
        source_type=__ret__.source_type,
        status=__ret__.status,
        tags=__ret__.tags,
        type=__ret__.type,
        unique_identifier=__ret__.unique_identifier,
        uri=__ret__.uri)


@_utilities.lift_output_func(get_artifact_source)
def get_artifact_source_output(expand: Optional[pulumi.Input[Optional[str]]] = None,
                               lab_name: Optional[pulumi.Input[str]] = None,
                               name: Optional[pulumi.Input[str]] = None,
                               resource_group_name: Optional[pulumi.Input[str]] = None,
                               opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetArtifactSourceResult]:
    """
    Get artifact source.


    :param str expand: Specify the $expand query. Example: 'properties($select=displayName)'
    :param str lab_name: The name of the lab.
    :param str name: The name of the artifact source.
    :param str resource_group_name: The name of the resource group.
    """
    pulumi.log.warn("""get_artifact_source is deprecated: Version 2016-05-15 will be removed in v2 of the provider.""")
    ...
