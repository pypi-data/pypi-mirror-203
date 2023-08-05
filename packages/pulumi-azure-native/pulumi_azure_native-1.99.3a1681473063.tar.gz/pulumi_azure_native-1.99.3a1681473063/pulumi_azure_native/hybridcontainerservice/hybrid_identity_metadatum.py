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
from ._enums import *
from ._inputs import *

__all__ = ['HybridIdentityMetadatumArgs', 'HybridIdentityMetadatum']

@pulumi.input_type
class HybridIdentityMetadatumArgs:
    def __init__(__self__, *,
                 provisioned_clusters_name: pulumi.Input[str],
                 resource_group_name: pulumi.Input[str],
                 hybrid_identity_metadata_resource_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input['ProvisionedClusterIdentityArgs']] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 resource_uid: Optional[pulumi.Input[str]] = None):
        """
        The set of arguments for constructing a HybridIdentityMetadatum resource.
        :param pulumi.Input[str] provisioned_clusters_name: Parameter for the name of the provisioned cluster
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] hybrid_identity_metadata_resource_name: Parameter for the name of the hybrid identity metadata resource.
        :param pulumi.Input['ProvisionedClusterIdentityArgs'] identity: The identity of the provisioned cluster.
        :param pulumi.Input[str] public_key: Onboarding public key for provisioning the Managed identity for the HybridAKS cluster.
        :param pulumi.Input[str] resource_uid: Unique id of the parent provisioned cluster resource.
        """
        pulumi.set(__self__, "provisioned_clusters_name", provisioned_clusters_name)
        pulumi.set(__self__, "resource_group_name", resource_group_name)
        if hybrid_identity_metadata_resource_name is not None:
            pulumi.set(__self__, "hybrid_identity_metadata_resource_name", hybrid_identity_metadata_resource_name)
        if identity is not None:
            pulumi.set(__self__, "identity", identity)
        if public_key is not None:
            pulumi.set(__self__, "public_key", public_key)
        if resource_uid is not None:
            pulumi.set(__self__, "resource_uid", resource_uid)

    @property
    @pulumi.getter(name="provisionedClustersName")
    def provisioned_clusters_name(self) -> pulumi.Input[str]:
        """
        Parameter for the name of the provisioned cluster
        """
        return pulumi.get(self, "provisioned_clusters_name")

    @provisioned_clusters_name.setter
    def provisioned_clusters_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "provisioned_clusters_name", value)

    @property
    @pulumi.getter(name="resourceGroupName")
    def resource_group_name(self) -> pulumi.Input[str]:
        """
        The name of the resource group. The name is case insensitive.
        """
        return pulumi.get(self, "resource_group_name")

    @resource_group_name.setter
    def resource_group_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "resource_group_name", value)

    @property
    @pulumi.getter(name="hybridIdentityMetadataResourceName")
    def hybrid_identity_metadata_resource_name(self) -> Optional[pulumi.Input[str]]:
        """
        Parameter for the name of the hybrid identity metadata resource.
        """
        return pulumi.get(self, "hybrid_identity_metadata_resource_name")

    @hybrid_identity_metadata_resource_name.setter
    def hybrid_identity_metadata_resource_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hybrid_identity_metadata_resource_name", value)

    @property
    @pulumi.getter
    def identity(self) -> Optional[pulumi.Input['ProvisionedClusterIdentityArgs']]:
        """
        The identity of the provisioned cluster.
        """
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: Optional[pulumi.Input['ProvisionedClusterIdentityArgs']]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> Optional[pulumi.Input[str]]:
        """
        Onboarding public key for provisioning the Managed identity for the HybridAKS cluster.
        """
        return pulumi.get(self, "public_key")

    @public_key.setter
    def public_key(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "public_key", value)

    @property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> Optional[pulumi.Input[str]]:
        """
        Unique id of the parent provisioned cluster resource.
        """
        return pulumi.get(self, "resource_uid")

    @resource_uid.setter
    def resource_uid(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "resource_uid", value)


