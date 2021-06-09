import * as Yup from 'yup';
import {
  testDateString,
  testTimeString,
  veganValues,
} from '../GastroFormBase/formSchema';

export const OPENING_HOURS_DAYS = [
  'monday',
  'tuesday',
  'wednesday',
  'thursday',
  'friday',
  'saturday',
  'sunday',
];

const openingHoursDaySchema = Yup.object().shape({
  opening: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  closing: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
});

const buildSchemaObject = (keyList: Array<string>, type: Yup.BaseSchema) =>
  keyList.reduce((obj, key) => ({ ...obj, [key]: type }), {});

export const BASE_BOOLEAN_ATTRIBUTES = [
  'organic',
  'delivery',
  'handicappedAccessible',
];

export const booleanAttributeSchema = (attrList: Array<string>) =>
  attrList.reduce(
    (obj, key) => ({ ...obj, [key]: Yup.boolean().nullable() }),
    {},
  );

const locationBaseSchema = Yup.object().shape({
  name: Yup.string().max(100).required(),
  street: Yup.string().max(100).required(),
  postalCode: Yup.string().min(5).max(5).required(),
  city: Yup.string().max(20).required(),
  latitude: Yup.number().required(),
  longitude: Yup.number().required(),
  telephone: Yup.string().max(25).nullable(),
  website: Yup.string().url().nullable(),
  email: Yup.string().email().nullable(),
  vegan: Yup.number().oneOf(veganValues).required(),
  comment: Yup.string(),
  commentEnglish: Yup.string(),
  commentOpeningHours: Yup.string(),
  reviewLink: Yup.string().url().nullable(),
  closed: Yup.string()
    .test('testDateString', 'Date invalid', testDateString)
    .nullable(),
  textIntern: Yup.string().nullable(),
  publicTransport: Yup.string().nullable(),
  submitEmail: Yup.string().email().nullable(),
  hasSticker: Yup.boolean(),
  isSubmission: Yup.boolean(),
  openingHours: Yup.object().shape(
    buildSchemaObject(OPENING_HOURS_DAYS, openingHoursDaySchema),
  ),
  attributes: Yup.object().shape(
    booleanAttributeSchema(BASE_BOOLEAN_ATTRIBUTES),
  ),
  tags: Yup.array().of(Yup.string()),
});

export default locationBaseSchema;
