import React from 'react';
import { Route, Switch } from 'react-router-dom';
import Dashboard from './pages/Dashboard';
import LoginPage from './pages/LoginPage';
import { PagePaths } from './pages/constants';
import PrivateRoute from './components/PrivateRoute';
import PageContainer from './components/PageContainer';
import GastroNewPage from './pages/GastroNewPage';
import GastroEditPage from './pages/GastroEditPage';
import NotFoundPage from './pages/NotFoundPage';
import GastroClosed from './pages/GastroClosed';
import Submissions from './pages/Submissions';
import ProfilePage from './pages/ProfilePage';

const App = () => {
  return (
    <Switch>
      <Route path={PagePaths.LOGIN_PAGE} exact component={LoginPage} />
      <PrivateRoute path="/*">
        <PageContainer>
          <Switch>
            <Route
              path={PagePaths.DASHBOARD_PAGE}
              exact
              component={Dashboard}
            />
            <Route
              path={PagePaths.GASTROS_PAGE_CLOSED}
              exact
              component={GastroClosed}
            />
            <Route
              path={PagePaths.GASTROS_PAGE_SUBMISSIONS}
              exact
              component={Submissions}
            />
            <Route
              path={PagePaths.GASTRO_PAGE_NEW}
              exact
              component={GastroNewPage}
            />
            <Route
              path={PagePaths.GASTRO_PAGE_EDIT}
              exact
              component={GastroEditPage}
            />
            <Route
              path={PagePaths.PROFILE_PAGE}
              exact
              component={ProfilePage}
            />
            <Route path={PagePaths.PAGE_NOT_FOUND} component={NotFoundPage} />
          </Switch>
        </PageContainer>
      </PrivateRoute>
    </Switch>
  );
};

export default App;
