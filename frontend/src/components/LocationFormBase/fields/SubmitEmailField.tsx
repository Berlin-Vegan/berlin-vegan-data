import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';

import { Field, type FieldProps, useField } from 'formik';

const buildField = (
  <Grid>
    <Field name="submitEmail">
      {({ field, meta }: FieldProps) => (
        <TextField
          {...field}
          type="text"
          label="Submit Email"
          required
          error={meta.touched && Boolean(meta.error)}
          helperText={meta.touched && meta.error}
        />
      )}
    </Field>
  </Grid>
);

const SubmitEmailField = () => {
  const [, { value }] = useField('submitEmail');
  return value ? buildField : null;
};

export default SubmitEmailField;
