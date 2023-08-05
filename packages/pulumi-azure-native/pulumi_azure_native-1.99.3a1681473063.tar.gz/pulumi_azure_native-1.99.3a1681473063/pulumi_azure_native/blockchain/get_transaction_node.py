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
    'GetTransactionNodeResult',
    'AwaitableGetTransactionNodeResult',
    'get_transaction_node',
    'get_transaction_node_output',
]

@pulumi.output_type
class GetTransactionNodeResult:
    """
    Payload of the transaction node which is the request/response of the resource provider.
    """
    def __init__(__self__, dns=None, firewall_rules=None, id=None, location=None, name=None, password=None, provisioning_state=None, public_key=None, type=None, user_name=None):
        if dns and not isinstance(dns, str):
            raise TypeError("Expected argument 'dns' to be a str")
        pulumi.set(__self__, "dns", dns)
        if firewall_rules and not isinstance(firewall_rules, list):
            raise TypeError("Expected argument 'firewall_rules' to be a list")
        pulumi.set(__self__, "firewall_rules", firewall_rules)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if location and not isinstance(location, str):
            raise TypeError("Expected argument 'location' to be a str")
        pulumi.set(__self__, "location", location)
        if name and not isinstance(name, str):
            raise TypeError("Expected argument 'name' to be a str")
        pulumi.set(__self__, "name", name)
        if password and not isinstance(password, str):
            raise TypeError("Expected argument 'password' to be a str")
        pulumi.set(__self__, "password", password)
        if provisioning_state and not isinstance(provisioning_state, str):
            raise TypeError("Expected argument 'provisioning_state' to be a str")
        pulumi.set(__self__, "provisioning_state", provisioning_state)
        if public_key and not isinstance(public_key, str):
            raise TypeError("Expected argument 'public_key' to be a str")
        pulumi.set(__self__, "public_key", public_key)
        if type and not isinstance(type, str):
            raise TypeError("Expected argument 'type' to be a str")
        pulumi.set(__self__, "type", type)
        if user_name and not isinstance(user_name, str):
            raise TypeError("Expected argument 'user_name' to be a str")
        pulumi.set(__self__, "user_name", user_name)

    @property
    @pulumi.getter
    def dns(self) -> str:
        """
        Gets or sets the transaction node dns endpoint.
        """
        return pulumi.get(self, "dns")

    @property
    @pulumi.getter(name="firewallRules")
    def firewall_rules(self) -> Optional[Sequence['outputs.FirewallRuleResponse']]:
        """
        Gets or sets the firewall rules.
        """
        return pulumi.get(self, "firewall_rules")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        Fully qualified resource Id of the resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def location(self) -> Optional[str]:
        """
        Gets or sets the transaction node location.
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def password(self) -> Optional[str]:
        """
        Sets the transaction node dns endpoint basic auth password.
        """
        return pulumi.get(self, "password")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> str:
        """
        Gets or sets the blockchain member provision state.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> str:
        """
        Gets or sets the transaction node public key.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        The type of the service - e.g. "Microsoft.Blockchain"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userName")
    def user_name(self) -> str:
        """
        Gets or sets the transaction node dns endpoint basic auth user name.
        """
        return pulumi.get(self, "user_name")


class AwaitableGetTransactionNodeResult(GetTransactionNodeResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetTransactionNodeResult(
            dns=self.dns,
            firewall_rules=self.firewall_rules,
            id=self.id,
            location=self.location,
            name=self.name,
            password=self.password,
            provisioning_state=self.provisioning_state,
            public_key=self.public_key,
            type=self.type,
            user_name=self.user_name)


def get_transaction_node(blockchain_member_name: Optional[str] = None,
                         resource_group_name: Optional[str] = None,
                         transaction_node_name: Optional[str] = None,
                         opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetTransactionNodeResult:
    """
    Get the details of the transaction node.
    API Version: 2018-06-01-preview.


    :param str blockchain_member_name: Blockchain member name.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str transaction_node_name: Transaction node name.
    """
    __args__ = dict()
    __args__['blockchainMemberName'] = blockchain_member_name
    __args__['resourceGroupName'] = resource_group_name
    __args__['transactionNodeName'] = transaction_node_name
    opts = pulumi.InvokeOptions.merge(_utilities.get_invoke_opts_defaults(), opts)
    __ret__ = pulumi.runtime.invoke('azure-native:blockchain:getTransactionNode', __args__, opts=opts, typ=GetTransactionNodeResult).value

    return AwaitableGetTransactionNodeResult(
        dns=__ret__.dns,
        firewall_rules=__ret__.firewall_rules,
        id=__ret__.id,
        location=__ret__.location,
        name=__ret__.name,
        password=__ret__.password,
        provisioning_state=__ret__.provisioning_state,
        public_key=__ret__.public_key,
        type=__ret__.type,
        user_name=__ret__.user_name)


@_utilities.lift_output_func(get_transaction_node)
def get_transaction_node_output(blockchain_member_name: Optional[pulumi.Input[str]] = None,
                                resource_group_name: Optional[pulumi.Input[str]] = None,
                                transaction_node_name: Optional[pulumi.Input[str]] = None,
                                opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetTransactionNodeResult]:
    """
    Get the details of the transaction node.
    API Version: 2018-06-01-preview.


    :param str blockchain_member_name: Blockchain member name.
    :param str resource_group_name: The name of the resource group that contains the resource. You can obtain this value from the Azure Resource Manager API or the portal.
    :param str transaction_node_name: Transaction node name.
    """
    ...
