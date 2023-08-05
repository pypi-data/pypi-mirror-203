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
    'CompatibilityResponse',
    'DataDiskImageResponse',
    'IconUrisResponse',
    'OsDiskImageResponse',
    'ProductLinkResponse',
    'ProductPropertiesResponse',
    'ProductResponse',
    'SystemDataResponse',
]

@pulumi.output_type
class CompatibilityResponse(dict):
    """
    Product compatibility
    """
    def __init__(__self__, *,
                 description: Optional[str] = None,
                 is_compatible: Optional[bool] = None,
                 issues: Optional[Sequence[str]] = None,
                 message: Optional[str] = None):
        """
        Product compatibility
        :param str description: Full error message if any compatibility issues are found
        :param bool is_compatible: Tells if product is compatible with current device
        :param Sequence[str] issues: List of all issues found
        :param str message: Short error message if any compatibility issues are found
        """
        if description is not None:
            pulumi.set(__self__, "description", description)
        if is_compatible is not None:
            pulumi.set(__self__, "is_compatible", is_compatible)
        if issues is not None:
            pulumi.set(__self__, "issues", issues)
        if message is not None:
            pulumi.set(__self__, "message", message)

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        Full error message if any compatibility issues are found
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="isCompatible")
    def is_compatible(self) -> Optional[bool]:
        """
        Tells if product is compatible with current device
        """
        return pulumi.get(self, "is_compatible")

    @property
    @pulumi.getter
    def issues(self) -> Optional[Sequence[str]]:
        """
        List of all issues found
        """
        return pulumi.get(self, "issues")

    @property
    @pulumi.getter
    def message(self) -> Optional[str]:
        """
        Short error message if any compatibility issues are found
        """
        return pulumi.get(self, "message")


@pulumi.output_type
class DataDiskImageResponse(dict):
    """
    Data disk image.
    """
    def __init__(__self__, *,
                 lun: int,
                 source_blob_sas_uri: str):
        """
        Data disk image.
        :param int lun: The LUN.
        :param str source_blob_sas_uri: SAS key for source blob.
        """
        pulumi.set(__self__, "lun", lun)
        pulumi.set(__self__, "source_blob_sas_uri", source_blob_sas_uri)

    @property
    @pulumi.getter
    def lun(self) -> int:
        """
        The LUN.
        """
        return pulumi.get(self, "lun")

    @property
    @pulumi.getter(name="sourceBlobSasUri")
    def source_blob_sas_uri(self) -> str:
        """
        SAS key for source blob.
        """
        return pulumi.get(self, "source_blob_sas_uri")


@pulumi.output_type
class IconUrisResponse(dict):
    """
    Links to product icons.
    """
    def __init__(__self__, *,
                 hero: Optional[str] = None,
                 large: Optional[str] = None,
                 medium: Optional[str] = None,
                 small: Optional[str] = None,
                 wide: Optional[str] = None):
        """
        Links to product icons.
        :param str hero: URI to hero icon.
        :param str large: URI to large icon.
        :param str medium: URI to medium icon.
        :param str small: URI to small icon.
        :param str wide: URI to wide icon.
        """
        if hero is not None:
            pulumi.set(__self__, "hero", hero)
        if large is not None:
            pulumi.set(__self__, "large", large)
        if medium is not None:
            pulumi.set(__self__, "medium", medium)
        if small is not None:
            pulumi.set(__self__, "small", small)
        if wide is not None:
            pulumi.set(__self__, "wide", wide)

    @property
    @pulumi.getter
    def hero(self) -> Optional[str]:
        """
        URI to hero icon.
        """
        return pulumi.get(self, "hero")

    @property
    @pulumi.getter
    def large(self) -> Optional[str]:
        """
        URI to large icon.
        """
        return pulumi.get(self, "large")

    @property
    @pulumi.getter
    def medium(self) -> Optional[str]:
        """
        URI to medium icon.
        """
        return pulumi.get(self, "medium")

    @property
    @pulumi.getter
    def small(self) -> Optional[str]:
        """
        URI to small icon.
        """
        return pulumi.get(self, "small")

    @property
    @pulumi.getter
    def wide(self) -> Optional[str]:
        """
        URI to wide icon.
        """
        return pulumi.get(self, "wide")


