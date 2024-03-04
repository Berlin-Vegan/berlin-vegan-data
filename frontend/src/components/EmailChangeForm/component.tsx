import { useContext } from 'react';

import SaveIcon from '@mui/icons-material/Save';
import { Button } from '@mui/material';
import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';

import * as Yup from 'yup';
import { Field, Form, Formik } from 'formik';
import { TextField } from 'formik-mui';
import { useSnackbar } from 'notistack';
import { pathOr } from 'ramda';

import { AuthContext, TYPE_UPDATE_USER_EMAIL } from '@/providers/UserProvider';
import { authorizedFetch } from '@/utils/fetch';

const PREFIX = 'EmailChangeForm';

const classes = {
  saveButton: `${PREFIX}-saveButton`,
};

const StyledFormik = styled(Formik)(() => ({
  [`& .${classes.saveButton}`]: {
    marginTop: '10px',
  },
}));

const emailChangeForm = Yup.object().shape({
  email: Yup.string().email().nullable(),
});

const profileURL = '/api/v1/accounts/profile/';

const EmailChangeForm = () => {
  const { enqueueSnackbar } = useSnackbar();
  const { state, dispatch } = useContext(AuthContext);
  const email = pathOr('', ['userData', 'email'], state);

  return (
    <StyledFormik
      initialValues={{ email }}
      validationSchema={emailChangeForm}
      onSubmit={async (values, { setSubmitting, setErrors }) => {
        const res = await authorizedFetch(dispatch, profileURL, 'PATCH', values);
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
              <Field component={TextField} name="email" type="email" label="E-Mail" required />
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
          </Grid>
        </Form>
      )}
    </StyledFormik>
  );
};

export default EmailChangeForm;
