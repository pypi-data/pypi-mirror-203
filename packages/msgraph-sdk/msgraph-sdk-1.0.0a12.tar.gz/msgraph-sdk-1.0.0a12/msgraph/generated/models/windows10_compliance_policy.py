from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_compliance_policy, required_password_type

from . import device_compliance_policy

class Windows10CompliancePolicy(device_compliance_policy.DeviceCompliancePolicy):
    def __init__(self,) -> None:
        """
        Instantiates a new Windows10CompliancePolicy and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.windows10CompliancePolicy"
        # Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        self._bit_locker_enabled: Optional[bool] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation.
        self._code_integrity_enabled: Optional[bool] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        self._early_launch_anti_malware_driver_enabled: Optional[bool] = None
        # Maximum Windows Phone version.
        self._mobile_os_maximum_version: Optional[str] = None
        # Minimum Windows Phone version.
        self._mobile_os_minimum_version: Optional[str] = None
        # Maximum Windows 10 version.
        self._os_maximum_version: Optional[str] = None
        # Minimum Windows 10 version.
        self._os_minimum_version: Optional[str] = None
        # Indicates whether or not to block simple password.
        self._password_block_simple: Optional[bool] = None
        # The password expiration in days.
        self._password_expiration_days: Optional[int] = None
        # The number of character sets required in the password.
        self._password_minimum_character_set_count: Optional[int] = None
        # The minimum password length.
        self._password_minimum_length: Optional[int] = None
        # Minutes of inactivity before a password is required.
        self._password_minutes_of_inactivity_before_lock: Optional[int] = None
        # The number of previous passwords to prevent re-use of.
        self._password_previous_password_block_count: Optional[int] = None
        # Require a password to unlock Windows device.
        self._password_required: Optional[bool] = None
        # Require a password to unlock an idle device.
        self._password_required_to_unlock_from_idle: Optional[bool] = None
        # Possible values of required passwords.
        self._password_required_type: Optional[required_password_type.RequiredPasswordType] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation.
        self._require_healthy_device_report: Optional[bool] = None
        # Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        self._secure_boot_enabled: Optional[bool] = None
        # Require encryption on windows devices.
        self._storage_require_encryption: Optional[bool] = None
    
    @property
    def bit_locker_enabled(self,) -> Optional[bool]:
        """
        Gets the bitLockerEnabled property value. Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        Returns: Optional[bool]
        """
        return self._bit_locker_enabled
    
    @bit_locker_enabled.setter
    def bit_locker_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the bitLockerEnabled property value. Require devices to be reported healthy by Windows Device Health Attestation - bit locker is enabled
        Args:
            value: Value to set for the bit_locker_enabled property.
        """
        self._bit_locker_enabled = value
    
    @property
    def code_integrity_enabled(self,) -> Optional[bool]:
        """
        Gets the codeIntegrityEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Returns: Optional[bool]
        """
        return self._code_integrity_enabled
    
    @code_integrity_enabled.setter
    def code_integrity_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the codeIntegrityEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Args:
            value: Value to set for the code_integrity_enabled property.
        """
        self._code_integrity_enabled = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Windows10CompliancePolicy:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Windows10CompliancePolicy
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Windows10CompliancePolicy()
    
    @property
    def early_launch_anti_malware_driver_enabled(self,) -> Optional[bool]:
        """
        Gets the earlyLaunchAntiMalwareDriverEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        Returns: Optional[bool]
        """
        return self._early_launch_anti_malware_driver_enabled
    
    @early_launch_anti_malware_driver_enabled.setter
    def early_launch_anti_malware_driver_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the earlyLaunchAntiMalwareDriverEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - early launch antimalware driver is enabled.
        Args:
            value: Value to set for the early_launch_anti_malware_driver_enabled property.
        """
        self._early_launch_anti_malware_driver_enabled = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_compliance_policy, required_password_type

        fields: Dict[str, Callable[[Any], None]] = {
            "bitLockerEnabled": lambda n : setattr(self, 'bit_locker_enabled', n.get_bool_value()),
            "codeIntegrityEnabled": lambda n : setattr(self, 'code_integrity_enabled', n.get_bool_value()),
            "earlyLaunchAntiMalwareDriverEnabled": lambda n : setattr(self, 'early_launch_anti_malware_driver_enabled', n.get_bool_value()),
            "mobileOsMaximumVersion": lambda n : setattr(self, 'mobile_os_maximum_version', n.get_str_value()),
            "mobileOsMinimumVersion": lambda n : setattr(self, 'mobile_os_minimum_version', n.get_str_value()),
            "osMaximumVersion": lambda n : setattr(self, 'os_maximum_version', n.get_str_value()),
            "osMinimumVersion": lambda n : setattr(self, 'os_minimum_version', n.get_str_value()),
            "passwordBlockSimple": lambda n : setattr(self, 'password_block_simple', n.get_bool_value()),
            "passwordExpirationDays": lambda n : setattr(self, 'password_expiration_days', n.get_int_value()),
            "passwordMinimumCharacterSetCount": lambda n : setattr(self, 'password_minimum_character_set_count', n.get_int_value()),
            "passwordMinimumLength": lambda n : setattr(self, 'password_minimum_length', n.get_int_value()),
            "passwordMinutesOfInactivityBeforeLock": lambda n : setattr(self, 'password_minutes_of_inactivity_before_lock', n.get_int_value()),
            "passwordPreviousPasswordBlockCount": lambda n : setattr(self, 'password_previous_password_block_count', n.get_int_value()),
            "passwordRequired": lambda n : setattr(self, 'password_required', n.get_bool_value()),
            "passwordRequiredToUnlockFromIdle": lambda n : setattr(self, 'password_required_to_unlock_from_idle', n.get_bool_value()),
            "passwordRequiredType": lambda n : setattr(self, 'password_required_type', n.get_enum_value(required_password_type.RequiredPasswordType)),
            "requireHealthyDeviceReport": lambda n : setattr(self, 'require_healthy_device_report', n.get_bool_value()),
            "secureBootEnabled": lambda n : setattr(self, 'secure_boot_enabled', n.get_bool_value()),
            "storageRequireEncryption": lambda n : setattr(self, 'storage_require_encryption', n.get_bool_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mobile_os_maximum_version(self,) -> Optional[str]:
        """
        Gets the mobileOsMaximumVersion property value. Maximum Windows Phone version.
        Returns: Optional[str]
        """
        return self._mobile_os_maximum_version
    
    @mobile_os_maximum_version.setter
    def mobile_os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the mobileOsMaximumVersion property value. Maximum Windows Phone version.
        Args:
            value: Value to set for the mobile_os_maximum_version property.
        """
        self._mobile_os_maximum_version = value
    
    @property
    def mobile_os_minimum_version(self,) -> Optional[str]:
        """
        Gets the mobileOsMinimumVersion property value. Minimum Windows Phone version.
        Returns: Optional[str]
        """
        return self._mobile_os_minimum_version
    
    @mobile_os_minimum_version.setter
    def mobile_os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the mobileOsMinimumVersion property value. Minimum Windows Phone version.
        Args:
            value: Value to set for the mobile_os_minimum_version property.
        """
        self._mobile_os_minimum_version = value
    
    @property
    def os_maximum_version(self,) -> Optional[str]:
        """
        Gets the osMaximumVersion property value. Maximum Windows 10 version.
        Returns: Optional[str]
        """
        return self._os_maximum_version
    
    @os_maximum_version.setter
    def os_maximum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMaximumVersion property value. Maximum Windows 10 version.
        Args:
            value: Value to set for the os_maximum_version property.
        """
        self._os_maximum_version = value
    
    @property
    def os_minimum_version(self,) -> Optional[str]:
        """
        Gets the osMinimumVersion property value. Minimum Windows 10 version.
        Returns: Optional[str]
        """
        return self._os_minimum_version
    
    @os_minimum_version.setter
    def os_minimum_version(self,value: Optional[str] = None) -> None:
        """
        Sets the osMinimumVersion property value. Minimum Windows 10 version.
        Args:
            value: Value to set for the os_minimum_version property.
        """
        self._os_minimum_version = value
    
    @property
    def password_block_simple(self,) -> Optional[bool]:
        """
        Gets the passwordBlockSimple property value. Indicates whether or not to block simple password.
        Returns: Optional[bool]
        """
        return self._password_block_simple
    
    @password_block_simple.setter
    def password_block_simple(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordBlockSimple property value. Indicates whether or not to block simple password.
        Args:
            value: Value to set for the password_block_simple property.
        """
        self._password_block_simple = value
    
    @property
    def password_expiration_days(self,) -> Optional[int]:
        """
        Gets the passwordExpirationDays property value. The password expiration in days.
        Returns: Optional[int]
        """
        return self._password_expiration_days
    
    @password_expiration_days.setter
    def password_expiration_days(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordExpirationDays property value. The password expiration in days.
        Args:
            value: Value to set for the password_expiration_days property.
        """
        self._password_expiration_days = value
    
    @property
    def password_minimum_character_set_count(self,) -> Optional[int]:
        """
        Gets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Returns: Optional[int]
        """
        return self._password_minimum_character_set_count
    
    @password_minimum_character_set_count.setter
    def password_minimum_character_set_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumCharacterSetCount property value. The number of character sets required in the password.
        Args:
            value: Value to set for the password_minimum_character_set_count property.
        """
        self._password_minimum_character_set_count = value
    
    @property
    def password_minimum_length(self,) -> Optional[int]:
        """
        Gets the passwordMinimumLength property value. The minimum password length.
        Returns: Optional[int]
        """
        return self._password_minimum_length
    
    @password_minimum_length.setter
    def password_minimum_length(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinimumLength property value. The minimum password length.
        Args:
            value: Value to set for the password_minimum_length property.
        """
        self._password_minimum_length = value
    
    @property
    def password_minutes_of_inactivity_before_lock(self,) -> Optional[int]:
        """
        Gets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a password is required.
        Returns: Optional[int]
        """
        return self._password_minutes_of_inactivity_before_lock
    
    @password_minutes_of_inactivity_before_lock.setter
    def password_minutes_of_inactivity_before_lock(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordMinutesOfInactivityBeforeLock property value. Minutes of inactivity before a password is required.
        Args:
            value: Value to set for the password_minutes_of_inactivity_before_lock property.
        """
        self._password_minutes_of_inactivity_before_lock = value
    
    @property
    def password_previous_password_block_count(self,) -> Optional[int]:
        """
        Gets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent re-use of.
        Returns: Optional[int]
        """
        return self._password_previous_password_block_count
    
    @password_previous_password_block_count.setter
    def password_previous_password_block_count(self,value: Optional[int] = None) -> None:
        """
        Sets the passwordPreviousPasswordBlockCount property value. The number of previous passwords to prevent re-use of.
        Args:
            value: Value to set for the password_previous_password_block_count property.
        """
        self._password_previous_password_block_count = value
    
    @property
    def password_required(self,) -> Optional[bool]:
        """
        Gets the passwordRequired property value. Require a password to unlock Windows device.
        Returns: Optional[bool]
        """
        return self._password_required
    
    @password_required.setter
    def password_required(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequired property value. Require a password to unlock Windows device.
        Args:
            value: Value to set for the password_required property.
        """
        self._password_required = value
    
    @property
    def password_required_to_unlock_from_idle(self,) -> Optional[bool]:
        """
        Gets the passwordRequiredToUnlockFromIdle property value. Require a password to unlock an idle device.
        Returns: Optional[bool]
        """
        return self._password_required_to_unlock_from_idle
    
    @password_required_to_unlock_from_idle.setter
    def password_required_to_unlock_from_idle(self,value: Optional[bool] = None) -> None:
        """
        Sets the passwordRequiredToUnlockFromIdle property value. Require a password to unlock an idle device.
        Args:
            value: Value to set for the password_required_to_unlock_from_idle property.
        """
        self._password_required_to_unlock_from_idle = value
    
    @property
    def password_required_type(self,) -> Optional[required_password_type.RequiredPasswordType]:
        """
        Gets the passwordRequiredType property value. Possible values of required passwords.
        Returns: Optional[required_password_type.RequiredPasswordType]
        """
        return self._password_required_type
    
    @password_required_type.setter
    def password_required_type(self,value: Optional[required_password_type.RequiredPasswordType] = None) -> None:
        """
        Sets the passwordRequiredType property value. Possible values of required passwords.
        Args:
            value: Value to set for the password_required_type property.
        """
        self._password_required_type = value
    
    @property
    def require_healthy_device_report(self,) -> Optional[bool]:
        """
        Gets the requireHealthyDeviceReport property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Returns: Optional[bool]
        """
        return self._require_healthy_device_report
    
    @require_healthy_device_report.setter
    def require_healthy_device_report(self,value: Optional[bool] = None) -> None:
        """
        Sets the requireHealthyDeviceReport property value. Require devices to be reported as healthy by Windows Device Health Attestation.
        Args:
            value: Value to set for the require_healthy_device_report property.
        """
        self._require_healthy_device_report = value
    
    @property
    def secure_boot_enabled(self,) -> Optional[bool]:
        """
        Gets the secureBootEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        Returns: Optional[bool]
        """
        return self._secure_boot_enabled
    
    @secure_boot_enabled.setter
    def secure_boot_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the secureBootEnabled property value. Require devices to be reported as healthy by Windows Device Health Attestation - secure boot is enabled.
        Args:
            value: Value to set for the secure_boot_enabled property.
        """
        self._secure_boot_enabled = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_bool_value("bitLockerEnabled", self.bit_locker_enabled)
        writer.write_bool_value("codeIntegrityEnabled", self.code_integrity_enabled)
        writer.write_bool_value("earlyLaunchAntiMalwareDriverEnabled", self.early_launch_anti_malware_driver_enabled)
        writer.write_str_value("mobileOsMaximumVersion", self.mobile_os_maximum_version)
        writer.write_str_value("mobileOsMinimumVersion", self.mobile_os_minimum_version)
        writer.write_str_value("osMaximumVersion", self.os_maximum_version)
        writer.write_str_value("osMinimumVersion", self.os_minimum_version)
        writer.write_bool_value("passwordBlockSimple", self.password_block_simple)
        writer.write_int_value("passwordExpirationDays", self.password_expiration_days)
        writer.write_int_value("passwordMinimumCharacterSetCount", self.password_minimum_character_set_count)
        writer.write_int_value("passwordMinimumLength", self.password_minimum_length)
        writer.write_int_value("passwordMinutesOfInactivityBeforeLock", self.password_minutes_of_inactivity_before_lock)
        writer.write_int_value("passwordPreviousPasswordBlockCount", self.password_previous_password_block_count)
        writer.write_bool_value("passwordRequired", self.password_required)
        writer.write_bool_value("passwordRequiredToUnlockFromIdle", self.password_required_to_unlock_from_idle)
        writer.write_enum_value("passwordRequiredType", self.password_required_type)
        writer.write_bool_value("requireHealthyDeviceReport", self.require_healthy_device_report)
        writer.write_bool_value("secureBootEnabled", self.secure_boot_enabled)
        writer.write_bool_value("storageRequireEncryption", self.storage_require_encryption)
    
    @property
    def storage_require_encryption(self,) -> Optional[bool]:
        """
        Gets the storageRequireEncryption property value. Require encryption on windows devices.
        Returns: Optional[bool]
        """
        return self._storage_require_encryption
    
    @storage_require_encryption.setter
    def storage_require_encryption(self,value: Optional[bool] = None) -> None:
        """
        Sets the storageRequireEncryption property value. Require encryption on windows devices.
        Args:
            value: Value to set for the storage_require_encryption property.
        """
        self._storage_require_encryption = value
    

