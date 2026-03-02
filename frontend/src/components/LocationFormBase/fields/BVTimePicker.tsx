import type { SxProps } from '@mui/material/styles';
import { TimePicker as MuiTimePicker } from '@mui/x-date-pickers/TimePicker';

import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';

dayjs.extend(customParseFormat);

type BVTimePickerProps = {
  field: { name: string; value: string | null };
  form: {
    setFieldValue: (field: string, value: unknown, shouldValidate?: boolean) => void;
    setFieldTouched: (field: string, isTouched?: boolean, shouldValidate?: boolean) => void;
  };
  label?: string;
  inputFormat?: string;
  TextFieldProps?: Record<string, unknown>;
  sx?: SxProps;
};

const timeToStringOrNull = (
  value: dayjs.Dayjs | Date | string | null | undefined,
): string | null => {
  if (value == null) return null;
  const d = dayjs(value);
  return d.isValid() ? d.format('HH:mm:ss') : null;
};

const stringToDayjsOrNull = (stringTime: string | null) =>
  stringTime == null || stringTime === '' ? null : dayjs(stringTime, 'HH:mm:ss');

const BVTimePicker = ({
  field,
  form,
  label,
  inputFormat = 'HH:mm',
  TextFieldProps,
  sx,
}: BVTimePickerProps) => {
  const { name, value } = field;

  const handleChange = (newValue: dayjs.Dayjs | null) => {
    form.setFieldTouched(name, true, false);
    form.setFieldValue(name, timeToStringOrNull(newValue), true);
  };

  const helperSlotProps = TextFieldProps ? (TextFieldProps as Record<string, unknown>) : {};

  return (
    <MuiTimePicker
      label={label}
      value={stringToDayjsOrNull(value)}
      onChange={handleChange}
      sx={sx}
      slotProps={{ textField: { variant: 'standard', ...helperSlotProps } }}
      format={inputFormat}
    />
  );
};

BVTimePicker.displayName = 'BVTimePicker';

export default BVTimePicker;
