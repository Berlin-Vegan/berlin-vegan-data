import React, { FunctionComponent } from 'react';
import clsx from 'clsx';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import IconButton from '@material-ui/core/IconButton';
import MenuIcon from '@material-ui/icons/Menu';
import ExitToAppIcon from '@material-ui/icons/ExitToApp';
import { Button } from '@material-ui/core';

import { useStyles } from './styles';
import Logo from '../../berlin-vegan-logo.png';
import { authorizedFetch } from '../../utils/fetch';
import { store } from '../../store/store';

type AppBarComponentProps = {
  open: boolean;
  handleDrawerOpen: () => void;
};

const logoutUser = async (): Promise<void> => {
  const response = await authorizedFetch('/api/v1/accounts/logout/', 'POST');
  if (response.ok) {
    store.dispatch({ type: 'LOGOUT_USER' });
  }
};

const AppBarComponent: FunctionComponent<AppBarComponentProps> = ({
  open,
  handleDrawerOpen,
}) => {
  const classes = useStyles();

  return (
    <AppBar
      position="absolute"
      className={clsx(classes.appBar, open && classes.appBarShift)}
    >
      <Toolbar className={classes.toolbar}>
        <IconButton
          edge="start"
          color="inherit"
          aria-label="open drawer"
          onClick={handleDrawerOpen}
          className={clsx(classes.menuButton, open && classes.menuButtonHidden)}
        >
          <MenuIcon />
        </IconButton>
        <img src={Logo} alt="Berlin-Vegan Logo" className={classes.logo} />
        <Typography
          component="h1"
          variant="h6"
          color="inherit"
          noWrap
          className={classes.title}
        >
          Berlin-Vegan Data
        </Typography>
        <Button
          variant="contained"
          color="secondary"
          className={classes.logout}
          startIcon={<ExitToAppIcon />}
          onClick={logoutUser}
        >
          Logout
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default AppBarComponent;
