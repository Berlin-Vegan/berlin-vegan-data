import React from 'react';
import { Paper } from '@material-ui/core';

import { makeStyles } from '@material-ui/core/styles';
import GastroFormNew from '../../components/GastroFormNew';

const useStyles = makeStyles(() => ({
  paper: {
    padding: '16px',
  },
}));

const GastroNewPage = () => {
  const classes = useStyles();
  return (
    <Paper className={classes.paper}>
      <GastroFormNew />
    </Paper>
  );
};

export default GastroNewPage;
