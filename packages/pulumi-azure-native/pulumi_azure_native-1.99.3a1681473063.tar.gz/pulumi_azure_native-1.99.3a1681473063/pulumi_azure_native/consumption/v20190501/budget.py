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
from ._inputs import *

__all__ = ['BudgetArgs', 'Budget']

@pulumi.input_type
class BudgetArgs:
    def __init__(__self__, *,
                 amount: pulumi.Input[float],
                 category: pulumi.Input[Union[str, 'CategoryType']],
                 scope: pulumi.Input[str],
                 time_grain: pulumi.Input[Union[str, 'TimeGrainType']],
                 time_period: pulumi.Input['BudgetTimePeriodArgs'],
                 budget_name: Optional[pulumi.Input[str]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input['FilterArgs']] = None,
                 notifications: Optional[pulumi.Input[Mapping[str, pulumi.Input['NotificationArgs']]]] = None):
        """
        The set of arguments for constructing a Budget resource.
        :param pulumi.Input[float] amount: The total amount of cost to track with the budget
        :param pulumi.Input[Union[str, 'CategoryType']] category: The category of the budget, whether the budget tracks cost or usage.
        :param pulumi.Input[str] scope: The scope associated with budget operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope.
        :param pulumi.Input[Union[str, 'TimeGrainType']] time_grain: The time covered by a budget. Tracking of the amount will be reset based on the time grain.
        :param pulumi.Input['BudgetTimePeriodArgs'] time_period: Has start and end date of the budget. The start date must be first of the month and should be less than the end date. Budget start date must be on or after June 1, 2017. Future start date should not be more than three months. Past start date should  be selected within the timegrain period. There are no restrictions on the end date.
        :param pulumi.Input[str] budget_name: Budget Name.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input['FilterArgs'] filter: May be used to filter budgets by user-specified dimensions and/or tags.
        :param pulumi.Input[Mapping[str, pulumi.Input['NotificationArgs']]] notifications: Dictionary of notifications associated with the budget. Budget can have up to five notifications.
        """
        pulumi.set(__self__, "amount", amount)
        pulumi.set(__self__, "category", category)
        pulumi.set(__self__, "scope", scope)
        pulumi.set(__self__, "time_grain", time_grain)
        pulumi.set(__self__, "time_period", time_period)
        if budget_name is not None:
            pulumi.set(__self__, "budget_name", budget_name)
        if e_tag is not None:
            pulumi.set(__self__, "e_tag", e_tag)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if notifications is not None:
            pulumi.set(__self__, "notifications", notifications)

    @property
    @pulumi.getter
    def amount(self) -> pulumi.Input[float]:
        """
        The total amount of cost to track with the budget
        """
        return pulumi.get(self, "amount")

    @amount.setter
    def amount(self, value: pulumi.Input[float]):
        pulumi.set(self, "amount", value)

    @property
    @pulumi.getter
    def category(self) -> pulumi.Input[Union[str, 'CategoryType']]:
        """
        The category of the budget, whether the budget tracks cost or usage.
        """
        return pulumi.get(self, "category")

    @category.setter
    def category(self, value: pulumi.Input[Union[str, 'CategoryType']]):
        pulumi.set(self, "category", value)

    @property
    @pulumi.getter
    def scope(self) -> pulumi.Input[str]:
        """
        The scope associated with budget operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope.
        """
        return pulumi.get(self, "scope")

    @scope.setter
    def scope(self, value: pulumi.Input[str]):
        pulumi.set(self, "scope", value)

    @property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> pulumi.Input[Union[str, 'TimeGrainType']]:
        """
        The time covered by a budget. Tracking of the amount will be reset based on the time grain.
        """
        return pulumi.get(self, "time_grain")

    @time_grain.setter
    def time_grain(self, value: pulumi.Input[Union[str, 'TimeGrainType']]):
        pulumi.set(self, "time_grain", value)

    @property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> pulumi.Input['BudgetTimePeriodArgs']:
        """
        Has start and end date of the budget. The start date must be first of the month and should be less than the end date. Budget start date must be on or after June 1, 2017. Future start date should not be more than three months. Past start date should  be selected within the timegrain period. There are no restrictions on the end date.
        """
        return pulumi.get(self, "time_period")

    @time_period.setter
    def time_period(self, value: pulumi.Input['BudgetTimePeriodArgs']):
        pulumi.set(self, "time_period", value)

    @property
    @pulumi.getter(name="budgetName")
    def budget_name(self) -> Optional[pulumi.Input[str]]:
        """
        Budget Name.
        """
        return pulumi.get(self, "budget_name")

    @budget_name.setter
    def budget_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "budget_name", value)

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> Optional[pulumi.Input[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @e_tag.setter
    def e_tag(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "e_tag", value)

    @property
    @pulumi.getter
    def filter(self) -> Optional[pulumi.Input['FilterArgs']]:
        """
        May be used to filter budgets by user-specified dimensions and/or tags.
        """
        return pulumi.get(self, "filter")

    @filter.setter
    def filter(self, value: Optional[pulumi.Input['FilterArgs']]):
        pulumi.set(self, "filter", value)

    @property
    @pulumi.getter
    def notifications(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input['NotificationArgs']]]]:
        """
        Dictionary of notifications associated with the budget. Budget can have up to five notifications.
        """
        return pulumi.get(self, "notifications")

    @notifications.setter
    def notifications(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input['NotificationArgs']]]]):
        pulumi.set(self, "notifications", value)


