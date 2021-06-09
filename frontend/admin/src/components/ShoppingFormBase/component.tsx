import React, { FC } from 'react';

import LocationFormBase from '../LocationFormBase';
import {
  SHOPPING_BOOLEAN_ATTRIBUTES,
  SHOPPING_TAGS,
} from './shoppingFormSchema';

const ShoppingFormBase: FC = ({ children }) => (
  <LocationFormBase
    booleanAttrList={SHOPPING_BOOLEAN_ATTRIBUTES}
    tagList={SHOPPING_TAGS}
  >
    {children}
  </LocationFormBase>
);

export default ShoppingFormBase;
