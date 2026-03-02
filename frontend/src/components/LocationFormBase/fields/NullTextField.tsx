import React from 'react';

import TextField, { type TextFieldProps as MuiTextFieldProps } from '@mui/material/TextField';

import {
  emptyStringToNull,
  nullToEmptyString,
} from '@components/LocationFormBase/fields/constants.ts';
import type { FieldProps } from 'formik';

const NullTextField: React.FC<MuiTextFieldProps & FieldProps> = ({
  field,
  form,
  meta,
  ...props
}) => {
  const { name, value, ...restField } = field;
  const { setFieldValue } = form;

  const handleChange = (event: React.ChangeEvent<HTMLInputElement>) => {
    setFieldValue(name, emptyStringToNull(event.target.value));
  };

  return (
    <TextField
      {...restField}
      {...props}
      name={name}
      value={nullToEmptyString(value)}
      onChange={handleChange}
      error={meta && meta.touched && Boolean(meta.error)}
      helperText={meta && meta.touched && meta.error}
    />
  );
};

NullTextField.displayName = 'NullTextField';

export default NullTextField;
