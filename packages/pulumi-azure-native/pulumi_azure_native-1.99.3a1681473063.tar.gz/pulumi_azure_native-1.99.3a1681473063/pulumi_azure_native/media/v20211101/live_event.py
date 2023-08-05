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

__all__ = ['LiveEventArgs', 'LiveEvent']

@pulumi.input_type
class LiveEventArgs:
    def __init__(__self__, *,
                 account_name: pulumi.Input[str],
                 input: pulumi.Input['LiveEventInputArgs'],
                 resource_group_name: pulumi.Input[str],
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 cross_site_access_policies: Optional[pulumi.Input['CrossSiteAccessPoliciesArgs']] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input['LiveEventEncodingArgs']] = None,
                 hostname_prefix: Optional[pulumi.Input[str]] = None,
                 live_event_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input['LiveEventPreviewArgs']] = None,
                 stream_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'StreamOptionsFlag']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transcriptions: Optional[pulumi.Input[Sequence[pulumi.Input['LiveEventTranscriptionArgs']]]] = None,
                 use_static_hostname: Optional[pulumi.Input[bool]] = None):
        """
        The set of arguments for constructing a LiveEvent resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input['LiveEventInputArgs'] input: Live event input settings. It defines how the live event receives input from a contribution encoder.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[bool] auto_start: The flag indicates if the resource should be automatically started on creation.
        :param pulumi.Input['CrossSiteAccessPoliciesArgs'] cross_site_access_policies: Live event cross site access policies.
        :param pulumi.Input[str] description: A description for the live event.
        :param pulumi.Input['LiveEventEncodingArgs'] encoding: Encoding settings for the live event. It configures whether a live encoder is used for the live event and settings for the live encoder if it is used.
        :param pulumi.Input[str] hostname_prefix: When useStaticHostname is set to true, the hostnamePrefix specifies the first part of the hostname assigned to the live event preview and ingest endpoints. The final hostname would be a combination of this prefix, the media service account name and a short code for the Azure Media Services data center.
        :param pulumi.Input[str] live_event_name: The name of the live event, maximum length is 32.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input['LiveEventPreviewArgs'] preview: Live event preview settings. Preview allows live event producers to preview the live streaming content without creating any live output.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'StreamOptionsFlag']]]] stream_options: The options to use for the LiveEvent. This value is specified at creation time and cannot be updated. The valid values for the array entry values are 'Default' and 'LowLatency'.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input['LiveEventTranscriptionArgs']]] transcriptions: Live transcription settings for the live event. See https://go.microsoft.com/fwlink/?linkid=2133742 for more information about the live transcription feature.
        :param pulumi.Input[bool] use_static_hostname: Specifies whether a static hostname would be assigned to the live event preview and ingest endpoints. This value can only be updated if the live event is in Standby state
        """
        pulumi.set(__self__, "account_name", account_name)
        pulumi.set(__self__, "input", input)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if auto_start is not None:
            pulumi.set(__self__, "auto_start", auto_start)
        if cross_site_access_policies is not None:
            pulumi.set(__self__, "cross_site_access_policies", cross_site_access_policies)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if encoding is not None:
            pulumi.set(__self__, "encoding", encoding)
        if hostname_prefix is not None:
            pulumi.set(__self__, "hostname_prefix", hostname_prefix)
        if live_event_name is not None:
            pulumi.set(__self__, "live_event_name", live_event_name)
        if location is not None:
            pulumi.set(__self__, "location", location)
        if preview is not None:
            pulumi.set(__self__, "preview", preview)
        if stream_options is not None:
            pulumi.set(__self__, "stream_options", stream_options)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if transcriptions is not None:
            pulumi.set(__self__, "transcriptions", transcriptions)
        if use_static_hostname is not None:
            pulumi.set(__self__, "use_static_hostname", use_static_hostname)

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
    @pulumi.getter
    def input(self) -> pulumi.Input['LiveEventInputArgs']:
        """
        Live event input settings. It defines how the live event receives input from a contribution encoder.
        """
        return pulumi.get(self, "input")

    @input.setter
    def input(self, value: pulumi.Input['LiveEventInputArgs']):
        pulumi.set(self, "input", value)

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
    @pulumi.getter(name="autoStart")
    def auto_start(self) -> Optional[pulumi.Input[bool]]:
        """
        The flag indicates if the resource should be automatically started on creation.
        """
        return pulumi.get(self, "auto_start")

    @auto_start.setter
    def auto_start(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "auto_start", value)

    @property
    @pulumi.getter(name="crossSiteAccessPolicies")
    def cross_site_access_policies(self) -> Optional[pulumi.Input['CrossSiteAccessPoliciesArgs']]:
        """
        Live event cross site access policies.
        """
        return pulumi.get(self, "cross_site_access_policies")

    @cross_site_access_policies.setter
    def cross_site_access_policies(self, value: Optional[pulumi.Input['CrossSiteAccessPoliciesArgs']]):
        pulumi.set(self, "cross_site_access_policies", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        A description for the live event.
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter
    def encoding(self) -> Optional[pulumi.Input['LiveEventEncodingArgs']]:
        """
        Encoding settings for the live event. It configures whether a live encoder is used for the live event and settings for the live encoder if it is used.
        """
        return pulumi.get(self, "encoding")

    @encoding.setter
    def encoding(self, value: Optional[pulumi.Input['LiveEventEncodingArgs']]):
        pulumi.set(self, "encoding", value)

    @property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> Optional[pulumi.Input[str]]:
        """
        When useStaticHostname is set to true, the hostnamePrefix specifies the first part of the hostname assigned to the live event preview and ingest endpoints. The final hostname would be a combination of this prefix, the media service account name and a short code for the Azure Media Services data center.
        """
        return pulumi.get(self, "hostname_prefix")

    @hostname_prefix.setter
    def hostname_prefix(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hostname_prefix", value)

    @property
    @pulumi.getter(name="liveEventName")
    def live_event_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the live event, maximum length is 32.
        """
        return pulumi.get(self, "live_event_name")

    @live_event_name.setter
    def live_event_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "live_event_name", value)

    @property
    @pulumi.getter
    def location(self) -> Optional[pulumi.Input[str]]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @location.setter
    def location(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "location", value)

    @property
    @pulumi.getter
    def preview(self) -> Optional[pulumi.Input['LiveEventPreviewArgs']]:
        """
        Live event preview settings. Preview allows live event producers to preview the live streaming content without creating any live output.
        """
        return pulumi.get(self, "preview")

    @preview.setter
    def preview(self, value: Optional[pulumi.Input['LiveEventPreviewArgs']]):
        pulumi.set(self, "preview", value)

    @property
    @pulumi.getter(name="streamOptions")
    def stream_options(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'StreamOptionsFlag']]]]]:
        """
        The options to use for the LiveEvent. This value is specified at creation time and cannot be updated. The valid values for the array entry values are 'Default' and 'LowLatency'.
        """
        return pulumi.get(self, "stream_options")

    @stream_options.setter
    def stream_options(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'StreamOptionsFlag']]]]]):
        pulumi.set(self, "stream_options", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def transcriptions(self) -> Optional[pulumi.Input[Sequence[pulumi.Input['LiveEventTranscriptionArgs']]]]:
        """
        Live transcription settings for the live event. See https://go.microsoft.com/fwlink/?linkid=2133742 for more information about the live transcription feature.
        """
        return pulumi.get(self, "transcriptions")

    @transcriptions.setter
    def transcriptions(self, value: Optional[pulumi.Input[Sequence[pulumi.Input['LiveEventTranscriptionArgs']]]]):
        pulumi.set(self, "transcriptions", value)

    @property
    @pulumi.getter(name="useStaticHostname")
    def use_static_hostname(self) -> Optional[pulumi.Input[bool]]:
        """
        Specifies whether a static hostname would be assigned to the live event preview and ingest endpoints. This value can only be updated if the live event is in Standby state
        """
        return pulumi.get(self, "use_static_hostname")

    @use_static_hostname.setter
    def use_static_hostname(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "use_static_hostname", value)


class LiveEvent(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 cross_site_access_policies: Optional[pulumi.Input[pulumi.InputType['CrossSiteAccessPoliciesArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[pulumi.InputType['LiveEventEncodingArgs']]] = None,
                 hostname_prefix: Optional[pulumi.Input[str]] = None,
                 input: Optional[pulumi.Input[pulumi.InputType['LiveEventInputArgs']]] = None,
                 live_event_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[pulumi.InputType['LiveEventPreviewArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stream_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'StreamOptionsFlag']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transcriptions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveEventTranscriptionArgs']]]]] = None,
                 use_static_hostname: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        """
        The live event.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] account_name: The Media Services account name.
        :param pulumi.Input[bool] auto_start: The flag indicates if the resource should be automatically started on creation.
        :param pulumi.Input[pulumi.InputType['CrossSiteAccessPoliciesArgs']] cross_site_access_policies: Live event cross site access policies.
        :param pulumi.Input[str] description: A description for the live event.
        :param pulumi.Input[pulumi.InputType['LiveEventEncodingArgs']] encoding: Encoding settings for the live event. It configures whether a live encoder is used for the live event and settings for the live encoder if it is used.
        :param pulumi.Input[str] hostname_prefix: When useStaticHostname is set to true, the hostnamePrefix specifies the first part of the hostname assigned to the live event preview and ingest endpoints. The final hostname would be a combination of this prefix, the media service account name and a short code for the Azure Media Services data center.
        :param pulumi.Input[pulumi.InputType['LiveEventInputArgs']] input: Live event input settings. It defines how the live event receives input from a contribution encoder.
        :param pulumi.Input[str] live_event_name: The name of the live event, maximum length is 32.
        :param pulumi.Input[str] location: The geo-location where the resource lives
        :param pulumi.Input[pulumi.InputType['LiveEventPreviewArgs']] preview: Live event preview settings. Preview allows live event producers to preview the live streaming content without creating any live output.
        :param pulumi.Input[str] resource_group_name: The name of the resource group within the Azure subscription.
        :param pulumi.Input[Sequence[pulumi.Input[Union[str, 'StreamOptionsFlag']]]] stream_options: The options to use for the LiveEvent. This value is specified at creation time and cannot be updated. The valid values for the array entry values are 'Default' and 'LowLatency'.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: Resource tags.
        :param pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveEventTranscriptionArgs']]]] transcriptions: Live transcription settings for the live event. See https://go.microsoft.com/fwlink/?linkid=2133742 for more information about the live transcription feature.
        :param pulumi.Input[bool] use_static_hostname: Specifies whether a static hostname would be assigned to the live event preview and ingest endpoints. This value can only be updated if the live event is in Standby state
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: LiveEventArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The live event.

        :param str resource_name: The name of the resource.
        :param LiveEventArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(LiveEventArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 account_name: Optional[pulumi.Input[str]] = None,
                 auto_start: Optional[pulumi.Input[bool]] = None,
                 cross_site_access_policies: Optional[pulumi.Input[pulumi.InputType['CrossSiteAccessPoliciesArgs']]] = None,
                 description: Optional[pulumi.Input[str]] = None,
                 encoding: Optional[pulumi.Input[pulumi.InputType['LiveEventEncodingArgs']]] = None,
                 hostname_prefix: Optional[pulumi.Input[str]] = None,
                 input: Optional[pulumi.Input[pulumi.InputType['LiveEventInputArgs']]] = None,
                 live_event_name: Optional[pulumi.Input[str]] = None,
                 location: Optional[pulumi.Input[str]] = None,
                 preview: Optional[pulumi.Input[pulumi.InputType['LiveEventPreviewArgs']]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 stream_options: Optional[pulumi.Input[Sequence[pulumi.Input[Union[str, 'StreamOptionsFlag']]]]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 transcriptions: Optional[pulumi.Input[Sequence[pulumi.Input[pulumi.InputType['LiveEventTranscriptionArgs']]]]] = None,
                 use_static_hostname: Optional[pulumi.Input[bool]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = LiveEventArgs.__new__(LiveEventArgs)

            if account_name is None and not opts.urn:
                raise TypeError("Missing required property 'account_name'")
            __props__.__dict__["account_name"] = account_name
            __props__.__dict__["auto_start"] = auto_start
            __props__.__dict__["cross_site_access_policies"] = cross_site_access_policies
            __props__.__dict__["description"] = description
            __props__.__dict__["encoding"] = encoding
            __props__.__dict__["hostname_prefix"] = hostname_prefix
            if input is None and not opts.urn:
                raise TypeError("Missing required property 'input'")
            __props__.__dict__["input"] = input
            __props__.__dict__["live_event_name"] = live_event_name
            __props__.__dict__["location"] = location
            __props__.__dict__["preview"] = preview
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["stream_options"] = stream_options
            __props__.__dict__["tags"] = tags
            __props__.__dict__["transcriptions"] = transcriptions
            __props__.__dict__["use_static_hostname"] = use_static_hostname
            __props__.__dict__["created"] = None
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["resource_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:media:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20180330preview:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20180601preview:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20180701:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20190501preview:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20200501:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20210601:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20220801:LiveEvent"), pulumi.Alias(type_="azure-native:media/v20221101:LiveEvent")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(LiveEvent, __self__).__init__(
            'azure-native:media/v20211101:LiveEvent',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'LiveEvent':
        """
        Get an existing LiveEvent resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = LiveEventArgs.__new__(LiveEventArgs)

        __props__.__dict__["created"] = None
        __props__.__dict__["cross_site_access_policies"] = None
        __props__.__dict__["description"] = None
        __props__.__dict__["encoding"] = None
        __props__.__dict__["hostname_prefix"] = None
        __props__.__dict__["input"] = None
        __props__.__dict__["last_modified"] = None
        __props__.__dict__["location"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["preview"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["resource_state"] = None
        __props__.__dict__["stream_options"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["transcriptions"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["use_static_hostname"] = None
        return LiveEvent(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def created(self) -> pulumi.Output[str]:
        """
        The creation time for the live event
        """
        return pulumi.get(self, "created")

    @property
    @pulumi.getter(name="crossSiteAccessPolicies")
    def cross_site_access_policies(self) -> pulumi.Output[Optional['outputs.CrossSiteAccessPoliciesResponse']]:
        """
        Live event cross site access policies.
        """
        return pulumi.get(self, "cross_site_access_policies")

    @property
    @pulumi.getter
    def description(self) -> pulumi.Output[Optional[str]]:
        """
        A description for the live event.
        """
        return pulumi.get(self, "description")

    @property
    @pulumi.getter
    def encoding(self) -> pulumi.Output[Optional['outputs.LiveEventEncodingResponse']]:
        """
        Encoding settings for the live event. It configures whether a live encoder is used for the live event and settings for the live encoder if it is used.
        """
        return pulumi.get(self, "encoding")

    @property
    @pulumi.getter(name="hostnamePrefix")
    def hostname_prefix(self) -> pulumi.Output[Optional[str]]:
        """
        When useStaticHostname is set to true, the hostnamePrefix specifies the first part of the hostname assigned to the live event preview and ingest endpoints. The final hostname would be a combination of this prefix, the media service account name and a short code for the Azure Media Services data center.
        """
        return pulumi.get(self, "hostname_prefix")

    @property
    @pulumi.getter
    def input(self) -> pulumi.Output['outputs.LiveEventInputResponse']:
        """
        Live event input settings. It defines how the live event receives input from a contribution encoder.
        """
        return pulumi.get(self, "input")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The last modified time of the live event.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def location(self) -> pulumi.Output[str]:
        """
        The geo-location where the resource lives
        """
        return pulumi.get(self, "location")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def preview(self) -> pulumi.Output[Optional['outputs.LiveEventPreviewResponse']]:
        """
        Live event preview settings. Preview allows live event producers to preview the live streaming content without creating any live output.
        """
        return pulumi.get(self, "preview")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        The provisioning state of the live event.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="resourceState")
    def resource_state(self) -> pulumi.Output[str]:
        """
        The resource state of the live event. See https://go.microsoft.com/fwlink/?linkid=2139012 for more information.
        """
        return pulumi.get(self, "resource_state")

    @property
    @pulumi.getter(name="streamOptions")
    def stream_options(self) -> pulumi.Output[Optional[Sequence[str]]]:
        """
        The options to use for the LiveEvent. This value is specified at creation time and cannot be updated. The valid values for the array entry values are 'Default' and 'LowLatency'.
        """
        return pulumi.get(self, "stream_options")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system metadata relating to this resource.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        Resource tags.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def transcriptions(self) -> pulumi.Output[Optional[Sequence['outputs.LiveEventTranscriptionResponse']]]:
        """
        Live transcription settings for the live event. See https://go.microsoft.com/fwlink/?linkid=2133742 for more information about the live transcription feature.
        """
        return pulumi.get(self, "transcriptions")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter(name="useStaticHostname")
    def use_static_hostname(self) -> pulumi.Output[Optional[bool]]:
        """
        Specifies whether a static hostname would be assigned to the live event preview and ingest endpoints. This value can only be updated if the live event is in Standby state
        """
        return pulumi.get(self, "use_static_hostname")

