import React from 'react';
import { Field, useField } from 'formik';
import { TextField } from 'formik-material-ui';
import Grid from '@material-ui/core/Grid';

const buildField = (
  <Grid item>
    <Field
      component={TextField}
      name="submitEmail"
      type="text"
      label="Submit Email"
      required
    />
  </Grid>
);

const SubmitEmailField = () => {
  const [, { value }] = useField('submitEmail');

  return value ? buildField : null;
};

export default SubmitEmailField;
