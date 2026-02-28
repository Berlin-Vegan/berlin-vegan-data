import React from 'react';

import { FormHelperText } from '@mui/material';
import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import MuiSelect, { type SelectProps as MuiSelectProps } from '@mui/material/Select';
import type { Theme } from '@mui/material/styles';
import type { SxProps } from '@mui/system';

import type { FieldProps } from 'formik';

type BVSelectProps = MuiSelectProps & {
  label: string;
  labelId: string;
  readValue: (value: unknown) => unknown;
  setValue: (value: unknown) => unknown;
  children?: React.ReactNode;
  sxInputLabel?: SxProps<Theme>;
};

const BVSelect: React.FC<BVSelectProps & FieldProps> = ({
  field,
  form,
  meta,
  label,
  labelId,
  readValue,
  setValue,
  children,
  sxInputLabel,
  ...props
}) => {
  const { name, value, ...restField } = field;
  const { setFieldValue } = form;
  const showError = meta && meta.touched && Boolean(meta.error);

  return (
    <FormControl variant="standard" fullWidth error={showError}>
      <InputLabel id={labelId} sx={sxInputLabel}>
        {label}
      </InputLabel>
      <MuiSelect
        {...restField}
        {...props}
        labelId={labelId}
        id={name}
        value={readValue(value)}
        onChange={(e) => setFieldValue(name, setValue(e.target.value))}
        label={label}
      >
        {children}
      </MuiSelect>
      {showError && <FormHelperText>{meta.error}</FormHelperText>}
    </FormControl>
  );
};

export default BVSelect;
