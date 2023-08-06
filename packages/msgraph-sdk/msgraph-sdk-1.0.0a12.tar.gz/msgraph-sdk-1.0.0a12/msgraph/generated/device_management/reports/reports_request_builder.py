from __future__ import annotations
from dataclasses import dataclass
from kiota_abstractions.get_path_parameters import get_path_parameters
from kiota_abstractions.method import Method
from kiota_abstractions.request_adapter import RequestAdapter
from kiota_abstractions.request_information import RequestInformation
from kiota_abstractions.request_option import RequestOption
from kiota_abstractions.response_handler import ResponseHandler
from kiota_abstractions.serialization import Parsable, ParsableFactory
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from ...models import device_management_reports
    from ...models.o_data_errors import o_data_error
    from .export_jobs import export_jobs_request_builder
    from .get_cached_report import get_cached_report_request_builder
    from .get_compliance_policy_non_compliance_report import get_compliance_policy_non_compliance_report_request_builder
    from .get_compliance_policy_non_compliance_summary_report import get_compliance_policy_non_compliance_summary_report_request_builder
    from .get_compliance_setting_non_compliance_report import get_compliance_setting_non_compliance_report_request_builder
    from .get_configuration_policy_non_compliance_report import get_configuration_policy_non_compliance_report_request_builder
    from .get_configuration_policy_non_compliance_summary_report import get_configuration_policy_non_compliance_summary_report_request_builder
    from .get_configuration_setting_non_compliance_report import get_configuration_setting_non_compliance_report_request_builder
    from .get_device_management_intent_per_setting_contributing_profiles import get_device_management_intent_per_setting_contributing_profiles_request_builder
    from .get_device_management_intent_settings_report import get_device_management_intent_settings_report_request_builder
    from .get_device_non_compliance_report import get_device_non_compliance_report_request_builder
    from .get_devices_without_compliance_policy_report import get_devices_without_compliance_policy_report_request_builder
    from .get_historical_report import get_historical_report_request_builder
    from .get_noncompliant_devices_and_settings_report import get_noncompliant_devices_and_settings_report_request_builder
    from .get_policy_non_compliance_metadata import get_policy_non_compliance_metadata_request_builder
    from .get_policy_non_compliance_report import get_policy_non_compliance_report_request_builder
    from .get_policy_non_compliance_summary_report import get_policy_non_compliance_summary_report_request_builder
    from .get_report_filters import get_report_filters_request_builder
    from .get_setting_non_compliance_report import get_setting_non_compliance_report_request_builder

