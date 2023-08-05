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

__all__ = ['AssetFilterArgs', 'AssetFilter']

@pulumi.input_type
class AssetFilterArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 asset_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 filter_name: Optional[pulumi.Input[str]] = None,
                 first_quality: Optional[pulumi.Input['FirstQualityArgs']] = None,
                 presentation_time_range: Optional[pulumi.Input['PresentationTimeRangeArgs']] = None,
                 tracks: Optional[pulumi.Input[Sequence[pulumi.Input['FilterTrackSelectionArgs']]]] = None):
        """
        The set of arguments for constructing a AssetFilter resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[str] asset_name: The Asset name.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[str] filter_name: The Asset Filter name
        :param pulumi.Input['FirstQualityArgs'] first_quality: The first quality.
        :param pulumi.Input['PresentationTimeRangeArgs'] presentation_time_range: The presentation time range.
        :param pulumi.Input[Sequence[pulumi.Input['FilterTrackSelectionArgs']]] tracks: The tracks selection conditions.
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "asset_name", asset_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if filter_name is not None:
            pulumi.set(__self__, "filter_name", filter_name)
        if first_quality is not None:
            pulumi.set(__self__, "first_quality", first_quality)
        if presentation_time_range is not None:
            pulumi.set(__self__, "presentation_time_range", presentation_time_range)
        if tracks is not None:
            pulumi.set(__self__, "tracks", tracks)

    @property
    @pulumi.getter(name="accountName")
    def account_name(self) -> pulumi.Input[str]:
        """
        The Media Services account name.
        """
        return pulumi.get(self, "account_name")

    @account_name.setter
    def account_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "account_name", value)

    @property
    @pulumi.getter(name="assetName")
    def asset_name(self) -> pulumi.Input[str]:
        """
        The Asset name.
        """
        return pulumi.get(self, "asset_name")

    @asset_name.setter
    def asset_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "asset_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group within the Azure subscription.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="filterName")
    def filter_name(self) -> Optional[pulumi.Input[str]]:
        """
        The Asset Filter name
        """
        return pulumi.get(self, "filter_name")

    @filter_name.setter
    def filter_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "filter_name", value)

    @property
    @pulumi.getter(name="firstQuality")
    def first_quality(self) -> Optional[pulumi.Input['FirstQualityArgs']]:
        """
        The first quality.
        """
        return pulumi.get(self, "first_quality")

    @first_quality.setter
    def first_quality(self, value: Optional[pulumi.Input['FirstQualityArgs']]):
        pulumi.set(self, "first_quality", value)

    @property
    @pulumi.getter(name="presentationTimeRange")
    def presentation_time_range(self) -> Optional[pulumi.Input['PresentationTimeRangeArgs']]:
        """
        The presentation time range.
        """
        return pulumi.get(self, "presentation_time_range")

    @presentation_time_range.setter
    def presentation_time_range(self, value: Optional[pulumi.Input['PresentationTimeRangeArgs']]):
        pulumi.set(self, "presentation_time_range", value)

    @property
    @pulumi.getter
    def tracks(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['FilterTrackSelectionArgs']]]]:
        """
        The tracks selection conditions.
        """
        return pulumi.get(self, "tracks")

    @tracks.setter
    def tracks(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['FilterTrackSelectionArgs']]]]):
        pulumi.set(self, "tracks", value)


class AssetFilter(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 asset_name: Optional[pulumi.Input[str]] = None,
                 filter_name: Optional[pulumi.Input[str]] = None,
                 first_quality: Optional[pulumi.Input[pulumi.InputType['FirstQualityArgs']]] = None,
                 presentation_time_range: Optional[pulumi.Input[pulumi.InputType['PresentationTimeRangeArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tracks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FilterTrackSelectionArgs']]]]] = None,
                 __props__=None):
        """
        An Asset Filter.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[str] asset_name: The Asset name.
        :param pulumi.Input[str] filter_name: The Asset Filter name
        :param pulumi.Input[pulumi.InputType['FirstQualityArgs']] first_quality: The first quality.
        :param pulumi.Input[pulumi.InputType['PresentationTimeRangeArgs']] presentation_time_range: The presentation time range.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FilterTrackSelectionArgs']]]] tracks: The tracks selection conditions.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: AssetFilterArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        An Asset Filter.

        :param str resource_name: The name of the resource.
        :param AssetFilterArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(AssetFilterArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 asset_name: Optional[pulumi.Input[str]] = None,
                 filter_name: Optional[pulumi.Input[str]] = None,
                 first_quality: Optional[pulumi.Input[pulumi.InputType['FirstQualityArgs']]] = None,
                 presentation_time_range: Optional[pulumi.Input[pulumi.InputType['PresentationTimeRangeArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tracks: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['FilterTrackSelectionArgs']]]]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = AssetFilterArgs.__new__(AssetFilterArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            if asset_name is None and not opts.urn:
                raise TypeError("Missing required property 'asset_name'")
            __props__.__dict__["asset_name"] = asset_name
            __props__.__dict__["filter_name"] = filter_name
            __props__.__dict__["first_quality"] = first_quality
            __props__.__dict__["presentation_time_range"] = presentation_time_range
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tracks"] = tracks
            __props__.__dict__["name"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:media:AssetFilter"), pulumi.Alias(type_="azure-native:media/v20180701:AssetFilter"), pulumi.Alias(type_="azure-native:media/v20200501:AssetFilter"), pulumi.Alias(type_="azure-native:media/v20210601:AssetFilter"), pulumi.Alias(type_="azure-native:media/v20220801:AssetFilter"), pulumi.Alias(type_="azure-native:media/v20230101:AssetFilter")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(AssetFilter, __self__).__init__(
            'azure-native:media/v20211101:AssetFilter',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'AssetFilter':
        """
        Get an existing AssetFilter resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = AssetFilterArgs.__new__(AssetFilterArgs)

        __props__.__dict__["first_quality"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["presentation_time_range"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tracks"] = None
        __props__.__dict__["type"] = None
        return AssetFilter(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="firstQuality")
    def first_quality(self) -> pulumi.Output[Optional['outputs.FirstQualityResponse']]:
        """
        The first quality.
        """
        return pulumi.get(self, "first_quality")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="presentationTimeRange")
    def presentation_time_range(self) -> pulumi.Output[Optional['outputs.PresentationTimeRangeResponse']]:
        """
        The presentation time range.
        """
        return pulumi.get(self, "presentation_time_range")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tracks(self) -> pulumi.Output[Optional[Sequence['outputs.FilterTrackSelectionResponse']]]:
        """
        The tracks selection conditions.
        """
        return pulumi.get(self, "tracks")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

