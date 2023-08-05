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
    'GetGalleryImageResult',
    'AwaitableGetGalleryImageResult',
    'get_gallery_image',
    'get_gallery_image_output',
]

@pulumi.output_type
class GetGalleryImageResult:
    """
    Specifies information about the gallery image definition that you want to create or update.
    """
    def __init__(__self__, architecture=None, description=None, disallowed=None, end_of_life_date=None, eula=None, features=None, hyper_v_generation=None, id=None, identifier=None, location=None, name=None, os_state=None, os_type=None, privacy_statement_uri=None, provisioning_state=None, purchase_plan=None, recommended=None, release_note_uri=None, tags=None, type=None):
        if architecture and not isinstance(architecture, str):
            raise TypeError("Expected argument 'architecture' to be a str")
        pulumi.set(__self__, "architecture", architecture)
        if description and not isinstance(description, str):
            raise TypeError("Expected argument 'description' to be a str")
        pulumi.set(__self__, "description", description)
        if disallowed and not isinstance(disallowed, dict):
            raise TypeError("Expected argument 'disallowed' to be a dict")
        pulumi.set(__self__, "disallowed", disallowed)
        if end_of_life_date and not isinstance(end_of_life_date, str):
            raise TypeError("Expected argument 'end_of_life_date' to be a str")
        pulumi.set(__self__, "end_of_life_date", end_of_life_date)
        if eula and not isinstance(eula, str):
            raise TypeError("Expected argument 'eula' to be a str")
        pulumi.set(__self__, "eula", eula)
        if features and not isinstance(features, list):
            raise TypeError("Expected argument 'features' to be a list")
        pulumi.set(__self__, "features", features)
        if hyper_v_generation and not isinstance(hyper_v_generation, str):
            raise TypeError("Expected argument 'hyper_v_generation' to be a str")
        pulumi.set(__self__, "hyper_v_generation", hyper_v_generation)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if identifier and not isinstance(identifier, dict):
            raise TypeError("Expected argument 'identifier' to be a dict")
        pulumi.set(__self__, "identifier", identifier)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if os_state and not isinstance(os_state, str):
            raise TypeError("Expected argument 'os_state' to be a str")
        pulumi.set(__self__, "os_state", os_state)
        if os_type and not isinstance(os_type, str):
            raise TypeError("Expected argument 'os_type' to be a str")
        pulumi.set(__self__, "os_type", os_type)
        if privacy_statement_uri and not isinstance(privacy_statement_uri, str):
            raise TypeError("Expected argument 'privacy_statement_uri' to be a str")
        pulumi.set(__self__, "privacy_statement_uri", privacy_statement_uri)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if purchase_plan and not isinstance(purchase_plan, dict):
            raise TypeError("Expected argument 'purchase_plan' to be a dict")
        pulumi.set(__self__, "purchase_plan", purchase_plan)
        if recommended and not isinstance(recommended, dict):
            raise TypeError("Expected argument 'recommended' to be a dict")
        pulumi.set(__self__, "recommended", recommended)
        if release_note_uri and not isinstance(release_note_uri, str):
            raise TypeError("Expected argument 'release_note_uri' to be a str")
        pulumi.set(__self__, "release_note_uri", release_note_uri)
        if tags and not isinstance(tags, dict):
            raise TypeError("Expected argument 'tags' to be a dict")
        pulumi.set(__self__, "tags", tags)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def architecture(self) -> Optional[str]:
        """
        The architecture of the image. Applicable to OS disks only.
        """
        return pulumi.get(self, "architecture")

    @property
    @pulumi.getter
    def description(self) -> Optional[str]:
        """
        The description of this gallery image definition resource. This property is updatable.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def disallowed(self) -> Optional['outputs.DisallowedResponse']:
        """
        Describes the disallowed disk types.
        """
        return pulumi.get(self, "disallowed")

    @property
    @pulumi.getter(name="endOfLifeDate")
    def end_of_life_date(self) -> Optional[str]:
        """
        The end of life date of the gallery image definition. This property can be used for decommissioning purposes. This property is updatable.
        """
        return pulumi.get(self, "end_of_life_date")

    @property
    @pulumi.getter
    def eula(self) -> Optional[str]:
        """
        The Eula agreement for the gallery image definition.
        """
        return pulumi.get(self, "eula")

    @property
    @pulumi.getter
    def features(self) -> Optional[Sequence['outputs.GalleryImageFeatureResponse']]:
        """
        A list of gallery image features.
        """
        return pulumi.get(self, "features")

    @property
    @pulumi.getter(name="hyperVGeneration")
    def hyper_v_generation(self) -> Optional[str]:
        """
        The hypervisor generation of the Virtual Machine. Applicable to OS disks only.
        """
        return pulumi.get(self, "hyper_v_generation")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource Id
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def identifier(self) -> 'outputs.GalleryImageIdentifierResponse':
        """
        This is the gallery image definition identifier.
        """
        return pulumi.get(self, "identifier")

    @property
    @pulumi.getter
    def location(self) -> str:
        """
        Resource location
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="osState")
    def os_state(self) -> str:
        """
        This property allows the user to specify whether the virtual machines created under this image are 'Generalized' or 'Specialized'.
        """
        return pulumi.get(self, "os_state")

    @property
    @pulumi.getter(name="osType")
    def os_type(self) -> str:
        """
        This property allows you to specify the type of the OS that is included in the disk when creating a VM from a managed image. <br><br> Possible values are: <br><br> **Windows** <br><br> **Linux**
        """
        return pulumi.get(self, "os_type")

    @property
    @pulumi.getter(name="privacyStatementUri")
    def privacy_statement_uri(self) -> Optional[str]:
        """
        The privacy statement uri.
        """
        return pulumi.get(self, "privacy_statement_uri")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        The provisioning state, which only appears in the response.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="purchasePlan")
    def purchase_plan(self) -> Optional['outputs.ImagePurchasePlanResponse']:
        """
        Describes the gallery image definition purchase plan. This is used by marketplace images.
        """
        return pulumi.get(self, "purchase_plan")

    @property
    @pulumi.getter
    def recommended(self) -> Optional['outputs.RecommendedMachineConfigurationResponse']:
        """
        The properties describe the recommended machine configuration for this Image Definition. These properties are updatable.
        """
        return pulumi.get(self, "recommended")

    @property
    @pulumi.getter(name="releaseNoteUri")
    def release_note_uri(self) -> Optional[str]:
        """
        The release note uri.
        """
        return pulumi.get(self, "release_note_uri")

    @property
    @pulumi.getter
    def tags(self) -> Optional[Mapping[str, str]]:
        """
        Resource tags
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type
        """
        return pulumi.get(self, "type")


