import React from 'react';
import Container from '@material-ui/core/Container';
import { useSelector } from 'react-redux';
import { Redirect } from 'react-router-dom';
import LoginForm from '../components/LoginForm';
import { IAppState } from '../store/store';

const LoginPageComponent = () => (
  <Container component="main" maxWidth="xs">
    <LoginForm />
  </Container>
);

const LoginPage = () => {
  const authenticated = useSelector(
    (state: IAppState) => state.userState.authenticated
  );
  return authenticated ? <Redirect push to="/" /> : <LoginPageComponent />;
};

export default LoginPage;
