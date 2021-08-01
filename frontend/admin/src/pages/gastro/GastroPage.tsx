import React from 'react';

import LocationList from '../../components/LocationList';
import { buildListUrl } from '../../utils/utils';
import { GASTRO } from '../../utils/constants';

const GastroPage = () => (
  <>
    <LocationList
      label="Gastro"
      url={`${buildListUrl(GASTRO)}?closed=false&is_submission=false`}
    />
  </>
);

export default GastroPage;
