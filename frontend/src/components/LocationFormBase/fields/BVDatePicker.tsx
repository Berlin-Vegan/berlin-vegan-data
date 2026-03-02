import type { SxProps } from '@mui/material/styles';
import { DatePicker as MuiDatePicker } from '@mui/x-date-pickers/DatePicker';

import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';

dayjs.extend(customParseFormat);

type BVDatePickerProps = {
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

const dateToStringOrNull = (
  date: dayjs.Dayjs | Date | string | null | undefined,
): string | null => {
  if (date == null) return null;
  const d = dayjs(date);
  return d.isValid() ? d.format('YYYY-MM-DD') : null;
};

const stringToDayjsOrNull = (stringDate: string | null) =>
  stringDate == null || stringDate === '' ? null : dayjs(stringDate, 'YYYY-MM-DD');

const BVDatePicker = ({
  field,
  form,
  label,
  inputFormat = 'DD.MM.YYYY',
  TextFieldProps,
  sx,
}: BVDatePickerProps) => {
  const { name, value } = field;

  const handleChange = (newValue: dayjs.Dayjs | null) => {
    form.setFieldTouched(name, true, false);
    form.setFieldValue(name, dateToStringOrNull(newValue), true);
  };

  const helperSlotProps = TextFieldProps ? (TextFieldProps as Record<string, unknown>) : {};

  return (
    <MuiDatePicker
      label={label}
      value={stringToDayjsOrNull(value)}
      onChange={handleChange}
      sx={sx}
      slotProps={{ textField: { variant: 'standard', ...helperSlotProps } }}
      format={inputFormat}
    />
  );
};

BVDatePicker.displayName = 'BVDatePicker';

export default BVDatePicker;
