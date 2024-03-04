import LocationList from '@/components/LocationList';
import { SHOPPING } from '@/utils/constants';
import { buildListUrl } from '@/utils/utils';

const ShoppingClosedPage = () => (
  <>
    <LocationList
      label="Shopping"
      url={`${buildListUrl(SHOPPING)}?closed=true&is_submission=false`}
      type={SHOPPING}
    />
  </>
);

export default ShoppingClosedPage;
