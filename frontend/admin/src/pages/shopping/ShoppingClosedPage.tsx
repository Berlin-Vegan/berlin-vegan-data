import React from 'react';

import LocationList from '../../components/LocationList';
import { buildListUrl } from '../../utils/utils';
import { SHOPPING } from '../../utils/constants';

const ShoppingClosedPage = () => (
  <>
    <LocationList
      label="Shopping"
      url={`${buildListUrl(SHOPPING)}?closed=true&is_submission=false`}
    />
  </>
);

export default ShoppingClosedPage;
