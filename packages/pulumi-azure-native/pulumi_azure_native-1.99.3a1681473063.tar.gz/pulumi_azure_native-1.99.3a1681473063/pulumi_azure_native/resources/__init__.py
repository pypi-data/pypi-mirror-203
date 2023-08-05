# coding=utf-8
# *** WARNING: this file was generated by the Pulumi SDK Generator. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

from .. import _utilities
import typing
# Export this package's modules as members:
from ._enums import *
from .azure_cli_script import *
from .azure_power_shell_script import *
from .deployment import *
from .deployment_at_management_group_scope import *
from .deployment_at_scope import *
from .deployment_at_subscription_scope import *
from .deployment_at_tenant_scope import *
from .get_azure_cli_script import *
from .get_azure_power_shell_script import *
from .get_deployment import *
from .get_deployment_at_management_group_scope import *
from .get_deployment_at_scope import *
from .get_deployment_at_subscription_scope import *
from .get_deployment_at_tenant_scope import *
from .get_resource import *
from .get_resource_group import *
from .get_tag_at_scope import *
from .get_template_spec import *
from .get_template_spec_version import *
from .resource import *
from .resource_group import *
from .tag_at_scope import *
from .template_spec import *
from .template_spec_version import *
from ._inputs import *
from . import outputs

# Make subpackages available:
if typing.TYPE_CHECKING:
    import pulumi_azure_native.resources.v20151101 as __v20151101
    v20151101 = __v20151101
    import pulumi_azure_native.resources.v20160201 as __v20160201
    v20160201 = __v20160201
    import pulumi_azure_native.resources.v20160701 as __v20160701
    v20160701 = __v20160701
    import pulumi_azure_native.resources.v20160901 as __v20160901
    v20160901 = __v20160901
    import pulumi_azure_native.resources.v20170510 as __v20170510
    v20170510 = __v20170510
    import pulumi_azure_native.resources.v20180201 as __v20180201
    v20180201 = __v20180201
    import pulumi_azure_native.resources.v20180501 as __v20180501
    v20180501 = __v20180501
    import pulumi_azure_native.resources.v20190301 as __v20190301
    v20190301 = __v20190301
    import pulumi_azure_native.resources.v20190501 as __v20190501
    v20190501 = __v20190501
    import pulumi_azure_native.resources.v20190510 as __v20190510
    v20190510 = __v20190510
    import pulumi_azure_native.resources.v20190601preview as __v20190601preview
    v20190601preview = __v20190601preview
    import pulumi_azure_native.resources.v20190701 as __v20190701
    v20190701 = __v20190701
    import pulumi_azure_native.resources.v20190801 as __v20190801
    v20190801 = __v20190801
    import pulumi_azure_native.resources.v20191001 as __v20191001
    v20191001 = __v20191001
    import pulumi_azure_native.resources.v20191001preview as __v20191001preview
    v20191001preview = __v20191001preview
    import pulumi_azure_native.resources.v20200601 as __v20200601
    v20200601 = __v20200601
    import pulumi_azure_native.resources.v20200801 as __v20200801
    v20200801 = __v20200801
    import pulumi_azure_native.resources.v20201001 as __v20201001
    v20201001 = __v20201001
    import pulumi_azure_native.resources.v20210101 as __v20210101
    v20210101 = __v20210101
    import pulumi_azure_native.resources.v20210301preview as __v20210301preview
    v20210301preview = __v20210301preview
    import pulumi_azure_native.resources.v20210401 as __v20210401
    v20210401 = __v20210401
    import pulumi_azure_native.resources.v20210501 as __v20210501
    v20210501 = __v20210501
    import pulumi_azure_native.resources.v20220201 as __v20220201
    v20220201 = __v20220201
    import pulumi_azure_native.resources.v20220901 as __v20220901
    v20220901 = __v20220901
else:
    v20151101 = _utilities.lazy_import('pulumi_azure_native.resources.v20151101')
    v20160201 = _utilities.lazy_import('pulumi_azure_native.resources.v20160201')
    v20160701 = _utilities.lazy_import('pulumi_azure_native.resources.v20160701')
    v20160901 = _utilities.lazy_import('pulumi_azure_native.resources.v20160901')
    v20170510 = _utilities.lazy_import('pulumi_azure_native.resources.v20170510')
    v20180201 = _utilities.lazy_import('pulumi_azure_native.resources.v20180201')
    v20180501 = _utilities.lazy_import('pulumi_azure_native.resources.v20180501')
    v20190301 = _utilities.lazy_import('pulumi_azure_native.resources.v20190301')
    v20190501 = _utilities.lazy_import('pulumi_azure_native.resources.v20190501')
    v20190510 = _utilities.lazy_import('pulumi_azure_native.resources.v20190510')
    v20190601preview = _utilities.lazy_import('pulumi_azure_native.resources.v20190601preview')
    v20190701 = _utilities.lazy_import('pulumi_azure_native.resources.v20190701')
    v20190801 = _utilities.lazy_import('pulumi_azure_native.resources.v20190801')
    v20191001 = _utilities.lazy_import('pulumi_azure_native.resources.v20191001')
    v20191001preview = _utilities.lazy_import('pulumi_azure_native.resources.v20191001preview')
    v20200601 = _utilities.lazy_import('pulumi_azure_native.resources.v20200601')
    v20200801 = _utilities.lazy_import('pulumi_azure_native.resources.v20200801')
    v20201001 = _utilities.lazy_import('pulumi_azure_native.resources.v20201001')
    v20210101 = _utilities.lazy_import('pulumi_azure_native.resources.v20210101')
    v20210301preview = _utilities.lazy_import('pulumi_azure_native.resources.v20210301preview')
    v20210401 = _utilities.lazy_import('pulumi_azure_native.resources.v20210401')
    v20210501 = _utilities.lazy_import('pulumi_azure_native.resources.v20210501')
    v20220201 = _utilities.lazy_import('pulumi_azure_native.resources.v20220201')
    v20220901 = _utilities.lazy_import('pulumi_azure_native.resources.v20220901')

