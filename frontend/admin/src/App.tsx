import React from 'react';

import { Redirect, Route, Switch } from 'react-router-dom';

import LoginPage from './pages/LoginPage';
import { PagePaths } from './pages/constants';
import PrivateRoute from './components/PrivateRoute';
import PageContainer from './components/PageContainer';
import NotFoundPage from './pages/NotFoundPage';
import ProfilePage from './pages/ProfilePage';
import ShoppingPage from './pages/shopping/ShoppingPage';
import GastroPage from './pages/gastro/GastroPage';
import GastroClosed from './pages/gastro/GastroClosed';
import GastroSubmissionsPage from './pages/gastro/GastroSubmissionPage';
import GastroNewPage from './pages/gastro/GastroNewPage';
import GastroEditPage from './pages/gastro/GastroEditPage';
import ShoppingEditPage from './pages/shopping/ShoppingEditPage';
import ShoppingClosedPage from './pages/shopping/ShoppingClosedPage';
import ShoppingSubmissionPage from './pages/shopping/ShoppingSubmissionPage';
import ShoppingNewPage from './pages/shopping/ShoppingNewPage';

const App = () => (
  <Switch>
    <Route path={PagePaths.LOGIN_PAGE} exact component={LoginPage} />
    <PrivateRoute path="/*">
      <PageContainer>
        <Switch>
          <Route
            path={PagePaths.HOME}
            exact
            component={() => <Redirect to={PagePaths.GASTRO_DASHBOARD} />}
          />
          <Route
            path={PagePaths.GASTRO_DASHBOARD}
            exact
            component={GastroPage}
          />
          <Route
            path={PagePaths.GASTROS_PAGE_CLOSED}
            exact
            component={GastroClosed}
          />
          <Route
            path={PagePaths.GASTROS_PAGE_SUBMISSIONS}
            exact
            component={GastroSubmissionsPage}
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
            path={PagePaths.SHOPPING_PAGE}
            exact
            component={ShoppingPage}
          />
          <Route
            path={PagePaths.SHOPPING_CLOSED_PAGE}
            exact
            component={ShoppingClosedPage}
          />
          <Route
            path={PagePaths.SHOPPING_SUBMISSION_PAGE}
            exact
            component={ShoppingSubmissionPage}
          />
          <Route
            path={PagePaths.SHOPPING_PAGE_NEW}
            exact
            component={ShoppingNewPage}
          />
          <Route
            path={PagePaths.SHOPPING_PAGE_EDIT}
            exact
            component={ShoppingEditPage}
          />
          <Route path={PagePaths.PROFILE_PAGE} exact component={ProfilePage} />
          <Route path={PagePaths.PAGE_NOT_FOUND} component={NotFoundPage} />
        </Switch>
      </PageContainer>
    </PrivateRoute>
  </Switch>
);

export default App;
