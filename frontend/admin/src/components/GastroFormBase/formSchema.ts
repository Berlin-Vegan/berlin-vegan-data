import * as Yup from 'yup';
import { map } from 'ramda';
import { nthOr } from '../../utils/fp';
import { veganFieldOptions } from './fields/constants';

export const veganValues = map((item) => nthOr(0, 0)(item))(veganFieldOptions);

export const testTimeString = (value: string | null | undefined): boolean =>
  value === null ||
  (value !== undefined && /([01]\d|2[0-3]):([0-5]\d):([0-5]\d)/.test(value));

export const testDateString = (value: string | null | undefined): boolean =>
  value === null ||
  (value !== undefined &&
    /([12]\d{3}-(0[1-9]|1[0-2])-(0[1-9]|[12]\d|3[01]))/.test(value));

const gastroFormSchema = Yup.object().shape({
  name: Yup.string().max(100).required(),
  street: Yup.string().max(100).required(),
  postalCode: Yup.string().min(5).max(5).required(),
  city: Yup.string().max(20).required(),
  latitude: Yup.number().required(),
  longitude: Yup.number().required(),
  telephone: Yup.string().max(25).nullable(),
  website: Yup.string().url().nullable(),
  email: Yup.string().email().nullable(),
  openingMon: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  closingMon: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  openingTue: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  closingTue: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  openingWed: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  closingWed: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  openingThu: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  closingThu: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  openingFri: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  closingFri: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  openingSat: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  closingSat: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  openingSun: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  closingSun: Yup.string()
    .test('testTimeString', 'Time invalid', testTimeString)
    .nullable(),
  vegan: Yup.number().oneOf(veganValues).required(),
  comment: Yup.string(),
  commentEnglish: Yup.string(),
  commentOpen: Yup.string(),
  reviewLink: Yup.string().url().nullable(),
  closed: Yup.string()
    .test('testDateString', 'Date invalid', testDateString)
    .nullable(),
  textIntern: Yup.string().nullable(),
  district: Yup.string().required(),
  publicTransport: Yup.string().nullable(),
  handicappedAccessible: Yup.boolean().nullable(),
  handicappedAccessibleWc: Yup.boolean().nullable(),
  dog: Yup.boolean().nullable(),
  childChair: Yup.boolean().nullable(),
  catering: Yup.boolean().nullable(),
  delivery: Yup.boolean().nullable(),
  organic: Yup.boolean().nullable(),
  wlan: Yup.boolean().nullable(),
  glutenFree: Yup.boolean().nullable(),
  brunch: Yup.boolean().nullable(),
  seatsOutdoor: Yup.number().integer().nullable(),
  seatsIndoor: Yup.number().integer().nullable(),
  restaurant: Yup.boolean().required(),
  imbiss: Yup.boolean().required(),
  eiscafe: Yup.boolean().required(),
  cafe: Yup.boolean().required(),
  bar: Yup.boolean().required(),
  submitEmail: Yup.string().email().nullable(),
  hasSticker: Yup.boolean(),
  isSubmission: Yup.boolean(),
});

export default gastroFormSchema;
