import React from 'react';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import { SnackbarProvider } from 'notistack';
import GastroFormNew from './component';
import { standardComponentTest } from '../../utils/testing';

const ComponentWrapper = () => (
  <SnackbarProvider maxSnack={3}>
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <GastroFormNew />
    </MuiPickersUtilsProvider>
  </SnackbarProvider>
);

standardComponentTest(ComponentWrapper);
