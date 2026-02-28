import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

import { Field, type FieldProps } from 'formik';

const metaFormPart = (
  <>
    <Grid>
      <Typography variant="h5">Meta</Typography>
    </Grid>
    <Grid container spacing={1}>
      <Grid>
        <Field name="hasSticker">
          {({ field }: FieldProps) => (
            <label style={{ display: 'flex', alignItems: 'center', gap: 8 }}>
              <input type="checkbox" {...field} checked={!!field.value} />
              Sticker
            </label>
          )}
        </Field>
      </Grid>
    </Grid>
  </>
);

export default metaFormPart;
