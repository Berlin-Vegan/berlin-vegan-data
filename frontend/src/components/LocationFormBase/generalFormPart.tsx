import Grid from '@mui/material/Grid';
import Stack from '@mui/material/Stack';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';

import BVDatePicker from '@components/LocationFormBase/fields/BVDatePicker';
import { Field, type FieldProps } from 'formik';

import NullTextField from './fields/NullTextField';
import GetGeoButton from './getGeoButton';
import MapFormPart from './mapFormPart';

const GeneralFormPart = () => {
  return (
    <>
      <Grid>
        <Typography variant="h5">General</Typography>
      </Grid>
      <Grid container spacing={1}>
        <Grid container direction="column" spacing={1} size={4}>
          <Grid container direction="column">
            <Field name="name">
              {({ field, meta }: FieldProps) => (
                <TextField
                  {...field}
                  type="text"
                  label="Name"
                  variant="standard"
                  required
                  error={meta.touched && Boolean(meta.error)}
                  helperText={meta.touched && meta.error}
                />
              )}
            </Field>
          </Grid>
          <Grid container direction="column">
            <Field name="street">
              {({ field, meta }: FieldProps) => (
                <TextField
                  {...field}
                  type="text"
                  label="Street"
                  variant="standard"
                  required
                  error={meta.touched && Boolean(meta.error)}
                  helperText={meta.touched && meta.error}
                />
              )}
            </Field>
          </Grid>
          <Grid container spacing={1}>
            <Grid container size={6}>
              <Field name="city">
                {({ field, meta }: FieldProps) => (
                  <TextField
                    {...field}
                    type="text"
                    label="City"
                    variant="standard"
                    required
                    error={meta.touched && Boolean(meta.error)}
                    helperText={meta.touched && meta.error}
                    fullWidth
                  />
                )}
              </Field>
            </Grid>
            <Grid container size={6}>
              <Field name="postalCode">
                {({ field, meta }: FieldProps) => (
                  <TextField
                    {...field}
                    type="text"
                    label="Postal Code"
                    variant="standard"
                    required
                    error={meta.touched && Boolean(meta.error)}
                    helperText={meta.touched && meta.error}
                    fullWidth
                  />
                )}
              </Field>
            </Grid>
          </Grid>
        </Grid>
        <Grid container direction="column" size={4}>
          <Grid container spacing={1}>
            <Grid container size={6}>
              <Field name="latitude">
                {({ field, meta }: FieldProps) => (
                  <TextField
                    {...field}
                    type="number"
                    label="Lat"
                    variant="standard"
                    required
                    error={meta.touched && Boolean(meta.error)}
                    helperText={meta.touched && meta.error}
                    fullWidth
                  />
                )}
              </Field>
            </Grid>
            <Grid container size={6}>
              <Field name="longitude">
                {({ field, meta }: FieldProps) => (
                  <TextField
                    {...field}
                    type="number"
                    label="Long"
                    variant="standard"
                    required
                    error={meta.touched && Boolean(meta.error)}
                    helperText={meta.touched && meta.error}
                    fullWidth
                  />
                )}
              </Field>
            </Grid>
          </Grid>
          <Grid container size={12}>
            <MapFormPart />
          </Grid>
        </Grid>
        <Grid container spacing={1} size={4}>
          <Stack sx={{ width: '100%', justifyContent: 'space-between' }}>
            <Stack>
              <Field
                component={NullTextField}
                type="email"
                label="Mail"
                name="email"
                variant="standard"
              />
              <Field name="telephone">
                {({ field, meta }: FieldProps) => (
                  <TextField
                    {...field}
                    type="tel"
                    label="Telephone"
                    variant="standard"
                    error={meta.touched && Boolean(meta.error)}
                    helperText={meta.touched && meta.error}
                  />
                )}
              </Field>
              <Field
                component={NullTextField}
                type="url"
                label="Website"
                name="website"
                placeholder="https://"
                variant="standard"
              />
              <Field
                component={BVDatePicker}
                name="closed"
                label="Closed"
                TextFieldProps={{ variant: 'standard' }}
              />
            </Stack>
            <Stack sx={{ marginTop: 'min(15px)' }}>
              <GetGeoButton />
            </Stack>
          </Stack>
        </Grid>
      </Grid>
    </>
  );
};

export default GeneralFormPart;
