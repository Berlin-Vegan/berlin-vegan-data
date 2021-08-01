import React, { FC, FunctionComponent, useContext } from 'react';
import * as Yup from 'yup';
import { useSnackbar } from 'notistack';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import { Form, Formik } from 'formik';
import Grid from '@material-ui/core/Grid';
import { parseISO } from 'date-fns';
import { defaultTo } from 'ramda';
import { authorizedFetch } from '../../utils/fetch';
import { AuthContext } from '../../providers/UserProvider';
import Buttons from './buttons';
import useStyles from './styles';
import LocationBaseType from '../LocationFormBase/locationBaseType';

type LocationBaseFormEditType = {
  label: string;
  locationUrl: string;
  locationForm: FC;
  locationData: LocationBaseType;
  locationFormSchema: Yup.AnySchema;
};

const LocationBaseFormEdit: FunctionComponent<LocationBaseFormEditType> = ({
  label,
  locationUrl,
  locationForm,
  locationData,
  locationFormSchema,
}) => {
  const classes = useStyles();
  const { dispatch } = useContext(AuthContext);
  const { enqueueSnackbar } = useSnackbar();

  const LocationForm = locationForm;
  const { created, updated, lastEditor, ...formData } = locationData;

  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Formik
        initialValues={formData}
        validationSchema={locationFormSchema}
        onSubmit={async (values, { setSubmitting, setErrors }) => {
          const res = await authorizedFetch(
            dispatch,
            locationUrl,
            'PUT',
            values,
          );
          const data = await res.json();
          if (res.status === 200) {
            enqueueSnackbar(`${label} ${data.name} updated`, {
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
                  <div>
                    Created: {created ? parseISO(created).toDateString() : '–'}
                  </div>
                </Grid>
                <Grid item>
                  <div>
                    Updated: {updated ? parseISO(updated).toDateString() : '–'}
                  </div>
                </Grid>
              </Grid>
              <Grid container item md={6} justify="flex-end">
                <Grid item>
                  <div>Last Editor: {defaultTo('–', lastEditor)}</div>
                </Grid>
              </Grid>
            </Grid>
            <LocationForm>
              <Buttons
                submitForm={submitForm}
                isSubmitting={isSubmitting}
                locationUrl={locationUrl}
              />
            </LocationForm>
          </Form>
        )}
      </Formik>
    </MuiPickersUtilsProvider>
  );
};

export default LocationBaseFormEdit;
