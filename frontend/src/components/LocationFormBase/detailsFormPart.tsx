import MuiAlert from '@mui/material/Alert';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

import { css } from '@emotion/react';
import { Field, useField } from 'formik';
import { TextField } from 'formik-mui';

import ReviewFormControl from './fields/ReviewFormControl';

const DetailsFormPart = () => {
  const [, reviewMeta] = useField('review');
  const reviewEmpty = reviewMeta.value === '' || reviewMeta.value == null;

  return (
    <div
      css={css`
        & textarea {
          resize: vertical;
        }
      `}
    >
      <Grid item>
        <Typography variant="h5">Details</Typography>
      </Grid>
      {reviewEmpty ? null : (
        <MuiAlert
          elevation={6}
          variant="filled"
          severity="info"
          css={css`
            margin-top: 10px;
            margin-bottom: 10px;
          `}
        >
          The text of the review will be used.
        </MuiAlert>
      )}
      <Grid container item spacing={1}>
        <Grid item md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment in German"
            name="comment"
            variant="standard"
            multiline={true}
            rows={10}
            fullWidth
          />
        </Grid>
        <Grid item md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment in English"
            name="commentEnglish"
            variant="standard"
            multiline={true}
            rows={10}
            fullWidth
          />
        </Grid>
      </Grid>
      <Grid container item spacing={1}>
        <Grid item md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment Opening Hours"
            name="commentOpeningHours"
            variant="standard"
            multiline={true}
            rows={10}
            fullWidth
          />
        </Grid>
        <Grid item md={6}>
          <Field
            component={TextField}
            type="text"
            label="Text Intern"
            name="textIntern"
            variant="standard"
            multiline={true}
            rows={10}
            fullWidth
          />
        </Grid>
      </Grid>
      <Grid container item spacing={1}>
        <Grid item md={6}>
          <Field
            component={TextField}
            type="text"
            label="Public Transport"
            name="commentPublicTransport"
            variant="standard"
            fullWidth
          />
        </Grid>
        <Grid item md={6}>
          <ReviewFormControl />
        </Grid>
      </Grid>
    </div>
  );
};

export default DetailsFormPart;
