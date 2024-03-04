import LocationList from '@/components/LocationList';
import { SHOPPING } from '@/utils/constants';
import { buildListUrl } from '@/utils/utils';

const ShoppingPage = () => (
  <>
    <LocationList
      label="Shopping"
      url={`${buildListUrl(SHOPPING)}?closed=false&is_submission=false`}
      type={SHOPPING}
    />
  </>
);

export default ShoppingPage;
