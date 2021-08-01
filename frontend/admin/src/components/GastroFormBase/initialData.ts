import {
  initialLocationData,
  initialLocationBooleanAttributeData,
} from '../LocationBaseFormNew/initialData';

export const initialGastroLocationBooleanAttributeData = {
  ...initialLocationBooleanAttributeData,
  handicappedAccessibleWc: null,
  dog: null,
  childChair: null,
  catering: null,
  wlan: null,
  glutenFree: null,
  breakfast: null,
  brunch: null,
};

export const initialGastroLocationPositiveIntegerAttributeData = {
  seatsIndoor: 0,
  seatsOutdoor: 0,
};

const initialGastroData = {
  ...initialLocationData,
  attributes: {
    ...initialGastroLocationBooleanAttributeData,
    ...initialGastroLocationPositiveIntegerAttributeData,
  },
};

export default initialGastroData;
