import * as Yup from 'yup';
import locationBaseSchema, {
  BASE_BOOLEAN_ATTRIBUTES,
  booleanAttributeSchema,
  buildAttributeSchema,
} from '../LocationFormBase/formSchema';

export const GASTRO_TAGS = [
  'bar',
  'cafe',
  'ice cream parlor',
  'snack bar',
  'restaurant',
];

const gastroTagType = Yup.string().oneOf(GASTRO_TAGS);

export const GASTRO_BOOLEAN_ATTRIBUTES = [
  ...BASE_BOOLEAN_ATTRIBUTES,
  'handicappedAccessibleWc',
  'dog',
  'childChair',
  'catering',
  'wlan',
  'glutenFree',
  'breakfast',
  'brunch',
];

export const GASTRO_POSITIVE_INTEGER_ATTRIBUTES = [
  'seatsOutdoor',
  'seatsIndoor',
];

export const positiveIntegerAttributeSchema = (attrList: Array<string>) =>
  buildAttributeSchema(attrList, Yup.number().default(0).min(0));

export const gastroSchema = locationBaseSchema.shape({
  tags: Yup.array().of(gastroTagType),
  attributes: Yup.object()
    .shape(booleanAttributeSchema(GASTRO_BOOLEAN_ATTRIBUTES))
    .shape(positiveIntegerAttributeSchema(GASTRO_POSITIVE_INTEGER_ATTRIBUTES)),
});