@pulumi.output_type
class OsDiskImageResponse(dict):
    """
    OS disk image.
    """
    def __init__(__self__, *,
                 operating_system: str,
                 source_blob_sas_uri: str):
        """
        OS disk image.
        :param str operating_system: OS operating system type.
        :param str source_blob_sas_uri: SAS key for source blob.
        """
        pulumi.set(__self__, "operating_system", operating_system)
        pulumi.set(__self__, "source_blob_sas_uri", source_blob_sas_uri)

    @property
    @pulumi.getter(name="operatingSystem")
    def operating_system(self) -> str:
        """
        OS operating system type.
        """
        return pulumi.get(self, "operating_system")

    @property
    @pulumi.getter(name="sourceBlobSasUri")
    def source_blob_sas_uri(self) -> str:
        """
        SAS key for source blob.
        """
        return pulumi.get(self, "source_blob_sas_uri")


@pulumi.output_type
class ProductLinkResponse(dict):
    """
    Link with additional information about a product.
    """
    def __init__(__self__, *,
                 display_name: Optional[str] = None,
                 uri: Optional[str] = None):
        """
        Link with additional information about a product.
        :param str display_name: The description of the link.
        :param str uri: The URI corresponding to the link.
        """
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if uri is not None:
            pulumi.set(__self__, "uri", uri)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The description of the link.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def uri(self) -> Optional[str]:
        """
        The URI corresponding to the link.
        """
        return pulumi.get(self, "uri")


@pulumi.output_type
class ProductPropertiesResponse(dict):
    """
    Additional properties of the product
    """
    def __init__(__self__, *,
                 version: Optional[str] = None):
        """
        Additional properties of the product
        :param str version: The version.
        """
        if version is not None:
            pulumi.set(__self__, "version", version)

    @property
    @pulumi.getter
    def version(self) -> Optional[str]:
        """
        The version.
        """
        return pulumi.get(self, "version")


