# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ArmTemplateParameterArgs',
    'ManagementAssociationPropertiesArgs',
    'ManagementConfigurationPropertiesArgs',
    'SolutionPlanArgs',
    'SolutionPropertiesArgs',
]

@pulumi.input_type
class ArmTemplateParameterArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        Parameter to pass to ARM template
        :param pulumi.Input[str] name: name of the parameter.
        :param pulumi.Input[str] value: value for the parameter. In Jtoken 
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the parameter.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        value for the parameter. In Jtoken 
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


@pulumi.input_type
class ManagementAssociationPropertiesArgs:
    def __init__(__self__, *,
                 application_id: pulumi.Input[str]):
        """
        ManagementAssociation properties supported by the OperationsManagement resource provider.
        :param pulumi.Input[str] application_id: The applicationId of the appliance for this association.
        """
        pulumi.set(__self__, "application_id", application_id)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> pulumi.Input[str]:
        """
        The applicationId of the appliance for this association.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "application_id", value)


@pulumi.input_type
class ManagementConfigurationPropertiesArgs:
    def __init__(__self__, *,
                 parameters: pulumi.Input[Sequence[pulumi.Input['ArmTemplateParameterArgs']]],
                 parent_resource_type: pulumi.Input[str],
                 template: Any,
                 application_id: Optional[pulumi.Input[str]] = None):
        """
        ManagementConfiguration properties supported by the OperationsManagement resource provider.
        :param pulumi.Input[Sequence[pulumi.Input['ArmTemplateParameterArgs']]] parameters: Parameters to run the ARM template
        :param pulumi.Input[str] parent_resource_type: The type of the parent resource.
        :param Any template: The Json object containing the ARM template to deploy
        :param pulumi.Input[str] application_id: The applicationId of the appliance for this Management.
        """
        pulumi.set(__self__, "parameters", parameters)
        pulumi.set(__self__, "parent_resource_type", parent_resource_type)
        pulumi.set(__self__, "template", template)
        if application_id is not None:
            pulumi.set(__self__, "application_id", application_id)

    @property
    @pulumi.getter
    def parameters(self) -> pulumi.Input[Sequence[pulumi.Input['ArmTemplateParameterArgs']]]:
        """
        Parameters to run the ARM template
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: pulumi.Input[Sequence[pulumi.Input['ArmTemplateParameterArgs']]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="parentResourceType")
    def parent_resource_type(self) -> pulumi.Input[str]:
        """
        The type of the parent resource.
        """
        return pulumi.get(self, "parent_resource_type")

    @parent_resource_type.setter
    def parent_resource_type(self, value: pulumi.Input[str]):
        pulumi.set(self, "parent_resource_type", value)

    @property
    @pulumi.getter
    def template(self) -> Any:
        """
        The Json object containing the ARM template to deploy
        """
        return pulumi.get(self, "template")

    @template.setter
    def template(self, value: Any):
        pulumi.set(self, "template", value)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> Optional[pulumi.Input[str]]:
        """
        The applicationId of the appliance for this Management.
        """
        return pulumi.get(self, "application_id")

    @application_id.setter
    def application_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "application_id", value)


@pulumi.input_type
class SolutionPlanArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input[str]] = None,
                 product: Optional[pulumi.Input[str]] = None,
                 promotion_code: Optional[pulumi.Input[str]] = None,
                 publisher: Optional[pulumi.Input[str]] = None):
        """
        Plan for solution object supported by the OperationsManagement resource provider.
        :param pulumi.Input[str] name: name of the solution to be created. For Microsoft published solution it should be in the format of solutionType(workspaceName). SolutionType part is case sensitive. For third party solution, it can be anything.
        :param pulumi.Input[str] product: name of the solution to enabled/add. For Microsoft published gallery solution it should be in the format of OMSGallery/<solutionType>. This is case sensitive
        :param pulumi.Input[str] promotion_code: promotionCode, Not really used now, can you left as empty
        :param pulumi.Input[str] publisher: Publisher name. For gallery solution, it is Microsoft.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if product is not None:
            pulumi.set(__self__, "product", product)
        if promotion_code is not None:
            pulumi.set(__self__, "promotion_code", promotion_code)
        if publisher is not None:
            pulumi.set(__self__, "publisher", publisher)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        name of the solution to be created. For Microsoft published solution it should be in the format of solutionType(workspaceName). SolutionType part is case sensitive. For third party solution, it can be anything.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def product(self) -> Optional[pulumi.Input[str]]:
        """
        name of the solution to enabled/add. For Microsoft published gallery solution it should be in the format of OMSGallery/<solutionType>. This is case sensitive
        """
        return pulumi.get(self, "product")

    @product.setter
    def product(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "product", value)

    @property
    @pulumi.getter(name="promotionCode")
    def promotion_code(self) -> Optional[pulumi.Input[str]]:
        """
        promotionCode, Not really used now, can you left as empty
        """
        return pulumi.get(self, "promotion_code")

    @promotion_code.setter
    def promotion_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "promotion_code", value)

    @property
    @pulumi.getter
    def publisher(self) -> Optional[pulumi.Input[str]]:
        """
        Publisher name. For gallery solution, it is Microsoft.
        """
        return pulumi.get(self, "publisher")

    @publisher.setter
    def publisher(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "publisher", value)


@pulumi.input_type
class SolutionPropertiesArgs:
    def __init__(__self__, *,
                 workspace_resource_id: pulumi.Input[str],
                 contained_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 referenced_resources: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        Solution properties supported by the OperationsManagement resource provider.
        :param pulumi.Input[str] workspace_resource_id: The azure resourceId for the workspace where the solution will be deployed/enabled.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] contained_resources: The azure resources that will be contained within the solutions. They will be locked and gets deleted automatically when the solution is deleted.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] referenced_resources: The resources that will be referenced from this solution. Deleting any of those solution out of band will break the solution.
        """
        pulumi.set(__self__, "workspace_resource_id", workspace_resource_id)
        if contained_resources is not None:
            pulumi.set(__self__, "contained_resources", contained_resources)
        if referenced_resources is not None:
            pulumi.set(__self__, "referenced_resources", referenced_resources)

    @property
    @pulumi.getter(name="workspaceResourceId")
    def workspace_resource_id(self) -> pulumi.Input[str]:
        """
        The azure resourceId for the workspace where the solution will be deployed/enabled.
        """
        return pulumi.get(self, "workspace_resource_id")

    @workspace_resource_id.setter
    def workspace_resource_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "workspace_resource_id", value)

    @property
    @pulumi.getter(name="containedResources")
    def contained_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The azure resources that will be contained within the solutions. They will be locked and gets deleted automatically when the solution is deleted.
        """
        return pulumi.get(self, "contained_resources")

    @contained_resources.setter
    def contained_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "contained_resources", value)

    @property
    @pulumi.getter(name="referencedResources")
    def referenced_resources(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The resources that will be referenced from this solution. Deleting any of those solution out of band will break the solution.
        """
        return pulumi.get(self, "referenced_resources")

    @referenced_resources.setter
    def referenced_resources(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "referenced_resources", value)


