import { Grid } from '@mui/material';
import MenuItem from '@mui/material/MenuItem';

import { Field } from 'formik';
import { map } from 'ramda';

import FormControlNoYesUnknown from './fields/FormControlNoYesUnknown';
import { buildLabel } from './utils';

const yesNoUnknownInputs = (attr: string) => (
  <Grid container item direction="column" md={3} key={attr}>
    <Field
      component={FormControlNoYesUnknown}
      name={`attributes.${attr}`}
      label={buildLabel(attr)}
      variant="standard"
      inputProps={{
        name: `attributes.${attr}`,
        id: `attributes.${attr}-select`,
      }}
    >
      <MenuItem value="yes">Yes</MenuItem>
      <MenuItem value="no">No</MenuItem>
      <MenuItem value="unknown">Unknown</MenuItem>
    </Field>
  </Grid>
);

const booleanAttributesFormPart = (booleanAttrList: string[]) =>
  map((attr: string) => yesNoUnknownInputs(attr))(booleanAttrList);

export default booleanAttributesFormPart;
