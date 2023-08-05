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
    'GetSAPSupportedSkuResult',
    'AwaitableGetSAPSupportedSkuResult',
    'get_sap_supported_sku',
    'get_sap_supported_sku_output',
]

@pulumi.output_type
class GetSAPSupportedSkuResult:
    """
    The list of supported SKUs for different resources which are part of SAP deployment.
    """
    def __init__(__self__, supported_skus=None):
        if supported_skus and not isinstance(supported_skus, list):
            raise TypeError("Expected argument 'supported_skus' to be a list")
        pulumi.set(__self__, "supported_skus", supported_skus)

    @property
    @pulumi.getter(name="supportedSkus")
    def supported_skus(self) -> Optional[Sequence['outputs.SAPSupportedSkuResponse']]:
        """
        Gets the list of SAP supported SKUs.
        """
        return pulumi.get(self, "supported_skus")


class AwaitableGetSAPSupportedSkuResult(GetSAPSupportedSkuResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetSAPSupportedSkuResult(
            supported_skus=self.supported_skus)


def get_sap_supported_sku(app_location: Optional[str] = None,
                          database_type: Optional[Union[str, 'SAPDatabaseType']] = None,
                          deployment_type: Optional[Union[str, 'SAPDeploymentType']] = None,
                          environment: Optional[Union[str, 'SAPEnvironmentType']] = None,
                          high_availability_type: Optional[Union[str, 'SAPHighAvailabilityType']] = None,
                          location: Optional[str] = None,
                          sap_product: Optional[Union[str, 'SAPProductType']] = None,
                          opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetSAPSupportedSkuResult:
    """
    Get a list of SAP supported SKUs for ASCS, Application and Database tier.


    :param str app_location: The geo-location where the resource is to be created.
    :param Union[str, 'SAPDatabaseType'] database_type: The database type. Eg: HANA, DB2, etc
    :param Union[str, 'SAPDeploymentType'] deployment_type: The deployment type. Eg: SingleServer/ThreeTier
    :param Union[str, 'SAPEnvironmentType'] environment: Defines the environment type - Production/Non Production.
    :param Union[str, 'SAPHighAvailabilityType'] high_availability_type: The high availability type.
    :param str location: The name of Azure region.
    :param Union[str, 'SAPProductType'] sap_product: Defines the SAP Product type.
    """
    __args__ = dict()
    __args__['appLocation'] = app_location
    __args__['databaseType'] = database_type
    __args__['deploymentType'] = deployment_type
    __args__['environment'] = environment
    __args__['highAvailabilityType'] = high_availability_type
    __args__['location'] = location
    __args__['sapProduct'] = sap_product
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:workloads/v20211201preview:getSAPSupportedSku', __args__, opts=opts, typ=GetSAPSupportedSkuResult).value

    return AwaitableGetSAPSupportedSkuResult(
        supported_skus=__ret__.supported_skus)


@_utilities.lift_output_func(get_sap_supported_sku)
def get_sap_supported_sku_output(app_location: Optional[pulumi.Input[str]] = None,
                                 database_type: Optional[pulumi.Input[Union[str, 'SAPDatabaseType']]] = None,
                                 deployment_type: Optional[pulumi.Input[Union[str, 'SAPDeploymentType']]] = None,
                                 environment: Optional[pulumi.Input[Union[str, 'SAPEnvironmentType']]] = None,
                                 high_availability_type: Optional[pulumi.Input[Optional[Union[str, 'SAPHighAvailabilityType']]]] = None,
                                 location: Optional[pulumi.Input[str]] = None,
                                 sap_product: Optional[pulumi.Input[Union[str, 'SAPProductType']]] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetSAPSupportedSkuResult]:
    """
    Get a list of SAP supported SKUs for ASCS, Application and Database tier.


    :param str app_location: The geo-location where the resource is to be created.
    :param Union[str, 'SAPDatabaseType'] database_type: The database type. Eg: HANA, DB2, etc
    :param Union[str, 'SAPDeploymentType'] deployment_type: The deployment type. Eg: SingleServer/ThreeTier
    :param Union[str, 'SAPEnvironmentType'] environment: Defines the environment type - Production/Non Production.
    :param Union[str, 'SAPHighAvailabilityType'] high_availability_type: The high availability type.
    :param str location: The name of Azure region.
    :param Union[str, 'SAPProductType'] sap_product: Defines the SAP Product type.
    """
    ...
