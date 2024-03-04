import { useContext } from 'react';
import { useNavigate } from 'react-router-dom';

import DeleteIcon from '@mui/icons-material/Delete';
import SaveIcon from '@mui/icons-material/Save';
import { Button } from '@mui/material';
import Grid from '@mui/material/Grid';

import { useField } from 'formik';
import { useSnackbar } from 'notistack';

import { PagePaths } from '@/pages/constants';
import { AuthContext } from '@/providers/UserProvider';
import { authorizedFetch } from '@/utils/fetch';

interface IButtons {
  submitForm: () => void;
  isSubmitting: boolean;
  locationUrl: string;
}

const Buttons = ({ submitForm, isSubmitting, locationUrl }: IButtons) => {
  const { dispatch } = useContext(AuthContext);
  const { enqueueSnackbar } = useSnackbar();
  const navigate = useNavigate();
  const [, isSubmissionMeta, { setValue: setIsSubmission }] = useField('isSubmission');
  const [, nameMeta] = useField('name');

  const gastroDelete = async () => {
    const res = await authorizedFetch(dispatch, locationUrl, 'DELETE');
    if (res.status === 204) {
      enqueueSnackbar(`Gastro ${nameMeta.value} deleted`, {
        variant: 'success',
      });
      navigate(PagePaths.GASTRO_DASHBOARD);
    }
  };

  const publishGastro = async () => {
    const res = await authorizedFetch(dispatch, locationUrl, 'PATCH', {
      isSubmission: false,
    });
    if (res.status === 200) {
      enqueueSnackbar(`Gastro ${nameMeta.value} published`, {
        variant: 'success',
      });
      setIsSubmission(false);
    }
  };

  return (
    <Grid container spacing={1} justifyContent="flex-end">
      <Grid item>
        <Button
          variant="contained"
          color="secondary"
          disabled={isSubmitting}
          onClick={gastroDelete}
          name="delete"
        >
          Delete
        </Button>
      </Grid>
      {isSubmissionMeta.value ? (
        <Grid item>
          <Button
            variant="contained"
            color="primary"
            disabled={isSubmitting}
            onClick={publishGastro}
            name="publish"
            startIcon={<DeleteIcon />}
          >
            Publish
          </Button>
        </Grid>
      ) : (
        <></>
      )}
      <Grid item>
        <Button
          variant="contained"
          color="primary"
          disabled={isSubmitting}
          onClick={submitForm}
          name="save"
          startIcon={<SaveIcon />}
        >
          Save
        </Button>
      </Grid>
    </Grid>
  );
};

export default Buttons;
