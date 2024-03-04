import React from 'react';

import LocationList from '@/components/LocationList';
import { GASTRO } from '@/utils/constants';
import { buildListUrl } from '@/utils/utils';

const GastroSubmissionPage = () => (
  <>
    <LocationList
      label="Gastro"
      url={`${buildListUrl(GASTRO)}?closed=false&is_submission=true`}
      type={GASTRO}
    />
  </>
);

export default GastroSubmissionPage;
