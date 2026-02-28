import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

import { Field } from 'formik';

import BVKeyboardTimePicker from './fields/BVTimePicker';
import { OPENING_HOURS_DAYS } from './formSchema';

const buildName = (day: string, key: string) => `openingHours.${day}.${key}`;

const openingHourField = (day: string, label: string, key: string) => (
  <Field
    component={BVKeyboardTimePicker}
    label={label}
    ampm={false}
    variant="inline"
    name={buildName(day, key)}
    TextFieldProps={{ variant: 'standard' }}
  />
);

const openingClosingInputs = (day: string) => (
  <>
    {openingHourField(day, 'Opens at', 'opening')}
    {openingHourField(day, 'Closes at', 'closing')}
  </>
);

const OpeningHoursInput = ({ day }: { day: string }) => {
  return (
    <Grid container direction="column" key={day}>
      <Typography sx={{ textTransform: 'capitalize' }}>{day}</Typography>
      {openingClosingInputs(day)}
    </Grid>
  );
};

const OpeningHoursFormPart = (
  <>
    <Grid>
      <Typography variant="h5">Opening Hours</Typography>
    </Grid>
    <Grid container spacing={1}>
      {OPENING_HOURS_DAYS.map((day) => (
        <OpeningHoursInput key={day} day={day} />
      ))}
    </Grid>
  </>
);

export default OpeningHoursFormPart;
