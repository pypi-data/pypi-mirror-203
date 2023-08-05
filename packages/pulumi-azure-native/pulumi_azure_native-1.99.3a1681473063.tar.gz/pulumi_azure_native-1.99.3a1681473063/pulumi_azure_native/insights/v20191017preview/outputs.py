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
    'PrivateEndpointConnectionResponse',
    'PrivateEndpointPropertyResponse',
    'PrivateLinkServiceConnectionStatePropertyResponse',
    'WorkbookTemplateGalleryResponse',
    'WorkbookTemplateLocalizedGalleryResponse',
]

@pulumi.output_type
class PrivateEndpointConnectionResponse(dict):
    """
    A private endpoint connection
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "provisioningState":
            suggest = "provisioning_state"
        elif key == "privateEndpoint":
            suggest = "private_endpoint"
        elif key == "privateLinkServiceConnectionState":
            suggest = "private_link_service_connection_state"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateEndpointConnectionResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateEndpointConnectionResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 id: str,
                 name: str,
                 provisioning_state: str,
                 type: str,
                 private_endpoint: Optional['outputs.PrivateEndpointPropertyResponse'] = None,
                 private_link_service_connection_state: Optional['outputs.PrivateLinkServiceConnectionStatePropertyResponse'] = None):
        """
        A private endpoint connection
        :param str id: Azure resource Id
        :param str name: Azure resource name
        :param str provisioning_state: State of the private endpoint connection.
        :param str type: Azure resource type
        :param 'PrivateEndpointPropertyResponse' private_endpoint: Private endpoint which the connection belongs to.
        :param 'PrivateLinkServiceConnectionStatePropertyResponse' private_link_service_connection_state: Connection state of the private endpoint connection.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        pulumi.set(__self__, "type", type)
        if private_endpoint is not None:
            pulumi.set(__self__, "private_endpoint", private_endpoint)
        if private_link_service_connection_state is not None:
            pulumi.set(__self__, "private_link_service_connection_state", private_link_service_connection_state)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Azure resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Azure resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        State of the private endpoint connection.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Azure resource type
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="privateEndpoint")
    def private_endpoint(self) -> Optional['outputs.PrivateEndpointPropertyResponse']:
        """
        Private endpoint which the connection belongs to.
        """
        return pulumi.get(self, "private_endpoint")

    @property
    @pulumi.getter(name="privateLinkServiceConnectionState")
    def private_link_service_connection_state(self) -> Optional['outputs.PrivateLinkServiceConnectionStatePropertyResponse']:
        """
        Connection state of the private endpoint connection.
        """
        return pulumi.get(self, "private_link_service_connection_state")


@pulumi.output_type
class PrivateEndpointPropertyResponse(dict):
    """
    Private endpoint which the connection belongs to.
    """
    def __init__(__self__, *,
                 id: Optional[str] = None):
        """
        Private endpoint which the connection belongs to.
        :param str id: Resource id of the private endpoint.
        """
        if id is not None:
            pulumi.set(__self__, "id", id)

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        Resource id of the private endpoint.
        """
        return pulumi.get(self, "id")


@pulumi.output_type
class PrivateLinkServiceConnectionStatePropertyResponse(dict):
    """
    State of the private endpoint connection.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "actionsRequired":
            suggest = "actions_required"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in PrivateLinkServiceConnectionStatePropertyResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        PrivateLinkServiceConnectionStatePropertyResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        PrivateLinkServiceConnectionStatePropertyResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 actions_required: str,
                 description: str,
                 status: str):
        """
        State of the private endpoint connection.
        :param str actions_required: The actions required for private link service connection.
        :param str description: The private link service connection description.
        :param str status: The private link service connection status.
        """
        pulumi.set(__self__, "actions_required", actions_required)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "status", status)

    @property
    @pulumi.getter(name="actionsRequired")
    def actions_required(self) -> str:
        """
        The actions required for private link service connection.
        """
        return pulumi.get(self, "actions_required")

    @property
    @pulumi.getter
    def description(self) -> str:
        """
        The private link service connection description.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def status(self) -> str:
        """
        The private link service connection status.
        """
        return pulumi.get(self, "status")


@pulumi.output_type
class WorkbookTemplateGalleryResponse(dict):
    """
    Gallery information for a workbook template.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "resourceType":
            suggest = "resource_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkbookTemplateGalleryResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkbookTemplateGalleryResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkbookTemplateGalleryResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 category: Optional[str] = None,
                 name: Optional[str] = None,
                 order: Optional[int] = None,
                 resource_type: Optional[str] = None,
                 type: Optional[str] = None):
        """
        Gallery information for a workbook template.
        :param str category: Category for the gallery.
        :param str name: Name of the workbook template in the gallery.
        :param int order: Order of the template within the gallery.
        :param str resource_type: Azure resource type supported by the gallery.
        :param str type: Type of workbook supported by the workbook template.
        """
        if category is not None:
            pulumi.set(__self__, "category", category)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if order is not None:
            pulumi.set(__self__, "order", order)
        if resource_type is not None:
            pulumi.set(__self__, "resource_type", resource_type)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def category(self) -> Optional[str]:
        """
        Category for the gallery.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Name of the workbook template in the gallery.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def order(self) -> Optional[int]:
        """
        Order of the template within the gallery.
        """
        return pulumi.get(self, "order")

    @property
    @pulumi.getter(name="resourceType")
    def resource_type(self) -> Optional[str]:
        """
        Azure resource type supported by the gallery.
        """
        return pulumi.get(self, "resource_type")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Type of workbook supported by the workbook template.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class WorkbookTemplateLocalizedGalleryResponse(dict):
    """
    Localized template data and gallery information.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "templateData":
            suggest = "template_data"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in WorkbookTemplateLocalizedGalleryResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        WorkbookTemplateLocalizedGalleryResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        WorkbookTemplateLocalizedGalleryResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 galleries: Optional[Sequence['outputs.WorkbookTemplateGalleryResponse']] = None,
                 template_data: Optional[Any] = None):
        """
        Localized template data and gallery information.
        :param Sequence['WorkbookTemplateGalleryResponse'] galleries: Workbook galleries supported by the template.
        :param Any template_data: Valid JSON object containing workbook template payload.
        """
        if galleries is not None:
            pulumi.set(__self__, "galleries", galleries)
        if template_data is not None:
            pulumi.set(__self__, "template_data", template_data)

    @property
    @pulumi.getter
    def galleries(self) -> Optional[Sequence['outputs.WorkbookTemplateGalleryResponse']]:
        """
        Workbook galleries supported by the template.
        """
        return pulumi.get(self, "galleries")

    @property
    @pulumi.getter(name="templateData")
    def template_data(self) -> Optional[Any]:
        """
        Valid JSON object containing workbook template payload.
        """
        return pulumi.get(self, "template_data")