warnings.warn("""Version 2019-05-01 will be removed in v2 of the provider.""", DeprecationWarning)


class Budget(pulumi.CustomResource):
    warnings.warn("""Version 2019-05-01 will be removed in v2 of the provider.""", DeprecationWarning)

    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 amount: Optional[pulumi.Input[float]] = None,
                 budget_name: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[Union[str, 'CategoryType']]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[pulumi.InputType['FilterArgs']]] = None,
                 notifications: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['NotificationArgs']]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 time_grain: Optional[pulumi.Input[Union[str, 'TimeGrainType']]] = None,
                 time_period: Optional[pulumi.Input[pulumi.InputType['BudgetTimePeriodArgs']]] = None,
                 __props__=None):
        """
        A budget resource.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[float] amount: The total amount of cost to track with the budget
        :param pulumi.Input[str] budget_name: Budget Name.
        :param pulumi.Input[Union[str, 'CategoryType']] category: The category of the budget, whether the budget tracks cost or usage.
        :param pulumi.Input[str] e_tag: eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        :param pulumi.Input[pulumi.InputType['FilterArgs']] filter: May be used to filter budgets by user-specified dimensions and/or tags.
        :param pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['NotificationArgs']]]] notifications: Dictionary of notifications associated with the budget. Budget can have up to five notifications.
        :param pulumi.Input[str] scope: The scope associated with budget operations. This includes '/subscriptions/{subscriptionId}/' for subscription scope, '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}' for resourceGroup scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}' for Billing Account scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/departments/{departmentId}' for Department scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/enrollmentAccounts/{enrollmentAccountId}' for EnrollmentAccount scope, '/providers/Microsoft.Management/managementGroups/{managementGroupId}' for Management Group scope, '/providers/Microsoft.Billing/billingAccounts/{billingAccountId}/billingProfiles/{billingProfileId}' for billingProfile scope, 'providers/Microsoft.Billing/billingAccounts/{billingAccountId}/invoiceSections/{invoiceSectionId}' for invoiceSection scope.
        :param pulumi.Input[Union[str, 'TimeGrainType']] time_grain: The time covered by a budget. Tracking of the amount will be reset based on the time grain.
        :param pulumi.Input[pulumi.InputType['BudgetTimePeriodArgs']] time_period: Has start and end date of the budget. The start date must be first of the month and should be less than the end date. Budget start date must be on or after June 1, 2017. Future start date should not be more than three months. Past start date should  be selected within the timegrain period. There are no restrictions on the end date.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: BudgetArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        A budget resource.

        :param str resource_name: The name of the resource.
        :param BudgetArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(BudgetArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 amount: Optional[pulumi.Input[float]] = None,
                 budget_name: Optional[pulumi.Input[str]] = None,
                 category: Optional[pulumi.Input[Union[str, 'CategoryType']]] = None,
                 e_tag: Optional[pulumi.Input[str]] = None,
                 filter: Optional[pulumi.Input[pulumi.InputType['FilterArgs']]] = None,
                 notifications: Optional[pulumi.Input[Mapping[str, pulumi.Input[pulumi.InputType['NotificationArgs']]]]] = None,
                 scope: Optional[pulumi.Input[str]] = None,
                 time_grain: Optional[pulumi.Input[Union[str, 'TimeGrainType']]] = None,
                 time_period: Optional[pulumi.Input[pulumi.InputType['BudgetTimePeriodArgs']]] = None,
                 __props__=None):
        pulumi.log.warn("""Budget is deprecated: Version 2019-05-01 will be removed in v2 of the provider.""")
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = BudgetArgs.__new__(BudgetArgs)

            if amount is None and not opts.urn:
                raise TypeError("Missing required property 'amount'")
            __props__.__dict__["amount"] = amount
            __props__.__dict__["budget_name"] = budget_name
            if category is None and not opts.urn:
                raise TypeError("Missing required property 'category'")
            __props__.__dict__["category"] = category
            __props__.__dict__["e_tag"] = e_tag
            __props__.__dict__["filter"] = filter
            __props__.__dict__["notifications"] = notifications
            if scope is None and not opts.urn:
                raise TypeError("Missing required property 'scope'")
            __props__.__dict__["scope"] = scope
            if time_grain is None and not opts.urn:
                raise TypeError("Missing required property 'time_grain'")
            __props__.__dict__["time_grain"] = time_grain
            if time_period is None and not opts.urn:
                raise TypeError("Missing required property 'time_period'")
            __props__.__dict__["time_period"] = time_period
            __props__.__dict__["current_spend"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:consumption:Budget"), pulumi.Alias(type_="azure-native:consumption/v20190101:Budget"), pulumi.Alias(type_="azure-native:consumption/v20190401preview:Budget"), pulumi.Alias(type_="azure-native:consumption/v20190501preview:Budget"), pulumi.Alias(type_="azure-native:consumption/v20190601:Budget"), pulumi.Alias(type_="azure-native:consumption/v20191001:Budget"), pulumi.Alias(type_="azure-native:consumption/v20191101:Budget"), pulumi.Alias(type_="azure-native:consumption/v20210501:Budget"), pulumi.Alias(type_="azure-native:consumption/v20211001:Budget"), pulumi.Alias(type_="azure-native:consumption/v20220901:Budget")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(Budget, __self__).__init__(
            'azure-native:consumption/v20190501:Budget',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'Budget':
        """
        Get an existing Budget resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = BudgetArgs.__new__(BudgetArgs)

        __props__.__dict__["amount"] = None
        __props__.__dict__["category"] = None
        __props__.__dict__["current_spend"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["filter"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["notifications"] = None
        __props__.__dict__["time_grain"] = None
        __props__.__dict__["time_period"] = None
        __props__.__dict__["type"] = None
        return Budget(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def amount(self) -> pulumi.Output[float]:
        """
        The total amount of cost to track with the budget
        """
        return pulumi.get(self, "amount")

    @property
    @pulumi.getter
    def category(self) -> pulumi.Output[str]:
        """
        The category of the budget, whether the budget tracks cost or usage.
        """
        return pulumi.get(self, "category")

    @property
    @pulumi.getter(name="currentSpend")
    def current_spend(self) -> pulumi.Output['outputs.CurrentSpendResponse']:
        """
        The current amount of cost which is being tracked for a budget.
        """
        return pulumi.get(self, "current_spend")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[Optional[str]]:
        """
        eTag of the resource. To handle concurrent update scenario, this field will be used to determine whether the user is updating the latest version or not.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def filter(self) -> pulumi.Output[Optional['outputs.FilterResponse']]:
        """
        May be used to filter budgets by user-specified dimensions and/or tags.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def notifications(self) -> pulumi.Output[Optional[Mapping[str, 'outputs.NotificationResponse']]]:
        """
        Dictionary of notifications associated with the budget. Budget can have up to five notifications.
        """
        return pulumi.get(self, "notifications")

    @property
    @pulumi.getter(name="timeGrain")
    def time_grain(self) -> pulumi.Output[str]:
        """
        The time covered by a budget. Tracking of the amount will be reset based on the time grain.
        """
        return pulumi.get(self, "time_grain")

    @property
    @pulumi.getter(name="timePeriod")
    def time_period(self) -> pulumi.Output['outputs.BudgetTimePeriodResponse']:
        """
        Has start and end date of the budget. The start date must be first of the month and should be less than the end date. Budget start date must be on or after June 1, 2017. Future start date should not be more than three months. Past start date should  be selected within the timegrain period. There are no restrictions on the end date.
        """
        return pulumi.get(self, "time_period")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type.
        """
        return pulumi.get(self, "type")

