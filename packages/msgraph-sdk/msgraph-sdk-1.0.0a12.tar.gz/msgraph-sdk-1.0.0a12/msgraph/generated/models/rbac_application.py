from __future__ import annotations
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request

from . import entity

class RbacApplication(entity.Entity):
    def __init__(self,) -> None:
        """
        Instantiates a new RbacApplication and sets the default values.
        """
        super().__init__()
        # The OdataType property
        self.odata_type: Optional[str] = None
        # The resourceNamespaces property
        self._resource_namespaces: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None
        # Instances for active role assignments.
        self._role_assignment_schedule_instances: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]] = None
        # Requests for active role assignments to principals through PIM.
        self._role_assignment_schedule_requests: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]] = None
        # Schedules for active role assignment operations.
        self._role_assignment_schedules: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]] = None
        # Resource to grant access to users or groups.
        self._role_assignments: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None
        # Resource representing the roles allowed by RBAC providers and the permissions assigned to the roles.
        self._role_definitions: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None
        # Instances for role eligibility requests.
        self._role_eligibility_schedule_instances: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]] = None
        # Requests for role eligibilities for principals through PIM.
        self._role_eligibility_schedule_requests: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]] = None
        # Schedules for role eligibility operations.
        self._role_eligibility_schedules: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]] = None
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> RbacApplication:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: RbacApplication
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return RbacApplication()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import entity, unified_rbac_resource_namespace, unified_role_assignment, unified_role_assignment_schedule, unified_role_assignment_schedule_instance, unified_role_assignment_schedule_request, unified_role_definition, unified_role_eligibility_schedule, unified_role_eligibility_schedule_instance, unified_role_eligibility_schedule_request

        fields: Dict[str, Callable[[Any], None]] = {
            "resourceNamespaces": lambda n : setattr(self, 'resource_namespaces', n.get_collection_of_object_values(unified_rbac_resource_namespace.UnifiedRbacResourceNamespace)),
            "roleAssignments": lambda n : setattr(self, 'role_assignments', n.get_collection_of_object_values(unified_role_assignment.UnifiedRoleAssignment)),
            "roleAssignmentSchedules": lambda n : setattr(self, 'role_assignment_schedules', n.get_collection_of_object_values(unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule)),
            "roleAssignmentScheduleInstances": lambda n : setattr(self, 'role_assignment_schedule_instances', n.get_collection_of_object_values(unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance)),
            "roleAssignmentScheduleRequests": lambda n : setattr(self, 'role_assignment_schedule_requests', n.get_collection_of_object_values(unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest)),
            "roleDefinitions": lambda n : setattr(self, 'role_definitions', n.get_collection_of_object_values(unified_role_definition.UnifiedRoleDefinition)),
            "roleEligibilitySchedules": lambda n : setattr(self, 'role_eligibility_schedules', n.get_collection_of_object_values(unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule)),
            "roleEligibilityScheduleInstances": lambda n : setattr(self, 'role_eligibility_schedule_instances', n.get_collection_of_object_values(unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance)),
            "roleEligibilityScheduleRequests": lambda n : setattr(self, 'role_eligibility_schedule_requests', n.get_collection_of_object_values(unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def resource_namespaces(self,) -> Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]]:
        """
        Gets the resourceNamespaces property value. The resourceNamespaces property
        Returns: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]]
        """
        return self._resource_namespaces
    
    @resource_namespaces.setter
    def resource_namespaces(self,value: Optional[List[unified_rbac_resource_namespace.UnifiedRbacResourceNamespace]] = None) -> None:
        """
        Sets the resourceNamespaces property value. The resourceNamespaces property
        Args:
            value: Value to set for the resource_namespaces property.
        """
        self._resource_namespaces = value
    
    @property
    def role_assignment_schedule_instances(self,) -> Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]]:
        """
        Gets the roleAssignmentScheduleInstances property value. Instances for active role assignments.
        Returns: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]]
        """
        return self._role_assignment_schedule_instances
    
    @role_assignment_schedule_instances.setter
    def role_assignment_schedule_instances(self,value: Optional[List[unified_role_assignment_schedule_instance.UnifiedRoleAssignmentScheduleInstance]] = None) -> None:
        """
        Sets the roleAssignmentScheduleInstances property value. Instances for active role assignments.
        Args:
            value: Value to set for the role_assignment_schedule_instances property.
        """
        self._role_assignment_schedule_instances = value
    
    @property
    def role_assignment_schedule_requests(self,) -> Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]]:
        """
        Gets the roleAssignmentScheduleRequests property value. Requests for active role assignments to principals through PIM.
        Returns: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]]
        """
        return self._role_assignment_schedule_requests
    
    @role_assignment_schedule_requests.setter
    def role_assignment_schedule_requests(self,value: Optional[List[unified_role_assignment_schedule_request.UnifiedRoleAssignmentScheduleRequest]] = None) -> None:
        """
        Sets the roleAssignmentScheduleRequests property value. Requests for active role assignments to principals through PIM.
        Args:
            value: Value to set for the role_assignment_schedule_requests property.
        """
        self._role_assignment_schedule_requests = value
    
    @property
    def role_assignment_schedules(self,) -> Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]]:
        """
        Gets the roleAssignmentSchedules property value. Schedules for active role assignment operations.
        Returns: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]]
        """
        return self._role_assignment_schedules
    
    @role_assignment_schedules.setter
    def role_assignment_schedules(self,value: Optional[List[unified_role_assignment_schedule.UnifiedRoleAssignmentSchedule]] = None) -> None:
        """
        Sets the roleAssignmentSchedules property value. Schedules for active role assignment operations.
        Args:
            value: Value to set for the role_assignment_schedules property.
        """
        self._role_assignment_schedules = value
    
    @property
    def role_assignments(self,) -> Optional[List[unified_role_assignment.UnifiedRoleAssignment]]:
        """
        Gets the roleAssignments property value. Resource to grant access to users or groups.
        Returns: Optional[List[unified_role_assignment.UnifiedRoleAssignment]]
        """
        return self._role_assignments
    
    @role_assignments.setter
    def role_assignments(self,value: Optional[List[unified_role_assignment.UnifiedRoleAssignment]] = None) -> None:
        """
        Sets the roleAssignments property value. Resource to grant access to users or groups.
        Args:
            value: Value to set for the role_assignments property.
        """
        self._role_assignments = value
    
    @property
    def role_definitions(self,) -> Optional[List[unified_role_definition.UnifiedRoleDefinition]]:
        """
        Gets the roleDefinitions property value. Resource representing the roles allowed by RBAC providers and the permissions assigned to the roles.
        Returns: Optional[List[unified_role_definition.UnifiedRoleDefinition]]
        """
        return self._role_definitions
    
    @role_definitions.setter
    def role_definitions(self,value: Optional[List[unified_role_definition.UnifiedRoleDefinition]] = None) -> None:
        """
        Sets the roleDefinitions property value. Resource representing the roles allowed by RBAC providers and the permissions assigned to the roles.
        Args:
            value: Value to set for the role_definitions property.
        """
        self._role_definitions = value
    
    @property
    def role_eligibility_schedule_instances(self,) -> Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]]:
        """
        Gets the roleEligibilityScheduleInstances property value. Instances for role eligibility requests.
        Returns: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]]
        """
        return self._role_eligibility_schedule_instances
    
    @role_eligibility_schedule_instances.setter
    def role_eligibility_schedule_instances(self,value: Optional[List[unified_role_eligibility_schedule_instance.UnifiedRoleEligibilityScheduleInstance]] = None) -> None:
        """
        Sets the roleEligibilityScheduleInstances property value. Instances for role eligibility requests.
        Args:
            value: Value to set for the role_eligibility_schedule_instances property.
        """
        self._role_eligibility_schedule_instances = value
    
    @property
    def role_eligibility_schedule_requests(self,) -> Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]]:
        """
        Gets the roleEligibilityScheduleRequests property value. Requests for role eligibilities for principals through PIM.
        Returns: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]]
        """
        return self._role_eligibility_schedule_requests
    
    @role_eligibility_schedule_requests.setter
    def role_eligibility_schedule_requests(self,value: Optional[List[unified_role_eligibility_schedule_request.UnifiedRoleEligibilityScheduleRequest]] = None) -> None:
        """
        Sets the roleEligibilityScheduleRequests property value. Requests for role eligibilities for principals through PIM.
        Args:
            value: Value to set for the role_eligibility_schedule_requests property.
        """
        self._role_eligibility_schedule_requests = value
    
    @property
    def role_eligibility_schedules(self,) -> Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]]:
        """
        Gets the roleEligibilitySchedules property value. Schedules for role eligibility operations.
        Returns: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]]
        """
        return self._role_eligibility_schedules
    
    @role_eligibility_schedules.setter
    def role_eligibility_schedules(self,value: Optional[List[unified_role_eligibility_schedule.UnifiedRoleEligibilitySchedule]] = None) -> None:
        """
        Sets the roleEligibilitySchedules property value. Schedules for role eligibility operations.
        Args:
            value: Value to set for the role_eligibility_schedules property.
        """
        self._role_eligibility_schedules = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("resourceNamespaces", self.resource_namespaces)
        writer.write_collection_of_object_values("roleAssignments", self.role_assignments)
        writer.write_collection_of_object_values("roleAssignmentSchedules", self.role_assignment_schedules)
        writer.write_collection_of_object_values("roleAssignmentScheduleInstances", self.role_assignment_schedule_instances)
        writer.write_collection_of_object_values("roleAssignmentScheduleRequests", self.role_assignment_schedule_requests)
        writer.write_collection_of_object_values("roleDefinitions", self.role_definitions)
        writer.write_collection_of_object_values("roleEligibilitySchedules", self.role_eligibility_schedules)
        writer.write_collection_of_object_values("roleEligibilityScheduleInstances", self.role_eligibility_schedule_instances)
        writer.write_collection_of_object_values("roleEligibilityScheduleRequests", self.role_eligibility_schedule_requests)
    

