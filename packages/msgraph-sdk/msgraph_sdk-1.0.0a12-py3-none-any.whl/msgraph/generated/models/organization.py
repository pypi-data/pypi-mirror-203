from __future__ import annotations
from datetime import datetime
from kiota_abstractions.serialization import Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import assigned_plan, certificate_based_auth_configuration, directory_object, extension, mdm_authority, organizational_branding, partner_tenant_type, privacy_profile, provisioned_plan, verified_domain

from . import directory_object

class Organization(directory_object.DirectoryObject):
    def __init__(self,) -> None:
        """
        Instantiates a new Organization and sets the default values.
        """
        super().__init__()
        self.odata_type = "#microsoft.graph.organization"
        # The collection of service plans associated with the tenant. Not nullable.
        self._assigned_plans: Optional[List[assigned_plan.AssignedPlan]] = None
        # Branding for the organization. Nullable.
        self._branding: Optional[organizational_branding.OrganizationalBranding] = None
        # Telephone number for the organization. Although this is a string collection, only one number can be set for this property.
        self._business_phones: Optional[List[str]] = None
        # Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.
        self._certificate_based_auth_configuration: Optional[List[certificate_based_auth_configuration.CertificateBasedAuthConfiguration]] = None
        # City name of the address for the organization.
        self._city: Optional[str] = None
        # Country/region name of the address for the organization.
        self._country: Optional[str] = None
        # Country or region abbreviation for the organization in ISO 3166-2 format.
        self._country_letter_code: Optional[str] = None
        # Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._created_date_time: Optional[datetime] = None
        # Two-letter ISO 3166 country code indicating the default service usage location of an organization.
        self._default_usage_location: Optional[str] = None
        # The display name for the tenant.
        self._display_name: Optional[str] = None
        # The collection of open extensions defined for the organization. Read-only. Nullable.
        self._extensions: Optional[List[extension.Extension]] = None
        # Not nullable.
        self._marketing_notification_emails: Optional[List[str]] = None
        # Mobile device management authority.
        self._mobile_device_management_authority: Optional[mdm_authority.MdmAuthority] = None
        # The time and date at which the tenant was last synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        self._on_premises_last_sync_date_time: Optional[datetime] = None
        # true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced. Nullable. null if this object has never been synced from an on-premises directory (default).
        self._on_premises_sync_enabled: Optional[bool] = None
        # The type of partnership this tenant has with Microsoft. The possible values are: microsoftSupport, syndicatePartner, breadthPartner, breadthPartnerDelegatedAdmin, resellerPartnerDelegatedAdmin, valueAddedResellerPartnerDelegatedAdmin, unknownFutureValue. Nullable. For more information about the possible types, see partnerTenantType values.
        self._partner_tenant_type: Optional[partner_tenant_type.PartnerTenantType] = None
        # Postal code of the address for the organization.
        self._postal_code: Optional[str] = None
        # The preferred language for the organization. Should follow ISO 639-1 Code; for example, en.
        self._preferred_language: Optional[str] = None
        # The privacy profile of an organization.
        self._privacy_profile: Optional[privacy_profile.PrivacyProfile] = None
        # Not nullable.
        self._provisioned_plans: Optional[List[provisioned_plan.ProvisionedPlan]] = None
        # The securityComplianceNotificationMails property
        self._security_compliance_notification_mails: Optional[List[str]] = None
        # The securityComplianceNotificationPhones property
        self._security_compliance_notification_phones: Optional[List[str]] = None
        # State name of the address for the organization.
        self._state: Optional[str] = None
        # Street name of the address for organization.
        self._street: Optional[str] = None
        # Not nullable.
        self._technical_notification_mails: Optional[List[str]] = None
        # Not nullable. The tenant type option that was selected when the tenant was created. The possible values are:  AAD - An enterprise identity access management (IAM) service that serves business-to-employee and business-to-business (B2B) scenarios.  AAD B2C A customer identity access management (CIAM) service that serves business-to-consumer (B2C) scenarios.
        self._tenant_type: Optional[str] = None
        # The collection of domains associated with this tenant. Not nullable.
        self._verified_domains: Optional[List[verified_domain.VerifiedDomain]] = None
    
    @property
    def assigned_plans(self,) -> Optional[List[assigned_plan.AssignedPlan]]:
        """
        Gets the assignedPlans property value. The collection of service plans associated with the tenant. Not nullable.
        Returns: Optional[List[assigned_plan.AssignedPlan]]
        """
        return self._assigned_plans
    
    @assigned_plans.setter
    def assigned_plans(self,value: Optional[List[assigned_plan.AssignedPlan]] = None) -> None:
        """
        Sets the assignedPlans property value. The collection of service plans associated with the tenant. Not nullable.
        Args:
            value: Value to set for the assigned_plans property.
        """
        self._assigned_plans = value
    
    @property
    def branding(self,) -> Optional[organizational_branding.OrganizationalBranding]:
        """
        Gets the branding property value. Branding for the organization. Nullable.
        Returns: Optional[organizational_branding.OrganizationalBranding]
        """
        return self._branding
    
    @branding.setter
    def branding(self,value: Optional[organizational_branding.OrganizationalBranding] = None) -> None:
        """
        Sets the branding property value. Branding for the organization. Nullable.
        Args:
            value: Value to set for the branding property.
        """
        self._branding = value
    
    @property
    def business_phones(self,) -> Optional[List[str]]:
        """
        Gets the businessPhones property value. Telephone number for the organization. Although this is a string collection, only one number can be set for this property.
        Returns: Optional[List[str]]
        """
        return self._business_phones
    
    @business_phones.setter
    def business_phones(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the businessPhones property value. Telephone number for the organization. Although this is a string collection, only one number can be set for this property.
        Args:
            value: Value to set for the business_phones property.
        """
        self._business_phones = value
    
    @property
    def certificate_based_auth_configuration(self,) -> Optional[List[certificate_based_auth_configuration.CertificateBasedAuthConfiguration]]:
        """
        Gets the certificateBasedAuthConfiguration property value. Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.
        Returns: Optional[List[certificate_based_auth_configuration.CertificateBasedAuthConfiguration]]
        """
        return self._certificate_based_auth_configuration
    
    @certificate_based_auth_configuration.setter
    def certificate_based_auth_configuration(self,value: Optional[List[certificate_based_auth_configuration.CertificateBasedAuthConfiguration]] = None) -> None:
        """
        Sets the certificateBasedAuthConfiguration property value. Navigation property to manage certificate-based authentication configuration. Only a single instance of certificateBasedAuthConfiguration can be created in the collection.
        Args:
            value: Value to set for the certificate_based_auth_configuration property.
        """
        self._certificate_based_auth_configuration = value
    
    @property
    def city(self,) -> Optional[str]:
        """
        Gets the city property value. City name of the address for the organization.
        Returns: Optional[str]
        """
        return self._city
    
    @city.setter
    def city(self,value: Optional[str] = None) -> None:
        """
        Sets the city property value. City name of the address for the organization.
        Args:
            value: Value to set for the city property.
        """
        self._city = value
    
    @property
    def country(self,) -> Optional[str]:
        """
        Gets the country property value. Country/region name of the address for the organization.
        Returns: Optional[str]
        """
        return self._country
    
    @country.setter
    def country(self,value: Optional[str] = None) -> None:
        """
        Sets the country property value. Country/region name of the address for the organization.
        Args:
            value: Value to set for the country property.
        """
        self._country = value
    
    @property
    def country_letter_code(self,) -> Optional[str]:
        """
        Gets the countryLetterCode property value. Country or region abbreviation for the organization in ISO 3166-2 format.
        Returns: Optional[str]
        """
        return self._country_letter_code
    
    @country_letter_code.setter
    def country_letter_code(self,value: Optional[str] = None) -> None:
        """
        Sets the countryLetterCode property value. Country or region abbreviation for the organization in ISO 3166-2 format.
        Args:
            value: Value to set for the country_letter_code property.
        """
        self._country_letter_code = value
    
    @property
    def created_date_time(self,) -> Optional[datetime]:
        """
        Gets the createdDateTime property value. Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._created_date_time
    
    @created_date_time.setter
    def created_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the createdDateTime property value. Timestamp of when the organization was created. The value cannot be modified and is automatically populated when the organization is created. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the created_date_time property.
        """
        self._created_date_time = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> Organization:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: Organization
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return Organization()
    
    @property
    def default_usage_location(self,) -> Optional[str]:
        """
        Gets the defaultUsageLocation property value. Two-letter ISO 3166 country code indicating the default service usage location of an organization.
        Returns: Optional[str]
        """
        return self._default_usage_location
    
    @default_usage_location.setter
    def default_usage_location(self,value: Optional[str] = None) -> None:
        """
        Sets the defaultUsageLocation property value. Two-letter ISO 3166 country code indicating the default service usage location of an organization.
        Args:
            value: Value to set for the default_usage_location property.
        """
        self._default_usage_location = value
    
    @property
    def display_name(self,) -> Optional[str]:
        """
        Gets the displayName property value. The display name for the tenant.
        Returns: Optional[str]
        """
        return self._display_name
    
    @display_name.setter
    def display_name(self,value: Optional[str] = None) -> None:
        """
        Sets the displayName property value. The display name for the tenant.
        Args:
            value: Value to set for the display_name property.
        """
        self._display_name = value
    
    @property
    def extensions(self,) -> Optional[List[extension.Extension]]:
        """
        Gets the extensions property value. The collection of open extensions defined for the organization. Read-only. Nullable.
        Returns: Optional[List[extension.Extension]]
        """
        return self._extensions
    
    @extensions.setter
    def extensions(self,value: Optional[List[extension.Extension]] = None) -> None:
        """
        Sets the extensions property value. The collection of open extensions defined for the organization. Read-only. Nullable.
        Args:
            value: Value to set for the extensions property.
        """
        self._extensions = value
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import assigned_plan, certificate_based_auth_configuration, directory_object, extension, mdm_authority, organizational_branding, partner_tenant_type, privacy_profile, provisioned_plan, verified_domain

        fields: Dict[str, Callable[[Any], None]] = {
            "assignedPlans": lambda n : setattr(self, 'assigned_plans', n.get_collection_of_object_values(assigned_plan.AssignedPlan)),
            "branding": lambda n : setattr(self, 'branding', n.get_object_value(organizational_branding.OrganizationalBranding)),
            "businessPhones": lambda n : setattr(self, 'business_phones', n.get_collection_of_primitive_values(str)),
            "certificateBasedAuthConfiguration": lambda n : setattr(self, 'certificate_based_auth_configuration', n.get_collection_of_object_values(certificate_based_auth_configuration.CertificateBasedAuthConfiguration)),
            "city": lambda n : setattr(self, 'city', n.get_str_value()),
            "country": lambda n : setattr(self, 'country', n.get_str_value()),
            "countryLetterCode": lambda n : setattr(self, 'country_letter_code', n.get_str_value()),
            "createdDateTime": lambda n : setattr(self, 'created_date_time', n.get_datetime_value()),
            "defaultUsageLocation": lambda n : setattr(self, 'default_usage_location', n.get_str_value()),
            "displayName": lambda n : setattr(self, 'display_name', n.get_str_value()),
            "extensions": lambda n : setattr(self, 'extensions', n.get_collection_of_object_values(extension.Extension)),
            "marketingNotificationEmails": lambda n : setattr(self, 'marketing_notification_emails', n.get_collection_of_primitive_values(str)),
            "mobileDeviceManagementAuthority": lambda n : setattr(self, 'mobile_device_management_authority', n.get_enum_value(mdm_authority.MdmAuthority)),
            "onPremisesLastSyncDateTime": lambda n : setattr(self, 'on_premises_last_sync_date_time', n.get_datetime_value()),
            "onPremisesSyncEnabled": lambda n : setattr(self, 'on_premises_sync_enabled', n.get_bool_value()),
            "partnerTenantType": lambda n : setattr(self, 'partner_tenant_type', n.get_enum_value(partner_tenant_type.PartnerTenantType)),
            "postalCode": lambda n : setattr(self, 'postal_code', n.get_str_value()),
            "preferredLanguage": lambda n : setattr(self, 'preferred_language', n.get_str_value()),
            "privacyProfile": lambda n : setattr(self, 'privacy_profile', n.get_object_value(privacy_profile.PrivacyProfile)),
            "provisionedPlans": lambda n : setattr(self, 'provisioned_plans', n.get_collection_of_object_values(provisioned_plan.ProvisionedPlan)),
            "securityComplianceNotificationMails": lambda n : setattr(self, 'security_compliance_notification_mails', n.get_collection_of_primitive_values(str)),
            "securityComplianceNotificationPhones": lambda n : setattr(self, 'security_compliance_notification_phones', n.get_collection_of_primitive_values(str)),
            "state": lambda n : setattr(self, 'state', n.get_str_value()),
            "street": lambda n : setattr(self, 'street', n.get_str_value()),
            "technicalNotificationMails": lambda n : setattr(self, 'technical_notification_mails', n.get_collection_of_primitive_values(str)),
            "tenantType": lambda n : setattr(self, 'tenant_type', n.get_str_value()),
            "verifiedDomains": lambda n : setattr(self, 'verified_domains', n.get_collection_of_object_values(verified_domain.VerifiedDomain)),
        }
        super_fields = super().get_field_deserializers()
        fields.update(super_fields)
        return fields
    
    @property
    def marketing_notification_emails(self,) -> Optional[List[str]]:
        """
        Gets the marketingNotificationEmails property value. Not nullable.
        Returns: Optional[List[str]]
        """
        return self._marketing_notification_emails
    
    @marketing_notification_emails.setter
    def marketing_notification_emails(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the marketingNotificationEmails property value. Not nullable.
        Args:
            value: Value to set for the marketing_notification_emails property.
        """
        self._marketing_notification_emails = value
    
    @property
    def mobile_device_management_authority(self,) -> Optional[mdm_authority.MdmAuthority]:
        """
        Gets the mobileDeviceManagementAuthority property value. Mobile device management authority.
        Returns: Optional[mdm_authority.MdmAuthority]
        """
        return self._mobile_device_management_authority
    
    @mobile_device_management_authority.setter
    def mobile_device_management_authority(self,value: Optional[mdm_authority.MdmAuthority] = None) -> None:
        """
        Sets the mobileDeviceManagementAuthority property value. Mobile device management authority.
        Args:
            value: Value to set for the mobile_device_management_authority property.
        """
        self._mobile_device_management_authority = value
    
    @property
    def on_premises_last_sync_date_time(self,) -> Optional[datetime]:
        """
        Gets the onPremisesLastSyncDateTime property value. The time and date at which the tenant was last synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Returns: Optional[datetime]
        """
        return self._on_premises_last_sync_date_time
    
    @on_premises_last_sync_date_time.setter
    def on_premises_last_sync_date_time(self,value: Optional[datetime] = None) -> None:
        """
        Sets the onPremisesLastSyncDateTime property value. The time and date at which the tenant was last synced with the on-premises directory. The Timestamp type represents date and time information using ISO 8601 format and is always in UTC time. For example, midnight UTC on Jan 1, 2014 is 2014-01-01T00:00:00Z. Read-only.
        Args:
            value: Value to set for the on_premises_last_sync_date_time property.
        """
        self._on_premises_last_sync_date_time = value
    
    @property
    def on_premises_sync_enabled(self,) -> Optional[bool]:
        """
        Gets the onPremisesSyncEnabled property value. true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced. Nullable. null if this object has never been synced from an on-premises directory (default).
        Returns: Optional[bool]
        """
        return self._on_premises_sync_enabled
    
    @on_premises_sync_enabled.setter
    def on_premises_sync_enabled(self,value: Optional[bool] = None) -> None:
        """
        Sets the onPremisesSyncEnabled property value. true if this object is synced from an on-premises directory; false if this object was originally synced from an on-premises directory but is no longer synced. Nullable. null if this object has never been synced from an on-premises directory (default).
        Args:
            value: Value to set for the on_premises_sync_enabled property.
        """
        self._on_premises_sync_enabled = value
    
    @property
    def partner_tenant_type(self,) -> Optional[partner_tenant_type.PartnerTenantType]:
        """
        Gets the partnerTenantType property value. The type of partnership this tenant has with Microsoft. The possible values are: microsoftSupport, syndicatePartner, breadthPartner, breadthPartnerDelegatedAdmin, resellerPartnerDelegatedAdmin, valueAddedResellerPartnerDelegatedAdmin, unknownFutureValue. Nullable. For more information about the possible types, see partnerTenantType values.
        Returns: Optional[partner_tenant_type.PartnerTenantType]
        """
        return self._partner_tenant_type
    
    @partner_tenant_type.setter
    def partner_tenant_type(self,value: Optional[partner_tenant_type.PartnerTenantType] = None) -> None:
        """
        Sets the partnerTenantType property value. The type of partnership this tenant has with Microsoft. The possible values are: microsoftSupport, syndicatePartner, breadthPartner, breadthPartnerDelegatedAdmin, resellerPartnerDelegatedAdmin, valueAddedResellerPartnerDelegatedAdmin, unknownFutureValue. Nullable. For more information about the possible types, see partnerTenantType values.
        Args:
            value: Value to set for the partner_tenant_type property.
        """
        self._partner_tenant_type = value
    
    @property
    def postal_code(self,) -> Optional[str]:
        """
        Gets the postalCode property value. Postal code of the address for the organization.
        Returns: Optional[str]
        """
        return self._postal_code
    
    @postal_code.setter
    def postal_code(self,value: Optional[str] = None) -> None:
        """
        Sets the postalCode property value. Postal code of the address for the organization.
        Args:
            value: Value to set for the postal_code property.
        """
        self._postal_code = value
    
    @property
    def preferred_language(self,) -> Optional[str]:
        """
        Gets the preferredLanguage property value. The preferred language for the organization. Should follow ISO 639-1 Code; for example, en.
        Returns: Optional[str]
        """
        return self._preferred_language
    
    @preferred_language.setter
    def preferred_language(self,value: Optional[str] = None) -> None:
        """
        Sets the preferredLanguage property value. The preferred language for the organization. Should follow ISO 639-1 Code; for example, en.
        Args:
            value: Value to set for the preferred_language property.
        """
        self._preferred_language = value
    
    @property
    def privacy_profile(self,) -> Optional[privacy_profile.PrivacyProfile]:
        """
        Gets the privacyProfile property value. The privacy profile of an organization.
        Returns: Optional[privacy_profile.PrivacyProfile]
        """
        return self._privacy_profile
    
    @privacy_profile.setter
    def privacy_profile(self,value: Optional[privacy_profile.PrivacyProfile] = None) -> None:
        """
        Sets the privacyProfile property value. The privacy profile of an organization.
        Args:
            value: Value to set for the privacy_profile property.
        """
        self._privacy_profile = value
    
    @property
    def provisioned_plans(self,) -> Optional[List[provisioned_plan.ProvisionedPlan]]:
        """
        Gets the provisionedPlans property value. Not nullable.
        Returns: Optional[List[provisioned_plan.ProvisionedPlan]]
        """
        return self._provisioned_plans
    
    @provisioned_plans.setter
    def provisioned_plans(self,value: Optional[List[provisioned_plan.ProvisionedPlan]] = None) -> None:
        """
        Sets the provisionedPlans property value. Not nullable.
        Args:
            value: Value to set for the provisioned_plans property.
        """
        self._provisioned_plans = value
    
    @property
    def security_compliance_notification_mails(self,) -> Optional[List[str]]:
        """
        Gets the securityComplianceNotificationMails property value. The securityComplianceNotificationMails property
        Returns: Optional[List[str]]
        """
        return self._security_compliance_notification_mails
    
    @security_compliance_notification_mails.setter
    def security_compliance_notification_mails(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the securityComplianceNotificationMails property value. The securityComplianceNotificationMails property
        Args:
            value: Value to set for the security_compliance_notification_mails property.
        """
        self._security_compliance_notification_mails = value
    
    @property
    def security_compliance_notification_phones(self,) -> Optional[List[str]]:
        """
        Gets the securityComplianceNotificationPhones property value. The securityComplianceNotificationPhones property
        Returns: Optional[List[str]]
        """
        return self._security_compliance_notification_phones
    
    @security_compliance_notification_phones.setter
    def security_compliance_notification_phones(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the securityComplianceNotificationPhones property value. The securityComplianceNotificationPhones property
        Args:
            value: Value to set for the security_compliance_notification_phones property.
        """
        self._security_compliance_notification_phones = value
    
    def serialize(self,writer: SerializationWriter) -> None:
        """
        Serializes information the current object
        Args:
            writer: Serialization writer to use to serialize this model
        """
        if writer is None:
            raise Exception("writer cannot be undefined")
        super().serialize(writer)
        writer.write_collection_of_object_values("assignedPlans", self.assigned_plans)
        writer.write_object_value("branding", self.branding)
        writer.write_collection_of_primitive_values("businessPhones", self.business_phones)
        writer.write_collection_of_object_values("certificateBasedAuthConfiguration", self.certificate_based_auth_configuration)
        writer.write_str_value("city", self.city)
        writer.write_str_value("country", self.country)
        writer.write_str_value("countryLetterCode", self.country_letter_code)
        writer.write_datetime_value("createdDateTime", self.created_date_time)
        writer.write_str_value("defaultUsageLocation", self.default_usage_location)
        writer.write_str_value("displayName", self.display_name)
        writer.write_collection_of_object_values("extensions", self.extensions)
        writer.write_collection_of_primitive_values("marketingNotificationEmails", self.marketing_notification_emails)
        writer.write_enum_value("mobileDeviceManagementAuthority", self.mobile_device_management_authority)
        writer.write_datetime_value("onPremisesLastSyncDateTime", self.on_premises_last_sync_date_time)
        writer.write_bool_value("onPremisesSyncEnabled", self.on_premises_sync_enabled)
        writer.write_enum_value("partnerTenantType", self.partner_tenant_type)
        writer.write_str_value("postalCode", self.postal_code)
        writer.write_str_value("preferredLanguage", self.preferred_language)
        writer.write_object_value("privacyProfile", self.privacy_profile)
        writer.write_collection_of_object_values("provisionedPlans", self.provisioned_plans)
        writer.write_collection_of_primitive_values("securityComplianceNotificationMails", self.security_compliance_notification_mails)
        writer.write_collection_of_primitive_values("securityComplianceNotificationPhones", self.security_compliance_notification_phones)
        writer.write_str_value("state", self.state)
        writer.write_str_value("street", self.street)
        writer.write_collection_of_primitive_values("technicalNotificationMails", self.technical_notification_mails)
        writer.write_str_value("tenantType", self.tenant_type)
        writer.write_collection_of_object_values("verifiedDomains", self.verified_domains)
    
    @property
    def state(self,) -> Optional[str]:
        """
        Gets the state property value. State name of the address for the organization.
        Returns: Optional[str]
        """
        return self._state
    
    @state.setter
    def state(self,value: Optional[str] = None) -> None:
        """
        Sets the state property value. State name of the address for the organization.
        Args:
            value: Value to set for the state property.
        """
        self._state = value
    
    @property
    def street(self,) -> Optional[str]:
        """
        Gets the street property value. Street name of the address for organization.
        Returns: Optional[str]
        """
        return self._street
    
    @street.setter
    def street(self,value: Optional[str] = None) -> None:
        """
        Sets the street property value. Street name of the address for organization.
        Args:
            value: Value to set for the street property.
        """
        self._street = value
    
    @property
    def technical_notification_mails(self,) -> Optional[List[str]]:
        """
        Gets the technicalNotificationMails property value. Not nullable.
        Returns: Optional[List[str]]
        """
        return self._technical_notification_mails
    
    @technical_notification_mails.setter
    def technical_notification_mails(self,value: Optional[List[str]] = None) -> None:
        """
        Sets the technicalNotificationMails property value. Not nullable.
        Args:
            value: Value to set for the technical_notification_mails property.
        """
        self._technical_notification_mails = value
    
    @property
    def tenant_type(self,) -> Optional[str]:
        """
        Gets the tenantType property value. Not nullable. The tenant type option that was selected when the tenant was created. The possible values are:  AAD - An enterprise identity access management (IAM) service that serves business-to-employee and business-to-business (B2B) scenarios.  AAD B2C A customer identity access management (CIAM) service that serves business-to-consumer (B2C) scenarios.
        Returns: Optional[str]
        """
        return self._tenant_type
    
    @tenant_type.setter
    def tenant_type(self,value: Optional[str] = None) -> None:
        """
        Sets the tenantType property value. Not nullable. The tenant type option that was selected when the tenant was created. The possible values are:  AAD - An enterprise identity access management (IAM) service that serves business-to-employee and business-to-business (B2B) scenarios.  AAD B2C A customer identity access management (CIAM) service that serves business-to-consumer (B2C) scenarios.
        Args:
            value: Value to set for the tenant_type property.
        """
        self._tenant_type = value
    
    @property
    def verified_domains(self,) -> Optional[List[verified_domain.VerifiedDomain]]:
        """
        Gets the verifiedDomains property value. The collection of domains associated with this tenant. Not nullable.
        Returns: Optional[List[verified_domain.VerifiedDomain]]
        """
        return self._verified_domains
    
    @verified_domains.setter
    def verified_domains(self,value: Optional[List[verified_domain.VerifiedDomain]] = None) -> None:
        """
        Sets the verifiedDomains property value. The collection of domains associated with this tenant. Not nullable.
        Args:
            value: Value to set for the verified_domains property.
        """
        self._verified_domains = value
    

