import React, { FunctionComponent } from 'react';

import { useSelector } from 'react-redux';
import { Route, Redirect, RouteProps } from 'react-router-dom';
import { IAppState } from '../../store/store';
import { PagePaths } from '../../pages/constants';

const PrivateRoute: FunctionComponent<RouteProps> = ({ children, ...rest }) => {
  const authenticated = useSelector(
    (state: IAppState) => state.userState.authenticated
  );
  return authenticated ? (
    <Route {...rest} render={() => children} />
  ) : (
    <Redirect to={PagePaths.LOGIN_PAGE} />
  );
};

export default PrivateRoute;
