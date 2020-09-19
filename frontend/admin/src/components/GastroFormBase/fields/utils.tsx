import React from 'react';
import MenuItem from '@material-ui/core/MenuItem';
import { map } from 'ramda';
import { nthOr } from '../../../utils/fp';

const menuItem = (value: number | string, label: string) => (
  <MenuItem value={value} key={value}>
    {label}
  </MenuItem>
);

export const menuItems = (fieldOptions: Array<[number | string, string]>) =>
  map((item) => menuItem(nthOr('', 0)(item), nthOr('', 1)(item)))(fieldOptions);
