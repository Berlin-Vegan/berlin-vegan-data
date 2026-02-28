import { PropsWithChildren, useState } from 'react';
import Container from '@mui/material/Container';
import Box from '@mui/material/Box';

import AppBar from '../AppBar';
import Drawer from '../Drawer';

const PageContainer = ({ children }: PropsWithChildren) => {
  const [open, setOpen] = useState(true);

  const toggleDrawer = () => {
    setOpen(!open);
  };

  return (
    <Box sx={{ display: 'flex' }}>
      <AppBar open={open} toggleDrawer={toggleDrawer} />
      <Drawer open={open} toggleDrawer={toggleDrawer} />
      <Box component="main" sx={{ flexGrow: 1, height: '100vh', overflow: 'auto' }}>
        <Box sx={(theme) => theme.mixins.toolbar} />
        <Container maxWidth="xl" sx={{ pt: 4, pb: 4 }}>
          <>{children}</>
        </Container>
      </Box>
    </Box>
  );
};

export default PageContainer;
