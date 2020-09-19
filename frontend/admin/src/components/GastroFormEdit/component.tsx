import React, { FunctionComponent } from 'react';
import { useSnackbar } from 'notistack';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import { Form, Formik } from 'formik';
import Grid from '@material-ui/core/Grid';
import { parseISO } from 'date-fns';
import { defaultTo } from 'ramda';
import gastroFormSchema from '../GastroFormBase/formSchema';
import { authorizedFetch } from '../../utils/fetch';
import { GastroDataType } from './types';
import useStyles from './styles';
import Buttons from './buttons';
import GastroBaseForm from '../GastroFormBase';

interface IGastroFormEdit {
  gastroData: GastroDataType;
}

const GastroFormEdit: FunctionComponent<IGastroFormEdit> = ({ gastroData }) => {
  const classes = useStyles();
  const { enqueueSnackbar } = useSnackbar();
  const { created, updated, idString, lastEditor, ...formData } = gastroData;
  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Formik
        initialValues={formData}
        validationSchema={gastroFormSchema}
        onSubmit={async (values, { setSubmitting, setErrors }) => {
          const res = await authorizedFetch(
            `/api/v1/gastros/${idString}/`,
            'PUT',
            values
          );
          const data = await res.json();
          if (res.status === 200) {
            enqueueSnackbar(`Gastro ${data.name} updated`, {
              variant: 'success',
            });
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
            <Grid container className={classes.metaInfo}>
              <Grid container item spacing={1} md={6}>
                <Grid item>
                  <div>Created: {parseISO(created).toDateString()}</div>
                </Grid>
                <Grid item>
                  <div>Updated: {parseISO(updated).toDateString()}</div>
                </Grid>
              </Grid>
              <Grid container item md={6} justify="flex-end">
                <Grid item>
                  <div>Last Editor: {defaultTo('–', lastEditor)}</div>
                </Grid>
              </Grid>
            </Grid>
            <GastroBaseForm>
              <Buttons
                submitForm={submitForm}
                isSubmitting={isSubmitting}
                idString={idString}
              />
            </GastroBaseForm>
          </Form>
        )}
      </Formik>
    </MuiPickersUtilsProvider>
  );
};

export default GastroFormEdit;
