import { PropsWithChildren, useState } from 'react';

import Container from '@mui/material/Container';

import AppBar from '../AppBar';
import Drawer from '../Drawer';
import { useStyles } from './styles';

const PageContainer = ({ children }: PropsWithChildren) => {
  const classes = useStyles();
  const [open, setOpen] = useState(true);

  const toggleDrawer = () => {
    setOpen(!open);
  };

  return (
    <div className={classes.root}>
      <AppBar open={open} toggleDrawer={toggleDrawer} />
      <Drawer open={open} toggleDrawer={toggleDrawer} />
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
