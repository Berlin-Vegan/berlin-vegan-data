import React from 'react';

import LocationList from '../../components/LocationList';
import { buildListUrl } from '../../utils/utils';
import { SHOPPING } from '../../utils/constants';

const ShoppingPage = () => (
  <>
    <LocationList
      label="Shopping"
      url={`${buildListUrl(SHOPPING)}?closed=false&is_submission=false`}
    />
  </>
);

export default ShoppingPage;
