import React from 'react';

import MuiTextField, { TextFieldProps as MuiTextFieldProps } from '@mui/material/TextField';

import { TextFieldProps, fieldToTextField } from 'formik-mui';

export const nullToEmptyString = (value: string | null | unknown) => (value === null ? '' : value);

export const emptyStringToNull = (value: string) => (value === '' ? null : value);

const fieldToNullTextField = (props: TextFieldProps): MuiTextFieldProps => {
  const fieldToTextFieldProps = fieldToTextField(props);
  return {
    ...fieldToTextFieldProps,
    value: nullToEmptyString(fieldToTextFieldProps.value),
  };
};

const NullTextField = ({ children, ...props }: TextFieldProps) => {
  const {
    form: { setFieldValue },
    field: { name },
  } = props;

  const onChange = React.useCallback(
    (event: React.ChangeEvent<HTMLInputElement>) => {
      const { value } = event.target;
      setFieldValue(name, emptyStringToNull(value));
    },
    [setFieldValue, name],
  );

  return (
    <MuiTextField {...fieldToNullTextField(props)} onChange={onChange}>
      {children}
    </MuiTextField>
  );
};

NullTextField.displayName = 'NullTextField';

export default NullTextField;
