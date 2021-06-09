import React, { FC } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Paper } from '@material-ui/core';

const useStyles = makeStyles(() => ({
  paper: {
    padding: '16px',
  },
}));

const PaperDefault: FC = ({ children }) => {
  const classes = useStyles();
  return <Paper className={classes.paper}>{children}</Paper>;
};

export default PaperDefault;
