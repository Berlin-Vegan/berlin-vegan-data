import React from 'react';

import { styled } from '@mui/material/styles';

import { Paper } from '@mui/material';
const PREFIX = 'NotFoundPage';

const classes = {
  paper: `${PREFIX}-paper`
};

const StyledPaper = styled(Paper)(() => ({
  [`&.${classes.paper}`]: {
    padding: '16px',
  }
}));

const NotFoundPage = () => {


  return (
    <StyledPaper className={classes.paper}>
      <div>Page not Found – 404 </div>
    </StyledPaper>
  );
};

export default NotFoundPage;
