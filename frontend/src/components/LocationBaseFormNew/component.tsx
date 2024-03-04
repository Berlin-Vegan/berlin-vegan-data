import React, { useContext } from 'react';
import { useNavigate } from 'react-router-dom';

import { LocalizationProvider } from '@mui/x-date-pickers';
import { AdapterDayjs } from '@mui/x-date-pickers/AdapterDayjs';

import * as Yup from 'yup';
import LocationBaseType from '@components/LocationFormBase/locationBaseType';
import { Form, Formik } from 'formik';
import { useSnackbar } from 'notistack';

import { AuthContext } from '@/providers/UserProvider';
import { LocationType } from '@/utils/constants';
import { authorizedFetch } from '@/utils/fetch';
import { buildFEDetailUrl, buildListUrl } from '@/utils/utils';

import buttons from './buttons';

type ILocationBaseFormNew = {
  label: string;
  type: LocationType;
  locationForm: React.ElementType;
  locationFormSchema: Yup.AnySchema;
  initialData: LocationBaseType;
};

const LocationBaseFormNew = ({
  label,
  type,
  locationForm,
  locationFormSchema,
  initialData,
}: ILocationBaseFormNew) => {
  const { dispatch } = useContext(AuthContext);
  const { enqueueSnackbar } = useSnackbar();
  const navigate = useNavigate();

  const LocationForm = locationForm;

  return (
    <LocalizationProvider dateAdapter={AdapterDayjs}>
      <Formik
        initialValues={initialData}
        validationSchema={locationFormSchema}
        onSubmit={async (values, { setSubmitting, setErrors }) => {
          const res = await authorizedFetch(dispatch, buildListUrl(type), 'POST', values);
          const data = await res.json();
          if (res.status === 201) {
            enqueueSnackbar(`${label} ${data.name} created`, {
              variant: 'success',
            });
            navigate(buildFEDetailUrl(type, data.id));
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
            <LocationForm>{buttons(submitForm, isSubmitting)}</LocationForm>
          </Form>
        )}
      </Formik>
    </LocalizationProvider>
  );
};

export default LocationBaseFormNew;
