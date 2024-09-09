import { PropsWithChildren } from 'react';

import LocationFormBase from '../LocationFormBase';
import { SHOPPING_BOOLEAN_ATTRIBUTES, SHOPPING_TAGS } from './shoppingFormSchema';

const ShoppingFormBase = ({ children }: PropsWithChildren) => (
  <LocationFormBase
    booleanAttrList={SHOPPING_BOOLEAN_ATTRIBUTES}
    tagList={SHOPPING_TAGS}
    positiveIntegerAttrList={[]}
    veganOption={true}
  >
    {children}
  </LocationFormBase>
);

export default ShoppingFormBase;
