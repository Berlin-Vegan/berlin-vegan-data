import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { Field } from 'formik';
import BVKeyboardTimePicker from './fields/KeyboardTimePicker';

const openHoursList = [
  'Monday',
  'Tuesday',
  'Wednesday',
  'Thursday',
  'Friday',
  'Saturday',
  'Sunday',
];

const sliceDay = (day: string) => day.slice(0, 3);
const buildName = (day: string, key: string) => `${key}${sliceDay(day)}`;

const openingHourField = (day: string, label: string, key: string) => (
  <Field
    component={BVKeyboardTimePicker}
    label={label}
    ampm={false}
    variant="inline"
    name={buildName(day, key)}
  />
);

const openingClosingInputs = (day: string) => (
  <>
    {openingHourField(day, 'Opens at', 'opening')}
    {openingHourField(day, 'Closes at', 'closing')}
  </>
);

const openingHoursInput = (day: string) => (
  <Grid container item direction="column" md={2} key={day}>
    <Grid item>
      <Typography variant="subtitle2">{day}</Typography>
    </Grid>
    {openingClosingInputs(day)}
  </Grid>
);

const openingHoursFormPart = (
  <>
    <Grid item>
      <Typography variant="h5">Opening Hours</Typography>
    </Grid>
    <Grid container item direction="row" spacing={1} justify="space-between">
      {openHoursList.map((day) => openingHoursInput(day))}
    </Grid>
  </>
);

export default openingHoursFormPart;
