import React, { FC, FunctionComponent, useContext } from 'react';
import * as Yup from 'yup';
import { Form, Formik } from 'formik';
import DateFnsUtils from '@date-io/date-fns';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import { useHistory } from 'react-router-dom';
import { useSnackbar } from 'notistack';
import { authorizedFetch } from '../../utils/fetch';
import { AuthContext } from '../../providers/UserProvider';
import buttons from '../GastroFormNew/buttons';
import { LocationType } from '../../utils/constants';
import { buildFEDetailUrl, buildListUrl } from '../../utils/utils';
import LocationBaseType from '../LocationFormBase/locationBaseType';

type ILocationBaseFormNew = {
  label: string;
  type: LocationType;
  locationForm: FC;
  locationFormSchema: Yup.AnySchema;
  initialData: LocationBaseType;
};

const LocationBaseFormNew: FunctionComponent<ILocationBaseFormNew> = ({
  label,
  type,
  locationForm,
  locationFormSchema,
  initialData,
}) => {
  const { dispatch } = useContext(AuthContext);
  const { enqueueSnackbar } = useSnackbar();
  const history = useHistory();

  const LocationForm = locationForm;

  return (
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Formik
        initialValues={initialData}
        validationSchema={locationFormSchema}
        onSubmit={async (values, { setSubmitting, setErrors }) => {
          const res = await authorizedFetch(
            dispatch,
            buildListUrl(type),
            'POST',
            values,
          );
          const data = await res.json();
          if (res.status === 201) {
            enqueueSnackbar(`${label} ${data.name} created`, {
              variant: 'success',
            });
            history.push(buildFEDetailUrl(type, data.id));
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
    </MuiPickersUtilsProvider>
  );
};

export default LocationBaseFormNew;
