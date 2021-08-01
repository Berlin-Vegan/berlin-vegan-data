import React from 'react';

import LocationList from '../../components/LocationList';
import { buildListUrl } from '../../utils/utils';
import { GASTRO } from '../../utils/constants';

const GastroSubmissionPage = () => (
  <>
    <LocationList
      label="Gastro"
      url={`${buildListUrl(GASTRO)}?closed=false&is_submission=true`}
    />
  </>
);

export default GastroSubmissionPage;
