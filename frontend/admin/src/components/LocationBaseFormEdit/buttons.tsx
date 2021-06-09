import React, { FC, useContext } from 'react';
import { useField } from 'formik';
import { useSnackbar } from 'notistack';
import Grid from '@material-ui/core/Grid';
import { Button } from '@material-ui/core';
import DeleteIcon from '@material-ui/icons/Delete';
import { useHistory } from 'react-router-dom';
import SaveIcon from '@material-ui/icons/Save';
import { authorizedFetch } from '../../utils/fetch';
import { PagePaths } from '../../pages/constants';
import { AuthContext } from '../../providers/UserProvider';

interface IButtons {
  submitForm: () => void;
  isSubmitting: boolean;
  locationUrl: string;
}

const Buttons: FC<IButtons> = ({ submitForm, isSubmitting, locationUrl }) => {
  const { dispatch } = useContext(AuthContext);
  const { enqueueSnackbar } = useSnackbar();
  const history = useHistory();
  const [, isSubmissionMeta, { setValue: setIsSubmission }] = useField(
    'isSubmission',
  );
  const [, nameMeta] = useField('name');

  const gastroDelete = async () => {
    const res = await authorizedFetch(dispatch, locationUrl, 'DELETE');
    if (res.status === 204) {
      enqueueSnackbar(`Gastro ${nameMeta.value} deleted`, {
        variant: 'success',
      });
      history.push(PagePaths.GASTRO_DASHBOARD);
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
    <Grid container spacing={1} justify="flex-end">
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
