import React from 'react';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import { SnackbarProvider } from 'notistack';
import GastroFormEdit from './component';
import { standardComponentTest } from '../../utils/testing';
import GastroDetailValid from '../GastroFormBase/__tests__/fixtures/GastroDetailVaild.json';

const GASTRO_DATA = {
  created: '2000-11-22T04:01:00.000',
  updated: '2000-11-22T04:01:00.000',
  idString: '2beb528cb3fba46f6f4511ba36505f05',
  lastEditor: 'testUser',
  isSubmission: true,
  ...GastroDetailValid,
};

const ComponentWrapper = () => (
  <SnackbarProvider maxSnack={3}>
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <GastroFormEdit gastroData={GASTRO_DATA} />
    </MuiPickersUtilsProvider>
  </SnackbarProvider>
);

standardComponentTest(ComponentWrapper, GASTRO_DATA);
