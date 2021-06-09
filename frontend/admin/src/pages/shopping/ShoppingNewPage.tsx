import React from 'react';

import ShoppingFormBase from '../../components/ShoppingFormBase';
import { shoppingSchema } from '../../components/ShoppingFormBase/shoppingFormSchema';
import { SHOPPING } from '../../utils/constants';
import LocationBaseFormNew from '../../components/LocationBaseFormNew';
import initialShoppingData from '../../components/ShoppingFormBase/initialData';

const ShoppingNewPage = () => (
  <LocationBaseFormNew
    type={SHOPPING}
    label="Shopping"
    locationForm={ShoppingFormBase}
    locationFormSchema={shoppingSchema}
    initialData={initialShoppingData}
  />
);

export default ShoppingNewPage;
