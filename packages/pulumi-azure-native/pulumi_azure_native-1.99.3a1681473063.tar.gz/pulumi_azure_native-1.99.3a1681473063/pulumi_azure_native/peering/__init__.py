# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .connection_monitor_test import *
from .get_connection_monitor_test import *
from .get_peer_asn import *
from .get_peering import *
from .get_peering_service import *
from .get_prefix import *
from .get_registered_asn import *
from .get_registered_prefix import *
from .peer_asn import *
from .peering import *
from .peering_service import *
from .prefix import *
from .registered_asn import *
from .registered_prefix import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.peering.v20190801preview as __v20190801preview
    v20190801preview = __v20190801preview
    import pulumi_azure_native.peering.v20190901preview as __v20190901preview
    v20190901preview = __v20190901preview
    import pulumi_azure_native.peering.v20200101preview as __v20200101preview
    v20200101preview = __v20200101preview
    import pulumi_azure_native.peering.v20200401 as __v20200401
    v20200401 = __v20200401
    import pulumi_azure_native.peering.v20201001 as __v20201001
    v20201001 = __v20201001
    import pulumi_azure_native.peering.v20210101 as __v20210101
    v20210101 = __v20210101
    import pulumi_azure_native.peering.v20210601 as __v20210601
    v20210601 = __v20210601
    import pulumi_azure_native.peering.v20220101 as __v20220101
    v20220101 = __v20220101
    import pulumi_azure_native.peering.v20220601 as __v20220601
    v20220601 = __v20220601
    import pulumi_azure_native.peering.v20221001 as __v20221001
    v20221001 = __v20221001
else:
    v20190801preview = _utilities.lazy_import('pulumi_azure_native.peering.v20190801preview')
    v20190901preview = _utilities.lazy_import('pulumi_azure_native.peering.v20190901preview')
    v20200101preview = _utilities.lazy_import('pulumi_azure_native.peering.v20200101preview')
    v20200401 = _utilities.lazy_import('pulumi_azure_native.peering.v20200401')
    v20201001 = _utilities.lazy_import('pulumi_azure_native.peering.v20201001')
    v20210101 = _utilities.lazy_import('pulumi_azure_native.peering.v20210101')
    v20210601 = _utilities.lazy_import('pulumi_azure_native.peering.v20210601')
    v20220101 = _utilities.lazy_import('pulumi_azure_native.peering.v20220101')
    v20220601 = _utilities.lazy_import('pulumi_azure_native.peering.v20220601')
    v20221001 = _utilities.lazy_import('pulumi_azure_native.peering.v20221001')

