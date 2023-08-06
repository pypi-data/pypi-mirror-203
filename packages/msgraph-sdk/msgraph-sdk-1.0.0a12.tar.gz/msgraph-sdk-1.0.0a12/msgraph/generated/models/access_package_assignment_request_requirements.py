from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import access_package_question, entitlement_management_schedule

class AccessPackageAssignmentRequestRequirements(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new accessPackageAssignmentRequestRequirements and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # Indicates whether the requestor is allowed to set a custom schedule.
        self._allow_custom_assignment_schedule: Optional[bool] = None
        # Indicates whether a request to add must be approved by an approver.
        self._is_approval_required_for_add: Optional[bool] = None
        # Indicates whether a request to update must be approved by an approver.
        self._is_approval_required_for_update: Optional[bool] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
        # The description of the policy that the user is trying to request access using.
        self._policy_description: Optional[str] = None
        # The display name of the policy that the user is trying to request access using.
        self._policy_display_name: Optional[str] = None
        # The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
        self._policy_id: Optional[str] = None
        # The questions property
        self._questions: Optional[List[access_package_question.AccessPackageQuestion]] = None
        # Schedule restrictions enforced, if any.
        self._schedule: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None
    
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
    def allow_custom_assignment_schedule(self,) -> Optional[bool]:
        """
        Gets the allowCustomAssignmentSchedule property value. Indicates whether the requestor is allowed to set a custom schedule.
        Returns: Optional[bool]
        """
        return self._allow_custom_assignment_schedule
    
    @allow_custom_assignment_schedule.setter
    def allow_custom_assignment_schedule(self,value: Optional[bool] = None) -> None:
        """
        Sets the allowCustomAssignmentSchedule property value. Indicates whether the requestor is allowed to set a custom schedule.
        Args:
            value: Value to set for the allow_custom_assignment_schedule property.
        """
        self._allow_custom_assignment_schedule = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> AccessPackageAssignmentRequestRequirements:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: AccessPackageAssignmentRequestRequirements
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return AccessPackageAssignmentRequestRequirements()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import access_package_question, entitlement_management_schedule

        fields: Dict[str, Callable[[Any], None]] = {
            "allowCustomAssignmentSchedule": lambda n : setattr(self, 'allow_custom_assignment_schedule', n.get_bool_value()),
            "isApprovalRequiredForAdd": lambda n : setattr(self, 'is_approval_required_for_add', n.get_bool_value()),
            "isApprovalRequiredForUpdate": lambda n : setattr(self, 'is_approval_required_for_update', n.get_bool_value()),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
            "policyDescription": lambda n : setattr(self, 'policy_description', n.get_str_value()),
            "policyDisplayName": lambda n : setattr(self, 'policy_display_name', n.get_str_value()),
            "policyId": lambda n : setattr(self, 'policy_id', n.get_str_value()),
            "questions": lambda n : setattr(self, 'questions', n.get_collection_of_object_values(access_package_question.AccessPackageQuestion)),
            "schedule": lambda n : setattr(self, 'schedule', n.get_object_value(entitlement_management_schedule.EntitlementManagementSchedule)),
        }
        return fields
    
    @property
    def is_approval_required_for_add(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequiredForAdd property value. Indicates whether a request to add must be approved by an approver.
        Returns: Optional[bool]
        """
        return self._is_approval_required_for_add
    
    @is_approval_required_for_add.setter
    def is_approval_required_for_add(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequiredForAdd property value. Indicates whether a request to add must be approved by an approver.
        Args:
            value: Value to set for the is_approval_required_for_add property.
        """
        self._is_approval_required_for_add = value
    
    @property
    def is_approval_required_for_update(self,) -> Optional[bool]:
        """
        Gets the isApprovalRequiredForUpdate property value. Indicates whether a request to update must be approved by an approver.
        Returns: Optional[bool]
        """
        return self._is_approval_required_for_update
    
    @is_approval_required_for_update.setter
    def is_approval_required_for_update(self,value: Optional[bool] = None) -> None:
        """
        Sets the isApprovalRequiredForUpdate property value. Indicates whether a request to update must be approved by an approver.
        Args:
            value: Value to set for the is_approval_required_for_update property.
        """
        self._is_approval_required_for_update = value
    
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
    
    @property
    def policy_description(self,) -> Optional[str]:
        """
        Gets the policyDescription property value. The description of the policy that the user is trying to request access using.
        Returns: Optional[str]
        """
        return self._policy_description
    
    @policy_description.setter
    def policy_description(self,value: Optional[str] = None) -> None:
        """
        Sets the policyDescription property value. The description of the policy that the user is trying to request access using.
        Args:
            value: Value to set for the policy_description property.
        """
        self._policy_description = value
    
    @property
    def policy_display_name(self,) -> Optional[str]:
        """
        Gets the policyDisplayName property value. The display name of the policy that the user is trying to request access using.
        Returns: Optional[str]
        """
        return self._policy_display_name
    
    @policy_display_name.setter
    def policy_display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the policyDisplayName property value. The display name of the policy that the user is trying to request access using.
        Args:
            value: Value to set for the policy_display_name property.
        """
        self._policy_display_name = value
    
    @property
    def policy_id(self,) -> Optional[str]:
        """
        Gets the policyId property value. The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
        Returns: Optional[str]
        """
        return self._policy_id
    
    @policy_id.setter
    def policy_id(self,value: Optional[str] = None) -> None:
        """
        Sets the policyId property value. The identifier of the policy that these requirements are associated with. This identifier can be used when creating a new assignment request.
        Args:
            value: Value to set for the policy_id property.
        """
        self._policy_id = value
    
    @property
    def questions(self,) -> Optional[List[access_package_question.AccessPackageQuestion]]:
        """
        Gets the questions property value. The questions property
        Returns: Optional[List[access_package_question.AccessPackageQuestion]]
        """
        return self._questions
    
    @questions.setter
    def questions(self,value: Optional[List[access_package_question.AccessPackageQuestion]] = None) -> None:
        """
        Sets the questions property value. The questions property
        Args:
            value: Value to set for the questions property.
        """
        self._questions = value
    
    @property
    def schedule(self,) -> Optional[entitlement_management_schedule.EntitlementManagementSchedule]:
        """
        Gets the schedule property value. Schedule restrictions enforced, if any.
        Returns: Optional[entitlement_management_schedule.EntitlementManagementSchedule]
        """
        return self._schedule
    
    @schedule.setter
    def schedule(self,value: Optional[entitlement_management_schedule.EntitlementManagementSchedule] = None) -> None:
        """
        Sets the schedule property value. Schedule restrictions enforced, if any.
        Args:
            value: Value to set for the schedule property.
        """
        self._schedule = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        writer.write_bool_value("allowCustomAssignmentSchedule", self.allow_custom_assignment_schedule)
        writer.write_bool_value("isApprovalRequiredForAdd", self.is_approval_required_for_add)
        writer.write_bool_value("isApprovalRequiredForUpdate", self.is_approval_required_for_update)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_str_value("policyDescription", self.policy_description)
        writer.write_str_value("policyDisplayName", self.policy_display_name)
        writer.write_str_value("policyId", self.policy_id)
        writer.write_collection_of_object_values("questions", self.questions)
        writer.write_object_value("schedule", self.schedule)
        writer.write_additional_data_value(self.additional_data)
    

