import React from 'react';

import { Paper } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import PasswordChangeForm from '../components/PasswordChangeForm';
import EmailChangeForm from '../components/EmailChangeForm';

const useStyles = makeStyles(() => ({
  paper: {
    padding: '16px',
  },
}));

const ProfilePage = () => {
  const classes = useStyles();

  return (
    <Paper className={classes.paper}>
      <PasswordChangeForm />
      <EmailChangeForm />
    </Paper>
  );
};

export default ProfilePage;
