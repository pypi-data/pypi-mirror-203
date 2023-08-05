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
    'BudgetTimePeriodResponse',
    'CurrentSpendResponse',
    'KpiPropertiesResponse',
    'NotificationResponse',
    'PivotPropertiesResponse',
    'ReportConfigAggregationResponse',
    'ReportConfigComparisonExpressionResponse',
    'ReportConfigDatasetConfigurationResponse',
    'ReportConfigDatasetResponse',
    'ReportConfigFilterResponse',
    'ReportConfigGroupingResponse',
    'ReportConfigSortingResponse',
    'ReportConfigTimePeriodResponse',
]

@pulumi.output_type
class BudgetTimePeriodResponse(dict):
    """
    The start and end date for a budget.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "startDate":
            suggest = "start_date"
        elif key == "endDate":
            suggest = "end_date"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in BudgetTimePeriodResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        BudgetTimePeriodResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        BudgetTimePeriodResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 start_date: str,
                 end_date: Optional[str] = None):
        """
        The start and end date for a budget.
        :param str start_date: The start date for the budget.
        :param str end_date: The end date for the budget. If not provided, we default this to 10 years from the start date.
        """
        pulumi.set(__self__, "start_date", start_date)
        if end_date is not None:
            pulumi.set(__self__, "end_date", end_date)

    @property
    @pulumi.getter(name="startDate")
    def start_date(self) -> str:
        """
        The start date for the budget.
        """
        return pulumi.get(self, "start_date")

    @property
    @pulumi.getter(name="endDate")
    def end_date(self) -> Optional[str]:
        """
        The end date for the budget. If not provided, we default this to 10 years from the start date.
        """
        return pulumi.get(self, "end_date")


@pulumi.output_type
class CurrentSpendResponse(dict):
    """
    The current amount of cost which is being tracked for a budget.
    """
    def __init__(__self__, *,
                 amount: float,
                 unit: str):
        """
        The current amount of cost which is being tracked for a budget.
        :param float amount: The total amount of cost which is being tracked by the budget.
        :param str unit: The unit of measure for the budget amount.
        """
        pulumi.set(__self__, "amount", amount)
        pulumi.set(__self__, "unit", unit)

    @property
    @pulumi.getter
    def amount(self) -> float:
        """
        The total amount of cost which is being tracked by the budget.
        """
        return pulumi.get(self, "amount")

    @property
    @pulumi.getter
    def unit(self) -> str:
        """
        The unit of measure for the budget amount.
        """
        return pulumi.get(self, "unit")


@pulumi.output_type
class KpiPropertiesResponse(dict):
    """
    Each KPI must contain a 'type' and 'enabled' key.
    """
    def __init__(__self__, *,
                 enabled: Optional[bool] = None,
                 id: Optional[str] = None,
                 type: Optional[str] = None):
        """
        Each KPI must contain a 'type' and 'enabled' key.
        :param bool enabled: show the KPI in the UI?
        :param str id: ID of resource related to metric (budget).
        :param str type: KPI type (Forecast, Budget).
        """
        if enabled is not None:
            pulumi.set(__self__, "enabled", enabled)
        if id is not None:
            pulumi.set(__self__, "id", id)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def enabled(self) -> Optional[bool]:
        """
        show the KPI in the UI?
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def id(self) -> Optional[str]:
        """
        ID of resource related to metric (budget).
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        KPI type (Forecast, Budget).
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class NotificationResponse(dict):
    """
    The notification associated with a budget.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "contactEmails":
            suggest = "contact_emails"
        elif key == "contactGroups":
            suggest = "contact_groups"
        elif key == "contactRoles":
            suggest = "contact_roles"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in NotificationResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        NotificationResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        NotificationResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 contact_emails: Sequence[str],
                 enabled: bool,
                 operator: str,
                 threshold: float,
                 contact_groups: Optional[Sequence[str]] = None,
                 contact_roles: Optional[Sequence[str]] = None):
        """
        The notification associated with a budget.
        :param Sequence[str] contact_emails: Email addresses to send the budget notification to when the threshold is exceeded.
        :param bool enabled: The notification is enabled or not.
        :param str operator: The comparison operator.
        :param float threshold: Threshold value associated with a notification. Notification is sent when the cost exceeded the threshold. It is always percent and has to be between 0 and 1000.
        :param Sequence[str] contact_groups: Action groups to send the budget notification to when the threshold is exceeded.
        :param Sequence[str] contact_roles: Contact roles to send the budget notification to when the threshold is exceeded.
        """
        pulumi.set(__self__, "contact_emails", contact_emails)
        pulumi.set(__self__, "enabled", enabled)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "threshold", threshold)
        if contact_groups is not None:
            pulumi.set(__self__, "contact_groups", contact_groups)
        if contact_roles is not None:
            pulumi.set(__self__, "contact_roles", contact_roles)

    @property
    @pulumi.getter(name="contactEmails")
    def contact_emails(self) -> Sequence[str]:
        """
        Email addresses to send the budget notification to when the threshold is exceeded.
        """
        return pulumi.get(self, "contact_emails")

    @property
    @pulumi.getter
    def enabled(self) -> bool:
        """
        The notification is enabled or not.
        """
        return pulumi.get(self, "enabled")

    @property
    @pulumi.getter
    def operator(self) -> str:
        """
        The comparison operator.
        """
        return pulumi.get(self, "operator")

    @property
    @pulumi.getter
    def threshold(self) -> float:
        """
        Threshold value associated with a notification. Notification is sent when the cost exceeded the threshold. It is always percent and has to be between 0 and 1000.
        """
        return pulumi.get(self, "threshold")

    @property
    @pulumi.getter(name="contactGroups")
    def contact_groups(self) -> Optional[Sequence[str]]:
        """
        Action groups to send the budget notification to when the threshold is exceeded.
        """
        return pulumi.get(self, "contact_groups")

    @property
    @pulumi.getter(name="contactRoles")
    def contact_roles(self) -> Optional[Sequence[str]]:
        """
        Contact roles to send the budget notification to when the threshold is exceeded.
        """
        return pulumi.get(self, "contact_roles")


