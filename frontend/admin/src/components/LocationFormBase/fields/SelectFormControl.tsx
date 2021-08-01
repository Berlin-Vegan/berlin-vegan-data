import React, { FC } from 'react';
import InputLabel from '@material-ui/core/InputLabel';
import MuiSelect, {
  SelectProps as MuiSelectProps,
} from '@material-ui/core/Select';
import { Field } from 'formik';
import { SelectProps, fieldToSelect } from 'formik-material-ui';
import MenuItem from '@material-ui/core/MenuItem';
import FormControl from '@material-ui/core/FormControl';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
  capitalizeTitle: {
    textTransform: 'capitalize',
  },
}));

interface IMappingDict {
  [id: string]: boolean | null;
}

const UNKNOWN = 'unknown';

const mappingDict: IMappingDict = {
  yes: true,
  no: false,
  [UNKNOWN]: null,
};

export const stringToBoolean = (value: string): boolean | null =>
  Object.prototype.hasOwnProperty.call(mappingDict, value)
    ? mappingDict[value]
    : null;

export const booleanToString = (value: boolean | null | unknown): string => {
  if (typeof value !== 'boolean') {
    return UNKNOWN;
  }
  for (const key in mappingDict) {
    if (mappingDict[key] === value) return key;
  }
  return UNKNOWN;
};

const fieldValueToString = (props: SelectProps): MuiSelectProps => {
  const fieldToSelectProps = fieldToSelect(props);
  return {
    ...fieldToSelectProps,
    value: booleanToString(fieldToSelectProps.value),
  };
};

const SelectYesNoUnknown = ({ children, ...props }: SelectProps) => {
  const {
    form: { setFieldValue },
    field: { name },
  } = props;
  const onChange = React.useCallback(
    (event) => {
      const { value } = event.target;
      setFieldValue(name, stringToBoolean(value));
    },
    [setFieldValue, name],
  );
  return (
    <MuiSelect {...fieldValueToString(props)} onChange={onChange}>
      {children}
    </MuiSelect>
  );
};

interface IFormControlProps {
  label: string;
  name: string;
}

const FormControlNoYesUnknown: FC<IFormControlProps> = ({ label, name }) => {
  const classes = useStyles();
  return (
    <FormControl required>
      <InputLabel htmlFor={name} className={classes.capitalizeTitle}>
        {label}
      </InputLabel>
      <Field
        component={SelectYesNoUnknown}
        name={name}
        inputProps={{
          id: name,
        }}
      >
        <MenuItem value="yes">Yes</MenuItem>
        <MenuItem value="no">No</MenuItem>
        <MenuItem value="unknown">Unknown</MenuItem>
      </Field>
    </FormControl>
  );
};

export default FormControlNoYesUnknown;
