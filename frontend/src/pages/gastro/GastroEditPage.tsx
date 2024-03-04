import GastroFormBase from '@/components/GastroFormBase';
import { gastroSchema } from '@/components/GastroFormBase/gastroFormSchema';
import LocationEdit from '@/components/LocationEdit';
import { GASTRO } from '@/utils/constants';

const GastroEditPage = () => (
  <LocationEdit
    type={GASTRO}
    label="Gastro"
    locationForm={GastroFormBase}
    locationFormSchema={gastroSchema}
  />
);

export default GastroEditPage;