class HybridIdentityMetadatum(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hybrid_identity_metadata_resource_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ProvisionedClusterIdentityArgs']]] = None,
                 provisioned_clusters_name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_uid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        Defines the hybridIdentityMetadata.
        API Version: 2022-05-01-preview.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hybrid_identity_metadata_resource_name: Parameter for the name of the hybrid identity metadata resource.
        :param pulumi.Input[pulumi.InputType['ProvisionedClusterIdentityArgs']] identity: The identity of the provisioned cluster.
        :param pulumi.Input[str] provisioned_clusters_name: Parameter for the name of the provisioned cluster
        :param pulumi.Input[str] public_key: Onboarding public key for provisioning the Managed identity for the HybridAKS cluster.
        :param pulumi.Input[str] resource_group_name: The name of the resource group. The name is case insensitive.
        :param pulumi.Input[str] resource_uid: Unique id of the parent provisioned cluster resource.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HybridIdentityMetadatumArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        Defines the hybridIdentityMetadata.
        API Version: 2022-05-01-preview.

        :param str resource_name: The name of the resource.
        :param HybridIdentityMetadatumArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HybridIdentityMetadatumArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hybrid_identity_metadata_resource_name: Optional[pulumi.Input[str]] = None,
                 identity: Optional[pulumi.Input[pulumi.InputType['ProvisionedClusterIdentityArgs']]] = None,
                 provisioned_clusters_name: Optional[pulumi.Input[str]] = None,
                 public_key: Optional[pulumi.Input[str]] = None,
                 resource_group_name: Optional[pulumi.Input[str]] = None,
                 resource_uid: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        opts = pulumi.ResourceOptions.merge(_utilities.get_resource_opts_defaults(), opts)
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HybridIdentityMetadatumArgs.__new__(HybridIdentityMetadatumArgs)

            __props__.__dict__["hybrid_identity_metadata_resource_name"] = hybrid_identity_metadata_resource_name
            __props__.__dict__["identity"] = identity
            if provisioned_clusters_name is None and not opts.urn:
                raise TypeError("Missing required property 'provisioned_clusters_name'")
            __props__.__dict__["provisioned_clusters_name"] = provisioned_clusters_name
            __props__.__dict__["public_key"] = public_key
            if resource_group_name is None and not opts.urn:
                raise TypeError("Missing required property 'resource_group_name'")
            __props__.__dict__["resource_group_name"] = resource_group_name
            __props__.__dict__["resource_uid"] = resource_uid
            __props__.__dict__["name"] = None
            __props__.__dict__["provisioning_state"] = None
            __props__.__dict__["system_data"] = None
            __props__.__dict__["type"] = None
        alias_opts = pulumi.ResourceOptions(aliases=[pulumi.Alias(type_="azure-native:hybridcontainerservice/v20220501preview:HybridIdentityMetadatum")])
        opts = pulumi.ResourceOptions.merge(opts, alias_opts)
        super(HybridIdentityMetadatum, __self__).__init__(
            'azure-native:hybridcontainerservice:HybridIdentityMetadatum',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None) -> 'HybridIdentityMetadatum':
        """
        Get an existing HybridIdentityMetadatum resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = HybridIdentityMetadatumArgs.__new__(HybridIdentityMetadatumArgs)

        __props__.__dict__["identity"] = None
        __props__.__dict__["name"] = None
        __props__.__dict__["provisioning_state"] = None
        __props__.__dict__["public_key"] = None
        __props__.__dict__["resource_uid"] = None
        __props__.__dict__["system_data"] = None
        __props__.__dict__["type"] = None
        return HybridIdentityMetadatum(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Output[Optional['outputs.ProvisionedClusterIdentityResponse']]:
        """
        The identity of the provisioned cluster.
        """
        return pulumi.get(self, "identity")

    @property
    @pulumi.getter
    def name(self) -> pulumi.Output[str]:
        """
        The name of the resource
        """
        return pulumi.get(self, "name")

    @property
    @pulumi.getter(name="provisioningState")
    def provisioning_state(self) -> pulumi.Output[str]:
        """
        provisioning state of the hybridIdentityMetadata resource.
        """
        return pulumi.get(self, "provisioning_state")

    @property
    @pulumi.getter(name="publicKey")
    def public_key(self) -> pulumi.Output[Optional[str]]:
        """
        Onboarding public key for provisioning the Managed identity for the HybridAKS cluster.
        """
        return pulumi.get(self, "public_key")

    @property
    @pulumi.getter(name="resourceUid")
    def resource_uid(self) -> pulumi.Output[Optional[str]]:
        """
        Unique id of the parent provisioned cluster resource.
        """
        return pulumi.get(self, "resource_uid")

    @property
    @pulumi.getter(name="systemData")
    def system_data(self) -> pulumi.Output['outputs.SystemDataResponse']:
        """
        The system data.
        """
        return pulumi.get(self, "system_data")

    @property
    @pulumi.getter
    def type(self) -> pulumi.Output[str]:
        """
        The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or "Microsoft.Storage/storageAccounts"
        """
        return pulumi.get(self, "type")