@pulumi.output_type
class ProductResponse(dict):
    """
    Product information.
    """
    def __init__(__self__, *,
                 id: str,
                 name: str,
                 system_data: 'outputs.SystemDataResponse',
                 type: str,
                 billing_part_number: Optional[str] = None,
                 compatibility: Optional['outputs.CompatibilityResponse'] = None,
                 description: Optional[str] = None,
                 display_name: Optional[str] = None,
                 etag: Optional[str] = None,
                 gallery_item_identity: Optional[str] = None,
                 icon_uris: Optional['outputs.IconUrisResponse'] = None,
                 legal_terms: Optional[str] = None,
                 links: Optional[Sequence['outputs.ProductLinkResponse']] = None,
                 offer: Optional[str] = None,
                 offer_version: Optional[str] = None,
                 payload_length: Optional[float] = None,
                 privacy_policy: Optional[str] = None,
                 product_kind: Optional[str] = None,
                 product_properties: Optional['outputs.ProductPropertiesResponse'] = None,
                 publisher_display_name: Optional[str] = None,
                 publisher_identifier: Optional[str] = None,
                 sku: Optional[str] = None,
                 vm_extension_type: Optional[str] = None):
        """
        Product information.
        :param str id: ID of the resource.
        :param str name: Name of the resource.
        :param 'SystemDataResponse' system_data: Metadata pertaining to creation and last modification of the resource.
        :param str type: Type of Resource.
        :param str billing_part_number: The part number used for billing purposes.
        :param 'CompatibilityResponse' compatibility: Product compatibility with current device.
        :param str description: The description of the product.
        :param str display_name: The display name of the product.
        :param str etag: The entity tag used for optimistic concurrency when modifying the resource.
        :param str gallery_item_identity: The identifier of the gallery item corresponding to the product.
        :param 'IconUrisResponse' icon_uris: Additional links available for this product.
        :param str legal_terms: The legal terms.
        :param Sequence['ProductLinkResponse'] links: Additional links available for this product.
        :param str offer: The offer representing the product.
        :param str offer_version: The version of the product offer.
        :param float payload_length: The length of product content.
        :param str privacy_policy: The privacy policy.
        :param str product_kind: The kind of the product (virtualMachine or virtualMachineExtension)
        :param 'ProductPropertiesResponse' product_properties: Additional properties for the product.
        :param str publisher_display_name: The user-friendly name of the product publisher.
        :param str publisher_identifier: Publisher identifier.
        :param str sku: The product SKU.
        :param str vm_extension_type: The type of the Virtual Machine Extension.
        """
        pulumi.set(__self__, "id", id)
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "system_data", system_data)
        pulumi.set(__self__, "type", type)
        if billing_part_number is not None:
            pulumi.set(__self__, "billing_part_number", billing_part_number)
        if compatibility is not None:
            pulumi.set(__self__, "compatibility", compatibility)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)
        if etag is not None:
            pulumi.set(__self__, "etag", etag)
        if gallery_item_identity is not None:
            pulumi.set(__self__, "gallery_item_identity", gallery_item_identity)
        if icon_uris is not None:
            pulumi.set(__self__, "icon_uris", icon_uris)
        if legal_terms is not None:
            pulumi.set(__self__, "legal_terms", legal_terms)
        if links is not None:
            pulumi.set(__self__, "links", links)
        if offer is not None:
            pulumi.set(__self__, "offer", offer)
        if offer_version is not None:
            pulumi.set(__self__, "offer_version", offer_version)
        if payload_length is not None:
            pulumi.set(__self__, "payload_length", payload_length)
        if privacy_policy is not None:
            pulumi.set(__self__, "privacy_policy", privacy_policy)
        if product_kind is not None:
            pulumi.set(__self__, "product_kind", product_kind)
        if product_properties is not None:
            pulumi.set(__self__, "product_properties", product_properties)
        if publisher_display_name is not None:
            pulumi.set(__self__, "publisher_display_name", publisher_display_name)
        if publisher_identifier is not None:
            pulumi.set(__self__, "publisher_identifier", publisher_identifier)
        if sku is not None:
            pulumi.set(__self__, "sku", sku)
        if vm_extension_type is not None:
            pulumi.set(__self__, "vm_extension_type", vm_extension_type)

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        ID of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        Metadata pertaining to creation and last modification of the resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Type of Resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="billingPartNumber")
    def billing_part_number(self) -> Optional[str]:
        """
        The part number used for billing purposes.
        """
        return pulumi.get(self, "billing_part_number")

    @property
    @pulumi.getter
    def compatibility(self) -> Optional['outputs.CompatibilityResponse']:
        """
        Product compatibility with current device.
        """
        return pulumi.get(self, "compatibility")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of the product.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[str]:
        """
        The display name of the product.
        """
        return pulumi.get(self, "display_name")

    @property
    @pulumi.getter
    def etag(self) -> Optional[str]:
        """
        The entity tag used for optimistic concurrency when modifying the resource.
        """
        return pulumi.get(self, "etag")

    @property
    @pulumi.getter(name="galleryItemIdentity")
    def gallery_item_identity(self) -> Optional[str]:
        """
        The identifier of the gallery item corresponding to the product.
        """
        return pulumi.get(self, "gallery_item_identity")

    @property
    @pulumi.getter(name="iconUris")
    def icon_uris(self) -> Optional['outputs.IconUrisResponse']:
        """
        Additional links available for this product.
        """
        return pulumi.get(self, "icon_uris")

    @property
    @pulumi.getter(name="legalTerms")
    def legal_terms(self) -> Optional[str]:
        """
        The legal terms.
        """
        return pulumi.get(self, "legal_terms")

    @property
    @pulumi.getter
    def links(self) -> Optional[Sequence['outputs.ProductLinkResponse']]:
        """
        Additional links available for this product.
        """
        return pulumi.get(self, "links")

    @property
    @pulumi.getter
    def offer(self) -> Optional[str]:
        """
        The offer representing the product.
        """
        return pulumi.get(self, "offer")

    @property
    @pulumi.getter(name="offerVersion")
    def offer_version(self) -> Optional[str]:
        """
        The version of the product offer.
        """
        return pulumi.get(self, "offer_version")

    @property
    @pulumi.getter(name="payloadLength")
    def payload_length(self) -> Optional[float]:
        """
        The length of product content.
        """
        return pulumi.get(self, "payload_length")

    @property
    @pulumi.getter(name="privacyPolicy")
    def privacy_policy(self) -> Optional[str]:
        """
        The privacy policy.
        """
        return pulumi.get(self, "privacy_policy")

    @property
    @pulumi.getter(name="productKind")
    def product_kind(self) -> Optional[str]:
        """
        The kind of the product (virtualMachine or virtualMachineExtension)
        """
        return pulumi.get(self, "product_kind")

    @property
    @pulumi.getter(name="productProperties")
    def product_properties(self) -> Optional['outputs.ProductPropertiesResponse']:
        """
        Additional properties for the product.
        """
        return pulumi.get(self, "product_properties")

    @property
    @pulumi.getter(name="publisherDisplayName")
    def publisher_display_name(self) -> Optional[str]:
        """
        The user-friendly name of the product publisher.
        """
        return pulumi.get(self, "publisher_display_name")

    @property
    @pulumi.getter(name="publisherIdentifier")
    def publisher_identifier(self) -> Optional[str]:
        """
        Publisher identifier.
        """
        return pulumi.get(self, "publisher_identifier")

    @property
    @pulumi.getter
    def sku(self) -> Optional[str]:
        """
        The product SKU.
        """
        return pulumi.get(self, "sku")

    @property
    @pulumi.getter(name="vmExtensionType")
    def vm_extension_type(self) -> Optional[str]:
        """
        The type of the Virtual Machine Extension.
        """
        return pulumi.get(self, "vm_extension_type")


