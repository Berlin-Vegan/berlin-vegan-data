import { PropsWithChildren } from 'react';

import LocationFormBase from '../LocationFormBase';
import { SHOPPING_BOOLEAN_ATTRIBUTES, SHOPPING_TAGS } from './shoppingFormSchema';

const ShoppingFormBase = ({ children }: PropsWithChildren) => (
  <LocationFormBase
    booleanAttrList={SHOPPING_BOOLEAN_ATTRIBUTES}
    tagList={SHOPPING_TAGS}
    positiveIntegerAttrList={[]}
  >
    {children}
  </LocationFormBase>
);

export default ShoppingFormBase;
