# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from ... import _utilities

__all__ = ['KeyValueArgs', 'KeyValue']

@pulumi.input_type
class KeyValueArgs:
    def __init__(__self__, *,
                 config_store_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 content_type: Optional[pulumi.Input[str]] = None,
                 key_value_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a KeyValue resource.
        :param pulumi.Input[str] config_store_name: The name of the configuration store.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[str] content_type: The content type of the key-value's value.
               Providing a proper content-type can enable transformations of values when they are retrieved by applications.
        :param pulumi.Input[str] key_value_name: Identifier of key and label combination. Key and label are joined by $ character. Label is optional.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A dictionary of tags that can help identify what a key-value may be applicable for.
        :param pulumi.Input[str] value: The value of the key-value.
        """
        pulumi.set(__self__, "config_store_name", config_store_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if content_type is not None:
            pulumi.set(__self__, "content_type", content_type)
        if key_value_name is not None:
            pulumi.set(__self__, "key_value_name", key_value_name)
        if tags is not None:
            pulumi.set(__self__, "tags", tags)
        if value is not None:
            pulumi.set(__self__, "value", value)

    @property
    @pulumi.getter(name="configStoreName")
    def config_store_name(self) -> pulumi.Input[str]:
        """
        The name of the configuration store.
        """
        return pulumi.get(self, "config_store_name")

    @config_store_name.setter
    def config_store_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "config_store_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group to which the container registry belongs.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> Optional[pulumi.Input[str]]:
        """
        The content type of the key-value's value.
        Providing a proper content-type can enable transformations of values when they are retrieved by applications.
        """
        return pulumi.get(self, "content_type")

    @content_type.setter
    def content_type(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "content_type", value)

    @property
    @pulumi.getter(name="keyValueName")
    def key_value_name(self) -> Optional[pulumi.Input[str]]:
        """
        Identifier of key and label combination. Key and label are joined by $ character. Label is optional.
        """
        return pulumi.get(self, "key_value_name")

    @key_value_name.setter
    def key_value_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "key_value_name", value)

    @property
    @pulumi.getter
    def tags(self) -> Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]:
        """
        A dictionary of tags that can help identify what a key-value may be applicable for.
        """
        return pulumi.get(self, "tags")

    @tags.setter
    def tags(self, value: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]]):
        pulumi.set(self, "tags", value)

    @property
    @pulumi.getter
    def value(self) -> Optional[pulumi.Input[str]]:
        """
        The value of the key-value.
        """
        return pulumi.get(self, "value")

    @value.setter
    def value(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "value", value)


class KeyValue(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_store_name: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 key_value_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The key-value resource along with all resource properties.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] config_store_name: The name of the configuration store.
        :param pulumi.Input[str] content_type: The content type of the key-value's value.
               Providing a proper content-type can enable transformations of values when they are retrieved by applications.
        :param pulumi.Input[str] key_value_name: Identifier of key and label combination. Key and label are joined by $ character. Label is optional.
        :param pulumi.Input[str] resource_group_name: The name of the resource group to which the container registry belongs.
        :param pulumi.Input[Mapping[str, pulumi.Input[str]]] tags: A dictionary of tags that can help identify what a key-value may be applicable for.
        :param pulumi.Input[str] value: The value of the key-value.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: KeyValueArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The key-value resource along with all resource properties.

        :param str resource_name: The name of the resource.
        :param KeyValueArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(KeyValueArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 config_store_name: Optional[pulumi.Input[str]] = None,
                 content_type: Optional[pulumi.Input[str]] = None,
                 key_value_name: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 tags: Optional[pulumi.Input[Mapping[str, pulumi.Input[str]]]] = None,
                 value: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = KeyValueArgs.__new__(KeyValueArgs)

            if config_store_name is None and not opts.urn:
                raise TypeError("Missing required property 'config_store_name'")
            __props__.__dict__["config_store_name"] = config_store_name
            __props__.__dict__["content_type"] = content_type
            __props__.__dict__["key_value_name"] = key_value_name
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["tags"] = tags
            __props__.__dict__["value"] = value
            __props__.__dict__["e_tag"] = None
            __props__.__dict__["key"] = None
            __props__.__dict__["label"] = None
            __props__.__dict__["last_modified"] = None
            __props__.__dict__["locked"] = None
            __props__.__dict__["name"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:appconfiguration:KeyValue"), pulumi.Alias(type_="azure-native:appconfiguration/v20200701preview:KeyValue"), pulumi.Alias(type_="azure-native:appconfiguration/v20210301preview:KeyValue"), pulumi.Alias(type_="azure-native:appconfiguration/v20211001preview:KeyValue"), pulumi.Alias(type_="azure-native:appconfiguration/v20220301preview:KeyValue"), pulumi.Alias(type_="azure-native:appconfiguration/v20230301:KeyValue")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(KeyValue, __self__).__init__(
            'azure-native:appconfiguration/v20220501:KeyValue',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'KeyValue':
        """
        Get an existing KeyValue resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = KeyValueArgs.__new__(KeyValueArgs)

        __props__.__dict__["content_type"] = None
        __props__.__dict__["e_tag"] = None
        __props__.__dict__["key"] = None
        __props__.__dict__["label"] = None
        __props__.__dict__["last_modified"] = None
        __props__.__dict__["locked"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["tags"] = None
        __props__.__dict__["type"] = None
        __props__.__dict__["value"] = None
        return KeyValue(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="contentType")
    def content_type(self) -> pulumi.Output[Optional[str]]:
        """
        The content type of the key-value's value.
        Providing a proper content-type can enable transformations of values when they are retrieved by applications.
        """
        return pulumi.get(self, "content_type")

    @property
    @pulumi.getter(name="eTag")
    def e_tag(self) -> pulumi.Output[str]:
        """
        An ETag indicating the state of a key-value within a configuration store.
        """
        return pulumi.get(self, "e_tag")

    @property
    @pulumi.getter
    def key(self) -> pulumi.Output[str]:
        """
        The primary identifier of a key-value.
        The key is used in unison with the label to uniquely identify a key-value.
        """
        return pulumi.get(self, "key")

    @property
    @pulumi.getter
    def label(self) -> pulumi.Output[str]:
        """
        A value used to group key-values.
        The label is used in unison with the key to uniquely identify a key-value.
        """
        return pulumi.get(self, "label")

    @property
    @pulumi.getter(name="lastModified")
    def last_modified(self) -> pulumi.Output[str]:
        """
        The last time a modifying operation was performed on the given key-value.
        """
        return pulumi.get(self, "last_modified")

    @property
    @pulumi.getter
    def locked(self) -> pulumi.Output[bool]:
        """
        A value indicating whether the key-value is locked.
        A locked key-value may not be modified until it is unlocked.
        """
        return pulumi.get(self, "locked")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource.
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter
    def tags(self) -> pulumi.Output[Optional[Mapping[str, str]]]:
        """
        A dictionary of tags that can help identify what a key-value may be applicable for.
        """
        return pulumi.get(self, "tags")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource.
        """
        return pulumi.get(self, "type")

    @property
    @pulumi.getter
    def value(self) -> pulumi.Output[Optional[str]]:
        """
        The value of the key-value.
        """
        return pulumi.get(self, "value")

