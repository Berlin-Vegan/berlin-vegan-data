import React, { Dispatch, SetStateAction, useContext, useState } from 'react';
import Avatar from '@mui/material/Avatar';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import { Typography } from '@mui/material';
import TextField from '@mui/material/TextField';
import Button from '@mui/material/Button';
import clsx from 'clsx';
import { __, propOr, isEmpty, assoc, ifElse } from 'ramda';
import useStyles from './styles';
import {
  AuthContext,
  TYPE_SET_USER_DATA,
  TYPE_USER_LOGIN,
  UserDispatch,
} from '@/providers/UserProvider';
import { authorizedFetch } from '@/utils/fetch';
import { getCSRFToken } from '@/utils/cookie';

const getUserData = (userDispatch: UserDispatch) =>
  authorizedFetch(userDispatch, '/api/v1/accounts/profile/').then((res) => res.json());

const initialHeader = { 'Content-Type': 'application/json' };
const setCSRFToken = assoc('X-CSRFToken', __, initialHeader);
const getHeader = ifElse(
  (x: string) => !isEmpty(x),
  (x) => setCSRFToken(x),
  () => initialHeader,
);

const login = async (
  username: string,
  password: string,
  setErrors: Dispatch<SetStateAction<IErrorsState>>,
  userDispatch: UserDispatch,
): Promise<void> => {
  const response = await fetch('/api/v1/accounts/login/', {
    method: 'POST',
    headers: getHeader(getCSRFToken()),
    body: JSON.stringify({ login: username, password }),
  });

  if (response.status === 200) {
    userDispatch({ type: TYPE_USER_LOGIN });
    const userData = await getUserData(userDispatch);
    userDispatch({ type: TYPE_SET_USER_DATA, payload: userData });
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
  const { dispatch: userDispatch } = useContext(AuthContext);
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
    login(formState.username, formState.password, setErrors, userDispatch);
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
            errorsState.detail && classes.error,
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
