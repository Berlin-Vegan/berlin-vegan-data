import React, { FunctionComponent, useState } from 'react';
import Container from '@material-ui/core/Container';

import AppBar from '../AppBar';
import Drawer from '../Drawer';
import { useStyles } from './styles';

const PageContainer: FunctionComponent = ({ children }) => {
  const classes = useStyles();
  const [open, setOpen] = useState(true);

  const handleDrawerOpen = (): void => {
    setOpen(true);
  };
  const handleDrawerClose = (): void => {
    setOpen(false);
  };

  return (
    <div className={classes.root}>
      <AppBar open={open} handleDrawerOpen={handleDrawerOpen} />
      <Drawer open={open} handleDrawerClose={handleDrawerClose} />
      <main className={classes.content}>
        <div className={classes.appBarSpacer} />
        <Container maxWidth="xl" className={classes.container}>
          <>{children}</>
        </Container>
      </main>
    </div>
  );
};

export default PageContainer;
