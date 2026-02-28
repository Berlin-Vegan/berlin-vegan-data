import { Grid } from '@mui/material';
import MenuItem from '@mui/material/MenuItem';

import BVSelect from '@components/LocationFormBase/fields/BVSelect';
import { Field } from 'formik';
import { map } from 'ramda';

import { buildLabel } from './utils';

interface IMappingDict {
  [id: string]: boolean | null;
}

const UNKNOWN = 'unknown';

const mappingDict: IMappingDict = {
  yes: true,
  no: false,
  [UNKNOWN]: null,
};

export const stringToBoolean = (value: string | unknown): boolean | null => {
  if (typeof value == 'string') {
    return Object.prototype.hasOwnProperty.call(mappingDict, value) ? mappingDict[value] : null;
  }
  return null;
};

export const booleanToString = (value: boolean | null | unknown): string => {
  if (typeof value !== 'boolean') {
    return UNKNOWN;
  }
  for (const key in mappingDict) {
    if (mappingDict[key] === value) return key;
  }
  return UNKNOWN;
};

const yesNoUnknownInputs = (attr: string) => (
  <Grid key={attr} size={3}>
    <Field
      component={BVSelect}
      name={`attributes.${attr}`}
      label={buildLabel(attr)}
      variant="standard"
      sxInputLabel={{ textTransform: 'capitalize' }}
      inputProps={{
        name: `attributes.${attr}`,
        id: `attributes.${attr}-select`,
      }}
      readValue={booleanToString}
      setValue={stringToBoolean}
    >
      <MenuItem value="yes">Yes</MenuItem>
      <MenuItem value="no">No</MenuItem>
      <MenuItem value="unknown">Unknown</MenuItem>
    </Field>
  </Grid>
);

const booleanAttributesFormPart = (booleanAttrList: string[]) =>
  map((attr: string) => yesNoUnknownInputs(attr))(booleanAttrList);

export default booleanAttributesFormPart;
