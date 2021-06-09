import React from 'react';

import LocationList from '../../components/LocationList';
import { buildListUrl } from '../../utils/utils';
import { SHOPPING } from '../../utils/constants';

const ShoppingSubmissionPage = () => (
  <>
    <LocationList
      label="Shopping"
      url={`${buildListUrl(SHOPPING)}?closed=false&is_submission=true`}
    />
  </>
);

export default ShoppingSubmissionPage;
