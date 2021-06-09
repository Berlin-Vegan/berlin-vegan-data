import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { Field } from 'formik';
import BVKeyboardTimePicker from '../GastroFormBase/fields/KeyboardTimePicker';
import { OPENING_HOURS_DAYS } from './formSchema';
import useStyles from './styles';

const buildName = (day: string, key: string) => `openingHours.${day}.${key}`;

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

const OpeningHoursInput = ({ day }: { day: string }) => {
  const classes = useStyles();

  return (
    <Grid container item direction="column" md={2} key={day}>
      <Grid item>
        <Typography variant="subtitle2" className={classes.capitalizeTitle}>
          {day}
        </Typography>
      </Grid>
      {openingClosingInputs(day)}
    </Grid>
  );
};

const openingHoursFormPart = (
  <>
    <Grid item>
      <Typography variant="h5">Opening Hours</Typography>
    </Grid>
    <Grid container item direction="row" spacing={1} justify="space-between">
      {OPENING_HOURS_DAYS.map((day) => (
        <OpeningHoursInput key={day} day={day} />
      ))}
    </Grid>
  </>
);

export default openingHoursFormPart;
