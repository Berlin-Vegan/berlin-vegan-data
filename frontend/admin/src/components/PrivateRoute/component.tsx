import React, { FunctionComponent, useContext } from 'react';

import { Route, Redirect, RouteProps } from 'react-router-dom';

import { PagePaths } from '../../pages/constants';
import { AuthContext } from '../../providers/UserProvider';

const PrivateRoute: FunctionComponent<RouteProps> = ({ children, ...rest }) => {
  const { state: authState } = useContext(AuthContext);
  return authState.authenticated ? (
    <Route {...rest} render={() => children} />
  ) : (
    <Redirect to={PagePaths.LOGIN_PAGE} />
  );
};

export default PrivateRoute;
