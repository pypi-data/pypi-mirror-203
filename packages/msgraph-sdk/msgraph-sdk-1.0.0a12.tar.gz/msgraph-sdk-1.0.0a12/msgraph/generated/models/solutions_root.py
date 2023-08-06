from __future__ import annotations
from kiota_abstractions.serialization import AdditionalDataHolder, Parsable, ParseNode, SerializationWriter
from typing import Any, Callable, Dict, List, Optional, TYPE_CHECKING, Union

if TYPE_CHECKING:
    from . import booking_business, booking_currency

class SolutionsRoot(AdditionalDataHolder, Parsable):
    def __init__(self,) -> None:
        """
        Instantiates a new SolutionsRoot and sets the default values.
        """
        # Stores additional data not described in the OpenAPI description found when deserializing. Can be used for serialization as well.
        self._additional_data: Dict[str, Any] = {}

        # The bookingBusinesses property
        self._booking_businesses: Optional[List[booking_business.BookingBusiness]] = None
        # The bookingCurrencies property
        self._booking_currencies: Optional[List[booking_currency.BookingCurrency]] = None
        # The OdataType property
        self._odata_type: Optional[str] = None
    
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
    def booking_businesses(self,) -> Optional[List[booking_business.BookingBusiness]]:
        """
        Gets the bookingBusinesses property value. The bookingBusinesses property
        Returns: Optional[List[booking_business.BookingBusiness]]
        """
        return self._booking_businesses
    
    @booking_businesses.setter
    def booking_businesses(self,value: Optional[List[booking_business.BookingBusiness]] = None) -> None:
        """
        Sets the bookingBusinesses property value. The bookingBusinesses property
        Args:
            value: Value to set for the booking_businesses property.
        """
        self._booking_businesses = value
    
    @property
    def booking_currencies(self,) -> Optional[List[booking_currency.BookingCurrency]]:
        """
        Gets the bookingCurrencies property value. The bookingCurrencies property
        Returns: Optional[List[booking_currency.BookingCurrency]]
        """
        return self._booking_currencies
    
    @booking_currencies.setter
    def booking_currencies(self,value: Optional[List[booking_currency.BookingCurrency]] = None) -> None:
        """
        Sets the bookingCurrencies property value. The bookingCurrencies property
        Args:
            value: Value to set for the booking_currencies property.
        """
        self._booking_currencies = value
    
    @staticmethod
    def create_from_discriminator_value(parse_node: Optional[ParseNode] = None) -> SolutionsRoot:
        """
        Creates a new instance of the appropriate class based on discriminator value
        Args:
            parseNode: The parse node to use to read the discriminator value and create the object
        Returns: SolutionsRoot
        """
        if parse_node is None:
            raise Exception("parse_node cannot be undefined")
        return SolutionsRoot()
    
    def get_field_deserializers(self,) -> Dict[str, Callable[[ParseNode], None]]:
        """
        The deserialization information for the current model
        Returns: Dict[str, Callable[[ParseNode], None]]
        """
        from . import booking_business, booking_currency

        fields: Dict[str, Callable[[Any], None]] = {
            "bookingBusinesses": lambda n : setattr(self, 'booking_businesses', n.get_collection_of_object_values(booking_business.BookingBusiness)),
            "bookingCurrencies": lambda n : setattr(self, 'booking_currencies', n.get_collection_of_object_values(booking_currency.BookingCurrency)),
            "@odata.type": lambda n : setattr(self, 'odata_type', n.get_str_value()),
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
        writer.write_collection_of_object_values("bookingBusinesses", self.booking_businesses)
        writer.write_collection_of_object_values("bookingCurrencies", self.booking_currencies)
        writer.write_str_value("@odata.type", self.odata_type)
        writer.write_additional_data_value(self.additional_data)
    

