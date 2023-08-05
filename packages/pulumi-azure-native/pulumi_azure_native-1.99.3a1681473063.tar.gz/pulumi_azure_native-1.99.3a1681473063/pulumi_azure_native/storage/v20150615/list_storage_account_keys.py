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
    'ListStorageAccountKeysResult',
    'AwaitableListStorageAccountKeysResult',
    'list_storage_account_keys',
    'list_storage_account_keys_output',
]

@pulumi.output_type
class ListStorageAccountKeysResult:
    """
    The access keys for the storage account.
    """
    def __init__(__self__, key1=None, key2=None):
        if key1 and not isinstance(key1, str):
            raise TypeError("Expected argument 'key1' to be a str")
        pulumi.set(__self__, "key1", key1)
        if key2 and not isinstance(key2, str):
            raise TypeError("Expected argument 'key2' to be a str")
        pulumi.set(__self__, "key2", key2)

    @property
    @pulumi.getter
    def key1(self) -> Optional[str]:
        """
        The value of key 1.
        """
        return pulumi.get(self, "key1")

    @property
    @pulumi.getter
    def key2(self) -> Optional[str]:
        """
        The value of key 2.
        """
        return pulumi.get(self, "key2")


class AwaitableListStorageAccountKeysResult(ListStorageAccountKeysResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return ListStorageAccountKeysResult(
            key1=self.key1,
            key2=self.key2)


def list_storage_account_keys(account_name: Optional[str] = None,
                              resource_group_name: Optional[str] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableListStorageAccountKeysResult:
    """
    Lists the access keys for the specified storage account.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    __args__ = dict()
    __args__['accountName'] = account_name
    __args__['resourceGroupName'] = resource_group_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:storage/v20150615:listStorageAccountKeys', __args__, opts=opts, typ=ListStorageAccountKeysResult).value

    return AwaitableListStorageAccountKeysResult(
        key1=__ret__.key1,
        key2=__ret__.key2)


@_utilities.lift_output_func(list_storage_account_keys)
def list_storage_account_keys_output(account_name: Optional[pulumi.Input[str]] = None,
                                     resource_group_name: Optional[pulumi.Input[str]] = None,
                                     opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[ListStorageAccountKeysResult]:
    """
    Lists the access keys for the specified storage account.


    :param str account_name: The name of the storage account within the specified resource group. Storage account names must be between 3 and 24 characters in length and use numbers and lower-case letters only.
    :param str resource_group_name: The name of the resource group within the user's subscription. The name is case insensitive.
    """
    ...
