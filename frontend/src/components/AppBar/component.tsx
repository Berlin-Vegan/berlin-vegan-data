import { useContext } from 'react';

import ExitToAppIcon from '@mui/icons-material/ExitToApp';
import MenuIcon from '@mui/icons-material/Menu';
import { Button } from '@mui/material';
import MuiAppBar, { type AppBarProps as MuiAppBarProps } from '@mui/material/AppBar';
import Box from '@mui/material/Box';
import IconButton from '@mui/material/IconButton';
import Toolbar from '@mui/material/Toolbar';
import Typography from '@mui/material/Typography';
import { styled } from '@mui/material/styles';

import { drawerWidth } from '@components/PageContainer/styles';
import { pathOr } from 'ramda';

import Logo from '@/assets/berlin-vegan-logo.png';
import { AuthContext, TYPE_USER_LOGOUT, type UserDispatch } from '@/providers/UserProvider';
import { authorizedFetch } from '@/utils/fetch';

import { styles } from './styles';

interface AppBarProps extends MuiAppBarProps {
  open?: boolean;
}

const AppBar = styled(MuiAppBar, {
  shouldForwardProp: (prop) => prop !== 'open',
})<AppBarProps>(({ theme, open }) => ({
  zIndex: theme.zIndex.drawer + 1,
  transition: theme.transitions.create(['width', 'margin'], {
    easing: theme.transitions.easing.sharp,
    duration: theme.transitions.duration.leavingScreen,
  }),
  ...(open && {
    marginLeft: drawerWidth,
    width: `calc(100% - ${drawerWidth}px)`,
    transition: theme.transitions.create(['width', 'margin'], {
      easing: theme.transitions.easing.sharp,
      duration: theme.transitions.duration.enteringScreen,
    }),
  }),
}));

type AppBarComponentProps = {
  open: boolean;
  toggleDrawer: () => void;
};

const logoutUser = async (userDispatch: UserDispatch): Promise<void> => {
  const response = await authorizedFetch(userDispatch, '/api/v1/accounts/logout/', 'POST');
  if (response.ok) {
    userDispatch({ type: TYPE_USER_LOGOUT });
  }
};

const AppBarComponent = ({ open, toggleDrawer }: AppBarComponentProps) => {
  const { state, dispatch: userDispatch } = useContext(AuthContext);
  const username = pathOr('–', ['userData', 'username'], state);

  return (
    <AppBar position="absolute" open={open}>
      <Toolbar sx={styles.toolbar}>
        <IconButton
          edge="start"
          color="inherit"
          aria-label="open drawer"
          onClick={toggleDrawer}
          sx={{
            marginRight: '36px',
            ...(open && { display: 'none' }),
          }}
          size="large"
        >
          <MenuIcon />
        </IconButton>
        <Box component="img" src={Logo} alt="Berlin-Vegan Logo" sx={styles.logo} />
        <Typography component="h1" variant="h6" color="inherit" noWrap sx={styles.title}>
          Berlin-Vegan Data
        </Typography>
        <Typography>{username}</Typography>
        <Button
          variant="contained"
          color="error"
          sx={styles.logout}
          startIcon={<ExitToAppIcon />}
          onClick={() => logoutUser(userDispatch)}
        >
          Logout
        </Button>
      </Toolbar>
    </AppBar>
  );
};

export default AppBarComponent;
