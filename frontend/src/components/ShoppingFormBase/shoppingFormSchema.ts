import * as Yup from 'yup';
import locationBaseSchema, {
  BASE_BOOLEAN_ATTRIBUTES,
  booleanAttributeSchema,
} from '../LocationFormBase/formSchema';

export const SHOPPING_TAGS = [
  'foods',
  'clothing',
  'toiletries',
  'supermarket',
  'hairdressers',
  'sports',
  'tattoostudio',
  'accommodation',
];

const shoppingTagType = Yup.string().oneOf(SHOPPING_TAGS);

export const SHOPPING_BOOLEAN_ATTRIBUTES = [
  ...BASE_BOOLEAN_ATTRIBUTES,
  'webshop',
];

export const shoppingSchema = locationBaseSchema.shape({
  tags: Yup.array().of(shoppingTagType),
  attributes: Yup.object().shape(
    booleanAttributeSchema(SHOPPING_BOOLEAN_ATTRIBUTES),
  ),
});
