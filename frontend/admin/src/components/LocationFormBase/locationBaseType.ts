type LocationBaseAttributesType = {
  [index: string]: null | boolean;
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
  attributes: LocationBaseAttributesType;
  openingHours: OpeningHoursType;
};

export default LocationBaseType;
