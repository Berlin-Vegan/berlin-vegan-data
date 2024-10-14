import React from 'react';

import FormControl from '@mui/material/FormControl';
import InputLabel from '@mui/material/InputLabel';
import MuiSelect from '@mui/material/Select';
import { FormHelperText } from '@mui/material';
import { SelectProps as MuiSelectProps } from '@mui/material/Select';

import { getIn } from 'formik';
import { SelectProps } from 'formik-mui';

export interface BVSelectProps extends SelectProps {
  readValue: (value: unknown) => unknown;
  setValue: (value: unknown) => unknown;
}

// modified copy of https://github.com/stackworx/formik-mui/blob/main/packages/formik-mui/src/Select.tsx#L18
const BVFieldToSelect = (
  {
    readValue,
    setValue,
    disabled,
    // eslint-disable-next-line @typescript-eslint/no-unused-vars
    field: { onBlur: _onBlur, onChange: fieldOnChange, ...field },
    form: { isSubmitting, touched, errors, setFieldTouched, setFieldValue },
    onClose,
    ...props
  }: Omit<BVSelectProps, 'formControl' | 'formHelperText' | 'inputLabel'>,
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
): MuiSelectProps & { formError: any } => {
  const fieldError = getIn(errors, field.name);
  const showError = getIn(touched, field.name) && !!fieldError;

  return {
    disabled: disabled ?? isSubmitting,
    error: showError,
    formError: showError ? fieldError : undefined,
    onBlur: () => {
      // no-op
    },
    onChange:
      fieldOnChange ??
      (() => {
        // no-op
      }),
    // we must use `onClose` instead of `onChange` to be able to trigger validation when users click outside of the select list.
    onClose:
      onClose ??
      (async (e: React.SyntheticEvent) => {
        // eslint-disable-next-line @typescript-eslint/no-explicit-any
        const dataset = (e.target as any).dataset as DOMStringMap;
        if (dataset && dataset.value) {
          // out-of-sync issue since November 2019: https://github.com/formium/formik/issues/2059#issuecomment-890613538
          // without the await, formik validates with the former value
          await setFieldValue(field.name, setValue(dataset.value), false);
        }
        setFieldTouched(field.name, true, true);
      }),
    ...field,
    value: readValue(field.value),
    ...props,
  };
};

const BVSelect = ({ formControl, inputLabel, formHelperText, ...selectProps }: BVSelectProps) => {
  const { error, formError, disabled, ...selectFieldProps } = BVFieldToSelect(selectProps);
  const { children: formHelperTextChildren, ...formHelperTextProps } = formHelperText || {};
  const shouldDisplayFormHelperText = error || formHelperTextChildren;

  return (
    <FormControl disabled={disabled} error={error} {...formControl}>
      <InputLabel id={selectFieldProps.labelId} {...inputLabel}>
        {selectFieldProps.label}
      </InputLabel>
      <MuiSelect {...selectFieldProps} />
      {shouldDisplayFormHelperText && (
        <FormHelperText {...formHelperTextProps}>
          {error ? formError : formHelperTextChildren}
        </FormHelperText>
      )}
    </FormControl>
  );
};

export default BVSelect;
