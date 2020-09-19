import * as React from 'react';
import {
  KeyboardDatePicker as MuiKeyboardDatePicker,
  KeyboardDatePickerProps as MuiKeyboardDatePickerProps,
} from '@material-ui/pickers';
import {
  fieldToKeyboardDatePicker,
  KeyboardDatePickerProps,
} from 'formik-material-ui-pickers';
import { format, parse } from 'date-fns';

const dateFormat = 'yyyy-MM-dd';

export const dateStringToDate = (value: string | null | undefined) => {
  if (typeof value === 'string') {
    const date = parse(value, dateFormat, new Date());
    return isNaN(date.getTime()) ? new Date() : date;
  }
  return value;
};

export const dateToDateString = (value: Date | null): string | null =>
  value !== null ? format(value, dateFormat) : value;

const fieldToBVKeyboardDatePicker = (
  props: KeyboardDatePickerProps
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
    [setFieldValue, name]
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
