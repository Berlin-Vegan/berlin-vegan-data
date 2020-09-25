import React, { Dispatch, SetStateAction, useState } from 'react';
import Avatar from '@material-ui/core/Avatar';
import LockOutlinedIcon from '@material-ui/icons/LockOutlined';
import { Typography } from '@material-ui/core';
import TextField from '@material-ui/core/TextField';
import Button from '@material-ui/core/Button';
import clsx from 'clsx';
import { propOr, __ } from 'ramda';
import useStyles from './styles';
import { store } from '../../store/store';

const login = async (
  username: string,
  password: string,
  setErrors: Dispatch<SetStateAction<IErrorsState>>
): Promise<void> => {
  const response = await fetch('/api/v1/accounts/login/', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ login: username, password }),
  });

  if (response.status === 200) {
    store.dispatch({ type: 'LOGIN_USER' });
  } else {
    const errors = await response.json();
    const propEmpty = propOr('', __, errors);

    setErrors({
      detail: propEmpty('detail'),
      login: propEmpty('login'),
      password: propEmpty('password'),
    });
  }
};

interface IErrorsState {
  detail: string;
  login: string;
  password: string;
}

const LoginForm = () => {
  const classes = useStyles();
  const [formState, setFormState] = useState({ username: '', password: '' });
  const [errorsState, setErrors] = useState<IErrorsState>({
    detail: '',
    login: '',
    password: '',
  });

  const handleFormChange = (e: React.ChangeEvent<HTMLInputElement>) =>
    setFormState({ ...formState, [e.target.name]: e.target.value });
  const handleButtonClick = (e: React.MouseEvent) => {
    e.preventDefault();
    login(formState.username, formState.password, setErrors);
  };

  return (
    <div className={classes.paper}>
      <Avatar className={classes.avatar}>
        <LockOutlinedIcon />
      </Avatar>
      <Typography component="h1" variant="h5">
        Sign in
      </Typography>
      <form className={classes.form}>
        <Typography
          variant="subtitle1"
          className={clsx(
            !errorsState.detail && classes.noError,
            errorsState.detail && classes.error
          )}
        >
          {errorsState.detail}
        </Typography>
        <TextField
          error={!!errorsState.login}
          variant="outlined"
          margin="normal"
          required
          fullWidth
          id="username"
          label="Username"
          name="username"
          autoComplete="username"
          autoFocus
          onChange={handleFormChange}
          helperText={errorsState.login}
        />
        <TextField
          error={!!errorsState.password}
          variant="outlined"
          margin="normal"
          required
          fullWidth
          name="password"
          label="Password"
          type="password"
          id="password"
          autoComplete="current-password"
          onChange={handleFormChange}
          helperText={errorsState.password}
        />
        <Button
          type="submit"
          fullWidth
          variant="contained"
          color="primary"
          className={classes.submit}
          onClick={handleButtonClick}
        >
          Sign In
        </Button>
      </form>
    </div>
  );
};

export default LoginForm;