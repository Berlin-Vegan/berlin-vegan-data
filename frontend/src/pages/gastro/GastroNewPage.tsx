import GastroFormBase from '@/components/GastroFormBase';
import { gastroSchema } from '@/components/GastroFormBase/gastroFormSchema';
import initialGastroData from '@/components/GastroFormBase/initialData';
import LocationBaseFormNew from '@/components/LocationBaseFormNew';
import { GASTRO } from '@/utils/constants';

const GastroNewPage = () => (
  <LocationBaseFormNew
    type={GASTRO}
    label="Gastro"
    locationForm={GastroFormBase}
    locationFormSchema={gastroSchema}
    initialData={initialGastroData}
  />
);

export default GastroNewPage;
