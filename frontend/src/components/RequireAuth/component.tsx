import { useContext } from 'react';
import { Navigate } from 'react-router-dom';

import { PagePaths } from '@/pages/constants';
import { AuthContext } from '@/providers/UserProvider';

const RequireAuth = ({ children }: { children: JSX.Element }) => {
  const { state: authState } = useContext(AuthContext);
  return authState.authenticated ? children : <Navigate to={PagePaths.LOGIN_PAGE} />;
};

export default RequireAuth;
