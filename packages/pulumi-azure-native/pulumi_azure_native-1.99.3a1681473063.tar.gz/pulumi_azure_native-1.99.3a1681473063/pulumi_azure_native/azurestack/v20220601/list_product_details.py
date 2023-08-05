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
    'ListProductDetailsResult',
    'AwaitableListProductDetailsResult',
    'list_product_details',
    'list_product_details_output',
]

@pulumi.output_type
class ListProductDetailsResult:
    """
    Extended description about the product required for installing it into Azure Stack.
    """
    def __init__(__self__, compute_role=None, data_disk_images=None, gallery_package_blob_sas_uri=None, is_system_extension=None, os_disk_image=None, product_kind=None, support_multiple_extensions=None, uri=None, version=None, vm_os_type=None, vm_scale_set_enabled=None):
        if compute_role and not isinstance(compute_role, str):
            raise TypeError("Expected argument 'compute_role' to be a str")
        pulumi.set(__self__, "compute_role", compute_role)
        if data_disk_images and not isinstance(data_disk_images, list):
            raise TypeError("Expected argument 'data_disk_images' to be a list")
        pulumi.set(__self__, "data_disk_images", data_disk_images)
        if gallery_package_blob_sas_uri and not isinstance(gallery_package_blob_sas_uri, str):
            raise TypeError("Expected argument 'gallery_package_blob_sas_uri' to be a str")
        pulumi.set(__self__, "gallery_package_blob_sas_uri", gallery_package_blob_sas_uri)
        if is_system_extension and not isinstance(is_system_extension, bool):
            raise TypeError("Expected argument 'is_system_extension' to be a bool")
        pulumi.set(__self__, "is_system_extension", is_system_extension)
        if os_disk_image and not isinstance(os_disk_image, dict):
            raise TypeError("Expected argument 'os_disk_image' to be a dict")
        pulumi.set(__self__, "os_disk_image", os_disk_image)
        if product_kind and not isinstance(product_kind, str):
            raise TypeError("Expected argument 'product_kind' to be a str")
        pulumi.set(__self__, "product_kind", product_kind)
        if support_multiple_extensions and not isinstance(support_multiple_extensions, bool):
            raise TypeError("Expected argument 'support_multiple_extensions' to be a bool")
        pulumi.set(__self__, "support_multiple_extensions", support_multiple_extensions)
        if uri and not isinstance(uri, str):
            raise TypeError("Expected argument 'uri' to be a str")
        pulumi.set(__self__, "uri", uri)
        if version and not isinstance(version, str):
            raise TypeError("Expected argument 'version' to be a str")
        pulumi.set(__self__, "version", version)
        if vm_os_type and not isinstance(vm_os_type, str):
            raise TypeError("Expected argument 'vm_os_type' to be a str")
        pulumi.set(__self__, "vm_os_type", vm_os_type)
        if vm_scale_set_enabled and not isinstance(vm_scale_set_enabled, bool):
            raise TypeError("Expected argument 'vm_scale_set_enabled' to be a bool")
        pulumi.set(__self__, "vm_scale_set_enabled", vm_scale_set_enabled)

    @property
    @pulumi.getter(name="computeRole")
    def compute_role(self) -> str:
        """
        Specifies kind of compute role included in the package.
        """
        return pulumi.get(self, "compute_role")

    @property
    @pulumi.getter(name="dataDiskImages")
    def data_disk_images(self) -> Sequence['outputs.DataDiskImageResponse']:
        """
        List of attached data disks.
        """
        return pulumi.get(self, "data_disk_images")

    @property
    @pulumi.getter(name="galleryPackageBlobSasUri")
    def gallery_package_blob_sas_uri(self) -> str:
        """
        The URI to the .azpkg file that provides information required for showing product in the gallery.
        """
        return pulumi.get(self, "gallery_package_blob_sas_uri")

    @property
    @pulumi.getter(name="isSystemExtension")
    def is_system_extension(self) -> bool:
        """
        Specifies if product is a Virtual Machine Extension.
        """
        return pulumi.get(self, "is_system_extension")

    @property
    @pulumi.getter(name="osDiskImage")
    def os_disk_image(self) -> 'outputs.OsDiskImageResponse':
        """
        OS disk image used by product.
        """
        return pulumi.get(self, "os_disk_image")

    @property
    @pulumi.getter(name="productKind")
    def product_kind(self) -> str:
        """
        Specifies the kind of the product (virtualMachine or virtualMachineExtension).
        """
        return pulumi.get(self, "product_kind")

    @property
    @pulumi.getter(name="supportMultipleExtensions")
    def support_multiple_extensions(self) -> bool:
        """
        Indicates if specified product supports multiple extensions.
        """
        return pulumi.get(self, "support_multiple_extensions")

    @property
    @pulumi.getter
    def uri(self) -> str:
        """
        The URI.
        """
        return pulumi.get(self, "uri")

    @property
    @pulumi.getter
    def version(self) -> str:
        """
        Specifies product version.
        """
        return pulumi.get(self, "version")

    @property
    @pulumi.getter(name="vmOsType")
    def vm_os_type(self) -> str:
        """
        Specifies operating system used by the product.
        """
        return pulumi.get(self, "vm_os_type")

    @property
    @pulumi.getter(name="vmScaleSetEnabled")
    def vm_scale_set_enabled(self) -> bool:
        """
        Indicates if virtual machine Scale Set is enabled in the specified product.
        """
        return pulumi.get(self, "vm_scale_set_enabled")


