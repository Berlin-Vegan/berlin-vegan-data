import React from 'react';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { Field } from 'formik';
import { TextField } from 'formik-material-ui';
import { makeStyles } from '@material-ui/core/styles';
import NullTextField from '../GastroFormBase/fields/NullTextField';

const useStyles = makeStyles(() => ({
  textAreaMulti: {
    '& textarea': {
      resize: 'vertical',
    },
  },
}));

const DetailsFormPart = () => {
  const classes = useStyles();

  return (
    <>
      <Grid item>
        <Typography variant="h5">Details</Typography>
      </Grid>
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
            name="publicTransport"
          />
        </Grid>
        <Grid container item direction="column" md={6}>
          <Field
            component={NullTextField}
            type="text"
            label="Review Link"
            name="reviewLink"
            placeholder="https://www.berlin-vegan.de/..."
          />
        </Grid>
      </Grid>
    </>
  );
};

export default DetailsFormPart;