@pulumi.output_type
class PivotPropertiesResponse(dict):
    """
    Each pivot must contain a 'type' and 'name'.
    """
    def __init__(__self__, *,
                 name: Optional[str] = None,
                 type: Optional[str] = None):
        """
        Each pivot must contain a 'type' and 'name'.
        :param str name: Data field to show in view.
        :param str type: Data type to show in view.
        """
        if name is not None:
            pulumi.set(__self__, "name", name)
        if type is not None:
            pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> Optional[str]:
        """
        Data field to show in view.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> Optional[str]:
        """
        Data type to show in view.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ReportConfigAggregationResponse(dict):
    """
    The aggregation expression to be used in the report.
    """
    def __init__(__self__, *,
                 function: str,
                 name: str):
        """
        The aggregation expression to be used in the report.
        :param str function: The name of the aggregation function to use.
        :param str name: The name of the column to aggregate.
        """
        pulumi.set(__self__, "function", function)
        pulumi.set(__self__, "name", name)

    @property
    @pulumi.getter
    def function(self) -> str:
        """
        The name of the aggregation function to use.
        """
        return pulumi.get(self, "function")

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the column to aggregate.
        """
        return pulumi.get(self, "name")


@pulumi.output_type
class ReportConfigComparisonExpressionResponse(dict):
    """
    The comparison expression to be used in the report.
    """
    def __init__(__self__, *,
                 name: str,
                 operator: str,
                 values: Sequence[str]):
        """
        The comparison expression to be used in the report.
        :param str name: The name of the column to use in comparison.
        :param str operator: The operator to use for comparison.
        :param Sequence[str] values: Array of values to use for comparison
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "operator", operator)
        pulumi.set(__self__, "values", values)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the column to use in comparison.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def operator(self) -> str:
        """
        The operator to use for comparison.
        """
        return pulumi.get(self, "operator")

    @property
    @pulumi.getter
    def values(self) -> Sequence[str]:
        """
        Array of values to use for comparison
        """
        return pulumi.get(self, "values")


@pulumi.output_type
class ReportConfigDatasetConfigurationResponse(dict):
    """
    The configuration of dataset in the report.
    """
    def __init__(__self__, *,
                 columns: Optional[Sequence[str]] = None):
        """
        The configuration of dataset in the report.
        :param Sequence[str] columns: Array of column names to be included in the report. Any valid report column name is allowed. If not provided, then report includes all columns.
        """
        if columns is not None:
            pulumi.set(__self__, "columns", columns)

    @property
    @pulumi.getter
    def columns(self) -> Optional[Sequence[str]]:
        """
        Array of column names to be included in the report. Any valid report column name is allowed. If not provided, then report includes all columns.
        """
        return pulumi.get(self, "columns")


