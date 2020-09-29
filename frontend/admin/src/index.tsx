import React from 'react';
import ReactDOM from 'react-dom';
import * as Sentry from '@sentry/react';
import CssBaseline from '@material-ui/core/CssBaseline';
import 'fontsource-roboto';
import { ThemeProvider } from '@material-ui/core/styles';
import { BrowserRouter as Router } from 'react-router-dom';
import { SnackbarProvider } from 'notistack';

import App from './App';
import * as serviceWorker from './serviceWorker';
import theme from './theme';
import 'mapbox-gl/dist/mapbox-gl.css';
import { UserProvider } from './providers/UserProvider';

Sentry.init({
  dsn: process.env.REACT_APP_SENTRY_DSN,
});

ReactDOM.render(
  <React.StrictMode>
    <UserProvider>
      <ThemeProvider theme={theme}>
        <CssBaseline />
        <Router>
          <SnackbarProvider maxSnack={3}>
            <App />
          </SnackbarProvider>
        </Router>
      </ThemeProvider>
    </UserProvider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
