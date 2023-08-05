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

__all__ = [
    'ActionGroupsInformationArgs',
    'DetectorArgs',
    'ThrottlingInformationArgs',
]

@pulumi.input_type
class ActionGroupsInformationArgs:
    def __init__(__self__, *,
                 group_ids: pulumi.Input[Sequence[pulumi.Input[str]]],
                 custom_email_subject: Optional[pulumi.Input[str]] = None,
                 custom_webhook_payload: Optional[pulumi.Input[str]] = None):
        """
        The Action Groups information, used by the alert rule.
        :param pulumi.Input[Sequence[pulumi.Input[str]]] group_ids: The Action Group resource IDs.
        :param pulumi.Input[str] custom_email_subject: An optional custom email subject to use in email notifications.
        :param pulumi.Input[str] custom_webhook_payload: An optional custom web-hook payload to use in web-hook notifications.
        """
        pulumi.set(__self__, "group_ids", group_ids)
        if custom_email_subject is not None:
            pulumi.set(__self__, "custom_email_subject", custom_email_subject)
        if custom_webhook_payload is not None:
            pulumi.set(__self__, "custom_webhook_payload", custom_webhook_payload)

    @property
    @pulumi.getter(name="groupIds")
    def group_ids(self) -> pulumi.Input[Sequence[pulumi.Input[str]]]:
        """
        The Action Group resource IDs.
        """
        return pulumi.get(self, "group_ids")

    @group_ids.setter
    def group_ids(self, value: pulumi.Input[Sequence[pulumi.Input[str]]]):
        pulumi.set(self, "group_ids", value)

    @property
    @pulumi.getter(name="customEmailSubject")
    def custom_email_subject(self) -> Optional[pulumi.Input[str]]:
        """
        An optional custom email subject to use in email notifications.
        """
        return pulumi.get(self, "custom_email_subject")

    @custom_email_subject.setter
    def custom_email_subject(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_email_subject", value)

    @property
    @pulumi.getter(name="customWebhookPayload")
    def custom_webhook_payload(self) -> Optional[pulumi.Input[str]]:
        """
        An optional custom web-hook payload to use in web-hook notifications.
        """
        return pulumi.get(self, "custom_webhook_payload")

    @custom_webhook_payload.setter
    def custom_webhook_payload(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "custom_webhook_payload", value)


@pulumi.input_type
class DetectorArgs:
    def __init__(__self__, *,
                 id: pulumi.Input[str],
                 description: Optional[pulumi.Input[str]] = None,
                 image_paths: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 name: Optional[pulumi.Input[str]] = None,
                 parameters: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 supported_resource_types: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None):
        """
        The detector information. By default this is not populated, unless it's specified in expandDetector
        :param pulumi.Input[str] id: The detector id.
        :param pulumi.Input[str] description: The Smart Detector description. By default this is not populated, unless it's specified in expandDetector
        :param pulumi.Input[Sequence[pulumi.Input[str]]] image_paths: The Smart Detector image path. By default this is not populated, unless it's specified in expandDetector
        :param pulumi.Input[str] name: The Smart Detector name. By default this is not populated, unless it's specified in expandDetector
        :param pulumi.Input[Mapping[str, Any]] parameters: The detector's parameters.'
        :param pulumi.Input[Sequence[pulumi.Input[str]]] supported_resource_types: The Smart Detector supported resource types. By default this is not populated, unless it's specified in expandDetector
        """
        pulumi.set(__self__, "id", id)
        if description is not None:
            pulumi.set(__self__, "description", description)
        if image_paths is not None:
            pulumi.set(__self__, "image_paths", image_paths)
        if name is not None:
            pulumi.set(__self__, "name", name)
        if parameters is not None:
            pulumi.set(__self__, "parameters", parameters)
        if supported_resource_types is not None:
            pulumi.set(__self__, "supported_resource_types", supported_resource_types)

    @property
    @pulumi.getter
    def id(self) -> pulumi.Input[str]:
        """
        The detector id.
        """
        return pulumi.get(self, "id")

    @id.setter
    def id(self, value: pulumi.Input[str]):
        pulumi.set(self, "id", value)

    @property
    @pulumi.getter
    def description(self) -> Optional[pulumi.Input[str]]:
        """
        The Smart Detector description. By default this is not populated, unless it's specified in expandDetector
        """
        return pulumi.get(self, "description")

    @description.setter
    def description(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "description", value)

    @property
    @pulumi.getter(name="imagePaths")
    def image_paths(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Smart Detector image path. By default this is not populated, unless it's specified in expandDetector
        """
        return pulumi.get(self, "image_paths")

    @image_paths.setter
    def image_paths(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "image_paths", value)

    @property
    @pulumi.getter
    def name(self) -> Optional[pulumi.Input[str]]:
        """
        The Smart Detector name. By default this is not populated, unless it's specified in expandDetector
        """
        return pulumi.get(self, "name")

    @name.setter
    def name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "name", value)

    @property
    @pulumi.getter
    def parameters(self) -> Optional[pulumi.Input[Mapping[str, Any]]]:
        """
        The detector's parameters.'
        """
        return pulumi.get(self, "parameters")

    @parameters.setter
    def parameters(self, value: Optional[pulumi.Input[Mapping[str, Any]]]):
        pulumi.set(self, "parameters", value)

    @property
    @pulumi.getter(name="supportedResourceTypes")
    def supported_resource_types(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        """
        The Smart Detector supported resource types. By default this is not populated, unless it's specified in expandDetector
        """
        return pulumi.get(self, "supported_resource_types")

    @supported_resource_types.setter
    def supported_resource_types(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "supported_resource_types", value)


@pulumi.input_type
class ThrottlingInformationArgs:
    def __init__(__self__, *,
                 duration: Optional[pulumi.Input[str]] = None):
        """
        Optional throttling information for the alert rule.
        :param pulumi.Input[str] duration: The required duration (in ISO8601 format) to wait before notifying on the alert rule again. The time granularity must be in minutes and minimum value is 0 minutes
        """
        if duration is not None:
            pulumi.set(__self__, "duration", duration)

    @property
    @pulumi.getter
    def duration(self) -> Optional[pulumi.Input[str]]:
        """
        The required duration (in ISO8601 format) to wait before notifying on the alert rule again. The time granularity must be in minutes and minimum value is 0 minutes
        """
        return pulumi.get(self, "duration")

    @duration.setter
    def duration(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "duration", value)


