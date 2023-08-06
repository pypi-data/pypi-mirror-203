from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import deleted_team, entity, workforce_integration

from . import entity

class Teamwork(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new Teamwork and sets the default values.
        """
        super().__init__()
        # The deleted team.
        self._deleted_teams: Optional[List[deleted_team.DeletedTeam]] = None
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The workforceIntegrations property
        self._workforce_integrations: Optional[List[workforce_integration.WorkforceIntegration]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Teamwork:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Teamwork
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Teamwork()
    
    @property
    def deleted_teams(self,) -> Optional[List[deleted_team.DeletedTeam]]:
        """
        Gets the deletedTeams property value. The deleted team.
        Returns: Optional[List[deleted_team.DeletedTeam]]
        """
        return self._deleted_teams
    
    @deleted_teams.setter
    def deleted_teams(self,value: Optional[List[deleted_team.DeletedTeam]] = None) -> None:
        """
        Sets the deletedTeams property value. The deleted team.
        Args:
            value: Value to set for the deleted_teams property.
        """
        self._deleted_teams = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import deleted_team, entity, workforce_integration

        fields: Dict[str, Callable[[Any], None]] = {
            "deletedTeams": lambda n : setattr(self, 'deleted_teams', n.get_collection_of_object_values(deleted_team.DeletedTeam)),
            "workforceIntegrations": lambda n : setattr(self, 'workforce_integrations', n.get_collection_of_object_values(workforce_integration.WorkforceIntegration)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("deletedTeams", self.deleted_teams)
        writer.write_collection_of_object_values("workforceIntegrations", self.workforce_integrations)
    
    @property
    def workforce_integrations(self,) -> Optional[List[workforce_integration.WorkforceIntegration]]:
        """
        Gets the workforceIntegrations property value. The workforceIntegrations property
        Returns: Optional[List[workforce_integration.WorkforceIntegration]]
        """
        return self._workforce_integrations
    
    @workforce_integrations.setter
    def workforce_integrations(self,value: Optional[List[workforce_integration.WorkforceIntegration]] = None) -> None:
        """
        Sets the workforceIntegrations property value. The workforceIntegrations property
        Args:
            value: Value to set for the workforce_integrations property.
        """
        self._workforce_integrations = value
    

