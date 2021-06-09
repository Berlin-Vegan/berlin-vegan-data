import React from 'react';
import { SnackbarProvider } from 'notistack';
import { standardComponentTest } from '../../utils/testing';
import EmailChangeForm from './component';

const EmailChangeFormWrapper = (initial: object) => (
  <SnackbarProvider maxSnack={3}>
    <EmailChangeForm />
  </SnackbarProvider>
);

standardComponentTest(EmailChangeFormWrapper);
