import LocationList from '@/components/LocationList';
import { GASTRO } from '@/utils/constants';
import { buildListUrl } from '@/utils/utils';

const GastroPage = () => (
  <>
    <LocationList
      label="Gastro"
      url={`${buildListUrl(GASTRO)}?closed=false&is_submission=false`}
      type={GASTRO}
    />
  </>
);

export default GastroPage;
