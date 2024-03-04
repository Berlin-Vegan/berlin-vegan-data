import React from 'react';

import { styled } from '@mui/material/styles';

import { Paper } from '@mui/material';

import EmailChangeForm from '@/components/EmailChangeForm';
import PasswordChangeForm from '@/components/PasswordChangeForm';

const PREFIX = 'ProfilePage';

const classes = {
  paper: `${PREFIX}-paper`
};

const StyledPaper = styled(Paper)(() => ({
  [`&.${classes.paper}`]: {
    padding: '16px',
  }
}));

const ProfilePage = () => {


  return (
    <StyledPaper className={classes.paper}>
      <PasswordChangeForm />
      <EmailChangeForm />
    </StyledPaper>
  );
};

export default ProfilePage;
