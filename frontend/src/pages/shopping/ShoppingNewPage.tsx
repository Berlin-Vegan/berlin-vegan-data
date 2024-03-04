import LocationBaseFormNew from '@/components/LocationBaseFormNew';
import ShoppingFormBase from '@/components/ShoppingFormBase';
import initialShoppingData from '@/components/ShoppingFormBase/initialData';
import { shoppingSchema } from '@/components/ShoppingFormBase/shoppingFormSchema';
import { SHOPPING } from '@/utils/constants';

const ShoppingNewPage = () => (
  <LocationBaseFormNew
    type={SHOPPING}
    label="Shopping"
    locationForm={ShoppingFormBase}
    locationFormSchema={shoppingSchema}
    initialData={initialShoppingData}
  />
);

export default ShoppingNewPage;
