import { Grid } from '@mui/material';

import { Field } from 'formik';
import { TextField } from 'formik-mui';
import { map } from 'ramda';

import { buildLabel } from './utils';
import { styled } from '@mui/material/styles';

const CapitalizeTextField = styled(TextField)({
  '& label': { textTransform: 'capitalize' },
});

const positiveIntegerInput = (attr: string) => (
  <Grid container item direction="column" md={3} key={attr}>
    <Field
      component={CapitalizeTextField}
      type="number"
      label={buildLabel(attr)}
      name={`attributes.${attr}`}
      min="1"
      variant="standard"
      InputProps={{ inputProps: { min: 0 } }}
    />
  </Grid>
);

const positiveIntegerAttributesFormPart = (positiveIntegerAttrLit: string[]) =>
  map((attr: string) => positiveIntegerInput(attr))(positiveIntegerAttrLit);

export default positiveIntegerAttributesFormPart;
