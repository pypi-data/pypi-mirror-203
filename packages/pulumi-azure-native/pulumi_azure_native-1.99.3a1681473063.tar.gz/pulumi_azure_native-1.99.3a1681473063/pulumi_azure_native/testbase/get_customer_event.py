# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities
from . import outputs

__all__ = [
    'GetCustomerEventResult',
    'AwaitableGetCustomerEventResult',
    'get_customer_event',
    'get_customer_event_output',
]

@pulumi.output_type
class GetCustomerEventResult:
    """
    The Customer Notification Event resource.
    """
    def __init__(__self__, event_name=None, id=None, name=None, receivers=None, system_data=None, type=None):
        if event_name and not isinstance(event_name, str):
            raise TypeError("Expected argument 'event_name' to be a str")
        pulumi.set(__self__, "event_name", event_name)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if receivers and not isinstance(receivers, list):
            raise TypeError("Expected argument 'receivers' to be a list")
        pulumi.set(__self__, "receivers", receivers)
        if system_data and not isinstance(system_data, dict):
            raise TypeError("Expected argument 'system_data' to be a dict")
        pulumi.set(__self__, "system_data", system_data)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter(name="eventName")
    def event_name(self) -> str:
        """
        The name of the event subscribed to.
        """
        return pulumi.get(self, "event_name")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Resource ID.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def receivers(self) -> Sequence['outputs.NotificationEventReceiverResponse']:
        """
        The notification event receivers.
        """
        return pulumi.get(self, "receivers")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> 'outputs.SystemDataResponse':
        """
        The system metadata relating to this resource
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Resource type.
        """
        return pulumi.get(self, "type")


class AwaitableGetCustomerEventResult(GetCustomerEventResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetCustomerEventResult(
            event_name=self.event_name,
            id=self.id,
            name=self.name,
            receivers=self.receivers,
            system_data=self.system_data,
            type=self.type)


def get_customer_event(customer_event_name: Optional[str] = None,
                       resource_group_name: Optional[str] = None,
                       test_base_account_name: Optional[str] = None,
                       opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetCustomerEventResult:
    """
    Gets a Test Base CustomerEvent.
    API Version: 2022-04-01-preview.


    :param str customer_event_name: The resource name of the Test Base Customer event.
    :param str resource_group_name: The name of the resource group that contains the resource.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    __args__ = dict()
    __args__['customerEventName'] = customer_event_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['testBaseAccountName'] = test_base_account_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:testbase:getCustomerEvent', __args__, opts=opts, typ=GetCustomerEventResult).value

    return AwaitableGetCustomerEventResult(
        event_name=__ret__.event_name,
        id=__ret__.id,
        name=__ret__.name,
        receivers=__ret__.receivers,
        system_data=__ret__.system_data,
        type=__ret__.type)


@_utilities.lift_output_func(get_customer_event)
def get_customer_event_output(customer_event_name: Optional[pulumi.Input[str]] = None,
                              resource_group_name: Optional[pulumi.Input[str]] = None,
                              test_base_account_name: Optional[pulumi.Input[str]] = None,
                              opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetCustomerEventResult]:
    """
    Gets a Test Base CustomerEvent.
    API Version: 2022-04-01-preview.


    :param str customer_event_name: The resource name of the Test Base Customer event.
    :param str resource_group_name: The name of the resource group that contains the resource.
    :param str test_base_account_name: The resource name of the Test Base Account.
    """
    ...
