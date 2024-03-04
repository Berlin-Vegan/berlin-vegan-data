const openingHoursDay = {
  opening: null,
  closing: null,
};

const openingHours = {
  monday: openingHoursDay,
  tuesday: openingHoursDay,
  wednesday: openingHoursDay,
  thursday: openingHoursDay,
  friday: openingHoursDay,
  saturday: openingHoursDay,
  sunday: openingHoursDay,
};

export const initialLocationData = {
  name: '',
  street: '',
  postalCode: '',
  city: 'Berlin',
  latitude: '',
  longitude: '',
  telephone: '',
  website: '',
  email: '',
  comment: '',
  commentEnglish: '',
  commentOpeningHours: '',
  commentPublicTransport: '',
  reviewLink: '',
  closed: null,
  textIntern: '',
  hasSticker: false,
  publicTransport: '',
  vegan: 5,
  isSubmission: false,
  tags: [],
  openingHours,
  review: '',
};

export const initialLocationBooleanAttributeData = {
  organic: null,
  delivery: null,
  handicappedAccessible: null,
};
