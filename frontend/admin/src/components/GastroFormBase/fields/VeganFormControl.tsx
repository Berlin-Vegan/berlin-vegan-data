import React from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import { Field } from 'formik';
import { Select } from 'formik-material-ui';
import FormControl from '@material-ui/core/FormControl';
import { veganFieldOptions } from './constants';
import { menuItems } from './utils';

const veganFormControl = (
  <FormControl required>
    <InputLabel id="vegan-label">Vegan</InputLabel>
    <Field
      component={Select}
      name="vegan"
      type="number"
      inputProps={{
        id: 'vegan',
        labelId: 'vegan-label',
      }}
    >
      {menuItems(veganFieldOptions)}
    </Field>
  </FormControl>
);

export default veganFormControl;
