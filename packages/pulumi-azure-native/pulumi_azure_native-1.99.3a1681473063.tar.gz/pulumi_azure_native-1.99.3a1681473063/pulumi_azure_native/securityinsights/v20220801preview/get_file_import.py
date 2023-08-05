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
    'GetFileImportResult',
    'AwaitableGetFileImportResult',
    'get_file_import',
    'get_file_import_output',
]

@pulumi.output_type
class GetFileImportResult:
    """
    Represents a file import in Azure Security Insights.
    """
    def __init__(__self__, content_type=None, created_time_utc=None, error_file=None, errors_preview=None, files_valid_until_time_utc=None, id=None, import_file=None, import_valid_until_time_utc=None, ingested_record_count=None, ingestion_mode=None, name=None, source=None, state=None, system_data=None, total_record_count=None, type=None, valid_record_count=None):
        if content_type and not isinstance(content_type, str):
            raise TypeError("Expected argument 'content_type' to be a str")
        pulumi.set(__self__, "content_type", content_type)
        if created_time_utc and not isinstance(created_time_utc, str):
            raise TypeError("Expected argument 'created_time_utc' to be a str")
        pulumi.set(__self__, "created_time_utc", created_time_utc)
        if error_file and not isinstance(error_file, dict):
            raise TypeError("Expected argument 'error_file' to be a dict")
        pulumi.set(__self__, "error_file", error_file)
        if errors_preview and not isinstance(errors_preview, list):
            raise TypeError("Expected argument 'errors_preview' to be a list")
        pulumi.set(__self__, "errors_preview", errors_preview)
        if files_valid_until_time_utc and not isinstance(files_valid_until_time_utc, str):
            raise TypeError("Expected argument 'files_valid_until_time_utc' to be a str")
        pulumi.set(__self__, "files_valid_until_time_utc", files_valid_until_time_utc)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if import_file and not isinstance(import_file, dict):
            raise TypeError("Expected argument 'import_file' to be a dict")
        pulumi.set(__self__, "import_file", import_file)
        if import_valid_until_time_utc and not isinstance(import_valid_until_time_utc, str):
            raise TypeError("Expected argument 'import_valid_until_time_utc' to be a str")
        pulumi.set(__self__, "import_valid_until_time_utc", import_valid_until_time_utc)
        if ingested_record_count and not isinstance(ingested_record_count, int):
            raise TypeError("Expected argument 'ingested_record_count' to be a int")
        pulumi.set(__self__, "ingested_record_count", ingested_record_count)
        if ingestion_mode and not isinstance(ingestion_mode, str):
            raise TypeError("Expected argument 'ingestion_mode' to be a str")
        pulumi.set(__self__, "ingestion_mode", ingestion_mode)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if source and not isinstance(source, str):
            raise TypeError("Expected argument 'source' to be a str")
        pulumi.set(__self__, "source", source)
        if state and not isinstance(state, str):
            raise TypeError("Expected argument 'state' to be a str")
        pulumi.set(__self__, "state", state)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if total_record_count and not isinstance(total_record_count, int):
            raise TypeError("Expected argument 'total_record_count' to be a int")
        pulumi.set(__self__, "total_record_count", total_record_count)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if valid_record_count and not isinstance(valid_record_count, int):
            raise TypeError("Expected argument 'valid_record_count' to be a int")
        pulumi.set(__self__, "valid_record_count", valid_record_count)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> str:
        """
        The content type of this file.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="createdTimeUTC")
    def created_time_utc(self) -> str:
        """
        The time the file was imported.
        """
        return pulumi.get(self, "created_time_utc")

    @property
    @pulumi.getter(name="errorFile")
    def error_file(self) -> 'outputs.FileMetadataResponse':
        """
        Represents the error file (if the import was ingested with errors or failed the validation).
        """
        return pulumi.get(self, "error_file")

    @property
    @pulumi.getter(name="errorsPreview")
    def errors_preview(self) -> Sequence['outputs.ValidationErrorResponse']:
        """
        An ordered list of some of the errors that were encountered during validation.
        """
        return pulumi.get(self, "errors_preview")

    @property
    @pulumi.getter(name="filesValidUntilTimeUTC")
    def files_valid_until_time_utc(self) -> str:
        """
        The time the files associated with this import are deleted from the storage account.
        """
        return pulumi.get(self, "files_valid_until_time_utc")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource ID for the resource. Ex - /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="importFile")
    def import_file(self) -> 'outputs.FileMetadataResponse':
        """
        Represents the imported file.
        """
        return pulumi.get(self, "import_file")

    @property
    @pulumi.getter(name="importValidUntilTimeUTC")
    def import_valid_until_time_utc(self) -> str:
        """
        The time the file import record is soft deleted from the database and history.
        """
        return pulumi.get(self, "import_valid_until_time_utc")

    @property
    @pulumi.getter(name="ingestedRecordCount")
    def ingested_record_count(self) -> int:
        """
        The number of records that have been successfully ingested.
        """
        return pulumi.get(self, "ingested_record_count")

    @property
    @pulumi.getter(name="ingestionMode")
    def ingestion_mode(self) -> str:
        """
        Describes how to ingest the records in the file.
        """
        return pulumi.get(self, "ingestion_mode")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def source(self) -> str:
        """
        The source for the data in the file.
        """
        return pulumi.get(self, "source")

    @property
    @pulumi.getter
    def state(self) -> str:
        """
        The state of the file import.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Azure Resource Manager metadata containing createdBy and modifiedBy information.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter(name="totalRecordCount")
    def total_record_count(self) -> int:
        """
        The number of records in the file.
        """
        return pulumi.get(self, "total_record_count")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="validRecordCount")
    def valid_record_count(self) -> int:
        """
        The number of records that have passed validation.
        """
        return pulumi.get(self, "valid_record_count")


