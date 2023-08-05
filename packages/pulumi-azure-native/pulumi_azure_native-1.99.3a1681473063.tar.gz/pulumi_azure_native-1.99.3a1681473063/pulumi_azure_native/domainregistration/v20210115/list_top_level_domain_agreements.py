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
    'ListTopLevelDomainAgreementsResult',
    'AwaitableListTopLevelDomainAgreementsResult',
    'list_top_level_domain_agreements',
    'list_top_level_domain_agreements_output',
]

@pulumi.output_type
class ListTopLevelDomainAgreementsResult:
    """
    Collection of top-level domain legal agreements.
    """
    def __init__(__self__, next_link=None, value=None):
        if next_link and not isinstance(next_link, str):
            raise TypeError("Expected argument 'next_link' to be a str")
        pulumi.set(__self__, "next_link", next_link)
        if value and not isinstance(value, list):
            raise TypeError("Expected argument 'value' to be a list")
        pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="nextLink")
    def next_link(self) -> str:
        """
        Link to next page of resources.
        """
        return pulumi.get(self, "next_link")

    @property
    @pulumi.getter
    def value(self) -> Sequence['outputs.TldLegalAgreementResponse']:
        """
        Collection of resources.
        """
        return pulumi.get(self, "value")


class AwaitableListTopLevelDomainAgreementsResult(ListTopLevelDomainAgreementsResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListTopLevelDomainAgreementsResult(
            next_link=self.next_link,
            value=self.value)


def list_top_level_domain_agreements(for_transfer: Optional[bool] = None,
                                     include_privacy: Optional[bool] = None,
                                     name: Optional[str] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListTopLevelDomainAgreementsResult:
    """
    Gets all legal agreements that user needs to accept before purchasing a domain.


    :param bool for_transfer: If <code>true</code>, then the list of agreements will include agreements for domain transfer as well; otherwise, <code>false</code>.
    :param bool include_privacy: If <code>true</code>, then the list of agreements will include agreements for domain privacy as well; otherwise, <code>false</code>.
    :param str name: Name of the top-level domain.
    """
    __args__ = dict()
    __args__['forTransfer'] = for_transfer
    __args__['includePrivacy'] = include_privacy
    __args__['name'] = name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:domainregistration/v20210115:listTopLevelDomainAgreements', __args__, opts=opts, typ=ListTopLevelDomainAgreementsResult).value

    return AwaitableListTopLevelDomainAgreementsResult(
        next_link=__ret__.next_link,
        value=__ret__.value)


@_utilities.lift_output_func(list_top_level_domain_agreements)
def list_top_level_domain_agreements_output(for_transfer: Optional[pulumi.Input[Optional[bool]]] = None,
                                            include_privacy: Optional[pulumi.Input[Optional[bool]]] = None,
                                            name: Optional[pulumi.Input[str]] = None,
                                            opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListTopLevelDomainAgreementsResult]:
    """
    Gets all legal agreements that user needs to accept before purchasing a domain.


    :param bool for_transfer: If <code>true</code>, then the list of agreements will include agreements for domain transfer as well; otherwise, <code>false</code>.
    :param bool include_privacy: If <code>true</code>, then the list of agreements will include agreements for domain privacy as well; otherwise, <code>false</code>.
    :param str name: Name of the top-level domain.
    """
    ...
