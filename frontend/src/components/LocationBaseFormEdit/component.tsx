import React, { type FC, type FunctionComponent, useContext } from 'react';

import Grid from '@mui/material/Grid';
import { grey } from '@mui/material/colors';
import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

import * as Yup from 'yup';
import dayjs from 'dayjs';
import { Form, Formik } from 'formik';
import { useSnackbar } from 'notistack';
import { defaultTo } from 'ramda';

import { AuthContext } from '@/providers/UserProvider';
import { DATE_FORMAT } from '@/utils/constants';
import { authorizedFetch } from '@/utils/fetch';

import type { LocationBaseType } from '../LocationFormBase/locationBaseType';
import PaperDefault from '../PaperDefault';
import Buttons from './buttons';

type LocationBaseFormEditType = {
  label: string;
  locationUrl: string;
  locationForm: FC<{ children: React.ReactNode }>;
  locationData: LocationBaseType;
  locationFormSchema: Yup.AnySchema;
  setLocationDataState: React.Dispatch<React.SetStateAction<LocationBaseType>>;
};

const LocationBaseFormEdit: FunctionComponent<LocationBaseFormEditType> = ({
  label,
  locationUrl,
  locationForm,
  locationData,
  locationFormSchema,
  setLocationDataState,
}) => {
  const { dispatch } = useContext(AuthContext);
  const { enqueueSnackbar } = useSnackbar();

  const LocationForm = locationForm;
  const { created, updated, lastEditor, ...formData } = locationData;

  return (
    <PaperDefault>
      <LocalizationProvider dateAdapter={AdapterDayjs}>
        <Formik
          initialValues={formData}
          validationSchema={locationFormSchema}
          onSubmit={async (values, { setSubmitting, setErrors }) => {
            const res = await authorizedFetch(dispatch, locationUrl, 'PUT', values);
            const data = await res.json();
            if (res.status === 200) {
              setLocationDataState(data);
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
              <Grid container sx={{ color: grey[600] }}>
                <Grid container spacing={1}>
                  <Grid>
                    <div>Created: {created ? dayjs(created).format(DATE_FORMAT) : '–'}</div>
                  </Grid>
                  <Grid>
                    <div>Updated: {updated ? dayjs(updated).format(DATE_FORMAT) : '–'}</div>
                  </Grid>
                </Grid>
                <Grid container justifyContent="flex-end">
                  <Grid>
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
      </LocalizationProvider>
    </PaperDefault>
  );
};

export default LocationBaseFormEdit;
