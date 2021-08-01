import React from 'react';
import { map } from 'ramda';
import { Grid } from '@material-ui/core';
import { Field } from 'formik';
import { TextField } from 'formik-material-ui';
import { buildLabel } from './utils';

const positiveIntegerInput = (attr: string) => (
  <Grid container item direction="column" md={3} key={attr}>
    <Field
      component={TextField}
      type="number"
      label={buildLabel(attr)}
      name={`attributes.${attr}`}
      min="1"
      InputProps={{ inputProps: { min: 0 } }}
    />
  </Grid>
);

const positiveIntegerAttributesFormPart = (positiveIntegerAttrLit: string[]) =>
  map((attr: string) => positiveIntegerInput(attr))(positiveIntegerAttrLit);

export default positiveIntegerAttributesFormPart;
