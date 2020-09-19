import React from 'react';
import ReactDOM from 'react-dom';
import * as Sentry from '@sentry/react';
import CssBaseline from '@material-ui/core/CssBaseline';
import 'fontsource-roboto';
import { ThemeProvider } from '@material-ui/core/styles';
import { Provider } from 'react-redux';
import { BrowserRouter as Router } from 'react-router-dom';
import { PersistGate } from 'redux-persist/integration/react';
import { SnackbarProvider } from 'notistack';
import { persistor, store } from './store/store';

import App from './App';
import * as serviceWorker from './serviceWorker';
import theme from './theme';
import 'mapbox-gl/dist/mapbox-gl.css';

Sentry.init({
  dsn: process.env.REACT_APP_SENTRY_DSN,
});

ReactDOM.render(
  <React.StrictMode>
    <Provider store={store}>
      <PersistGate loading={null} persistor={persistor}>
        <ThemeProvider theme={theme}>
          <CssBaseline />
          <Router>
            <SnackbarProvider maxSnack={3}>
              <App />
            </SnackbarProvider>
          </Router>
        </ThemeProvider>
      </PersistGate>
    </Provider>
  </React.StrictMode>,
  document.getElementById('root')
);

// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
