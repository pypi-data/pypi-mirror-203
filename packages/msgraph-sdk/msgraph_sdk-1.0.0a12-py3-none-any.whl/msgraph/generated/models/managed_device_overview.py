from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import device_exchange_access_state_summary, device_operating_system_summary, entity

from . import entity

class ManagedDeviceOverview(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new managedDeviceOverview and sets the default values.
        """
        super().__init__()
        # Distribution of Exchange Access State in Intune
        self._device_exchange_access_state_summary: Optional[device_exchange_access_state_summary.DeviceExchangeAccessStateSummary] = None
        # Device operating system summary.
        self._device_operating_system_summary: Optional[device_operating_system_summary.DeviceOperatingSystemSummary] = None
        # The number of devices enrolled in both MDM and EAS
        self._dual_enrolled_device_count: Optional[int] = None
        # Total enrolled device count. Does not include PC devices managed via Intune PC Agent
        self._enrolled_device_count: Optional[int] = None
        # The number of devices enrolled in MDM
        self._mdm_enrolled_count: Optional[int] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> ManagedDeviceOverview:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: ManagedDeviceOverview
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return ManagedDeviceOverview()
    
    @property
    def device_exchange_access_state_summary(self,) -> Optional[device_exchange_access_state_summary.DeviceExchangeAccessStateSummary]:
        """
        Gets the deviceExchangeAccessStateSummary property value. Distribution of Exchange Access State in Intune
        Returns: Optional[device_exchange_access_state_summary.DeviceExchangeAccessStateSummary]
        """
        return self._device_exchange_access_state_summary
    
    @device_exchange_access_state_summary.setter
    def device_exchange_access_state_summary(self,value: Optional[device_exchange_access_state_summary.DeviceExchangeAccessStateSummary] = None) -> None:
        """
        Sets the deviceExchangeAccessStateSummary property value. Distribution of Exchange Access State in Intune
        Args:
            value: Value to set for the device_exchange_access_state_summary property.
        """
        self._device_exchange_access_state_summary = value
    
    @property
    def device_operating_system_summary(self,) -> Optional[device_operating_system_summary.DeviceOperatingSystemSummary]:
        """
        Gets the deviceOperatingSystemSummary property value. Device operating system summary.
        Returns: Optional[device_operating_system_summary.DeviceOperatingSystemSummary]
        """
        return self._device_operating_system_summary
    
    @device_operating_system_summary.setter
    def device_operating_system_summary(self,value: Optional[device_operating_system_summary.DeviceOperatingSystemSummary] = None) -> None:
        """
        Sets the deviceOperatingSystemSummary property value. Device operating system summary.
        Args:
            value: Value to set for the device_operating_system_summary property.
        """
        self._device_operating_system_summary = value
    
    @property
    def dual_enrolled_device_count(self,) -> Optional[int]:
        """
        Gets the dualEnrolledDeviceCount property value. The number of devices enrolled in both MDM and EAS
        Returns: Optional[int]
        """
        return self._dual_enrolled_device_count
    
    @dual_enrolled_device_count.setter
    def dual_enrolled_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the dualEnrolledDeviceCount property value. The number of devices enrolled in both MDM and EAS
        Args:
            value: Value to set for the dual_enrolled_device_count property.
        """
        self._dual_enrolled_device_count = value
    
    @property
    def enrolled_device_count(self,) -> Optional[int]:
        """
        Gets the enrolledDeviceCount property value. Total enrolled device count. Does not include PC devices managed via Intune PC Agent
        Returns: Optional[int]
        """
        return self._enrolled_device_count
    
    @enrolled_device_count.setter
    def enrolled_device_count(self,value: Optional[int] = None) -> None:
        """
        Sets the enrolledDeviceCount property value. Total enrolled device count. Does not include PC devices managed via Intune PC Agent
        Args:
            value: Value to set for the enrolled_device_count property.
        """
        self._enrolled_device_count = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import device_exchange_access_state_summary, device_operating_system_summary, entity

        fields: Dict[str, Callable[[Any], None]] = {
            "deviceExchangeAccessStateSummary": lambda n : setattr(self, 'device_exchange_access_state_summary', n.get_object_value(device_exchange_access_state_summary.DeviceExchangeAccessStateSummary)),
            "deviceOperatingSystemSummary": lambda n : setattr(self, 'device_operating_system_summary', n.get_object_value(device_operating_system_summary.DeviceOperatingSystemSummary)),
            "dualEnrolledDeviceCount": lambda n : setattr(self, 'dual_enrolled_device_count', n.get_int_value()),
            "enrolledDeviceCount": lambda n : setattr(self, 'enrolled_device_count', n.get_int_value()),
            "mdmEnrolledCount": lambda n : setattr(self, 'mdm_enrolled_count', n.get_int_value()),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def mdm_enrolled_count(self,) -> Optional[int]:
        """
        Gets the mdmEnrolledCount property value. The number of devices enrolled in MDM
        Returns: Optional[int]
        """
        return self._mdm_enrolled_count
    
    @mdm_enrolled_count.setter
    def mdm_enrolled_count(self,value: Optional[int] = None) -> None:
        """
        Sets the mdmEnrolledCount property value. The number of devices enrolled in MDM
        Args:
            value: Value to set for the mdm_enrolled_count property.
        """
        self._mdm_enrolled_count = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_object_value("deviceExchangeAccessStateSummary", self.device_exchange_access_state_summary)
        writer.write_object_value("deviceOperatingSystemSummary", self.device_operating_system_summary)
        writer.write_int_value("dualEnrolledDeviceCount", self.dual_enrolled_device_count)
        writer.write_int_value("enrolledDeviceCount", self.enrolled_device_count)
        writer.write_int_value("mdmEnrolledCount", self.mdm_enrolled_count)
    

