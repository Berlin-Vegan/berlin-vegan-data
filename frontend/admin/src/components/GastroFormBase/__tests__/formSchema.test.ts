import GastroDetailValid from './fixtures/GastroDetailVaild.json';
import gastroFormSchema, { testTimeString } from '../formSchema';

test('valid gastro object', () => gastroFormSchema
    .validate(GastroDetailValid)
    .then((result) => expect(result).toBeTruthy()));

test('testTimeString true', () => {
  expect(testTimeString('00:00:00')).toBeTruthy();
  expect(testTimeString('01:01:01')).toBeTruthy();
  expect(testTimeString('10:59:59')).toBeTruthy();
  expect(testTimeString('11:59:59')).toBeTruthy();
  expect(testTimeString('23:59:59')).toBeTruthy();
});

test('testTimeString false', () => {
  expect(testTimeString('00:00')).toBeFalsy();
  expect(testTimeString('01:01-01')).toBeFalsy();
  expect(testTimeString('10:59:60')).toBeFalsy();
  expect(testTimeString('11:60:59')).toBeFalsy();
  expect(testTimeString('24:00:00')).toBeFalsy();
  expect(testTimeString('24:10:10')).toBeFalsy();
});
