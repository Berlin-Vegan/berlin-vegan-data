import React from 'react';
import { Field, Form, Formik } from 'formik';
import { useSnackbar } from 'notistack';
import { TextField } from 'formik-material-ui';
import Grid from '@material-ui/core/Grid';
import Typography from '@material-ui/core/Typography';
import SaveIcon from '@material-ui/icons/Save';
import { Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { authorizedFetch } from '../../utils/fetch';

const useStyles = makeStyles(() => ({
  saveButton: {
    marginTop: '10px',
  },
}));

const initial = {
  oldPassword: '',
  password: '',
  passwordConfirm: '',
};

const PasswordChangeForm = () => {
  const classes = useStyles();
  const { enqueueSnackbar } = useSnackbar();

  return (
    <Formik
      initialValues={initial}
      onSubmit={async (values, { setSubmitting, setErrors, setValues }) => {
        const res = await authorizedFetch(
          '/api/v1/accounts/change-password/',
          'POST',
          values
        );
        const data = await res.json();
        if (res.status === 200) {
          enqueueSnackbar('Password updated', {
            variant: 'success',
          });
        }
        if (res.status === 400) {
          enqueueSnackbar('Form invalid', {
            variant: 'error',
          });
          setErrors(data);
        }
        setValues(initial, false);
        setSubmitting(false);
      }}
    >
      {({ submitForm, isSubmitting }) => (
        <Form>
          <Grid container spacing={1} direction="column" md={4}>
            <Typography variant="h5">Change Password</Typography>
            <Field
              component={TextField}
              name="oldPassword"
              type="password"
              label="Old Password"
              required
            />
            <Field
              component={TextField}
              name="password"
              type="password"
              label="New Passowrd"
              required
            />
            <Field
              component={TextField}
              name="passwordConfirm"
              type="password"
              label="New Password Confirmation"
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
        </Form>
      )}
    </Formik>
  );
};

export default PasswordChangeForm;
