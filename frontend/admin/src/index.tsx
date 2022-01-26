import React from 'react';
import ReactDOM from 'react-dom';

import * as Sentry from '@sentry/react';
import { Integrations } from '@sentry/tracing';

import CssBaseline from '@material-ui/core/CssBaseline';
import '@fontsource/roboto';
import { ThemeProvider } from '@material-ui/core/styles';
import { BrowserRouter as Router } from 'react-router-dom';
import { SnackbarProvider } from 'notistack';

import App from './App';
import * as serviceWorker from './serviceWorker';
import theme from './theme';
import 'mapbox-gl/dist/mapbox-gl.css';
import Providers from './providers';

Sentry.init({
  dsn: process.env.REACT_APP_SENTRY_DSN,
  integrations: [new Integrations.BrowserTracing()],
});

ReactDOM.render(
  <React.StrictMode>
    <Providers>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Router>
          <SnackbarProvider maxSnack={3}>
            <App />
          </SnackbarProvider>
        </Router>
      </ThemeProvider>
    </Providers>
  </React.StrictMode>,
  document.getElementById('root'),
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
