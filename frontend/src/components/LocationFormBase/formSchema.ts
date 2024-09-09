import * as Yup from 'yup';

export const OPENING_HOURS_DAYS = [
  'monday',
  'tuesday',
  'wednesday',
  'thursday',
  'friday',
  'saturday',
  'sunday',
];

export const testTimeString = (value: string | null | undefined): boolean =>
  value === null || (value !== undefined && /([01]\d|2[0-3]):([0-5]\d):([0-5]\d)/.test(value));

const testDateString = (value: string | null | undefined): boolean =>
  value === null ||
  (value !== undefined && /([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/.test(value));

const openingHoursDaySchema = Yup.object().shape({
  opening: Yup.string().test('testTimeString', 'Time invalid', testTimeString).nullable(),
  closing: Yup.string().test('testTimeString', 'Time invalid', testTimeString).nullable(),
});

const buildSchemaObject = (keyList: Array<string>, type: Yup.AnySchema) =>
  keyList.reduce((obj, key) => ({ ...obj, [key]: type }), {});

export const BASE_BOOLEAN_ATTRIBUTES = ['organic', 'delivery', 'handicappedAccessible'];

export const buildAttributeSchema = (attrList: Array<string>, attrType: Yup.AnySchema) =>
  attrList.reduce((obj, key) => ({ ...obj, [key]: attrType }), {});

export const booleanAttributeSchema = (attrList: Array<string>) =>
  buildAttributeSchema(attrList, Yup.boolean().nullable());

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
  vegan: Yup.number().oneOf([5, 4, 2]).required(),
  comment: Yup.string(),
  commentEnglish: Yup.string(),
  commentOpeningHours: Yup.string(),
  commentPublicTransport: Yup.string(),
  reviewLink: Yup.string().url().nullable(),
  closed: Yup.string().test('testDateString', 'Date invalid', testDateString).nullable(),
  textIntern: Yup.string().nullable(),
  publicTransport: Yup.string().nullable(),
  submitEmail: Yup.string().email().nullable(),
  hasSticker: Yup.boolean(),
  isSubmission: Yup.boolean(),
  openingHours: Yup.object().shape(buildSchemaObject(OPENING_HOURS_DAYS, openingHoursDaySchema)),
  attributes: Yup.object().shape(booleanAttributeSchema(BASE_BOOLEAN_ATTRIBUTES)),
  tags: Yup.array().of(Yup.string()),
  review: Yup.number().nullable(),
});

export default locationBaseSchema;
