import React from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import { Field } from 'formik';
import { Select } from 'formik-material-ui';
import FormControl from '@material-ui/core/FormControl';
import { menuItems } from './utils';
import { districtFieldOptions } from './constants';

const districtFormControl = (
  <FormControl required>
    <InputLabel id="vegan-label">Vegan</InputLabel>
    <Field
      component={Select}
      type="text"
      label="District"
      name="district"
      required
      inputProps={{
        id: 'district',
        labelId: 'district-label',
      }}
    >
      {menuItems(districtFieldOptions)}
    </Field>
  </FormControl>
);

export default districtFormControl;