class AwaitableGetFileImportResult(GetFileImportResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetFileImportResult(
            content_type=self.content_type,
            created_time_utc=self.created_time_utc,
            error_file=self.error_file,
            errors_preview=self.errors_preview,
            files_valid_until_time_utc=self.files_valid_until_time_utc,
            id=self.id,
            import_file=self.import_file,
            import_valid_until_time_utc=self.import_valid_until_time_utc,
            ingested_record_count=self.ingested_record_count,
            ingestion_mode=self.ingestion_mode,
            name=self.name,
            source=self.source,
            state=self.state,
            system_data=self.system_data,
            total_record_count=self.total_record_count,
            type=self.type,
            valid_record_count=self.valid_record_count)


def get_file_import(file_import_id: Optional[str] = None,
                    resource_group_name: Optional[str] = None,
                    workspace_name: Optional[str] = None,
                    opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetFileImportResult:
    """
    Gets a file import.


    :param str file_import_id: File import ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    __args__ = dict()
    __args__['fileImportId'] = file_import_id
    __args__['resourceGroupName'] = resource_group_name
    __args__['workspaceName'] = workspace_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:securityinsights/v20220801preview:getFileImport', __args__, opts=opts, typ=GetFileImportResult).value

    return AwaitableGetFileImportResult(
        content_type=__ret__.content_type,
        created_time_utc=__ret__.created_time_utc,
        error_file=__ret__.error_file,
        errors_preview=__ret__.errors_preview,
        files_valid_until_time_utc=__ret__.files_valid_until_time_utc,
        id=__ret__.id,
        import_file=__ret__.import_file,
        import_valid_until_time_utc=__ret__.import_valid_until_time_utc,
        ingested_record_count=__ret__.ingested_record_count,
        ingestion_mode=__ret__.ingestion_mode,
        name=__ret__.name,
        source=__ret__.source,
        state=__ret__.state,
        system_data=__ret__.system_data,
        total_record_count=__ret__.total_record_count,
        type=__ret__.type,
        valid_record_count=__ret__.valid_record_count)


@_utilities.lift_output_func(get_file_import)
def get_file_import_output(file_import_id: Optional[pulumi.Input[str]] = None,
                           resource_group_name: Optional[pulumi.Input[str]] = None,
                           workspace_name: Optional[pulumi.Input[str]] = None,
                           opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetFileImportResult]:
    """
    Gets a file import.


    :param str file_import_id: File import ID
    :param str resource_group_name: The name of the resource group. The name is case insensitive.
    :param str workspace_name: The name of the workspace.
    """
    ...
