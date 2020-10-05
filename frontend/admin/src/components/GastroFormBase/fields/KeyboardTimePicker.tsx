import * as React from 'react';
import {
  KeyboardTimePicker as MuiKeyboardTimePicker,
  KeyboardTimePickerProps as MuiKeyboardTimePickerProps,
} from '@material-ui/pickers';
import {
  fieldToKeyboardTimePicker,
  KeyboardTimePickerProps,
} from 'formik-material-ui-pickers';
import { getHours, getMinutes, parse } from 'date-fns';

export const timeStringToDate = (value: string | null | undefined) => {
  if (typeof value === 'string') {
    return parse(value, 'HH:mm:ss', new Date());
  }
  return value;
};

const withLeadingZero = (value: number): string =>
  value < 10 ? `0${value}` : `${value}`;

const getHoursWithZero = (date: Date) => withLeadingZero(getHours(date));
const getMinutesWithZero = (date: Date) => withLeadingZero(getMinutes(date));

const getTimeString = (date: Date) =>
  `${getHoursWithZero(date)}:${getMinutesWithZero(date)}:00`;

export const dateToTimeString = (date: Date | null): string | null =>
  date !== null ? getTimeString(date) : date;

const fieldToBVKeyboardTimePicker = (
  props: KeyboardTimePickerProps
): MuiKeyboardTimePickerProps =>
  fieldToKeyboardTimePicker({
    ...props,
    field: { ...props.field, value: timeStringToDate(props.field.value) },
  });

const BVKeyboardTimePicker = ({
  children,
  ...props
}: KeyboardTimePickerProps) => {
  const {
    form: { setFieldValue },
    field: { name },
  } = props;
  const onChange = React.useCallback(
    (date) => {
      setFieldValue(name, dateToTimeString(date));
    },
    [setFieldValue, name]
  );

  return (
    <MuiKeyboardTimePicker
      {...fieldToBVKeyboardTimePicker(props)}
      onChange={onChange}
    >
      {children}
    </MuiKeyboardTimePicker>
  );
};

BVKeyboardTimePicker.displayName = 'BVKeyboardTimePicker';

export default BVKeyboardTimePicker;
