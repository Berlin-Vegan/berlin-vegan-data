import { TimePicker as MuiTimePicker } from '@mui/x-date-pickers';

import dayjs from 'dayjs';
import customParseFormat from 'dayjs/plugin/customParseFormat';
import { TimePickerProps, fieldToTimePicker } from 'formik-mui-x-date-pickers';

dayjs.extend(customParseFormat);

const timeToStringOrNull = (date: Date | null): string | null =>
  date === null ? null : dayjs(date).format('HH:mm:ss');

const stringToDate = (stringTime: string | null): Date | string =>
  stringTime === null ? '' : dayjs(stringTime, 'HH:mm:ss').toDate();

const BVTimePicker = ({ children, ...props }: TimePickerProps) => {
  const {
    form: { setFieldValue, setFieldTouched },
    field: { name },
  } = props;
  const handleChange = (date: Date | null) => {
    setFieldTouched(name, true, false);
    setFieldValue(name, timeToStringOrNull(date), true);
  };

  return (
    <MuiTimePicker
      {...fieldToTimePicker({
        ...props,
        field: { ...props.field, value: stringToDate(props.field.value) },
      })}
      onChange={handleChange}
    >
      {children}
    </MuiTimePicker>
  );
};

BVTimePicker.displayName = 'BVTimePicker';

export default BVTimePicker;
