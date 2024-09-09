import { Field } from 'formik';
import { Select } from 'formik-mui';
import { FormControl, MenuItem } from '@mui/material';
import { VEGAN_OPTIONS_FIELD } from '@components/LocationFormBase/fields/constants';

const veganMenuItem = (key: number, label: string) => (
  <MenuItem value={key} key={`veganOption${key}`}>
    {label}
  </MenuItem>
);

const veganFormControl = (
  <FormControl required>
    <Field
      component={Select}
      name="vegan"
      label="Vegan"
      type="number"
      inputProps={{
        id: 'vegan-select',
        name: 'vegan',
      }}
    >
      {[...VEGAN_OPTIONS_FIELD.entries()].map(([key, value]) => veganMenuItem(key, value))}
    </Field>
  </FormControl>
);

export default veganFormControl;
