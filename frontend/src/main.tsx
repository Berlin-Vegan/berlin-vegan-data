import React from 'react';
import ReactDOM from 'react-dom/client';
import { BrowserRouter as Router } from 'react-router-dom';

import CssBaseline from '@mui/material/CssBaseline';
import { StyledEngineProvider, ThemeProvider } from '@mui/material/styles';

import * as Sentry from '@sentry/react';
import '@fontsource/roboto';
import { SnackbarProvider } from 'notistack';

import App from './App';
import Providers from './providers';
import theme from './theme';

Sentry.init({
  dsn: import.meta.env.VITE_SENTRY_DSN,
});

ReactDOM.createRoot(document.getElementById('root') as HTMLElement).render(
  <React.StrictMode>
    <Providers>
      <StyledEngineProvider injectFirst>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <Router>
            <SnackbarProvider maxSnack={3}>
              <App />
            </SnackbarProvider>
          </Router>
        </ThemeProvider>
      </StyledEngineProvider>
    </Providers>
  </React.StrictMode>,
);
