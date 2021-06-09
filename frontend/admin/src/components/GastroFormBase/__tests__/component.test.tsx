import React from 'react';
import { MuiPickersUtilsProvider } from '@material-ui/pickers';
import DateFnsUtils from '@date-io/date-fns';
import { SnackbarProvider } from 'notistack';
import GastroBaseForm from '../component';
import { standardComponentTest } from '../../../utils/testing';
import GastroDetailValid from './fixtures/GastroDetailVaild.json';
import { Wrapper } from './fields.test';

const ComponentWrapper = () => (
  <SnackbarProvider maxSnack={3}>
    <MuiPickersUtilsProvider utils={DateFnsUtils}>
      <Wrapper initial={GastroDetailValid}>
        <GastroBaseForm />
      </Wrapper>
    </MuiPickersUtilsProvider>
  </SnackbarProvider>
);

standardComponentTest(ComponentWrapper);
