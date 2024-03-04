import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

import { Field } from 'formik';
import { CheckboxWithLabel } from 'formik-mui';

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
