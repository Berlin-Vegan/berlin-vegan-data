import React, { FunctionComponent } from 'react';
import { Form, Formik } from 'formik';
import DateFnsUtils from '@date-io/date-fns';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import { useHistory } from 'react-router-dom';
import { useSnackbar } from 'notistack';
import gastroFormSchema from '../GastroFormBase/formSchema';
import { authorizedFetch } from '../../utils/fetch';
import buttons from './buttons';
import initial from './initialData';
import GastroBaseForm from '../GastroFormBase';

const GastroFormNew: FunctionComponent = () => {
  const { enqueueSnackbar } = useSnackbar();
  const history = useHistory();

  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Formik
        initialValues={initial}
        validationSchema={gastroFormSchema}
        onSubmit={async (values, { setSubmitting, setErrors }) => {
          const res = await authorizedFetch('/api/v1/gastros/', 'POST', values);
          const data = await res.json();
          if (res.status === 201) {
            enqueueSnackbar(`Gastro ${data.name} created`, {
              variant: 'success',
            });
            history.push(`/gastro/${data.idString}/edit`);
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
            <GastroBaseForm>{buttons(submitForm, isSubmitting)}</GastroBaseForm>
          </Form>
        )}
      </Formik>
    </MuiPickersUtilsProvider>
  );
};

export default GastroFormNew;
