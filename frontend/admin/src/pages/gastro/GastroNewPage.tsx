import React from 'react';

import LocationBaseFormNew from '../../components/LocationBaseFormNew';
import { GASTRO } from '../../utils/constants';
import GastroFormBase from '../../components/GastroFormBase';
import { gastroSchema } from '../../components/GastroFormBase/gastroFormSchema';
import initialGastroData from '../../components/GastroFormBase/initialData';

const GastroNewPage = () => (
  <LocationBaseFormNew
    type={GASTRO}
    label="Gastro"
    locationForm={GastroFormBase}
    locationFormSchema={gastroSchema}
    initialData={initialGastroData}
  />
);

export default GastroNewPage;
