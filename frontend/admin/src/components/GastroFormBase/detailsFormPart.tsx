import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { Field } from 'formik';
import { TextField } from 'formik-material-ui';
import { makeStyles } from '@material-ui/core/styles';
import { map } from 'ramda';
import FormControlNoYesUnknown from './fields/SelectFormControl';
import NullTextField from './fields/NullTextField';
import { nthOr } from '../../utils/fp';

const yesNoUnkownList = [
  ['Wheelchair Accessible', 'handicappedAccessible'],
  ['Wheelchair Accessible Toilet', 'handicappedAccessibleWc'],
  ['Dogs Allowed', 'dog'],
  ['High Chair', 'childChair'],
  ['Catering', 'catering'],
  ['Delivery service', 'delivery'],
  ['Organic', 'organic'],
  ['Wi-Fi', 'wlan'],
  ['Gluten-free Options', 'glutenFree'],
  ['Vegan Breakfast', 'breakfast'],
  ['Brunch', 'brunch'],
];

const yesNoUnknownInputs = (label: string, name: string) => (
  <Grid container item direction="column" md={3} key={name}>
    <FormControlNoYesUnknown label={label} name={name} />
  </Grid>
);

const nthOrEmpty = nthOr('');
const createYesNoUnknownInputs = map((entry) =>
  yesNoUnknownInputs(nthOrEmpty(0)(entry), nthOrEmpty(1)(entry))
)(yesNoUnkownList);

const useStyles = makeStyles(() => ({
  textAreaMulti: {
    '& textarea': {
      resize: 'vertical',
    },
  },
}));

const DetailsFormPart = () => {
  const classes = useStyles();

  return (
    <>
      <Grid item>
        <Typography variant="h5">Details</Typography>
      </Grid>
      <Grid container item spacing={1} className={classes.textAreaMulti}>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment in German"
            name="comment"
            multiline={true}
            rows={10}
          />
        </Grid>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment in English"
            name="commentEnglish"
            multiline={true}
            rows={10}
          />
        </Grid>
      </Grid>
      <Grid container item spacing={1} className={classes.textAreaMulti}>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment Opening Hours"
            name="commentOpen"
            multiline={true}
            rows={10}
          />
        </Grid>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Text Intern"
            name="textIntern"
            multiline={true}
            rows={10}
          />
        </Grid>
      </Grid>
      <Grid container item spacing={1}>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Public Transport"
            name="publicTransport"
          />
        </Grid>
        <Grid container item direction="column" md={6}>
          <Field
            component={NullTextField}
            type="text"
            label="Review Link"
            name="reviewLink"
          />
        </Grid>
      </Grid>
      <Grid container item spacing={1}>
        {createYesNoUnknownInputs}
        <Grid container item direction="column" md={3}>
          <Field
            component={TextField}
            type="number"
            label="Seats Outdoor"
            name="seatsOutdoor"
          />
        </Grid>
        <Grid container item direction="column" md={3}>
          <Field
            component={TextField}
            type="number"
            label="Seats Indoor"
            name="seatsIndoor"
          />
        </Grid>
      </Grid>
    </>
  );
};

export default DetailsFormPart;
