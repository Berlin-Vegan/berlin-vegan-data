import React from 'react';

import LocationEdit from '../../components/LocationEdit';
import ShoppingFormBase from '../../components/ShoppingFormBase';
import { shoppingSchema } from '../../components/ShoppingFormBase/shoppingFormSchema';
import { SHOPPING } from '../../utils/constants';

const ShoppingEditPage = () => (
  <LocationEdit
    type={SHOPPING}
    label="Shopping"
    locationForm={ShoppingFormBase}
    locationFormSchema={shoppingSchema}
  />
);

export default ShoppingEditPage;
