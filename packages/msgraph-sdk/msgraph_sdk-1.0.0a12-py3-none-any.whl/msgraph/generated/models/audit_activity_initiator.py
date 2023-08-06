from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import app_identity, user_identity

class AuditActivityInitiator(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new auditActivityInitiator and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # If the resource initiating the activity is an app, this property indicates all the app related information like appId, Name, servicePrincipalId, Name.
        self._app: Optional[app_identity.AppIdentity] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # If the resource initiating the activity is a user, this property Indicates all the user related information like userId, Name, UserPrinicpalName.
        self._user: Optional[user_identity.UserIdentity] = None
    
    @property
    def additional_data(self,) -> Dict[str, Any]:
        """
        Gets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Returns: Dict[str, Any]
        """
        return self._additional_data
    
    @additional_data.setter
    def additional_data(self,value: Dict[str, Any]) -> None:
        """
        Sets the additionalData property value. Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        Args:
            value: Value to set for the AdditionalData property.
        """
        self._additional_data = value
    
    @property
    def app(self,) -> Optional[app_identity.AppIdentity]:
        """
        Gets the app property value. If the resource initiating the activity is an app, this property indicates all the app related information like appId, Name, servicePrincipalId, Name.
        Returns: Optional[app_identity.AppIdentity]
        """
        return self._app
    
    @app.setter
    def app(self,value: Optional[app_identity.AppIdentity] = None) -> None:
        """
        Sets the app property value. If the resource initiating the activity is an app, this property indicates all the app related information like appId, Name, servicePrincipalId, Name.
        Args:
            value: Value to set for the app property.
        """
        self._app = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AuditActivityInitiator:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AuditActivityInitiator
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AuditActivityInitiator()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import app_identity, user_identity

        fields: Dict[str, Callable[[Any], None]] = {
            "app": lambda n : setattr(self, 'app', n.get_object_value(app_identity.AppIdentity)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "user": lambda n : setattr(self, 'user', n.get_object_value(user_identity.UserIdentity)),
        }
        return fields
    
    @property
    def odata_type(self,) -> Optional[str]:
        """
        Gets the @odata.type property value. The OdataType property
        Returns: Optional[str]
        """
        return self._odata_type
    
    @odata_type.setter
    def odata_type(self,value: Optional[str] = None) -> None:
        """
        Sets the @odata.type property value. The OdataType property
        Args:
            value: Value to set for the odata_type property.
        """
        self._odata_type = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_object_value("app", self.app)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_object_value("user", self.user)
        writer.write_additional_data_value(self.additional_data)
    
    @property
    def user(self,) -> Optional[user_identity.UserIdentity]:
        """
        Gets the user property value. If the resource initiating the activity is a user, this property Indicates all the user related information like userId, Name, UserPrinicpalName.
        Returns: Optional[user_identity.UserIdentity]
        """
        return self._user
    
    @user.setter
    def user(self,value: Optional[user_identity.UserIdentity] = None) -> None:
        """
        Sets the user property value. If the resource initiating the activity is a user, this property Indicates all the user related information like userId, Name, UserPrinicpalName.
        Args:
            value: Value to set for the user property.
        """
        self._user = value
    

