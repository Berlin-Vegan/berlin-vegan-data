import { DatePicker as MuiDatePicker } from '@mui/x-date-pickers/DatePicker';

import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { DatePickerProps, fieldToDatePicker } from 'formik-mui-x-date-pickers';

dayjs.extend(customParseFormat);

const dateToStringOrNull = (date: Date | null): string | null =>
  date === null ? null : dayjs(date).format('YYYY-MM-DD');

const stringToDate = (stringDate: string | null): Date | string =>
  stringDate === null ? '' : dayjs(stringDate, 'YYYY-MM-DD').toDate();

const BVDatePicker = ({ children, ...props }: DatePickerProps) => {
  const {
    form: { setFieldValue, setFieldTouched },
    field: { name },
  } = props;

  const handleChange = (date: Date | null) => {
    setFieldTouched(name, true, false);
    setFieldValue(name, dateToStringOrNull(date), true);
  };

  return (
    <MuiDatePicker
      {...fieldToDatePicker({
        ...props,
        field: { ...props.field, value: stringToDate(props.field.value) },
      })}
      onChange={handleChange}
      textField={{ variant: 'standard' }}
    >
      {children}
    </MuiDatePicker>
  );
};

BVDatePicker.displayName = 'BVDatePicker';

export default BVDatePicker;
