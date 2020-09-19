import React from 'react';
import Typography from '@material-ui/core/Typography';
import Grid from '@material-ui/core/Grid';
import { CheckboxWithLabel } from 'formik-material-ui';
import { Field } from 'formik';
import { map } from 'ramda';
import { nthOr } from '../../utils/fp';

const tagList = [
  ['Restaurant', 'restaurant'],
  ['Snack Bar', 'imbiss'],
  ['Ice Cream Parlor', 'eiscafe'],
  ['Café', 'cafe'],
  ['Bar', 'bar'],
];

const checkBox = (label: string, name: string) => (
  <Grid item md={2} key={name}>
    <Field
      component={CheckboxWithLabel}
      name={name}
      Label={{ label }}
      type="checkbox"
    />
  </Grid>
);

const nthOrEmpty = nthOr('');

const buildTagList = map((tag) =>
  checkBox(nthOrEmpty(0)(tag), nthOrEmpty(1)(tag))
)(tagList);

const tagsFormPart = (
  <>
    <Grid item>
      <Typography variant="h5">Tags</Typography>
    </Grid>
    <Grid container item spacing={1}>
      {buildTagList}
    </Grid>
  </>
);

export default tagsFormPart;
