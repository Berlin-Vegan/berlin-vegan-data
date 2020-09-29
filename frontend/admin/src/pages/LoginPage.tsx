import React, { useContext } from 'react';
import Container from '@material-ui/core/Container';
import { Redirect } from 'react-router-dom';
import LoginForm from '../components/LoginForm';
import { AuthContext } from '../providers/UserProvider';

const LoginPageComponent = () => (
  <Container component="main" maxWidth="xs">
    <LoginForm />
  </Container>
);

const LoginPage = () => {
  const { state } = useContext(AuthContext);

  return state.authenticated ? (
    <Redirect push to="/" />
  ) : (
    <LoginPageComponent />
  );
};

export default LoginPage;
