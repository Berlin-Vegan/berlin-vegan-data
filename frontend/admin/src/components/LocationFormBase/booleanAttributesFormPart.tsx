import React from 'react';
import { join, map, pipe, split } from 'ramda';
import { Grid } from '@material-ui/core';
import FormControlNoYesUnknown from '../GastroFormBase/fields/SelectFormControl';

const buildLabel = (key: string): string =>
  pipe(split(/(?=[A-Z])/), join(' '))(key);

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
