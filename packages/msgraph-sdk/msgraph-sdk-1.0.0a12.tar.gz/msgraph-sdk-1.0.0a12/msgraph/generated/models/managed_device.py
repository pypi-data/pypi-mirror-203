from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import compliance_state, configuration_manager_client_enabled_features, device_action_result, device_category, device_compliance_policy_state, device_configuration_state, device_enrollment_type, device_health_attestation_state, device_management_exchange_access_state, device_management_exchange_access_state_reason, device_registration_state, entity, managed_device_owner_type, managed_device_partner_reported_health_state, management_agent_type, user

from . import entity

class ManagedDevice(entity.Entity):
    """
    Devices that are managed or pre-enrolled through Intune
    """
    def __init__(self,) -> None:
        """
        Instantiates a new managedDevice and sets the default values.
        """
        super().__init__()
        # The code that allows the Activation Lock on managed device to be bypassed. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity in LIST call. Individual GET call with select query options is needed to retrieve actual values. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        self._activation_lock_bypass_code: Optional[str] = None
        # Android security patch level. This property is read-only.
        self._android_security_patch_level: Optional[str] = None
        # The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        self._azure_a_d_device_id: Optional[str] = None
        # Whether the device is Azure Active Directory registered. This property is read-only.
        self._azure_a_d_registered: Optional[bool] = None
        # The DateTime when device compliance grace period expires. This property is read-only.
        self._compliance_grace_period_expiration_date_time: Optional[datetime] = None
        # Compliance state.
        self._compliance_state: Optional[compliance_state.ComplianceState] = None
        # ConfigrMgr client enabled features. This property is read-only.
        self._configuration_manager_client_enabled_features: Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures] = None
        # List of ComplexType deviceActionResult objects. This property is read-only.
        self._device_action_results: Optional[List[device_action_result.DeviceActionResult]] = None
        # Device category
        self._device_category: Optional[device_category.DeviceCategory] = None
        # Device category display name. This property is read-only.
        self._device_category_display_name: Optional[str] = None
        # Device compliance policy states for this device.
        self._device_compliance_policy_states: Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]] = None
        # Device configuration states for this device.
        self._device_configuration_states: Optional[List[device_configuration_state.DeviceConfigurationState]] = None
        # Possible ways of adding a mobile device to management.
        self._device_enrollment_type: Optional[device_enrollment_type.DeviceEnrollmentType] = None
        # The device health attestation state. This property is read-only.
        self._device_health_attestation_state: Optional[device_health_attestation_state.DeviceHealthAttestationState] = None
        # Name of the device. This property is read-only.
        self._device_name: Optional[str] = None
        # Device registration status.
        self._device_registration_state: Optional[device_registration_state.DeviceRegistrationState] = None
        # Whether the device is Exchange ActiveSync activated. This property is read-only.
        self._eas_activated: Optional[bool] = None
        # Exchange ActivationSync activation time of the device. This property is read-only.
        self._eas_activation_date_time: Optional[datetime] = None
        # Exchange ActiveSync Id of the device. This property is read-only.
        self._eas_device_id: Optional[str] = None
        # Email(s) for the user associated with the device. This property is read-only.
        self._email_address: Optional[str] = None
        # Enrollment time of the device. This property is read-only.
        self._enrolled_date_time: Optional[datetime] = None
        # Indicates Ethernet MAC Address of the device. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity. Individual get call with select query options is needed to retrieve actual values. Example: deviceManagement/managedDevices({managedDeviceId})?$select=ethernetMacAddress Supports: $select. $Search is not supported. Read-only. This property is read-only.
        self._ethernet_mac_address: Optional[str] = None
        # Device Exchange Access State.
        self._exchange_access_state: Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState] = None
        # Device Exchange Access State Reason.
        self._exchange_access_state_reason: Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason] = None
        # Last time the device contacted Exchange. This property is read-only.
        self._exchange_last_successful_sync_date_time: Optional[datetime] = None
        # Free Storage in Bytes. Default value is 0. Read-only. This property is read-only.
        self._free_storage_space_in_bytes: Optional[int] = None
        # Integrated Circuit Card Identifier, it is A SIM card's unique identification number. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        self._iccid: Optional[str] = None
        # IMEI. This property is read-only.
        self._imei: Optional[str] = None
        # Device encryption status. This property is read-only.
        self._is_encrypted: Optional[bool] = None
        # Device supervised status. This property is read-only.
        self._is_supervised: Optional[bool] = None
        # whether the device is jail broken or rooted. This property is read-only.
        self._jail_broken: Optional[str] = None
        # The date and time that the device last completed a successful sync with Intune. This property is read-only.
        self._last_sync_date_time: Optional[datetime] = None
        # Automatically generated name to identify a device. Can be overwritten to a user friendly name.
        self._managed_device_name: Optional[str] = None
        # Owner type of device.
        self._managed_device_owner_type: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None
        # The managementAgent property
        self._management_agent: Optional[management_agent_type.ManagementAgentType] = None
        # Reports device management certificate expiration date. This property is read-only.
        self._management_certificate_expiration_date: Optional[datetime] = None
        # Manufacturer of the device. This property is read-only.
        self._manufacturer: Optional[str] = None
        # MEID. This property is read-only.
        self._meid: Optional[str] = None
        # Model of the device. This property is read-only.
        self._model: Optional[str] = None
        # Notes on the device created by IT Admin. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select.  $Search is not supported.
        self._notes: Optional[str] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # Operating system of the device. Windows, iOS, etc. This property is read-only.
        self._operating_system: Optional[str] = None
        # Operating system version of the device. This property is read-only.
        self._os_version: Optional[str] = None
        # Available health states for the Device Health API
        self._partner_reported_threat_state: Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState] = None
        # Phone number of the device. This property is read-only.
        self._phone_number: Optional[str] = None
        # Total Memory in Bytes. Return default value 0 in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. Default value is 0. Read-only. This property is read-only.
        self._physical_memory_in_bytes: Optional[int] = None
        # An error string that identifies issues when creating Remote Assistance session objects. This property is read-only.
        self._remote_assistance_session_error_details: Optional[str] = None
        # Url that allows a Remote Assistance session to be established with the device. This property is read-only.
        self._remote_assistance_session_url: Optional[str] = None
        # Reports if the managed iOS device is user approval enrollment. This property is read-only.
        self._require_user_enrollment_approval: Optional[bool] = None
        # SerialNumber. This property is read-only.
        self._serial_number: Optional[str] = None
        # Subscriber Carrier. This property is read-only.
        self._subscriber_carrier: Optional[str] = None
        # Total Storage in Bytes. This property is read-only.
        self._total_storage_space_in_bytes: Optional[int] = None
        # Unique Device Identifier for iOS and macOS devices. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        self._udid: Optional[str] = None
        # User display name. This property is read-only.
        self._user_display_name: Optional[str] = None
        # Unique Identifier for the user associated with the device. This property is read-only.
        self._user_id: Optional[str] = None
        # Device user principal name. This property is read-only.
        self._user_principal_name: Optional[str] = None
        # The primary users associated with the managed device.
        self._users: Optional[List[user.User]] = None
        # Wi-Fi MAC. This property is read-only.
        self._wi_fi_mac_address: Optional[str] = None
    
    @property
    def activation_lock_bypass_code(self,) -> Optional[str]:
        """
        Gets the activationLockBypassCode property value. The code that allows the Activation Lock on managed device to be bypassed. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity in LIST call. Individual GET call with select query options is needed to retrieve actual values. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Returns: Optional[str]
        """
        return self._activation_lock_bypass_code
    
    @activation_lock_bypass_code.setter
    def activation_lock_bypass_code(self,value: Optional[str] = None) -> None:
        """
        Sets the activationLockBypassCode property value. The code that allows the Activation Lock on managed device to be bypassed. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity in LIST call. Individual GET call with select query options is needed to retrieve actual values. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Args:
            value: Value to set for the activation_lock_bypass_code property.
        """
        self._activation_lock_bypass_code = value
    
    @property
    def android_security_patch_level(self,) -> Optional[str]:
        """
        Gets the androidSecurityPatchLevel property value. Android security patch level. This property is read-only.
        Returns: Optional[str]
        """
        return self._android_security_patch_level
    
    @android_security_patch_level.setter
    def android_security_patch_level(self,value: Optional[str] = None) -> None:
        """
        Sets the androidSecurityPatchLevel property value. Android security patch level. This property is read-only.
        Args:
            value: Value to set for the android_security_patch_level property.
        """
        self._android_security_patch_level = value
    
    @property
    def azure_a_d_device_id(self,) -> Optional[str]:
        """
        Gets the azureADDeviceId property value. The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        Returns: Optional[str]
        """
        return self._azure_a_d_device_id
    
    @azure_a_d_device_id.setter
    def azure_a_d_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the azureADDeviceId property value. The unique identifier for the Azure Active Directory device. Read only. This property is read-only.
        Args:
            value: Value to set for the azure_a_d_device_id property.
        """
        self._azure_a_d_device_id = value
    
    @property
    def azure_a_d_registered(self,) -> Optional[bool]:
        """
        Gets the azureADRegistered property value. Whether the device is Azure Active Directory registered. This property is read-only.
        Returns: Optional[bool]
        """
        return self._azure_a_d_registered
    
    @azure_a_d_registered.setter
    def azure_a_d_registered(self,value: Optional[bool] = None) -> None:
        """
        Sets the azureADRegistered property value. Whether the device is Azure Active Directory registered. This property is read-only.
        Args:
            value: Value to set for the azure_a_d_registered property.
        """
        self._azure_a_d_registered = value
    
    @property
    def compliance_grace_period_expiration_date_time(self,) -> Optional[datetime]:
        """
        Gets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._compliance_grace_period_expiration_date_time
    
    @compliance_grace_period_expiration_date_time.setter
    def compliance_grace_period_expiration_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the complianceGracePeriodExpirationDateTime property value. The DateTime when device compliance grace period expires. This property is read-only.
        Args:
            value: Value to set for the compliance_grace_period_expiration_date_time property.
        """
        self._compliance_grace_period_expiration_date_time = value
    
    @property
    def compliance_state(self,) -> Optional[compliance_state.ComplianceState]:
        """
        Gets the complianceState property value. Compliance state.
        Returns: Optional[compliance_state.ComplianceState]
        """
        return self._compliance_state
    
    @compliance_state.setter
    def compliance_state(self,value: Optional[compliance_state.ComplianceState] = None) -> None:
        """
        Sets the complianceState property value. Compliance state.
        Args:
            value: Value to set for the compliance_state property.
        """
        self._compliance_state = value
    
    @property
    def configuration_manager_client_enabled_features(self,) -> Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures]:
        """
        Gets the configurationManagerClientEnabledFeatures property value. ConfigrMgr client enabled features. This property is read-only.
        Returns: Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures]
        """
        return self._configuration_manager_client_enabled_features
    
    @configuration_manager_client_enabled_features.setter
    def configuration_manager_client_enabled_features(self,value: Optional[configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures] = None) -> None:
        """
        Sets the configurationManagerClientEnabledFeatures property value. ConfigrMgr client enabled features. This property is read-only.
        Args:
            value: Value to set for the configuration_manager_client_enabled_features property.
        """
        self._configuration_manager_client_enabled_features = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDevice:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDevice
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDevice()
    
    @property
    def device_action_results(self,) -> Optional[List[device_action_result.DeviceActionResult]]:
        """
        Gets the deviceActionResults property value. List of ComplexType deviceActionResult objects. This property is read-only.
        Returns: Optional[List[device_action_result.DeviceActionResult]]
        """
        return self._device_action_results
    
    @device_action_results.setter
    def device_action_results(self,value: Optional[List[device_action_result.DeviceActionResult]] = None) -> None:
        """
        Sets the deviceActionResults property value. List of ComplexType deviceActionResult objects. This property is read-only.
        Args:
            value: Value to set for the device_action_results property.
        """
        self._device_action_results = value
    
    @property
    def device_category(self,) -> Optional[device_category.DeviceCategory]:
        """
        Gets the deviceCategory property value. Device category
        Returns: Optional[device_category.DeviceCategory]
        """
        return self._device_category
    
    @device_category.setter
    def device_category(self,value: Optional[device_category.DeviceCategory] = None) -> None:
        """
        Sets the deviceCategory property value. Device category
        Args:
            value: Value to set for the device_category property.
        """
        self._device_category = value
    
    @property
    def device_category_display_name(self,) -> Optional[str]:
        """
        Gets the deviceCategoryDisplayName property value. Device category display name. This property is read-only.
        Returns: Optional[str]
        """
        return self._device_category_display_name
    
    @device_category_display_name.setter
    def device_category_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceCategoryDisplayName property value. Device category display name. This property is read-only.
        Args:
            value: Value to set for the device_category_display_name property.
        """
        self._device_category_display_name = value
    
    @property
    def device_compliance_policy_states(self,) -> Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]]:
        """
        Gets the deviceCompliancePolicyStates property value. Device compliance policy states for this device.
        Returns: Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]]
        """
        return self._device_compliance_policy_states
    
    @device_compliance_policy_states.setter
    def device_compliance_policy_states(self,value: Optional[List[device_compliance_policy_state.DeviceCompliancePolicyState]] = None) -> None:
        """
        Sets the deviceCompliancePolicyStates property value. Device compliance policy states for this device.
        Args:
            value: Value to set for the device_compliance_policy_states property.
        """
        self._device_compliance_policy_states = value
    
    @property
    def device_configuration_states(self,) -> Optional[List[device_configuration_state.DeviceConfigurationState]]:
        """
        Gets the deviceConfigurationStates property value. Device configuration states for this device.
        Returns: Optional[List[device_configuration_state.DeviceConfigurationState]]
        """
        return self._device_configuration_states
    
    @device_configuration_states.setter
    def device_configuration_states(self,value: Optional[List[device_configuration_state.DeviceConfigurationState]] = None) -> None:
        """
        Sets the deviceConfigurationStates property value. Device configuration states for this device.
        Args:
            value: Value to set for the device_configuration_states property.
        """
        self._device_configuration_states = value
    
    @property
    def device_enrollment_type(self,) -> Optional[device_enrollment_type.DeviceEnrollmentType]:
        """
        Gets the deviceEnrollmentType property value. Possible ways of adding a mobile device to management.
        Returns: Optional[device_enrollment_type.DeviceEnrollmentType]
        """
        return self._device_enrollment_type
    
    @device_enrollment_type.setter
    def device_enrollment_type(self,value: Optional[device_enrollment_type.DeviceEnrollmentType] = None) -> None:
        """
        Sets the deviceEnrollmentType property value. Possible ways of adding a mobile device to management.
        Args:
            value: Value to set for the device_enrollment_type property.
        """
        self._device_enrollment_type = value
    
    @property
    def device_health_attestation_state(self,) -> Optional[device_health_attestation_state.DeviceHealthAttestationState]:
        """
        Gets the deviceHealthAttestationState property value. The device health attestation state. This property is read-only.
        Returns: Optional[device_health_attestation_state.DeviceHealthAttestationState]
        """
        return self._device_health_attestation_state
    
    @device_health_attestation_state.setter
    def device_health_attestation_state(self,value: Optional[device_health_attestation_state.DeviceHealthAttestationState] = None) -> None:
        """
        Sets the deviceHealthAttestationState property value. The device health attestation state. This property is read-only.
        Args:
            value: Value to set for the device_health_attestation_state property.
        """
        self._device_health_attestation_state = value
    
    @property
    def device_name(self,) -> Optional[str]:
        """
        Gets the deviceName property value. Name of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._device_name
    
    @device_name.setter
    def device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the deviceName property value. Name of the device. This property is read-only.
        Args:
            value: Value to set for the device_name property.
        """
        self._device_name = value
    
    @property
    def device_registration_state(self,) -> Optional[device_registration_state.DeviceRegistrationState]:
        """
        Gets the deviceRegistrationState property value. Device registration status.
        Returns: Optional[device_registration_state.DeviceRegistrationState]
        """
        return self._device_registration_state
    
    @device_registration_state.setter
    def device_registration_state(self,value: Optional[device_registration_state.DeviceRegistrationState] = None) -> None:
        """
        Sets the deviceRegistrationState property value. Device registration status.
        Args:
            value: Value to set for the device_registration_state property.
        """
        self._device_registration_state = value
    
    @property
    def eas_activated(self,) -> Optional[bool]:
        """
        Gets the easActivated property value. Whether the device is Exchange ActiveSync activated. This property is read-only.
        Returns: Optional[bool]
        """
        return self._eas_activated
    
    @eas_activated.setter
    def eas_activated(self,value: Optional[bool] = None) -> None:
        """
        Sets the easActivated property value. Whether the device is Exchange ActiveSync activated. This property is read-only.
        Args:
            value: Value to set for the eas_activated property.
        """
        self._eas_activated = value
    
    @property
    def eas_activation_date_time(self,) -> Optional[datetime]:
        """
        Gets the easActivationDateTime property value. Exchange ActivationSync activation time of the device. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._eas_activation_date_time
    
    @eas_activation_date_time.setter
    def eas_activation_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the easActivationDateTime property value. Exchange ActivationSync activation time of the device. This property is read-only.
        Args:
            value: Value to set for the eas_activation_date_time property.
        """
        self._eas_activation_date_time = value
    
    @property
    def eas_device_id(self,) -> Optional[str]:
        """
        Gets the easDeviceId property value. Exchange ActiveSync Id of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._eas_device_id
    
    @eas_device_id.setter
    def eas_device_id(self,value: Optional[str] = None) -> None:
        """
        Sets the easDeviceId property value. Exchange ActiveSync Id of the device. This property is read-only.
        Args:
            value: Value to set for the eas_device_id property.
        """
        self._eas_device_id = value
    
    @property
    def email_address(self,) -> Optional[str]:
        """
        Gets the emailAddress property value. Email(s) for the user associated with the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._email_address
    
    @email_address.setter
    def email_address(self,value: Optional[str] = None) -> None:
        """
        Sets the emailAddress property value. Email(s) for the user associated with the device. This property is read-only.
        Args:
            value: Value to set for the email_address property.
        """
        self._email_address = value
    
    @property
    def enrolled_date_time(self,) -> Optional[datetime]:
        """
        Gets the enrolledDateTime property value. Enrollment time of the device. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._enrolled_date_time
    
    @enrolled_date_time.setter
    def enrolled_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the enrolledDateTime property value. Enrollment time of the device. This property is read-only.
        Args:
            value: Value to set for the enrolled_date_time property.
        """
        self._enrolled_date_time = value
    
    @property
    def ethernet_mac_address(self,) -> Optional[str]:
        """
        Gets the ethernetMacAddress property value. Indicates Ethernet MAC Address of the device. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity. Individual get call with select query options is needed to retrieve actual values. Example: deviceManagement/managedDevices({managedDeviceId})?$select=ethernetMacAddress Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Returns: Optional[str]
        """
        return self._ethernet_mac_address
    
    @ethernet_mac_address.setter
    def ethernet_mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the ethernetMacAddress property value. Indicates Ethernet MAC Address of the device. Default, is Null (Non-Default property) for this property when returned as part of managedDevice entity. Individual get call with select query options is needed to retrieve actual values. Example: deviceManagement/managedDevices({managedDeviceId})?$select=ethernetMacAddress Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Args:
            value: Value to set for the ethernet_mac_address property.
        """
        self._ethernet_mac_address = value
    
    @property
    def exchange_access_state(self,) -> Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState]:
        """
        Gets the exchangeAccessState property value. Device Exchange Access State.
        Returns: Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState]
        """
        return self._exchange_access_state
    
    @exchange_access_state.setter
    def exchange_access_state(self,value: Optional[device_management_exchange_access_state.DeviceManagementExchangeAccessState] = None) -> None:
        """
        Sets the exchangeAccessState property value. Device Exchange Access State.
        Args:
            value: Value to set for the exchange_access_state property.
        """
        self._exchange_access_state = value
    
    @property
    def exchange_access_state_reason(self,) -> Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason]:
        """
        Gets the exchangeAccessStateReason property value. Device Exchange Access State Reason.
        Returns: Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason]
        """
        return self._exchange_access_state_reason
    
    @exchange_access_state_reason.setter
    def exchange_access_state_reason(self,value: Optional[device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason] = None) -> None:
        """
        Sets the exchangeAccessStateReason property value. Device Exchange Access State Reason.
        Args:
            value: Value to set for the exchange_access_state_reason property.
        """
        self._exchange_access_state_reason = value
    
    @property
    def exchange_last_successful_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the exchangeLastSuccessfulSyncDateTime property value. Last time the device contacted Exchange. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._exchange_last_successful_sync_date_time
    
    @exchange_last_successful_sync_date_time.setter
    def exchange_last_successful_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the exchangeLastSuccessfulSyncDateTime property value. Last time the device contacted Exchange. This property is read-only.
        Args:
            value: Value to set for the exchange_last_successful_sync_date_time property.
        """
        self._exchange_last_successful_sync_date_time = value
    
    @property
    def free_storage_space_in_bytes(self,) -> Optional[int]:
        """
        Gets the freeStorageSpaceInBytes property value. Free Storage in Bytes. Default value is 0. Read-only. This property is read-only.
        Returns: Optional[int]
        """
        return self._free_storage_space_in_bytes
    
    @free_storage_space_in_bytes.setter
    def free_storage_space_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the freeStorageSpaceInBytes property value. Free Storage in Bytes. Default value is 0. Read-only. This property is read-only.
        Args:
            value: Value to set for the free_storage_space_in_bytes property.
        """
        self._free_storage_space_in_bytes = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import compliance_state, configuration_manager_client_enabled_features, device_action_result, device_category, device_compliance_policy_state, device_configuration_state, device_enrollment_type, device_health_attestation_state, device_management_exchange_access_state, device_management_exchange_access_state_reason, device_registration_state, entity, managed_device_owner_type, managed_device_partner_reported_health_state, management_agent_type, user

        fields: Dict[str, Callable[[Any], None]] = {
            "activationLockBypassCode": lambda n : setattr(self, 'activation_lock_bypass_code', n.get_str_value()),
            "androidSecurityPatchLevel": lambda n : setattr(self, 'android_security_patch_level', n.get_str_value()),
            "azureADDeviceId": lambda n : setattr(self, 'azure_a_d_device_id', n.get_str_value()),
            "azureADRegistered": lambda n : setattr(self, 'azure_a_d_registered', n.get_bool_value()),
            "complianceGracePeriodExpirationDateTime": lambda n : setattr(self, 'compliance_grace_period_expiration_date_time', n.get_datetime_value()),
            "complianceState": lambda n : setattr(self, 'compliance_state', n.get_enum_value(compliance_state.ComplianceState)),
            "configurationManagerClientEnabledFeatures": lambda n : setattr(self, 'configuration_manager_client_enabled_features', n.get_object_value(configuration_manager_client_enabled_features.ConfigurationManagerClientEnabledFeatures)),
            "deviceActionResults": lambda n : setattr(self, 'device_action_results', n.get_collection_of_object_values(device_action_result.DeviceActionResult)),
            "deviceCategory": lambda n : setattr(self, 'device_category', n.get_object_value(device_category.DeviceCategory)),
            "deviceCategoryDisplayName": lambda n : setattr(self, 'device_category_display_name', n.get_str_value()),
            "deviceCompliancePolicyStates": lambda n : setattr(self, 'device_compliance_policy_states', n.get_collection_of_object_values(device_compliance_policy_state.DeviceCompliancePolicyState)),
            "deviceConfigurationStates": lambda n : setattr(self, 'device_configuration_states', n.get_collection_of_object_values(device_configuration_state.DeviceConfigurationState)),
            "deviceEnrollmentType": lambda n : setattr(self, 'device_enrollment_type', n.get_enum_value(device_enrollment_type.DeviceEnrollmentType)),
            "deviceHealthAttestationState": lambda n : setattr(self, 'device_health_attestation_state', n.get_object_value(device_health_attestation_state.DeviceHealthAttestationState)),
            "deviceName": lambda n : setattr(self, 'device_name', n.get_str_value()),
            "deviceRegistrationState": lambda n : setattr(self, 'device_registration_state', n.get_enum_value(device_registration_state.DeviceRegistrationState)),
            "easActivated": lambda n : setattr(self, 'eas_activated', n.get_bool_value()),
            "easActivationDateTime": lambda n : setattr(self, 'eas_activation_date_time', n.get_datetime_value()),
            "easDeviceId": lambda n : setattr(self, 'eas_device_id', n.get_str_value()),
            "emailAddress": lambda n : setattr(self, 'email_address', n.get_str_value()),
            "enrolledDateTime": lambda n : setattr(self, 'enrolled_date_time', n.get_datetime_value()),
            "ethernetMacAddress": lambda n : setattr(self, 'ethernet_mac_address', n.get_str_value()),
            "exchangeAccessState": lambda n : setattr(self, 'exchange_access_state', n.get_enum_value(device_management_exchange_access_state.DeviceManagementExchangeAccessState)),
            "exchangeAccessStateReason": lambda n : setattr(self, 'exchange_access_state_reason', n.get_enum_value(device_management_exchange_access_state_reason.DeviceManagementExchangeAccessStateReason)),
            "exchangeLastSuccessfulSyncDateTime": lambda n : setattr(self, 'exchange_last_successful_sync_date_time', n.get_datetime_value()),
            "freeStorageSpaceInBytes": lambda n : setattr(self, 'free_storage_space_in_bytes', n.get_int_value()),
            "iccid": lambda n : setattr(self, 'iccid', n.get_str_value()),
            "imei": lambda n : setattr(self, 'imei', n.get_str_value()),
            "isEncrypted": lambda n : setattr(self, 'is_encrypted', n.get_bool_value()),
            "isSupervised": lambda n : setattr(self, 'is_supervised', n.get_bool_value()),
            "jailBroken": lambda n : setattr(self, 'jail_broken', n.get_str_value()),
            "lastSyncDateTime": lambda n : setattr(self, 'last_sync_date_time', n.get_datetime_value()),
            "managedDeviceName": lambda n : setattr(self, 'managed_device_name', n.get_str_value()),
            "managedDeviceOwnerType": lambda n : setattr(self, 'managed_device_owner_type', n.get_enum_value(managed_device_owner_type.ManagedDeviceOwnerType)),
            "managementAgent": lambda n : setattr(self, 'management_agent', n.get_enum_value(management_agent_type.ManagementAgentType)),
            "managementCertificateExpirationDate": lambda n : setattr(self, 'management_certificate_expiration_date', n.get_datetime_value()),
            "manufacturer": lambda n : setattr(self, 'manufacturer', n.get_str_value()),
            "meid": lambda n : setattr(self, 'meid', n.get_str_value()),
            "model": lambda n : setattr(self, 'model', n.get_str_value()),
            "notes": lambda n : setattr(self, 'notes', n.get_str_value()),
            "operatingSystem": lambda n : setattr(self, 'operating_system', n.get_str_value()),
            "osVersion": lambda n : setattr(self, 'os_version', n.get_str_value()),
            "partnerReportedThreatState": lambda n : setattr(self, 'partner_reported_threat_state', n.get_enum_value(managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState)),
            "phoneNumber": lambda n : setattr(self, 'phone_number', n.get_str_value()),
            "physicalMemoryInBytes": lambda n : setattr(self, 'physical_memory_in_bytes', n.get_int_value()),
            "remoteAssistanceSessionErrorDetails": lambda n : setattr(self, 'remote_assistance_session_error_details', n.get_str_value()),
            "remoteAssistanceSessionUrl": lambda n : setattr(self, 'remote_assistance_session_url', n.get_str_value()),
            "requireUserEnrollmentApproval": lambda n : setattr(self, 'require_user_enrollment_approval', n.get_bool_value()),
            "serialNumber": lambda n : setattr(self, 'serial_number', n.get_str_value()),
            "subscriberCarrier": lambda n : setattr(self, 'subscriber_carrier', n.get_str_value()),
            "totalStorageSpaceInBytes": lambda n : setattr(self, 'total_storage_space_in_bytes', n.get_int_value()),
            "udid": lambda n : setattr(self, 'udid', n.get_str_value()),
            "users": lambda n : setattr(self, 'users', n.get_collection_of_object_values(user.User)),
            "userDisplayName": lambda n : setattr(self, 'user_display_name', n.get_str_value()),
            "userId": lambda n : setattr(self, 'user_id', n.get_str_value()),
            "userPrincipalName": lambda n : setattr(self, 'user_principal_name', n.get_str_value()),
            "wiFiMacAddress": lambda n : setattr(self, 'wi_fi_mac_address', n.get_str_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def iccid(self,) -> Optional[str]:
        """
        Gets the iccid property value. Integrated Circuit Card Identifier, it is A SIM card's unique identification number. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Returns: Optional[str]
        """
        return self._iccid
    
    @iccid.setter
    def iccid(self,value: Optional[str] = None) -> None:
        """
        Sets the iccid property value. Integrated Circuit Card Identifier, it is A SIM card's unique identification number. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Args:
            value: Value to set for the iccid property.
        """
        self._iccid = value
    
    @property
    def imei(self,) -> Optional[str]:
        """
        Gets the imei property value. IMEI. This property is read-only.
        Returns: Optional[str]
        """
        return self._imei
    
    @imei.setter
    def imei(self,value: Optional[str] = None) -> None:
        """
        Sets the imei property value. IMEI. This property is read-only.
        Args:
            value: Value to set for the imei property.
        """
        self._imei = value
    
    @property
    def is_encrypted(self,) -> Optional[bool]:
        """
        Gets the isEncrypted property value. Device encryption status. This property is read-only.
        Returns: Optional[bool]
        """
        return self._is_encrypted
    
    @is_encrypted.setter
    def is_encrypted(self,value: Optional[bool] = None) -> None:
        """
        Sets the isEncrypted property value. Device encryption status. This property is read-only.
        Args:
            value: Value to set for the is_encrypted property.
        """
        self._is_encrypted = value
    
    @property
    def is_supervised(self,) -> Optional[bool]:
        """
        Gets the isSupervised property value. Device supervised status. This property is read-only.
        Returns: Optional[bool]
        """
        return self._is_supervised
    
    @is_supervised.setter
    def is_supervised(self,value: Optional[bool] = None) -> None:
        """
        Sets the isSupervised property value. Device supervised status. This property is read-only.
        Args:
            value: Value to set for the is_supervised property.
        """
        self._is_supervised = value
    
    @property
    def jail_broken(self,) -> Optional[str]:
        """
        Gets the jailBroken property value. whether the device is jail broken or rooted. This property is read-only.
        Returns: Optional[str]
        """
        return self._jail_broken
    
    @jail_broken.setter
    def jail_broken(self,value: Optional[str] = None) -> None:
        """
        Sets the jailBroken property value. whether the device is jail broken or rooted. This property is read-only.
        Args:
            value: Value to set for the jail_broken property.
        """
        self._jail_broken = value
    
    @property
    def last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the lastSyncDateTime property value. The date and time that the device last completed a successful sync with Intune. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._last_sync_date_time
    
    @last_sync_date_time.setter
    def last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the lastSyncDateTime property value. The date and time that the device last completed a successful sync with Intune. This property is read-only.
        Args:
            value: Value to set for the last_sync_date_time property.
        """
        self._last_sync_date_time = value
    
    @property
    def managed_device_name(self,) -> Optional[str]:
        """
        Gets the managedDeviceName property value. Automatically generated name to identify a device. Can be overwritten to a user friendly name.
        Returns: Optional[str]
        """
        return self._managed_device_name
    
    @managed_device_name.setter
    def managed_device_name(self,value: Optional[str] = None) -> None:
        """
        Sets the managedDeviceName property value. Automatically generated name to identify a device. Can be overwritten to a user friendly name.
        Args:
            value: Value to set for the managed_device_name property.
        """
        self._managed_device_name = value
    
    @property
    def managed_device_owner_type(self,) -> Optional[managed_device_owner_type.ManagedDeviceOwnerType]:
        """
        Gets the managedDeviceOwnerType property value. Owner type of device.
        Returns: Optional[managed_device_owner_type.ManagedDeviceOwnerType]
        """
        return self._managed_device_owner_type
    
    @managed_device_owner_type.setter
    def managed_device_owner_type(self,value: Optional[managed_device_owner_type.ManagedDeviceOwnerType] = None) -> None:
        """
        Sets the managedDeviceOwnerType property value. Owner type of device.
        Args:
            value: Value to set for the managed_device_owner_type property.
        """
        self._managed_device_owner_type = value
    
    @property
    def management_agent(self,) -> Optional[management_agent_type.ManagementAgentType]:
        """
        Gets the managementAgent property value. The managementAgent property
        Returns: Optional[management_agent_type.ManagementAgentType]
        """
        return self._management_agent
    
    @management_agent.setter
    def management_agent(self,value: Optional[management_agent_type.ManagementAgentType] = None) -> None:
        """
        Sets the managementAgent property value. The managementAgent property
        Args:
            value: Value to set for the management_agent property.
        """
        self._management_agent = value
    
    @property
    def management_certificate_expiration_date(self,) -> Optional[datetime]:
        """
        Gets the managementCertificateExpirationDate property value. Reports device management certificate expiration date. This property is read-only.
        Returns: Optional[datetime]
        """
        return self._management_certificate_expiration_date
    
    @management_certificate_expiration_date.setter
    def management_certificate_expiration_date(self,value: Optional[datetime] = None) -> None:
        """
        Sets the managementCertificateExpirationDate property value. Reports device management certificate expiration date. This property is read-only.
        Args:
            value: Value to set for the management_certificate_expiration_date property.
        """
        self._management_certificate_expiration_date = value
    
    @property
    def manufacturer(self,) -> Optional[str]:
        """
        Gets the manufacturer property value. Manufacturer of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._manufacturer
    
    @manufacturer.setter
    def manufacturer(self,value: Optional[str] = None) -> None:
        """
        Sets the manufacturer property value. Manufacturer of the device. This property is read-only.
        Args:
            value: Value to set for the manufacturer property.
        """
        self._manufacturer = value
    
    @property
    def meid(self,) -> Optional[str]:
        """
        Gets the meid property value. MEID. This property is read-only.
        Returns: Optional[str]
        """
        return self._meid
    
    @meid.setter
    def meid(self,value: Optional[str] = None) -> None:
        """
        Sets the meid property value. MEID. This property is read-only.
        Args:
            value: Value to set for the meid property.
        """
        self._meid = value
    
    @property
    def model(self,) -> Optional[str]:
        """
        Gets the model property value. Model of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._model
    
    @model.setter
    def model(self,value: Optional[str] = None) -> None:
        """
        Sets the model property value. Model of the device. This property is read-only.
        Args:
            value: Value to set for the model property.
        """
        self._model = value
    
    @property
    def notes(self,) -> Optional[str]:
        """
        Gets the notes property value. Notes on the device created by IT Admin. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select.  $Search is not supported.
        Returns: Optional[str]
        """
        return self._notes
    
    @notes.setter
    def notes(self,value: Optional[str] = None) -> None:
        """
        Sets the notes property value. Notes on the device created by IT Admin. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select.  $Search is not supported.
        Args:
            value: Value to set for the notes property.
        """
        self._notes = value
    
    @property
    def operating_system(self,) -> Optional[str]:
        """
        Gets the operatingSystem property value. Operating system of the device. Windows, iOS, etc. This property is read-only.
        Returns: Optional[str]
        """
        return self._operating_system
    
    @operating_system.setter
    def operating_system(self,value: Optional[str] = None) -> None:
        """
        Sets the operatingSystem property value. Operating system of the device. Windows, iOS, etc. This property is read-only.
        Args:
            value: Value to set for the operating_system property.
        """
        self._operating_system = value
    
    @property
    def os_version(self,) -> Optional[str]:
        """
        Gets the osVersion property value. Operating system version of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._os_version
    
    @os_version.setter
    def os_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osVersion property value. Operating system version of the device. This property is read-only.
        Args:
            value: Value to set for the os_version property.
        """
        self._os_version = value
    
    @property
    def partner_reported_threat_state(self,) -> Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState]:
        """
        Gets the partnerReportedThreatState property value. Available health states for the Device Health API
        Returns: Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState]
        """
        return self._partner_reported_threat_state
    
    @partner_reported_threat_state.setter
    def partner_reported_threat_state(self,value: Optional[managed_device_partner_reported_health_state.ManagedDevicePartnerReportedHealthState] = None) -> None:
        """
        Sets the partnerReportedThreatState property value. Available health states for the Device Health API
        Args:
            value: Value to set for the partner_reported_threat_state property.
        """
        self._partner_reported_threat_state = value
    
    @property
    def phone_number(self,) -> Optional[str]:
        """
        Gets the phoneNumber property value. Phone number of the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self,value: Optional[str] = None) -> None:
        """
        Sets the phoneNumber property value. Phone number of the device. This property is read-only.
        Args:
            value: Value to set for the phone_number property.
        """
        self._phone_number = value
    
    @property
    def physical_memory_in_bytes(self,) -> Optional[int]:
        """
        Gets the physicalMemoryInBytes property value. Total Memory in Bytes. Return default value 0 in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. Default value is 0. Read-only. This property is read-only.
        Returns: Optional[int]
        """
        return self._physical_memory_in_bytes
    
    @physical_memory_in_bytes.setter
    def physical_memory_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the physicalMemoryInBytes property value. Total Memory in Bytes. Return default value 0 in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. Default value is 0. Read-only. This property is read-only.
        Args:
            value: Value to set for the physical_memory_in_bytes property.
        """
        self._physical_memory_in_bytes = value
    
    @property
    def remote_assistance_session_error_details(self,) -> Optional[str]:
        """
        Gets the remoteAssistanceSessionErrorDetails property value. An error string that identifies issues when creating Remote Assistance session objects. This property is read-only.
        Returns: Optional[str]
        """
        return self._remote_assistance_session_error_details
    
    @remote_assistance_session_error_details.setter
    def remote_assistance_session_error_details(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteAssistanceSessionErrorDetails property value. An error string that identifies issues when creating Remote Assistance session objects. This property is read-only.
        Args:
            value: Value to set for the remote_assistance_session_error_details property.
        """
        self._remote_assistance_session_error_details = value
    
    @property
    def remote_assistance_session_url(self,) -> Optional[str]:
        """
        Gets the remoteAssistanceSessionUrl property value. Url that allows a Remote Assistance session to be established with the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._remote_assistance_session_url
    
    @remote_assistance_session_url.setter
    def remote_assistance_session_url(self,value: Optional[str] = None) -> None:
        """
        Sets the remoteAssistanceSessionUrl property value. Url that allows a Remote Assistance session to be established with the device. This property is read-only.
        Args:
            value: Value to set for the remote_assistance_session_url property.
        """
        self._remote_assistance_session_url = value
    
    @property
    def require_user_enrollment_approval(self,) -> Optional[bool]:
        """
        Gets the requireUserEnrollmentApproval property value. Reports if the managed iOS device is user approval enrollment. This property is read-only.
        Returns: Optional[bool]
        """
        return self._require_user_enrollment_approval
    
    @require_user_enrollment_approval.setter
    def require_user_enrollment_approval(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireUserEnrollmentApproval property value. Reports if the managed iOS device is user approval enrollment. This property is read-only.
        Args:
            value: Value to set for the require_user_enrollment_approval property.
        """
        self._require_user_enrollment_approval = value
    
    @property
    def serial_number(self,) -> Optional[str]:
        """
        Gets the serialNumber property value. SerialNumber. This property is read-only.
        Returns: Optional[str]
        """
        return self._serial_number
    
    @serial_number.setter
    def serial_number(self,value: Optional[str] = None) -> None:
        """
        Sets the serialNumber property value. SerialNumber. This property is read-only.
        Args:
            value: Value to set for the serial_number property.
        """
        self._serial_number = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_enum_value("complianceState", self.compliance_state)
        writer.write_object_value("deviceCategory", self.device_category)
        writer.write_collection_of_object_values("deviceCompliancePolicyStates", self.device_compliance_policy_states)
        writer.write_collection_of_object_values("deviceConfigurationStates", self.device_configuration_states)
        writer.write_enum_value("deviceEnrollmentType", self.device_enrollment_type)
        writer.write_enum_value("deviceRegistrationState", self.device_registration_state)
        writer.write_enum_value("exchangeAccessState", self.exchange_access_state)
        writer.write_enum_value("exchangeAccessStateReason", self.exchange_access_state_reason)
        writer.write_str_value("managedDeviceName", self.managed_device_name)
        writer.write_enum_value("managedDeviceOwnerType", self.managed_device_owner_type)
        writer.write_enum_value("managementAgent", self.management_agent)
        writer.write_str_value("notes", self.notes)
        writer.write_enum_value("partnerReportedThreatState", self.partner_reported_threat_state)
        writer.write_collection_of_object_values("users", self.users)
    
    @property
    def subscriber_carrier(self,) -> Optional[str]:
        """
        Gets the subscriberCarrier property value. Subscriber Carrier. This property is read-only.
        Returns: Optional[str]
        """
        return self._subscriber_carrier
    
    @subscriber_carrier.setter
    def subscriber_carrier(self,value: Optional[str] = None) -> None:
        """
        Sets the subscriberCarrier property value. Subscriber Carrier. This property is read-only.
        Args:
            value: Value to set for the subscriber_carrier property.
        """
        self._subscriber_carrier = value
    
    @property
    def total_storage_space_in_bytes(self,) -> Optional[int]:
        """
        Gets the totalStorageSpaceInBytes property value. Total Storage in Bytes. This property is read-only.
        Returns: Optional[int]
        """
        return self._total_storage_space_in_bytes
    
    @total_storage_space_in_bytes.setter
    def total_storage_space_in_bytes(self,value: Optional[int] = None) -> None:
        """
        Sets the totalStorageSpaceInBytes property value. Total Storage in Bytes. This property is read-only.
        Args:
            value: Value to set for the total_storage_space_in_bytes property.
        """
        self._total_storage_space_in_bytes = value
    
    @property
    def udid(self,) -> Optional[str]:
        """
        Gets the udid property value. Unique Device Identifier for iOS and macOS devices. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Returns: Optional[str]
        """
        return self._udid
    
    @udid.setter
    def udid(self,value: Optional[str] = None) -> None:
        """
        Sets the udid property value. Unique Device Identifier for iOS and macOS devices. Return default value null in LIST managedDevices. Real value only returned in singel device GET call with device id and included in select parameter. Supports: $select. $Search is not supported. Read-only. This property is read-only.
        Args:
            value: Value to set for the udid property.
        """
        self._udid = value
    
    @property
    def user_display_name(self,) -> Optional[str]:
        """
        Gets the userDisplayName property value. User display name. This property is read-only.
        Returns: Optional[str]
        """
        return self._user_display_name
    
    @user_display_name.setter
    def user_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userDisplayName property value. User display name. This property is read-only.
        Args:
            value: Value to set for the user_display_name property.
        """
        self._user_display_name = value
    
    @property
    def user_id(self,) -> Optional[str]:
        """
        Gets the userId property value. Unique Identifier for the user associated with the device. This property is read-only.
        Returns: Optional[str]
        """
        return self._user_id
    
    @user_id.setter
    def user_id(self,value: Optional[str] = None) -> None:
        """
        Sets the userId property value. Unique Identifier for the user associated with the device. This property is read-only.
        Args:
            value: Value to set for the user_id property.
        """
        self._user_id = value
    
    @property
    def user_principal_name(self,) -> Optional[str]:
        """
        Gets the userPrincipalName property value. Device user principal name. This property is read-only.
        Returns: Optional[str]
        """
        return self._user_principal_name
    
    @user_principal_name.setter
    def user_principal_name(self,value: Optional[str] = None) -> None:
        """
        Sets the userPrincipalName property value. Device user principal name. This property is read-only.
        Args:
            value: Value to set for the user_principal_name property.
        """
        self._user_principal_name = value
    
    @property
    def users(self,) -> Optional[List[user.User]]:
        """
        Gets the users property value. The primary users associated with the managed device.
        Returns: Optional[List[user.User]]
        """
        return self._users
    
    @users.setter
    def users(self,value: Optional[List[user.User]] = None) -> None:
        """
        Sets the users property value. The primary users associated with the managed device.
        Args:
            value: Value to set for the users property.
        """
        self._users = value
    
    @property
    def wi_fi_mac_address(self,) -> Optional[str]:
        """
        Gets the wiFiMacAddress property value. Wi-Fi MAC. This property is read-only.
        Returns: Optional[str]
        """
        return self._wi_fi_mac_address
    
    @wi_fi_mac_address.setter
    def wi_fi_mac_address(self,value: Optional[str] = None) -> None:
        """
        Sets the wiFiMacAddress property value. Wi-Fi MAC. This property is read-only.
        Args:
            value: Value to set for the wi_fi_mac_address property.
        """
        self._wi_fi_mac_address = value
    

