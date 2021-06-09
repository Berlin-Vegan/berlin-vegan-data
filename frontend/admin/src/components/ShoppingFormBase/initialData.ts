import {
  initialLocationData,
  initialLocationBooleanAttributeData,
} from '../LocationBaseFormNew/initialData';

const initialShoppingData = {
  ...initialLocationData,
  attributes: {
    ...initialLocationBooleanAttributeData,
    webshop: null,
  },
};

export default initialShoppingData;
