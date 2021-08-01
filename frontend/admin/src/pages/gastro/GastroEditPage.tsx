import React from 'react';

import LocationEdit from '../../components/LocationEdit';
import { GASTRO } from '../../utils/constants';
import { gastroSchema } from '../../components/GastroFormBase/gastroFormSchema';
import GastroFormBase from '../../components/GastroFormBase';

const GastroEditPage = () => (
  <LocationEdit
    type={GASTRO}
    label="Shopping"
    locationForm={GastroFormBase}
    locationFormSchema={gastroSchema}
  />
);

export default GastroEditPage;
