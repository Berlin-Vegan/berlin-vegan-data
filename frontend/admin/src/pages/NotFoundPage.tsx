import React from 'react';
import { Paper } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
  paper: {
    padding: '16px',
  },
}));

const NotFoundPage = () => {
  const classes = useStyles();

  return (
    <Paper className={classes.paper}>
      <div>Page not Found – 404 </div>
    </Paper>
  );
};

export default NotFoundPage;
