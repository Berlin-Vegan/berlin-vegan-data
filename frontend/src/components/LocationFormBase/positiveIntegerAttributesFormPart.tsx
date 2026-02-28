import { Grid } from '@mui/material';
import TextField from '@mui/material/TextField';
import { styled } from '@mui/material/styles';

import { Field, type FieldProps } from 'formik';
import { map } from 'ramda';

import { buildLabel } from './utils';

const CapitalizeTextField = styled(TextField)({
  '& label': { textTransform: 'capitalize' },
});

const positiveIntegerInput = (attr: string) => (
  <Grid key={attr} size={3}>
    <Field name={`attributes.${attr}`}>
      {({ field, meta, form }: FieldProps) => (
        <CapitalizeTextField
          {...field}
          type="number"
          label={buildLabel(attr)}
          variant="standard"
          error={meta.touched && Boolean(meta.error)}
          helperText={meta.touched && meta.error}
          fullWidth
          onChange={(e) => {
            // Only allow positive integers or empty string
            const value = e.target.value;
            form.setFieldValue(
              field.name,
              value === '' ? '' : Math.max(1, parseInt(value, 10) || 1),
            );
          }}
        />
      )}
    </Field>
  </Grid>
);

const positiveIntegerAttributesFormPart = (positiveIntegerAttrLit: string[]) =>
  map((attr: string) => positiveIntegerInput(attr))(positiveIntegerAttrLit);

export default positiveIntegerAttributesFormPart;
