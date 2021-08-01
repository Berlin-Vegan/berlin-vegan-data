import React, { FC } from 'react';
import { Field, Form, Formik } from 'formik';

import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import MockDate from 'mockdate';
import FormControlNoYesUnknown, {
  booleanToString,
  stringToBoolean,
} from '../fields/SelectFormControl';
import { standardComponentTest } from '../../../utils/testing';
import NullTextField, {
  emptyStringToNull,
  nullToEmptyString,
} from '../fields/NullTextField';
import BVKeyboardTimePicker, {
  dateToTimeString,
  timeStringToDate,
} from '../fields/KeyboardTimePicker';
import BVKeyboardDatePicker, {
  dateStringToDate,
  dateToDateString,
} from '../fields/KeyboardDatePicker';

beforeEach(() => {
  MockDate.set('2000-11-22');
});

afterEach(() => {
  MockDate.reset();
});

test('null value is empty string nullToEmptyString', () => {
  const result = nullToEmptyString(null);
  expect(result).toBe('');
});

test('empty string is null emptyStringToNull', () => {
  const result = emptyStringToNull('');
  expect(result).toBe(null);
});

type WrapperProps = {
  initial: object;
};

export const Wrapper: FC<WrapperProps> = ({ children, initial = {} }) => (
  <Formik initialValues={initial} onSubmit={() => {}}>
    <Form>{children}</Form>
  </Formik>
);

const NullTextFieldWrapper = (initial: object) => (
  <Wrapper initial={initial}>
    <Field component={NullTextField} name="test" label="Test" />
  </Wrapper>
);

standardComponentTest(NullTextFieldWrapper, {});
standardComponentTest(NullTextFieldWrapper, { test: null });
standardComponentTest(NullTextFieldWrapper, { test: '' });
standardComponentTest(NullTextFieldWrapper, { test: 'erdfcv' });

test('string to bool|null stringToBoolean', () => {
  const resultYes = stringToBoolean('yes');
  expect(resultYes).toBeTruthy();

  const resultNo = stringToBoolean('no');
  expect(resultNo).toBeFalsy();

  const resultUnknown = stringToBoolean('unknown');
  expect(resultUnknown).toBeNull();
});

test('bool|null to string booleanToString', () => {
  const resultTrue = booleanToString(true);
  expect(resultTrue).toBe('yes');

  const resultFalse = booleanToString(false);
  expect(resultFalse).toBe('no');

  const resultNull = booleanToString(null);
  expect(resultNull).toBe('unknown');
});

const FormControlNoYesUnknownWrapper = (initial: object) => (
  <Wrapper initial={initial}>
    <FormControlNoYesUnknown label="Test" name="test" />
  </Wrapper>
);

standardComponentTest(FormControlNoYesUnknownWrapper, {});
standardComponentTest(FormControlNoYesUnknownWrapper, { test: null });
standardComponentTest(FormControlNoYesUnknownWrapper, { test: true });
standardComponentTest(FormControlNoYesUnknownWrapper, { test: false });

test('string to date|null|undefined timeStringToDate', () => {
  const resultNaNDate = timeStringToDate('');
  expect(resultNaNDate).not.toBeNull();
  expect(resultNaNDate).not.toBeUndefined();

  const resultDate = timeStringToDate('11:00:00');
  expect(resultDate).toStrictEqual(new Date('2000-11-22T11:00:00.000'));

  const resultNull = timeStringToDate(null);
  expect(resultNull).toBeNull();
});

test('date to string dateToTimeString', () => {
  const resultTimeString = dateToTimeString(
    new Date('2000-11-22T04:01:00.000'),
  );
  expect(resultTimeString).toStrictEqual('04:01:00');

  const resultNull = dateToTimeString(null);
  expect(resultNull).toBeNull();
});

const BVKeyboardTimePickerWrapper = (initial: object) => (
  <MuiPickersUtilsProvider utils={DateFnsUtils}>
    <Wrapper initial={initial}>
      <Field component={BVKeyboardTimePicker} name="test" label="Test" />
    </Wrapper>
  </MuiPickersUtilsProvider>
);

standardComponentTest(BVKeyboardTimePickerWrapper, { test: null });
standardComponentTest(BVKeyboardTimePickerWrapper, { test: '12:00:00' });

test('string to date|null|undefined dateStringToDate', () => {
  const resultNaNDate = dateStringToDate('');
  expect(resultNaNDate).not.toBeNull();
  expect(resultNaNDate).not.toBeUndefined();

  const resultString = dateStringToDate('2019-11-01');
  expect(resultString).toStrictEqual(new Date('2019-11-01T00:00:00.000'));

  const resultNull = dateStringToDate(null);
  expect(resultNull).toBeNull();
});

test('date to string dateToDateString', () => {
  const resultEmptyString = dateToDateString(
    new Date('2019-11-01T23:00:00.000'),
  );
  expect(resultEmptyString).toStrictEqual('2019-11-01');

  const resultNull = dateToDateString(null);
  expect(resultNull).toBeNull();
});

const BVKeyboardDatePickerWrapper = (initial: object) => (
  <MuiPickersUtilsProvider utils={DateFnsUtils}>
    <Wrapper initial={initial}>
      <Field component={BVKeyboardDatePicker} name="test" label="Test" />
    </Wrapper>
  </MuiPickersUtilsProvider>
);

standardComponentTest(BVKeyboardDatePickerWrapper);
standardComponentTest(BVKeyboardDatePickerWrapper, { test: null });
standardComponentTest(BVKeyboardDatePickerWrapper, { test: undefined });
standardComponentTest(BVKeyboardDatePickerWrapper, { test: '2019-11-01' });
