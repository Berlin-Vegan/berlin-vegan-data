import React from 'react';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import { SnackbarProvider } from 'notistack';
import { standardComponentTest } from '../../utils/testing';
import { Wrapper } from '../GastroFormBase/__tests__/fields.test';
import LocationFormBase from './component';
import { BASE_BOOLEAN_ATTRIBUTES } from './formSchema';
import {
  initialLocationBooleanAttributeData,
  initialLocationData,
} from '../LocationBaseFormNew/initialData';

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
        />
      </Wrapper>
    </MuiPickersUtilsProvider>
  </SnackbarProvider>
);

standardComponentTest(ComponentWrapper);
