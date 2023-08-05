# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities
from ._enums import *

__all__ = [
    'B2CResourceSKUArgs',
    'CreateTenantRequestBodyPropertiesArgs',
]

@pulumi.input_type
class B2CResourceSKUArgs:
    def __init__(__self__, *,
                 name: Optional[pulumi.Input['B2CResourceSKUName']] = None,
                 tier: Optional[pulumi.Input['B2CResourceSKUTier']] = None):
        """
        SKU properties of the Azure AD B2C tenant. Learn more about Azure AD B2C billing at [aka.ms/b2cBilling](https://aka.ms/b2cBilling).
        :param pulumi.Input['B2CResourceSKUName'] name: The name of the SKU for the tenant.
        :param pulumi.Input['B2CResourceSKUTier'] tier: The tier of the tenant.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if tier is not None:
            pulumi.set(__self__, "tier", tier)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input['B2CResourceSKUName']]:
        """
        The name of the SKU for the tenant.
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input['B2CResourceSKUName']]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def tier(self) -> Optional[pulumi.Input['B2CResourceSKUTier']]:
        """
        The tier of the tenant.
        """
        return pulumi.get(self, "tier")

    @tier.setter
    def tier(self, value: Optional[pulumi.Input['B2CResourceSKUTier']]):
        pulumi.set(self, "tier", value)


@pulumi.input_type
class CreateTenantRequestBodyPropertiesArgs:
    def __init__(__self__, *,
                 country_code: Optional[pulumi.Input[str]] = None,
                 display_name: Optional[pulumi.Input[str]] = None):
        """
        :param pulumi.Input[str] country_code: Country code of Azure tenant (e.g. 'US'). Refer to [aka.ms/B2CDataResidency](https://aka.ms/B2CDataResidency) to see valid country codes and corresponding data residency locations. If you do not see a country code in an valid data residency location, choose one from the list.
        :param pulumi.Input[str] display_name: The display name of the B2C tenant.
        """
        if country_code is not None:
            pulumi.set(__self__, "country_code", country_code)
        if display_name is not None:
            pulumi.set(__self__, "display_name", display_name)

    @property
    @pulumi.getter(name="countryCode")
    def country_code(self) -> Optional[pulumi.Input[str]]:
        """
        Country code of Azure tenant (e.g. 'US'). Refer to [aka.ms/B2CDataResidency](https://aka.ms/B2CDataResidency) to see valid country codes and corresponding data residency locations. If you do not see a country code in an valid data residency location, choose one from the list.
        """
        return pulumi.get(self, "country_code")

    @country_code.setter
    def country_code(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "country_code", value)

    @property
    @pulumi.getter(name="displayName")
    def display_name(self) -> Optional[pulumi.Input[str]]:
        """
        The display name of the B2C tenant.
        """
        return pulumi.get(self, "display_name")

    @display_name.setter
    def display_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "display_name", value)


