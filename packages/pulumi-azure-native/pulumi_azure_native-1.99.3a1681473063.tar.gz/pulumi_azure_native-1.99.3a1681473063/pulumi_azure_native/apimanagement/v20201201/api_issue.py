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

__all__ = ['ApiIssueArgs', 'ApiIssue']

@pulumi.input_type
class ApiIssueArgs:
    def __init__(__self__, *,
                 api_id: pulumi.Input[str],
                 description: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 service_name: pulumi.Input[str],
                 title: pulumi.Input[str],
                 user_id: pulumi.Input[str],
                 created_date: Optional[pulumi.Input[str]] = None,
                 issue_id: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'State']]] = None):
        """
        The set of arguments for constructing a ApiIssue resource.
        :param pulumi.Input[str] api_id: A resource identifier for the API the issue was created for.
        :param pulumi.Input[str] description: Text describing the issue.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[str] title: The issue title.
        :param pulumi.Input[str] user_id: A resource identifier for the user created the issue.
        :param pulumi.Input[str] created_date: Date and time when the issue was created.
        :param pulumi.Input[str] issue_id: Issue identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[Union[str, 'State']] state: Status of the issue.
        """
        pulumi.set(__self__, "api_id", api_id)
        pulumi.set(__self__, "description", description)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        pulumi.set(__self__, "service_name", service_name)
        pulumi.set(__self__, "title", title)
        pulumi.set(__self__, "user_id", user_id)
        if created_date is not None:
            pulumi.set(__self__, "created_date", created_date)
        if issue_id is not None:
            pulumi.set(__self__, "issue_id", issue_id)
        if state is not None:
            pulumi.set(__self__, "state", state)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Input[str]:
        """
        A resource identifier for the API the issue was created for.
        """
        return pulumi.get(self, "api_id")

    @api_id.setter
    def api_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "api_id", value)

    @property
    @pulumi.getter
    def description(self) -> pulumi.Input[str]:
        """
        Text describing the issue.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: pulumi.Input[str]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="serviceName")
    def service_name(self) -> pulumi.Input[str]:
        """
        The name of the API Management service.
        """
        return pulumi.get(self, "service_name")

    @service_name.setter
    def service_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "service_name", value)

    @property
    @pulumi.getter
    def title(self) -> pulumi.Input[str]:
        """
        The issue title.
        """
        return pulumi.get(self, "title")

    @title.setter
    def title(self, value: pulumi.Input[str]):
        pulumi.set(self, "title", value)

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Input[str]:
        """
        A resource identifier for the user created the issue.
        """
        return pulumi.get(self, "user_id")

    @user_id.setter
    def user_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "user_id", value)

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> Optional[pulumi.Input[str]]:
        """
        Date and time when the issue was created.
        """
        return pulumi.get(self, "created_date")

    @created_date.setter
    def created_date(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_date", value)

    @property
    @pulumi.getter(name="issueId")
    def issue_id(self) -> Optional[pulumi.Input[str]]:
        """
        Issue identifier. Must be unique in the current API Management service instance.
        """
        return pulumi.get(self, "issue_id")

    @issue_id.setter
    def issue_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "issue_id", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[Union[str, 'State']]]:
        """
        Status of the issue.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[Union[str, 'State']]]):
        pulumi.set(self, "state", value)


class ApiIssue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 created_date: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 issue_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'State']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Issue Contract details.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] api_id: A resource identifier for the API the issue was created for.
        :param pulumi.Input[str] created_date: Date and time when the issue was created.
        :param pulumi.Input[str] description: Text describing the issue.
        :param pulumi.Input[str] issue_id: Issue identifier. Must be unique in the current API Management service instance.
        :param pulumi.Input[str] resource_group_name: The name of the resource group.
        :param pulumi.Input[str] service_name: The name of the API Management service.
        :param pulumi.Input[Union[str, 'State']] state: Status of the issue.
        :param pulumi.Input[str] title: The issue title.
        :param pulumi.Input[str] user_id: A resource identifier for the user created the issue.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ApiIssueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Issue Contract details.

        :param str resource_name: The name of the resource.
        :param ApiIssueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ApiIssueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 api_id: Optional[pulumi.Input[str]] = None,
                 created_date: Optional[pulumi.Input[str]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 issue_id: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 service_name: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[Union[str, 'State']]] = None,
                 title: Optional[pulumi.Input[str]] = None,
                 user_id: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = ApiIssueArgs.__new__(ApiIssueArgs)

            if api_id is None and not opts.urn:
                raise TypeError("Missing required property 'api_id'")
            __props__.__dict__["api_id"] = api_id
            __props__.__dict__["created_date"] = created_date
            if description is None and not opts.urn:
                raise TypeError("Missing required property 'description'")
            __props__.__dict__["description"] = description
            __props__.__dict__["issue_id"] = issue_id
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            if service_name is None and not opts.urn:
                raise TypeError("Missing required property 'service_name'")
            __props__.__dict__["service_name"] = service_name
            __props__.__dict__["state"] = state
            if title is None and not opts.urn:
                raise TypeError("Missing required property 'title'")
            __props__.__dict__["title"] = title
            if user_id is None and not opts.urn:
                raise TypeError("Missing required property 'user_id'")
            __props__.__dict__["user_id"] = user_id
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:apimanagement:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20170301:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20180101:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20180601preview:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20190101:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20191201:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20191201preview:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20200601preview:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20210101preview:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20210401preview:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20210801:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20211201preview:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20220401preview:ApiIssue"), pulumi.Alias(type_="azure-native:apimanagement/v20220801:ApiIssue")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(ApiIssue, __self__).__init__(
            'azure-native:apimanagement/v20201201:ApiIssue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'ApiIssue':
        """
        Get an existing ApiIssue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = ApiIssueArgs.__new__(ApiIssueArgs)

        __props__.__dict__["api_id"] = None
        __props__.__dict__["created_date"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["state"] = None
        __props__.__dict__["title"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["user_id"] = None
        return ApiIssue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="apiId")
    def api_id(self) -> pulumi.Output[Optional[str]]:
        """
        A resource identifier for the API the issue was created for.
        """
        return pulumi.get(self, "api_id")

    @property
    @pulumi.getter(name="createdDate")
    def created_date(self) -> pulumi.Output[Optional[str]]:
        """
        Date and time when the issue was created.
        """
        return pulumi.get(self, "created_date")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[str]:
        """
        Text describing the issue.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        Resource name.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[Optional[str]]:
        """
        Status of the issue.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter
    def title(self) -> pulumi.Output[str]:
        """
        The issue title.
        """
        return pulumi.get(self, "title")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        Resource type for API Management resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="userId")
    def user_id(self) -> pulumi.Output[str]:
        """
        A resource identifier for the user created the issue.
        """
        return pulumi.get(self, "user_id")