class ReportsRequestBuilder():
    """
    Provides operations to manage the reports property of the microsoft.graph.deviceManagement entity.
    """
    def __init__(self,request_adapter: RequestAdapter, path_parameters: Optional[Union[Dict[str, Any], str]] = None) -> None:
        """
        Instantiates a new ReportsRequestBuilder and sets the default values.
        Args:
            pathParameters: The raw url or the Url template parameters for the request.
            requestAdapter: The request adapter to use to execute the requests.
        """
        if path_parameters is None:
            raise Exception("path_parameters cannot be undefined")
        if request_adapter is None:
            raise Exception("request_adapter cannot be undefined")
        # Url template to use to build the URL for the current request builder
        self.url_template: str = "{+baseurl}/deviceManagement/reports{?%24select,%24expand}"

        url_tpl_params = get_path_parameters(path_parameters)
        self.path_parameters = url_tpl_params
        self.request_adapter = request_adapter
    
    async def delete(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> None:
        """
        Delete navigation property reports for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        """
        request_info = self.to_delete_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        return await self.request_adapter.send_no_response_content_async(request_info, error_mapping)
    
    async def get(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Reports singleton
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_reports.DeviceManagementReports]
        """
        request_info = self.to_get_request_information(
            request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import device_management_reports

        return await self.request_adapter.send_async(request_info, device_management_reports.DeviceManagementReports, error_mapping)
    
    async def patch(self,body: Optional[device_management_reports.DeviceManagementReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> Optional[device_management_reports.DeviceManagementReports]:
        """
        Update the navigation property reports in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: Optional[device_management_reports.DeviceManagementReports]
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = self.to_patch_request_information(
            body, request_configuration
        )
        from ...models.o_data_errors import o_data_error

        error_mapping: Dict[str, ParsableFactory] = {
            "4XX": o_data_error.ODataError,
            "5XX": o_data_error.ODataError,
        }
        if not self.request_adapter:
            raise Exception("Http core is null") 
        from ...models import device_management_reports

        return await self.request_adapter.send_async(request_info, device_management_reports.DeviceManagementReports, error_mapping)
    
    def to_delete_request_information(self,request_configuration: Optional[ReportsRequestBuilderDeleteRequestConfiguration] = None) -> RequestInformation:
        """
        Delete navigation property reports for deviceManagement
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.DELETE
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_get_request_information(self,request_configuration: Optional[ReportsRequestBuilderGetRequestConfiguration] = None) -> RequestInformation:
        """
        Reports singleton
        Args:
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.GET
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.set_query_string_parameters_from_raw_object(request_configuration.query_parameters)
            request_info.add_request_options(request_configuration.options)
        return request_info
    
    def to_patch_request_information(self,body: Optional[device_management_reports.DeviceManagementReports] = None, request_configuration: Optional[ReportsRequestBuilderPatchRequestConfiguration] = None) -> RequestInformation:
        """
        Update the navigation property reports in deviceManagement
        Args:
            body: The request body
            requestConfiguration: Configuration for the request such as headers, query parameters, and middleware options.
        Returns: RequestInformation
        """
        if body is None:
            raise Exception("body cannot be undefined")
        request_info = RequestInformation()
        request_info.url_template = self.url_template
        request_info.path_parameters = self.path_parameters
        request_info.http_method = Method.PATCH
        request_info.headers["Accept"] = ["application/json"]
        if request_configuration:
            request_info.add_request_headers(request_configuration.headers)
            request_info.add_request_options(request_configuration.options)
        request_info.set_content_from_parsable(self.request_adapter, "application/json", body)
        return request_info
    
    @property
    def export_jobs(self) -> export_jobs_request_builder.ExportJobsRequestBuilder:
        """
        Provides operations to manage the exportJobs property of the microsoft.graph.deviceManagementReports entity.
        """
        from .export_jobs import export_jobs_request_builder

        return export_jobs_request_builder.ExportJobsRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_cached_report(self) -> get_cached_report_request_builder.GetCachedReportRequestBuilder:
        """
        Provides operations to call the getCachedReport method.
        """
        from .get_cached_report import get_cached_report_request_builder

        return get_cached_report_request_builder.GetCachedReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_report(self) -> get_compliance_policy_non_compliance_report_request_builder.GetCompliancePolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceReport method.
        """
        from .get_compliance_policy_non_compliance_report import get_compliance_policy_non_compliance_report_request_builder

        return get_compliance_policy_non_compliance_report_request_builder.GetCompliancePolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_policy_non_compliance_summary_report(self) -> get_compliance_policy_non_compliance_summary_report_request_builder.GetCompliancePolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getCompliancePolicyNonComplianceSummaryReport method.
        """
        from .get_compliance_policy_non_compliance_summary_report import get_compliance_policy_non_compliance_summary_report_request_builder

        return get_compliance_policy_non_compliance_summary_report_request_builder.GetCompliancePolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_compliance_setting_non_compliance_report(self) -> get_compliance_setting_non_compliance_report_request_builder.GetComplianceSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getComplianceSettingNonComplianceReport method.
        """
        from .get_compliance_setting_non_compliance_report import get_compliance_setting_non_compliance_report_request_builder

        return get_compliance_setting_non_compliance_report_request_builder.GetComplianceSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_report(self) -> get_configuration_policy_non_compliance_report_request_builder.GetConfigurationPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceReport method.
        """
        from .get_configuration_policy_non_compliance_report import get_configuration_policy_non_compliance_report_request_builder

        return get_configuration_policy_non_compliance_report_request_builder.GetConfigurationPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_policy_non_compliance_summary_report(self) -> get_configuration_policy_non_compliance_summary_report_request_builder.GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getConfigurationPolicyNonComplianceSummaryReport method.
        """
        from .get_configuration_policy_non_compliance_summary_report import get_configuration_policy_non_compliance_summary_report_request_builder

        return get_configuration_policy_non_compliance_summary_report_request_builder.GetConfigurationPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_configuration_setting_non_compliance_report(self) -> get_configuration_setting_non_compliance_report_request_builder.GetConfigurationSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getConfigurationSettingNonComplianceReport method.
        """
        from .get_configuration_setting_non_compliance_report import get_configuration_setting_non_compliance_report_request_builder

        return get_configuration_setting_non_compliance_report_request_builder.GetConfigurationSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_per_setting_contributing_profiles(self) -> get_device_management_intent_per_setting_contributing_profiles_request_builder.GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentPerSettingContributingProfiles method.
        """
        from .get_device_management_intent_per_setting_contributing_profiles import get_device_management_intent_per_setting_contributing_profiles_request_builder

        return get_device_management_intent_per_setting_contributing_profiles_request_builder.GetDeviceManagementIntentPerSettingContributingProfilesRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_management_intent_settings_report(self) -> get_device_management_intent_settings_report_request_builder.GetDeviceManagementIntentSettingsReportRequestBuilder:
        """
        Provides operations to call the getDeviceManagementIntentSettingsReport method.
        """
        from .get_device_management_intent_settings_report import get_device_management_intent_settings_report_request_builder

        return get_device_management_intent_settings_report_request_builder.GetDeviceManagementIntentSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_device_non_compliance_report(self) -> get_device_non_compliance_report_request_builder.GetDeviceNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getDeviceNonComplianceReport method.
        """
        from .get_device_non_compliance_report import get_device_non_compliance_report_request_builder

        return get_device_non_compliance_report_request_builder.GetDeviceNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_devices_without_compliance_policy_report(self) -> get_devices_without_compliance_policy_report_request_builder.GetDevicesWithoutCompliancePolicyReportRequestBuilder:
        """
        Provides operations to call the getDevicesWithoutCompliancePolicyReport method.
        """
        from .get_devices_without_compliance_policy_report import get_devices_without_compliance_policy_report_request_builder

        return get_devices_without_compliance_policy_report_request_builder.GetDevicesWithoutCompliancePolicyReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_historical_report(self) -> get_historical_report_request_builder.GetHistoricalReportRequestBuilder:
        """
        Provides operations to call the getHistoricalReport method.
        """
        from .get_historical_report import get_historical_report_request_builder

        return get_historical_report_request_builder.GetHistoricalReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_noncompliant_devices_and_settings_report(self) -> get_noncompliant_devices_and_settings_report_request_builder.GetNoncompliantDevicesAndSettingsReportRequestBuilder:
        """
        Provides operations to call the getNoncompliantDevicesAndSettingsReport method.
        """
        from .get_noncompliant_devices_and_settings_report import get_noncompliant_devices_and_settings_report_request_builder

        return get_noncompliant_devices_and_settings_report_request_builder.GetNoncompliantDevicesAndSettingsReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_metadata(self) -> get_policy_non_compliance_metadata_request_builder.GetPolicyNonComplianceMetadataRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceMetadata method.
        """
        from .get_policy_non_compliance_metadata import get_policy_non_compliance_metadata_request_builder

        return get_policy_non_compliance_metadata_request_builder.GetPolicyNonComplianceMetadataRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_report(self) -> get_policy_non_compliance_report_request_builder.GetPolicyNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceReport method.
        """
        from .get_policy_non_compliance_report import get_policy_non_compliance_report_request_builder

        return get_policy_non_compliance_report_request_builder.GetPolicyNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_policy_non_compliance_summary_report(self) -> get_policy_non_compliance_summary_report_request_builder.GetPolicyNonComplianceSummaryReportRequestBuilder:
        """
        Provides operations to call the getPolicyNonComplianceSummaryReport method.
        """
        from .get_policy_non_compliance_summary_report import get_policy_non_compliance_summary_report_request_builder

        return get_policy_non_compliance_summary_report_request_builder.GetPolicyNonComplianceSummaryReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_report_filters(self) -> get_report_filters_request_builder.GetReportFiltersRequestBuilder:
        """
        Provides operations to call the getReportFilters method.
        """
        from .get_report_filters import get_report_filters_request_builder

        return get_report_filters_request_builder.GetReportFiltersRequestBuilder(self.request_adapter, self.path_parameters)
    
    @property
    def get_setting_non_compliance_report(self) -> get_setting_non_compliance_report_request_builder.GetSettingNonComplianceReportRequestBuilder:
        """
        Provides operations to call the getSettingNonComplianceReport method.
        """
        from .get_setting_non_compliance_report import get_setting_non_compliance_report_request_builder

        return get_setting_non_compliance_report_request_builder.GetSettingNonComplianceReportRequestBuilder(self.request_adapter, self.path_parameters)
    
    @dataclass
    class ReportsRequestBuilderDeleteRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    
    @dataclass
    class ReportsRequestBuilderGetQueryParameters():
        """
        Reports singleton
        """
        def get_query_parameter(self,original_name: Optional[str] = None) -> str:
            """
            Maps the query parameters names to their encoded names for the URI template parsing.
            Args:
                originalName: The original query parameter name in the class.
            Returns: str
            """
            if original_name is None:
                raise Exception("original_name cannot be undefined")
            if original_name == "expand":
                return "%24expand"
            if original_name == "select":
                return "%24select"
            return original_name
        
        # Expand related entities
        expand: Optional[List[str]] = None

        # Select properties to be returned
        select: Optional[List[str]] = None

    
    @dataclass
    class ReportsRequestBuilderGetRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

        # Request query parameters
        query_parameters: Optional[ReportsRequestBuilder.ReportsRequestBuilderGetQueryParameters] = None

    
    @dataclass
    class ReportsRequestBuilderPatchRequestConfiguration():
        """
        Configuration for the request such as headers, query parameters, and middleware options.
        """
        # Request headers
        headers: Optional[Dict[str, Union[str, List[str]]]] = None

        # Request options
        options: Optional[List[RequestOption]] = None

    

