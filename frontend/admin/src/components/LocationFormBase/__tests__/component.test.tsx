import React from 'react';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import { SnackbarProvider } from 'notistack';
import { standardComponentTest } from '../../../utils/testing';
import { Wrapper } from './fields.test';
import LocationFormBase from '../component';
import { BASE_BOOLEAN_ATTRIBUTES } from '../formSchema';
import {
  initialLocationBooleanAttributeData,
  initialLocationData,
} from '../../LocationBaseFormNew/initialData';
import { GASTRO_POSITIVE_INTEGER_ATTRIBUTES } from '../../GastroFormBase/gastroFormSchema';

const initialFormData = {
  ...initialLocationData,
  attributes: {
    ...initialLocationBooleanAttributeData,
  },
};

const ComponentWrapper = () => (
  <SnackbarProvider maxSnack={3}>
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Wrapper initial={initialFormData}>
        <LocationFormBase
          booleanAttrList={BASE_BOOLEAN_ATTRIBUTES}
          tagList={['testTag']}
          positiveIntegerAttrList={GASTRO_POSITIVE_INTEGER_ATTRIBUTES}
        />
      </Wrapper>
    </MuiPickersUtilsProvider>
  </SnackbarProvider>
);

standardComponentTest(ComponentWrapper);
