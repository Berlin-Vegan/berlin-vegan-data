type NullBoolean = null | boolean;

type LocationBaseBooleanAttributesType = {
  organic: NullBoolean;
  delivery: NullBoolean;
  handicappedAccessible: NullBoolean;
};

type GastroBooleanAttributesType = LocationBaseBooleanAttributesType & {
  handicappedAccessibleWc: NullBoolean;
  dog: NullBoolean;
  childChair: NullBoolean;
  catering: NullBoolean;
  wlan: NullBoolean;
  glutenFree: NullBoolean;
  breakfast: NullBoolean;
  brunch: NullBoolean;
  seatsOutdoor: number;
  seatsIndoor: number;
};

type ShoppingBooleanAttributesType = LocationBaseBooleanAttributesType & {
  webshop: NullBoolean;
};

type OpeningHoursDayType = {
  opening: null | string;
  closing: null | string;
};

type OpeningHoursType = {
  monday: OpeningHoursDayType;
  tuesday: OpeningHoursDayType;
  wednesday: OpeningHoursDayType;
  thursday: OpeningHoursDayType;
  friday: OpeningHoursDayType;
  saturday: OpeningHoursDayType;
  sunday: OpeningHoursDayType;
};

type LocationBaseType = {
  id?: string;
  created?: string;
  updated?: string;
  lastEditor?: string;
  name: string;
  street: string;
  postalCode: string;
  city: string;
  vegan: number;
  latitude: string;
  longitude: string;
  telephone: string;
  website: string;
  email: string;
  comment: string;
  commentEnglish: string;
  commentOpeningHours: string;
  reviewLink: string;
  closed: null | string;
  textIntern: string;
  publicTransport: string;
  hasSticker: boolean;
  isSubmission: boolean;
  tags: string[];
  attributes: GastroBooleanAttributesType | ShoppingBooleanAttributesType;
  openingHours: OpeningHoursType;
  review: null | number;
};

export default LocationBaseType;
