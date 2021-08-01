import React from 'react';
import { map } from 'ramda';
import { Grid } from '@material-ui/core';
import FormControlNoYesUnknown from './fields/SelectFormControl';
import { buildLabel } from './utils';

const yesNoUnknownInputs = (attr: string) => (
  <Grid container item direction="column" md={3} key={attr}>
    <FormControlNoYesUnknown
      label={buildLabel(attr)}
      name={`attributes.${attr}`}
    />
  </Grid>
);

const booleanAttributesFormPart = (booleanAttrList: string[]) =>
  map((attr: string) => yesNoUnknownInputs(attr))(booleanAttrList);

export default booleanAttributesFormPart;
