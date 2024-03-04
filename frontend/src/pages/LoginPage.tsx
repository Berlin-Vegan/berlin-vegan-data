import { useContext } from 'react';
import { Navigate } from 'react-router-dom';

import Container from '@mui/material/Container';

import LoginForm from '@/components/LoginForm';
import { AuthContext } from '@/providers/UserProvider';

const LoginPageComponent = () => (
  <Container component="main" maxWidth="xs">
    <LoginForm />
  </Container>
);

const LoginPage = () => {
  const { state } = useContext(AuthContext);

  return state.authenticated ? <Navigate to="/" /> : <LoginPageComponent />;
};

export default LoginPage;