@pulumi.output_type
class ReportConfigDatasetResponse(dict):
    """
    The definition of data present in the report.
    """
    def __init__(__self__, *,
                 aggregation: Optional[Mapping[str, 'outputs.ReportConfigAggregationResponse']] = None,
                 configuration: Optional['outputs.ReportConfigDatasetConfigurationResponse'] = None,
                 filter: Optional['outputs.ReportConfigFilterResponse'] = None,
                 granularity: Optional[str] = None,
                 grouping: Optional[Sequence['outputs.ReportConfigGroupingResponse']] = None,
                 sorting: Optional[Sequence['outputs.ReportConfigSortingResponse']] = None):
        """
        The definition of data present in the report.
        :param Mapping[str, 'ReportConfigAggregationResponse'] aggregation: Dictionary of aggregation expression to use in the report. The key of each item in the dictionary is the alias for the aggregated column. Report can have up to 2 aggregation clauses.
        :param 'ReportConfigDatasetConfigurationResponse' configuration: Has configuration information for the data in the report. The configuration will be ignored if aggregation and grouping are provided.
        :param 'ReportConfigFilterResponse' filter: Has filter expression to use in the report.
        :param str granularity: The granularity of rows in the report.
        :param Sequence['ReportConfigGroupingResponse'] grouping: Array of group by expression to use in the report. Report can have up to 2 group by clauses.
        :param Sequence['ReportConfigSortingResponse'] sorting: Array of order by expression to use in the report.
        """
        if aggregation is not None:
            pulumi.set(__self__, "aggregation", aggregation)
        if configuration is not None:
            pulumi.set(__self__, "configuration", configuration)
        if filter is not None:
            pulumi.set(__self__, "filter", filter)
        if granularity is not None:
            pulumi.set(__self__, "granularity", granularity)
        if grouping is not None:
            pulumi.set(__self__, "grouping", grouping)
        if sorting is not None:
            pulumi.set(__self__, "sorting", sorting)

    @property
    @pulumi.getter
    def aggregation(self) -> Optional[Mapping[str, 'outputs.ReportConfigAggregationResponse']]:
        """
        Dictionary of aggregation expression to use in the report. The key of each item in the dictionary is the alias for the aggregated column. Report can have up to 2 aggregation clauses.
        """
        return pulumi.get(self, "aggregation")

    @property
    @pulumi.getter
    def configuration(self) -> Optional['outputs.ReportConfigDatasetConfigurationResponse']:
        """
        Has configuration information for the data in the report. The configuration will be ignored if aggregation and grouping are provided.
        """
        return pulumi.get(self, "configuration")

    @property
    @pulumi.getter
    def filter(self) -> Optional['outputs.ReportConfigFilterResponse']:
        """
        Has filter expression to use in the report.
        """
        return pulumi.get(self, "filter")

    @property
    @pulumi.getter
    def granularity(self) -> Optional[str]:
        """
        The granularity of rows in the report.
        """
        return pulumi.get(self, "granularity")

    @property
    @pulumi.getter
    def grouping(self) -> Optional[Sequence['outputs.ReportConfigGroupingResponse']]:
        """
        Array of group by expression to use in the report. Report can have up to 2 group by clauses.
        """
        return pulumi.get(self, "grouping")

    @property
    @pulumi.getter
    def sorting(self) -> Optional[Sequence['outputs.ReportConfigSortingResponse']]:
        """
        Array of order by expression to use in the report.
        """
        return pulumi.get(self, "sorting")


