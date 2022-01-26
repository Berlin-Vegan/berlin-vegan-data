import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { Field, useField } from 'formik';
import { TextField } from 'formik-material-ui';
import { makeStyles } from '@material-ui/core/styles';
import MuiAlert from '@material-ui/lab/Alert';
import ReviewFormControl from './fields/ReviewFormControl';

const useStyles = makeStyles(() => ({
  textAreaMulti: {
    '& textarea': {
      resize: 'vertical',
    },
  },
}));

const DetailsFormPart = () => {
  const classes = useStyles();
  const [, reviewMeta] = useField('review');
  const reviewEmpty = reviewMeta.value === '' || reviewMeta.value == null;

  return (
    <>
      <Grid item>
        <Typography variant="h5">Details</Typography>
      </Grid>
      {reviewEmpty ? null : (
        <MuiAlert elevation={6} variant="filled" severity="info">
          The text of the review will be used.
        </MuiAlert>
      )}
      <Grid container item spacing={1} className={classes.textAreaMulti}>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment in German"
            name="comment"
            multiline={true}
            rows={10}
          />
        </Grid>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment in English"
            name="commentEnglish"
            multiline={true}
            rows={10}
          />
        </Grid>
      </Grid>
      <Grid container item spacing={1} className={classes.textAreaMulti}>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Comment Opening Hours"
            name="commentOpeningHours"
            multiline={true}
            rows={10}
          />
        </Grid>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Text Intern"
            name="textIntern"
            multiline={true}
            rows={10}
          />
        </Grid>
      </Grid>
      <Grid container item spacing={1}>
        <Grid container item direction="column" md={6}>
          <Field
            component={TextField}
            type="text"
            label="Public Transport"
            name="commentPublicTransport"
          />
        </Grid>
        <Grid container item direction="column" md={6}>
          <ReviewFormControl />
        </Grid>
      </Grid>
    </>
  );
};

export default DetailsFormPart;
