import React, { useContext } from 'react';
import { useSnackbar } from 'notistack';
import { Field, Form, Formik } from 'formik';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import { TextField } from 'formik-material-ui';
import { Button } from '@material-ui/core';
import SaveIcon from '@material-ui/icons/Save';
import { makeStyles } from '@material-ui/core/styles';
import * as Yup from 'yup';
import { pathOr } from 'ramda';
import { authorizedFetch } from '../../utils/fetch';
import {
  AuthContext,
  TYPE_UPDATE_USER_EMAIL,
} from '../../providers/UserProvider';

const useStyles = makeStyles(() => ({
  saveButton: {
    marginTop: '10px',
  },
}));

const emailChangeForm = Yup.object().shape({
  email: Yup.string().email().nullable(),
});

const profileURL = '/api/v1/accounts/profile/';

const EmailChangeForm = () => {
  const classes = useStyles();
  const { enqueueSnackbar } = useSnackbar();
  const { state, dispatch } = useContext(AuthContext);
  const email = pathOr('', ['userData', 'email'], state);

  return (
    <Formik
      initialValues={{ email }}
      validationSchema={emailChangeForm}
      onSubmit={async (values, { setSubmitting, setErrors }) => {
        const res = await authorizedFetch(
          dispatch,
          profileURL,
          'PATCH',
          values,
        );
        const data = await res.json();
        if (res.status === 200) {
          enqueueSnackbar('Email updated', {
            variant: 'success',
          });
          dispatch({ type: TYPE_UPDATE_USER_EMAIL, payload: values.email });
        }
        if (res.status === 400) {
          enqueueSnackbar('Form invalid', {
            variant: 'error',
          });
          setErrors(data);
        }
        setSubmitting(false);
      }}
    >
      {({ submitForm, isSubmitting }) => (
        <Form>
          <Grid container spacing={1} direction="column">
            <Grid container item direction="column" md={4}>
              <Typography variant="h5">Change Email</Typography>
              <Field
                component={TextField}
                name="email"
                type="email"
                label="E-Mail"
                required
              />
              <Grid container justify="flex-end" className={classes.saveButton}>
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
          </Grid>
        </Form>
      )}
    </Formik>
  );
};

export default EmailChangeForm;
