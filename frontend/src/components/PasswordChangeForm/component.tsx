import React, { useContext } from 'react';

import SaveIcon from '@mui/icons-material/Save';
import { Button } from '@mui/material';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';

import { Field, Form, Formik } from 'formik';
import { TextField } from 'formik-mui';
import { useSnackbar } from 'notistack';

import { AuthContext } from '@/providers/UserProvider';
import { authorizedFetch } from '@/utils/fetch';

const PREFIX = 'PasswordChangeForm';

const classes = {
  saveButton: `${PREFIX}-saveButton`,
};

const StyledFormik = styled(Formik)(() => ({
  [`& .${classes.saveButton}`]: {
    marginTop: '10px',
  },
}));

const initial = {
  oldPassword: '',
  password: '',
  passwordConfirm: '',
};

const PasswordChangeForm = () => {
  const { dispatch } = useContext(AuthContext);

  const { enqueueSnackbar } = useSnackbar();

  return (
    <StyledFormik
      initialValues={initial}
      onSubmit={async (values, { setSubmitting, setErrors, setValues }) => {
        const res = await authorizedFetch(
          dispatch,
          '/api/v1/accounts/change-password/',
          'POST',
          values,
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
              label="New Password"
              required
            />
            <Field
              component={TextField}
              name="passwordConfirm"
              type="password"
              label="New Password Confirmation"
              required
            />
            <Grid container justifyContent="flex-end" className={classes.saveButton}>
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
    </StyledFormik>
  );
};

export default PasswordChangeForm;
