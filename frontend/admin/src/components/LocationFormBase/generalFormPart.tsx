import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { Field } from 'formik';
import { TextField } from 'formik-material-ui';
import { makeStyles } from '@material-ui/core/styles';
import MapFormPart from '../GastroFormBase/mapFormPart';
import NullTextField from '../GastroFormBase/fields/NullTextField';
import veganFormControl from '../GastroFormBase/fields/VeganFormControl';
import GetGeoButton from '../GastroFormBase/getGeoButton';
import BVKeyboardDatePicker from '../GastroFormBase/fields/KeyboardDatePicker';

const useStyles = makeStyles((theme) => ({
  gridGeoClosed: {
    marginTop: '6px',
  },
}));

const GeneralFormPart = () => {
  const classes = useStyles();

  return (
    <>
      <Grid item>
        <Typography variant="h5">General</Typography>
      </Grid>
      <Grid container item spacing={1}>
        <Grid container item direction="column" md={4}>
          <Field
            component={TextField}
            name="name"
            type="text"
            label="Name"
            required
          />
          <Field
            component={TextField}
            type="text"
            label="Street"
            name="street"
            required
          />
          <Grid
            container
            item
            spacing={1}
            direction="row"
            justify="space-between"
          >
            <Grid item>
              <Field
                component={TextField}
                type="text"
                label="City"
                name="city"
                required
              />
            </Grid>
            <Grid item>
              <Field
                component={TextField}
                type="text"
                label="Postal Code"
                name="postalCode"
                required
              />
            </Grid>
          </Grid>
        </Grid>
        <Grid container item md={4} direction="column">
          <Grid container item justify="space-between">
            <Field
              component={TextField}
              type="number"
              label="Lat"
              name="latitude"
              required
            />
            <Field
              component={TextField}
              type="number"
              label="Long"
              name="longitude"
              required
            />
          </Grid>
          <Grid container item>
            <MapFormPart />
          </Grid>
        </Grid>
        <Grid container item md={4} direction="column">
          <Field
            component={NullTextField}
            type="email"
            label="Mail"
            name="email"
          />
          <Field
            component={TextField}
            type="tel"
            label="Telephone"
            name="telephone"
          />
          {veganFormControl}
          <Field
            component={NullTextField}
            type="url"
            label="Website"
            name="website"
            placeholder="https://"
          />
          <Grid
            container
            item
            direction="row"
            justify="space-around"
            className={classes.gridGeoClosed}
          >
            <GetGeoButton />
            <Field
              component={BVKeyboardDatePicker}
              clearable="true"
              label="Closed"
              variant="inline"
              name="closed"
              format="MM/dd/yyyy"
            />
          </Grid>
        </Grid>
      </Grid>
    </>
  );
};

export default GeneralFormPart;
