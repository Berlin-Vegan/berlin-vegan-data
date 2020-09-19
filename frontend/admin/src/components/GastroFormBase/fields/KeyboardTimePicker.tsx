import * as React from 'react';
import {
  KeyboardTimePicker as MuiKeyboardTimePicker,
  KeyboardTimePickerProps as MuiKeyboardTimePickerProps,
} from '@material-ui/pickers';
import {
  fieldToKeyboardTimePicker,
  KeyboardTimePickerProps,
} from 'formik-material-ui-pickers';
import { format, parse } from 'date-fns';

export const timeStringToDate = (value: string | null | undefined) => {
  if (typeof value === 'string') {
    const date = parse(value, 'HH:mm:ss', new Date());
    return isNaN(date.getTime()) ? new Date() : date;
  }
  return value;
};

export const dateToTimeString = (value: Date | null): string | null =>
  value !== null ? `${format(value, 'HH:mm')}:00` : value;

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
