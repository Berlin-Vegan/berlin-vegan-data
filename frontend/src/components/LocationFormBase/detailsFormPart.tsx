import MuiAlert from '@mui/material/Alert';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Typography from '@mui/material/Typography';

import { Field, type FieldProps, useField } from 'formik';

import ReviewFormControl from './fields/ReviewFormControl';

const DetailsFormPart = () => {
  const [, reviewMeta] = useField('review');
  const reviewEmpty = reviewMeta.value === '' || reviewMeta.value == null;

  return (
    <div>
      <Grid>
        <Typography variant="h5">Details</Typography>
      </Grid>
      {reviewEmpty ? null : (
        <MuiAlert elevation={6} variant="filled" severity="info" sx={{ mt: 1.25, mb: 1.25 }}>
          The text of the review will be used.
        </MuiAlert>
      )}
      <Grid container spacing={1}>
        <Grid size={6}>
          <Field name="comment">
            {({ field, meta }: FieldProps) => (
              <TextField
                {...field}
                type="text"
                label="Comment in German"
                variant="standard"
                multiline
                rows={10}
                fullWidth
                error={meta.touched && Boolean(meta.error)}
                helperText={meta.touched && meta.error}
              />
            )}
          </Field>
        </Grid>
        <Grid size={6}>
          <Field name="commentEnglish">
            {({ field, meta }: FieldProps) => (
              <TextField
                {...field}
                type="text"
                label="Comment in English"
                variant="standard"
                multiline
                rows={10}
                fullWidth
                error={meta.touched && Boolean(meta.error)}
                helperText={meta.touched && meta.error}
              />
            )}
          </Field>
        </Grid>
      </Grid>
      <Grid container spacing={1}>
        <Grid size={6}>
          <Field name="commentOpeningHours">
            {({ field, meta }: FieldProps) => (
              <TextField
                {...field}
                type="text"
                label="Comment Opening Hours"
                variant="standard"
                multiline
                rows={10}
                fullWidth
                error={meta.touched && Boolean(meta.error)}
                helperText={meta.touched && meta.error}
              />
            )}
          </Field>
        </Grid>
        <Grid size={6}>
          <Field name="textIntern">
            {({ field, meta }: FieldProps) => (
              <TextField
                {...field}
                type="text"
                label="Text Intern"
                variant="standard"
                multiline
                rows={10}
                fullWidth
                error={meta.touched && Boolean(meta.error)}
                helperText={meta.touched && meta.error}
              />
            )}
          </Field>
        </Grid>
      </Grid>
      <Grid container spacing={1}>
        <Grid size={6}>
          <Field name="commentPublicTransport">
            {({ field, meta }: FieldProps) => (
              <TextField
                {...field}
                type="text"
                label="Public Transport"
                variant="standard"
                fullWidth
                error={meta.touched && Boolean(meta.error)}
                helperText={meta.touched && meta.error}
              />
            )}
          </Field>
        </Grid>
        <Grid size={6}>
          <ReviewFormControl />
        </Grid>
      </Grid>
    </div>
  );
};

export default DetailsFormPart;
