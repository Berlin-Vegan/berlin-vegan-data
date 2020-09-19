import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { Field } from 'formik';
import { CheckboxWithLabel } from 'formik-material-ui';

const metaFormPart = (
  <>
    <Grid item>
      <Typography variant="h5">Meta</Typography>
    </Grid>
    <Grid container item spacing={1}>
      <Grid item>
        <Field
          component={CheckboxWithLabel}
          name="hasSticker"
          Label={{ label: 'Sticker' }}
          type="checkbox"
        />
      </Grid>
    </Grid>
  </>
);

export default metaFormPart;
