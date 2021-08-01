import React from 'react';
import Grid from '@material-ui/core/Grid';
import { Button } from '@material-ui/core';

const buttons = (submitForm: () => void, isSubmitting: boolean) => (
  <Grid container spacing={1} justify="flex-end">
    <Grid item>
      <Button
        variant="contained"
        color="primary"
        disabled={isSubmitting}
        onClick={submitForm}
        name="save"
      >
        Save
      </Button>
    </Grid>
  </Grid>
);

export default buttons;
