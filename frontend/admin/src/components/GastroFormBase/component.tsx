import React, { FC } from 'react';

import LocationFormBase from '../LocationFormBase';
import {
  GASTRO_BOOLEAN_ATTRIBUTES,
  GASTRO_POSITIVE_INTEGER_ATTRIBUTES,
  GASTRO_TAGS,
} from './gastroFormSchema';

const GastroFormBase: FC = ({ children }) => (
  <LocationFormBase
    booleanAttrList={GASTRO_BOOLEAN_ATTRIBUTES}
    tagList={GASTRO_TAGS}
    positiveIntegerAttrList={GASTRO_POSITIVE_INTEGER_ATTRIBUTES}
  >
    {children}
  </LocationFormBase>
);

export default GastroFormBase;