@pulumi.output_type
class SystemDataResponse(dict):
    """
    Metadata pertaining to creation and last modification of the resource.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "createdAt":
            suggest = "created_at"
        elif key == "createdBy":
            suggest = "created_by"
        elif key == "createdByType":
            suggest = "created_by_type"
        elif key == "lastModifiedAt":
            suggest = "last_modified_at"
        elif key == "lastModifiedBy":
            suggest = "last_modified_by"
        elif key == "lastModifiedByType":
            suggest = "last_modified_by_type"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in SystemDataResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        SystemDataResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 created_at: Optional[str] = None,
                 created_by: Optional[str] = None,
                 created_by_type: Optional[str] = None,
                 last_modified_at: Optional[str] = None,
                 last_modified_by: Optional[str] = None,
                 last_modified_by_type: Optional[str] = None):
        """
        Metadata pertaining to creation and last modification of the resource.
        :param str created_at: The timestamp of resource creation (UTC).
        :param str created_by: The identity that created the resource.
        :param str created_by_type: The type of identity that created the resource.
        :param str last_modified_at: The timestamp of resource last modification (UTC)
        :param str last_modified_by: The identity that last modified the resource.
        :param str last_modified_by_type: The type of identity that last modified the resource.
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if created_by is not None:
            pulumi.set(__self__, "created_by", created_by)
        if created_by_type is not None:
            pulumi.set(__self__, "created_by_type", created_by_type)
        if last_modified_at is not None:
            pulumi.set(__self__, "last_modified_at", last_modified_at)
        if last_modified_by is not None:
            pulumi.set(__self__, "last_modified_by", last_modified_by)
        if last_modified_by_type is not None:
            pulumi.set(__self__, "last_modified_by_type", last_modified_by_type)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[str]:
        """
        The timestamp of resource creation (UTC).
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="createdBy")
    def created_by(self) -> Optional[str]:
        """
        The identity that created the resource.
        """
        return pulumi.get(self, "created_by")

    @property
    @pulumi.getter(name="createdByType")
    def created_by_type(self) -> Optional[str]:
        """
        The type of identity that created the resource.
        """
        return pulumi.get(self, "created_by_type")

    @property
    @pulumi.getter(name="lastModifiedAt")
    def last_modified_at(self) -> Optional[str]:
        """
        The timestamp of resource last modification (UTC)
        """
        return pulumi.get(self, "last_modified_at")

    @property
    @pulumi.getter(name="lastModifiedBy")
    def last_modified_by(self) -> Optional[str]:
        """
        The identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by")

    @property
    @pulumi.getter(name="lastModifiedByType")
    def last_modified_by_type(self) -> Optional[str]:
        """
        The type of identity that last modified the resource.
        """
        return pulumi.get(self, "last_modified_by_type")


