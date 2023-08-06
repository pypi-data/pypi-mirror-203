from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import android_custom_configuration, android_general_device_configuration, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, apple_device_features_configuration_base, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_user_overview, device_configuration_user_status, edition_upgrade_configuration, entity, ios_certificate_profile, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_update_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, setting_state_device_summary, shared_p_c_configuration, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_general_configuration, windows_defender_advanced_threat_protection_configuration, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_update_for_business_configuration

from . import entity

class DeviceConfiguration(entity.Entity):
    """
    Device Configuration.
    """
    def __init__(self,) -> None:
        """
        Instantiates a new deviceConfiguration and sets the default values.
        """
        super().__init__()
        # The list of assignments for the device configuration profile.
        self._assignments: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None
        # DateTime the object was created.
        self._created_date_time: Optional[datetime] = None
        # Admin provided description of the Device Configuration.
        self._description: Optional[str] = None
        # Device Configuration Setting State Device Summary
        self._device_setting_state_summaries: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None
        # Device Configuration devices status overview
        self._device_status_overview: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview] = None
        # Device configuration installation status by device.
        self._device_statuses: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]] = None
        # Admin provided name of the device configuration.
        self._display_name: Optional[str] = None
        # DateTime the object was last modified.
        self._last_modified_date_time: Optional[datetime] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Device Configuration users status overview
        self._user_status_overview: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview] = None
        # Device configuration installation status by user.
        self._user_statuses: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]] = None
        # Version of the device configuration.
        self._version: Optional[int] = None
    
    @property
    def assignments(self,) -> Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]]:
        """
        Gets the assignments property value. The list of assignments for the device configuration profile.
        Returns: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]]
        """
        return self._assignments
    
    @assignments.setter
    def assignments(self,value: Optional[List[device_configuration_assignment.DeviceConfigurationAssignment]] = None) -> None:
        """
        Sets the assignments property value. The list of assignments for the device configuration profile.
        Args:
            value: Value to set for the assignments property.
        """
        self._assignments = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. DateTime the object was created.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. DateTime the object was created.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> DeviceConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: DeviceConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        mapping_value_node = parse_node.get_child_node("@odata.type")
        if mapping_value_node:
            mapping_value = mapping_value_node.get_str_value()
            if mapping_value == "#microsoft.graph.androidCustomConfiguration":
                from . import android_custom_configuration

                return android_custom_configuration.AndroidCustomConfiguration()
            if mapping_value == "#microsoft.graph.androidGeneralDeviceConfiguration":
                from . import android_general_device_configuration

                return android_general_device_configuration.AndroidGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileCustomConfiguration":
                from . import android_work_profile_custom_configuration

                return android_work_profile_custom_configuration.AndroidWorkProfileCustomConfiguration()
            if mapping_value == "#microsoft.graph.androidWorkProfileGeneralDeviceConfiguration":
                from . import android_work_profile_general_device_configuration

                return android_work_profile_general_device_configuration.AndroidWorkProfileGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.appleDeviceFeaturesConfigurationBase":
                from . import apple_device_features_configuration_base

                return apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase()
            if mapping_value == "#microsoft.graph.editionUpgradeConfiguration":
                from . import edition_upgrade_configuration

                return edition_upgrade_configuration.EditionUpgradeConfiguration()
            if mapping_value == "#microsoft.graph.iosCertificateProfile":
                from . import ios_certificate_profile

                return ios_certificate_profile.IosCertificateProfile()
            if mapping_value == "#microsoft.graph.iosCustomConfiguration":
                from . import ios_custom_configuration

                return ios_custom_configuration.IosCustomConfiguration()
            if mapping_value == "#microsoft.graph.iosDeviceFeaturesConfiguration":
                from . import ios_device_features_configuration

                return ios_device_features_configuration.IosDeviceFeaturesConfiguration()
            if mapping_value == "#microsoft.graph.iosGeneralDeviceConfiguration":
                from . import ios_general_device_configuration

                return ios_general_device_configuration.IosGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.iosUpdateConfiguration":
                from . import ios_update_configuration

                return ios_update_configuration.IosUpdateConfiguration()
            if mapping_value == "#microsoft.graph.macOSCustomConfiguration":
                from . import mac_o_s_custom_configuration

                return mac_o_s_custom_configuration.MacOSCustomConfiguration()
            if mapping_value == "#microsoft.graph.macOSDeviceFeaturesConfiguration":
                from . import mac_o_s_device_features_configuration

                return mac_o_s_device_features_configuration.MacOSDeviceFeaturesConfiguration()
            if mapping_value == "#microsoft.graph.macOSGeneralDeviceConfiguration":
                from . import mac_o_s_general_device_configuration

                return mac_o_s_general_device_configuration.MacOSGeneralDeviceConfiguration()
            if mapping_value == "#microsoft.graph.sharedPCConfiguration":
                from . import shared_p_c_configuration

                return shared_p_c_configuration.SharedPCConfiguration()
            if mapping_value == "#microsoft.graph.windows10CustomConfiguration":
                from . import windows10_custom_configuration

                return windows10_custom_configuration.Windows10CustomConfiguration()
            if mapping_value == "#microsoft.graph.windows10EndpointProtectionConfiguration":
                from . import windows10_endpoint_protection_configuration

                return windows10_endpoint_protection_configuration.Windows10EndpointProtectionConfiguration()
            if mapping_value == "#microsoft.graph.windows10EnterpriseModernAppManagementConfiguration":
                from . import windows10_enterprise_modern_app_management_configuration

                return windows10_enterprise_modern_app_management_configuration.Windows10EnterpriseModernAppManagementConfiguration()
            if mapping_value == "#microsoft.graph.windows10GeneralConfiguration":
                from . import windows10_general_configuration

                return windows10_general_configuration.Windows10GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windows10SecureAssessmentConfiguration":
                from . import windows10_secure_assessment_configuration

                return windows10_secure_assessment_configuration.Windows10SecureAssessmentConfiguration()
            if mapping_value == "#microsoft.graph.windows10TeamGeneralConfiguration":
                from . import windows10_team_general_configuration

                return windows10_team_general_configuration.Windows10TeamGeneralConfiguration()
            if mapping_value == "#microsoft.graph.windows81GeneralConfiguration":
                from . import windows81_general_configuration

                return windows81_general_configuration.Windows81GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windowsDefenderAdvancedThreatProtectionConfiguration":
                from . import windows_defender_advanced_threat_protection_configuration

                return windows_defender_advanced_threat_protection_configuration.WindowsDefenderAdvancedThreatProtectionConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhone81CustomConfiguration":
                from . import windows_phone81_custom_configuration

                return windows_phone81_custom_configuration.WindowsPhone81CustomConfiguration()
            if mapping_value == "#microsoft.graph.windowsPhone81GeneralConfiguration":
                from . import windows_phone81_general_configuration

                return windows_phone81_general_configuration.WindowsPhone81GeneralConfiguration()
            if mapping_value == "#microsoft.graph.windowsUpdateForBusinessConfiguration":
                from . import windows_update_for_business_configuration

                return windows_update_for_business_configuration.WindowsUpdateForBusinessConfiguration()
        return DeviceConfiguration()
    
    @property
    def description(self,) -> Optional[str]:
        """
        Gets the description property value. Admin provided description of the Device Configuration.
        Returns: Optional[str]
        """
        return self._description
    
    @description.setter
    def description(self,value: Optional[str] = None) -> None:
        """
        Sets the description property value. Admin provided description of the Device Configuration.
        Args:
            value: Value to set for the description property.
        """
        self._description = value
    
    @property
    def device_setting_state_summaries(self,) -> Optional[List[setting_state_device_summary.SettingStateDeviceSummary]]:
        """
        Gets the deviceSettingStateSummaries property value. Device Configuration Setting State Device Summary
        Returns: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]]
        """
        return self._device_setting_state_summaries
    
    @device_setting_state_summaries.setter
    def device_setting_state_summaries(self,value: Optional[List[setting_state_device_summary.SettingStateDeviceSummary]] = None) -> None:
        """
        Sets the deviceSettingStateSummaries property value. Device Configuration Setting State Device Summary
        Args:
            value: Value to set for the device_setting_state_summaries property.
        """
        self._device_setting_state_summaries = value
    
    @property
    def device_status_overview(self,) -> Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview]:
        """
        Gets the deviceStatusOverview property value. Device Configuration devices status overview
        Returns: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview]
        """
        return self._device_status_overview
    
    @device_status_overview.setter
    def device_status_overview(self,value: Optional[device_configuration_device_overview.DeviceConfigurationDeviceOverview] = None) -> None:
        """
        Sets the deviceStatusOverview property value. Device Configuration devices status overview
        Args:
            value: Value to set for the device_status_overview property.
        """
        self._device_status_overview = value
    
    @property
    def device_statuses(self,) -> Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]]:
        """
        Gets the deviceStatuses property value. Device configuration installation status by device.
        Returns: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]]
        """
        return self._device_statuses
    
    @device_statuses.setter
    def device_statuses(self,value: Optional[List[device_configuration_device_status.DeviceConfigurationDeviceStatus]] = None) -> None:
        """
        Sets the deviceStatuses property value. Device configuration installation status by device.
        Args:
            value: Value to set for the device_statuses property.
        """
        self._device_statuses = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. Admin provided name of the device configuration.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. Admin provided name of the device configuration.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import android_custom_configuration, android_general_device_configuration, android_work_profile_custom_configuration, android_work_profile_general_device_configuration, apple_device_features_configuration_base, device_configuration_assignment, device_configuration_device_overview, device_configuration_device_status, device_configuration_user_overview, device_configuration_user_status, edition_upgrade_configuration, entity, ios_certificate_profile, ios_custom_configuration, ios_device_features_configuration, ios_general_device_configuration, ios_update_configuration, mac_o_s_custom_configuration, mac_o_s_device_features_configuration, mac_o_s_general_device_configuration, setting_state_device_summary, shared_p_c_configuration, windows10_custom_configuration, windows10_endpoint_protection_configuration, windows10_enterprise_modern_app_management_configuration, windows10_general_configuration, windows10_secure_assessment_configuration, windows10_team_general_configuration, windows81_general_configuration, windows_defender_advanced_threat_protection_configuration, windows_phone81_custom_configuration, windows_phone81_general_configuration, windows_update_for_business_configuration

        fields: Dict[str, Callable[[Any], None]] = {
            "assignments": lambda n : setattr(self, 'assignments', n.get_collection_of_object_values(device_configuration_assignment.DeviceConfigurationAssignment)),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "description": lambda n : setattr(self, 'description', n.get_str_value()),
            "deviceSettingStateSummaries": lambda n : setattr(self, 'device_setting_state_summaries', n.get_collection_of_object_values(setting_state_device_summary.SettingStateDeviceSummary)),
            "deviceStatuses": lambda n : setattr(self, 'device_statuses', n.get_collection_of_object_values(device_configuration_device_status.DeviceConfigurationDeviceStatus)),
            "deviceStatusOverview": lambda n : setattr(self, 'device_status_overview', n.get_object_value(device_configuration_device_overview.DeviceConfigurationDeviceOverview)),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "lastModifiedDateTime": lambda n : setattr(self, 'last_modified_date_time', n.get_datetime_value()),
            "userStatuses": lambda n : setattr(self, 'user_statuses', n.get_collection_of_object_values(device_configuration_user_status.DeviceConfigurationUserStatus)),
            "userStatusOverview": lambda n : setattr(self, 'user_status_overview', n.get_object_value(device_configuration_user_overview.DeviceConfigurationUserOverview)),
            "version": lambda n : setattr(self, 'version', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def last_modified_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastModifiedDateTime property value. DateTime the object was last modified.
        Returns: Optional[datetime]
        """
        return self._last_modified_date_time
    
    @last_modified_date_time.setter
    def last_modified_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastModifiedDateTime property value. DateTime the object was last modified.
        Args:
            value: Value to set for the last_modified_date_time property.
        """
        self._last_modified_date_time = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignments", self.assignments)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("description", self.description)
        writer.write_collection_of_object_values("deviceSettingStateSummaries", self.device_setting_state_summaries)
        writer.write_collection_of_object_values("deviceStatuses", self.device_statuses)
        writer.write_object_value("deviceStatusOverview", self.device_status_overview)
        writer.write_str_value("displayName", self.display_name)
        writer.write_datetime_value("lastModifiedDateTime", self.last_modified_date_time)
        writer.write_collection_of_object_values("userStatuses", self.user_statuses)
        writer.write_object_value("userStatusOverview", self.user_status_overview)
        writer.write_int_value("version", self.version)
    
    @property
    def user_status_overview(self,) -> Optional[device_configuration_user_overview.DeviceConfigurationUserOverview]:
        """
        Gets the userStatusOverview property value. Device Configuration users status overview
        Returns: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview]
        """
        return self._user_status_overview
    
    @user_status_overview.setter
    def user_status_overview(self,value: Optional[device_configuration_user_overview.DeviceConfigurationUserOverview] = None) -> None:
        """
        Sets the userStatusOverview property value. Device Configuration users status overview
        Args:
            value: Value to set for the user_status_overview property.
        """
        self._user_status_overview = value
    
    @property
    def user_statuses(self,) -> Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]]:
        """
        Gets the userStatuses property value. Device configuration installation status by user.
        Returns: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]]
        """
        return self._user_statuses
    
    @user_statuses.setter
    def user_statuses(self,value: Optional[List[device_configuration_user_status.DeviceConfigurationUserStatus]] = None) -> None:
        """
        Sets the userStatuses property value. Device configuration installation status by user.
        Args:
            value: Value to set for the user_statuses property.
        """
        self._user_statuses = value
    
    @property
    def version(self,) -> Optional[int]:
        """
        Gets the version property value. Version of the device configuration.
        Returns: Optional[int]
        """
        return self._version
    
    @version.setter
    def version(self,value: Optional[int] = None) -> None:
        """
        Sets the version property value. Version of the device configuration.
        Args:
            value: Value to set for the version property.
        """
        self._version = value
    