@pulumi.output_type
class ReportConfigFilterResponse(dict):
    """
    The filter expression to be used in the report.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "and":
            suggest = "and_"
        elif key == "not":
            suggest = "not_"
        elif key == "or":
            suggest = "or_"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReportConfigFilterResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReportConfigFilterResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReportConfigFilterResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 and_: Optional[Sequence['outputs.ReportConfigFilterResponse']] = None,
                 dimension: Optional['outputs.ReportConfigComparisonExpressionResponse'] = None,
                 not_: Optional['outputs.ReportConfigFilterResponse'] = None,
                 or_: Optional[Sequence['outputs.ReportConfigFilterResponse']] = None,
                 tag: Optional['outputs.ReportConfigComparisonExpressionResponse'] = None):
        """
        The filter expression to be used in the report.
        :param Sequence['ReportConfigFilterResponse'] and_: The logical "AND" expression. Must have at least 2 items.
        :param 'ReportConfigComparisonExpressionResponse' dimension: Has comparison expression for a dimension
        :param 'ReportConfigFilterResponse' not_: The logical "NOT" expression.
        :param Sequence['ReportConfigFilterResponse'] or_: The logical "OR" expression. Must have at least 2 items.
        :param 'ReportConfigComparisonExpressionResponse' tag: Has comparison expression for a tag
        """
        if and_ is not None:
            pulumi.set(__self__, "and_", and_)
        if dimension is not None:
            pulumi.set(__self__, "dimension", dimension)
        if not_ is not None:
            pulumi.set(__self__, "not_", not_)
        if or_ is not None:
            pulumi.set(__self__, "or_", or_)
        if tag is not None:
            pulumi.set(__self__, "tag", tag)

    @property
    @pulumi.getter(name="and")
    def and_(self) -> Optional[Sequence['outputs.ReportConfigFilterResponse']]:
        """
        The logical "AND" expression. Must have at least 2 items.
        """
        return pulumi.get(self, "and_")

    @property
    @pulumi.getter
    def dimension(self) -> Optional['outputs.ReportConfigComparisonExpressionResponse']:
        """
        Has comparison expression for a dimension
        """
        return pulumi.get(self, "dimension")

    @property
    @pulumi.getter(name="not")
    def not_(self) -> Optional['outputs.ReportConfigFilterResponse']:
        """
        The logical "NOT" expression.
        """
        return pulumi.get(self, "not_")

    @property
    @pulumi.getter(name="or")
    def or_(self) -> Optional[Sequence['outputs.ReportConfigFilterResponse']]:
        """
        The logical "OR" expression. Must have at least 2 items.
        """
        return pulumi.get(self, "or_")

    @property
    @pulumi.getter
    def tag(self) -> Optional['outputs.ReportConfigComparisonExpressionResponse']:
        """
        Has comparison expression for a tag
        """
        return pulumi.get(self, "tag")


@pulumi.output_type
class ReportConfigGroupingResponse(dict):
    """
    The group by expression to be used in the report.
    """
    def __init__(__self__, *,
                 name: str,
                 type: str):
        """
        The group by expression to be used in the report.
        :param str name: The name of the column to group. This version supports subscription lowest possible grain.
        :param str type: Has type of the column to group.
        """
        pulumi.set(__self__, "name", name)
        pulumi.set(__self__, "type", type)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the column to group. This version supports subscription lowest possible grain.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def type(self) -> str:
        """
        Has type of the column to group.
        """
        return pulumi.get(self, "type")


@pulumi.output_type
class ReportConfigSortingResponse(dict):
    """
    The order by expression to be used in the report.
    """
    def __init__(__self__, *,
                 name: str,
                 direction: Optional[str] = None):
        """
        The order by expression to be used in the report.
        :param str name: The name of the column to sort.
        :param str direction: Direction of sort.
        """
        pulumi.set(__self__, "name", name)
        if direction is not None:
            pulumi.set(__self__, "direction", direction)

    @property
    @pulumi.getter
    def name(self) -> str:
        """
        The name of the column to sort.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def direction(self) -> Optional[str]:
        """
        Direction of sort.
        """
        return pulumi.get(self, "direction")


@pulumi.output_type
class ReportConfigTimePeriodResponse(dict):
    """
    The start and end date for pulling data for the report.
    """
    @staticmethod
    def __key_warning(key: str):
        suggest = None
        if key == "from":
            suggest = "from_"

        if suggest:
            pulumi.log.warn(f"Key '{key}' not found in ReportConfigTimePeriodResponse. Access the value via the '{suggest}' property getter instead.")

    def __getitem__(self, key: str) -> Any:
        ReportConfigTimePeriodResponse.__key_warning(key)
        return super().__getitem__(key)

    def get(self, key: str, default = None) -> Any:
        ReportConfigTimePeriodResponse.__key_warning(key)
        return super().get(key, default)

    def __init__(__self__, *,
                 from_: str,
                 to: str):
        """
        The start and end date for pulling data for the report.
        :param str from_: The start date to pull data from.
        :param str to: The end date to pull data to.
        """
        pulumi.set(__self__, "from_", from_)
        pulumi.set(__self__, "to", to)

    @property
    @pulumi.getter(name="from")
    def from_(self) -> str:
        """
        The start date to pull data from.
        """
        return pulumi.get(self, "from_")

    @property
    @pulumi.getter
    def to(self) -> str:
        """
        The end date to pull data to.
        """
        return pulumi.get(self, "to")


