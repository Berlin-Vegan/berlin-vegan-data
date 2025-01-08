import Grid from '@mui/material/Grid';
import { Button } from '@mui/material';

const buttons = (submitForm: () => void, isSubmitting: boolean) => (
  <Grid container spacing={1} justifyContent="flex-end">
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
