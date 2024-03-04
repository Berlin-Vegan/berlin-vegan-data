import LocationList from '@/components/LocationList';
import { GASTRO } from '@/utils/constants';
import { buildListUrl } from '@/utils/utils';

const GastroClosedPage = () => (
  <>
    <LocationList
      label="Gastro"
      type={GASTRO}
      url={`${buildListUrl(GASTRO)}?closed=true&is_submission=false`}
    />
  </>
);

export default GastroClosedPage;
