from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import apple_device_features_configuration_base, ios_home_screen_item, ios_home_screen_page, ios_notification_settings

from . import apple_device_features_configuration_base

class IosDeviceFeaturesConfiguration(apple_device_features_configuration_base.AppleDeviceFeaturesConfigurationBase):
    def __init__(self,) -> None:
        """
        Instantiates a new IosDeviceFeaturesConfiguration and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.iosDeviceFeaturesConfiguration"
        # Asset tag information for the device, displayed on the login window and lock screen.
        self._asset_tag_template: Optional[str] = None
        # A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
        self._home_screen_dock_icons: Optional[List[ios_home_screen_item.IosHomeScreenItem]] = None
        # A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
        self._home_screen_pages: Optional[List[ios_home_screen_page.IosHomeScreenPage]] = None
        # A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
        self._lock_screen_footnote: Optional[str] = None
        # Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
        self._notification_settings: Optional[List[ios_notification_settings.IosNotificationSettings]] = None
    
    @property
    def asset_tag_template(self,) -> Optional[str]:
        """
        Gets the assetTagTemplate property value. Asset tag information for the device, displayed on the login window and lock screen.
        Returns: Optional[str]
        """
        return self._asset_tag_template
    
    @asset_tag_template.setter
    def asset_tag_template(self,value: Optional[str] = None) -> None:
        """
        Sets the assetTagTemplate property value. Asset tag information for the device, displayed on the login window and lock screen.
        Args:
            value: Value to set for the asset_tag_template property.
        """
        self._asset_tag_template = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> IosDeviceFeaturesConfiguration:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: IosDeviceFeaturesConfiguration
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return IosDeviceFeaturesConfiguration()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import apple_device_features_configuration_base, ios_home_screen_item, ios_home_screen_page, ios_notification_settings

        fields: Dict[str, Callable[[Any], None]] = {
            "assetTagTemplate": lambda n : setattr(self, 'asset_tag_template', n.get_str_value()),
            "homeScreenDockIcons": lambda n : setattr(self, 'home_screen_dock_icons', n.get_collection_of_object_values(ios_home_screen_item.IosHomeScreenItem)),
            "homeScreenPages": lambda n : setattr(self, 'home_screen_pages', n.get_collection_of_object_values(ios_home_screen_page.IosHomeScreenPage)),
            "lockScreenFootnote": lambda n : setattr(self, 'lock_screen_footnote', n.get_str_value()),
            "notificationSettings": lambda n : setattr(self, 'notification_settings', n.get_collection_of_object_values(ios_notification_settings.IosNotificationSettings)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def home_screen_dock_icons(self,) -> Optional[List[ios_home_screen_item.IosHomeScreenItem]]:
        """
        Gets the homeScreenDockIcons property value. A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_home_screen_item.IosHomeScreenItem]]
        """
        return self._home_screen_dock_icons
    
    @home_screen_dock_icons.setter
    def home_screen_dock_icons(self,value: Optional[List[ios_home_screen_item.IosHomeScreenItem]] = None) -> None:
        """
        Sets the homeScreenDockIcons property value. A list of app and folders to appear on the Home Screen Dock. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the home_screen_dock_icons property.
        """
        self._home_screen_dock_icons = value
    
    @property
    def home_screen_pages(self,) -> Optional[List[ios_home_screen_page.IosHomeScreenPage]]:
        """
        Gets the homeScreenPages property value. A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_home_screen_page.IosHomeScreenPage]]
        """
        return self._home_screen_pages
    
    @home_screen_pages.setter
    def home_screen_pages(self,value: Optional[List[ios_home_screen_page.IosHomeScreenPage]] = None) -> None:
        """
        Sets the homeScreenPages property value. A list of pages on the Home Screen. This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the home_screen_pages property.
        """
        self._home_screen_pages = value
    
    @property
    def lock_screen_footnote(self,) -> Optional[str]:
        """
        Gets the lockScreenFootnote property value. A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
        Returns: Optional[str]
        """
        return self._lock_screen_footnote
    
    @lock_screen_footnote.setter
    def lock_screen_footnote(self,value: Optional[str] = None) -> None:
        """
        Sets the lockScreenFootnote property value. A footnote displayed on the login window and lock screen. Available in iOS 9.3.1 and later.
        Args:
            value: Value to set for the lock_screen_footnote property.
        """
        self._lock_screen_footnote = value
    
    @property
    def notification_settings(self,) -> Optional[List[ios_notification_settings.IosNotificationSettings]]:
        """
        Gets the notificationSettings property value. Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
        Returns: Optional[List[ios_notification_settings.IosNotificationSettings]]
        """
        return self._notification_settings
    
    @notification_settings.setter
    def notification_settings(self,value: Optional[List[ios_notification_settings.IosNotificationSettings]] = None) -> None:
        """
        Sets the notificationSettings property value. Notification settings for each bundle id. Applicable to devices in supervised mode only (iOS 9.3 and later). This collection can contain a maximum of 500 elements.
        Args:
            value: Value to set for the notification_settings property.
        """
        self._notification_settings = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_str_value("assetTagTemplate", self.asset_tag_template)
        writer.write_collection_of_object_values("homeScreenDockIcons", self.home_screen_dock_icons)
        writer.write_collection_of_object_values("homeScreenPages", self.home_screen_pages)
        writer.write_str_value("lockScreenFootnote", self.lock_screen_footnote)
        writer.write_collection_of_object_values("notificationSettings", self.notification_settings)
    

