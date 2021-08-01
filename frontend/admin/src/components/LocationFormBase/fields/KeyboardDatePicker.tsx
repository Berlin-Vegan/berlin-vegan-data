import * as React from 'react';
import {
  KeyboardDatePicker as MuiKeyboardDatePicker,
  KeyboardDatePickerProps as MuiKeyboardDatePickerProps,
} from '@material-ui/pickers';
import {
  fieldToKeyboardDatePicker,
  KeyboardDatePickerProps,
} from 'formik-material-ui-pickers';
import { getDate, getMonth, getYear, parseISO } from 'date-fns';
import { withLeadingZero } from './utils';

export const dateStringToDate = (value: string | null | undefined) => {
  if (typeof value === 'string') {
    return parseISO(value);
  }
  return value;
};

const getMonthWithZero = (date: Date) => withLeadingZero(getMonth(date) + 1);
const getDayWithZero = (date: Date) => withLeadingZero(getDate(date));
const getDateString = (date: Date) =>
  `${getYear(date)}-${getMonthWithZero(date)}-${getDayWithZero(date)}`;

export const dateToDateString = (date: Date | null): string | null =>
  date !== null ? getDateString(date) : date;

const fieldToBVKeyboardDatePicker = (
  props: KeyboardDatePickerProps,
): MuiKeyboardDatePickerProps =>
  fieldToKeyboardDatePicker({
    ...props,
    field: { ...props.field, value: dateStringToDate(props.field.value) },
  });

const BVKeyboardDatePicker = ({
  children,
  ...props
}: KeyboardDatePickerProps) => {
  const {
    form: { setFieldValue },
    field: { name },
  } = props;
  const onChange = React.useCallback(
    (date) => {
      setFieldValue(name, dateToDateString(date));
    },
    [setFieldValue, name],
  );

  return (
    <MuiKeyboardDatePicker
      {...fieldToBVKeyboardDatePicker(props)}
      onChange={onChange}
    >
      {children}
    </MuiKeyboardDatePicker>
  );
};

BVKeyboardDatePicker.displayName = 'BVKeyboardDatePicker';

export default BVKeyboardDatePicker;
