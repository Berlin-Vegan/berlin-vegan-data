import React from 'react';

import LocationList from '../../components/LocationList';
import { buildListUrl } from '../../utils/utils';
import { GASTRO } from '../../utils/constants';

const GastroClosedPage = () => (
  <>
    <LocationList
      label="Gastro"
      url={`${buildListUrl(GASTRO)}?closed=true&is_submission=false`}
    />
  </>
);

export default GastroClosedPage;
