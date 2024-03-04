import React from 'react';

import LocationList from '@/components/LocationList';
import { SHOPPING } from '@/utils/constants';
import { buildListUrl } from '@/utils/utils';

const ShoppingSubmissionPage = () => (
  <>
    <LocationList
      label="Shopping"
      url={`${buildListUrl(SHOPPING)}?closed=false&is_submission=true`}
      type={SHOPPING}
    />
  </>
);

export default ShoppingSubmissionPage;