class AwaitableGetGalleryImageResult(GetGalleryImageResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetGalleryImageResult(
            architecture=self.architecture,
            description=self.description,
            disallowed=self.disallowed,
            end_of_life_date=self.end_of_life_date,
            eula=self.eula,
            features=self.features,
            hyper_v_generation=self.hyper_v_generation,
            id=self.id,
            identifier=self.identifier,
            location=self.location,
            name=self.name,
            os_state=self.os_state,
            os_type=self.os_type,
            privacy_statement_uri=self.privacy_statement_uri,
            provisioning_state=self.provisioning_state,
            purchase_plan=self.purchase_plan,
            recommended=self.recommended,
            release_note_uri=self.release_note_uri,
            tags=self.tags,
            type=self.type)


def get_gallery_image(gallery_image_name: Optional[str] = None,
                      gallery_name: Optional[str] = None,
                      resource_group_name: Optional[str] = None,
                      opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetGalleryImageResult:
    """
    Retrieves information about a gallery image definition.


    :param str gallery_image_name: The name of the gallery image definition to be retrieved.
    :param str gallery_name: The name of the Shared Image Gallery from which the Image Definitions are to be retrieved.
    :param str resource_group_name: The name of the resource group.
    """
    __args__ = dict()
    __args__['galleryImageName'] = gallery_image_name
    __args__['galleryName'] = gallery_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:compute/v20220303:getGalleryImage', __args__, opts=opts, typ=GetGalleryImageResult).value

    return AwaitableGetGalleryImageResult(
        architecture=__ret__.architecture,
        description=__ret__.description,
        disallowed=__ret__.disallowed,
        end_of_life_date=__ret__.end_of_life_date,
        eula=__ret__.eula,
        features=__ret__.features,
        hyper_v_generation=__ret__.hyper_v_generation,
        id=__ret__.id,
        identifier=__ret__.identifier,
        location=__ret__.location,
        name=__ret__.name,
        os_state=__ret__.os_state,
        os_type=__ret__.os_type,
        privacy_statement_uri=__ret__.privacy_statement_uri,
        provisioning_state=__ret__.provisioning_state,
        purchase_plan=__ret__.purchase_plan,
        recommended=__ret__.recommended,
        release_note_uri=__ret__.release_note_uri,
        tags=__ret__.tags,
        type=__ret__.type)


@_utilities.lift_output_func(get_gallery_image)
def get_gallery_image_output(gallery_image_name: Optional[pulumi.Input[str]] = None,
                             gallery_name: Optional[pulumi.Input[str]] = None,
                             resource_group_name: Optional[pulumi.Input[str]] = None,
                             opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetGalleryImageResult]:
    """
    Retrieves information about a gallery image definition.


    :param str gallery_image_name: The name of the gallery image definition to be retrieved.
    :param str gallery_name: The name of the Shared Image Gallery from which the Image Definitions are to be retrieved.
    :param str resource_group_name: The name of the resource group.
    """
    ...
