import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

import BVDatePicker from '@components/LocationFormBase/fields/BVDatePicker';
import { Field } from 'formik';
import { TextField } from 'formik-mui';

import NullTextField from './fields/NullTextField';
import GetGeoButton from './getGeoButton';
import MapFormPart from './mapFormPart';
import veganFormControl from '@components/LocationFormBase/fields/VeganFormControl';

const GeneralFormPart = ({ veganOption = false }: { veganOption: boolean }) => {
  return (
    <>
      <Grid item>
        <Typography variant="h5">General</Typography>
      </Grid>
      <Grid container item spacing={1}>
        <Grid container item direction="column" md={4} spacing={1}>
          <Grid container item direction="column">
            <Field
              component={TextField}
              name="name"
              type="text"
              label="Name"
              variant="standard"
              required
            />
          </Grid>
          <Grid container item direction="column">
            <Field
              component={TextField}
              type="text"
              label="Street"
              name="street"
              variant="standard"
              required
            />
          </Grid>
          <Grid container item spacing={1}>
            <Grid item md={6}>
              <Field
                component={TextField}
                type="text"
                label="City"
                name="city"
                variant="standard"
                required
              />
            </Grid>
            <Grid item md={6}>
              <Field
                component={TextField}
                type="text"
                label="Postal Code"
                name="postalCode"
                variant="standard"
                required
              />
            </Grid>
          </Grid>
        </Grid>
        <Grid container item md={4} direction="column">
          <Grid container item spacing={1}>
            <Grid item md={6}>
              <Field
                component={TextField}
                type="number"
                label="Lat"
                name="latitude"
                variant="standard"
                required
              />
            </Grid>
            <Grid item md={6}>
              <Field
                component={TextField}
                type="number"
                label="Long"
                name="longitude"
                variant="standard"
                required
              />
            </Grid>
          </Grid>
          <Grid container item>
            <MapFormPart />
          </Grid>
        </Grid>
        <Grid container item md={4} direction="column" spacing={1}>
          <Grid container item direction="column">
            <Field
              component={NullTextField}
              type="email"
              label="Mail"
              name="email"
              variant="standard"
            />
          </Grid>
          <Grid container item direction="column">
            <Field
              component={TextField}
              type="tel"
              label="Telephone"
              name="telephone"
              variant="standard"
            />
          </Grid>
          {veganOption ? (
            <Grid container item direction="column">
              {veganFormControl}
            </Grid>
          ) : null}
          <Grid container item direction="column">
            <Field
              component={NullTextField}
              type="url"
              label="Website"
              name="website"
              placeholder="https://"
              variant="standard"
            />
          </Grid>
          <Grid container item direction="row" justifyContent="space-around">
            <GetGeoButton />
            <Field
              component={BVDatePicker}
              name="closed"
              label="Closed"
              TextFieldProps={{ variant: 'standard' }}
            />
          </Grid>
        </Grid>
      </Grid>
    </>
  );
};

export default GeneralFormPart;