class AwaitableListProductDetailsResult(ListProductDetailsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListProductDetailsResult(
            compute_role=self.compute_role,
            data_disk_images=self.data_disk_images,
            gallery_package_blob_sas_uri=self.gallery_package_blob_sas_uri,
            is_system_extension=self.is_system_extension,
            os_disk_image=self.os_disk_image,
            product_kind=self.product_kind,
            support_multiple_extensions=self.support_multiple_extensions,
            uri=self.uri,
            version=self.version,
            vm_os_type=self.vm_os_type,
            vm_scale_set_enabled=self.vm_scale_set_enabled)


def list_product_details(product_name: Optional[str] = None,
                         registration_name: Optional[str] = None,
                         resource_group: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListProductDetailsResult:
    """
    Returns the extended properties of a product.


    :param str product_name: Name of the product.
    :param str registration_name: Name of the Azure Stack registration.
    :param str resource_group: Name of the resource group.
    """
    __args__ = dict()
    __args__['productName'] = product_name
    __args__['registrationName'] = registration_name
    __args__['resourceGroup'] = resource_group
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:azurestack/v20220601:listProductDetails', __args__, opts=opts, typ=ListProductDetailsResult).value

    return AwaitableListProductDetailsResult(
        compute_role=__ret__.compute_role,
        data_disk_images=__ret__.data_disk_images,
        gallery_package_blob_sas_uri=__ret__.gallery_package_blob_sas_uri,
        is_system_extension=__ret__.is_system_extension,
        os_disk_image=__ret__.os_disk_image,
        product_kind=__ret__.product_kind,
        support_multiple_extensions=__ret__.support_multiple_extensions,
        uri=__ret__.uri,
        version=__ret__.version,
        vm_os_type=__ret__.vm_os_type,
        vm_scale_set_enabled=__ret__.vm_scale_set_enabled)


@_utilities.lift_output_func(list_product_details)
def list_product_details_output(product_name: Optional[pulumi.Input[str]] = None,
                                registration_name: Optional[pulumi.Input[str]] = None,
                                resource_group: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListProductDetailsResult]:
    """
    Returns the extended properties of a product.


    :param str product_name: Name of the product.
    :param str registration_name: Name of the Azure Stack registration.
    :param str resource_group: Name of the resource group.
    """
    ...
