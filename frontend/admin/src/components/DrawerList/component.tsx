import React from 'react';
import ListItemIcon from '@material-ui/core/ListItemIcon';
import DashboardIcon from '@material-ui/icons/Dashboard';
import ListItemText from '@material-ui/core/ListItemText';
import CloseIcon from '@material-ui/icons/Close';
import ListIcon from '@material-ui/icons/List';
import AddIcon from '@material-ui/icons/Add';
import AccountBoxIcon from '@material-ui/icons/AccountBox';
import List from '@material-ui/core/List';
import Divider from '@material-ui/core/Divider';
import NavListItem from '../NavListItem';
import { PagePaths } from '../../pages/constants';

const mainListItem = (
  <>
    <NavListItem pathname={PagePaths.DASHBOARD_PAGE}>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Dashboard" />
    </NavListItem>
    <NavListItem pathname={PagePaths.GASTROS_PAGE_CLOSED}>
      <ListItemIcon>
        <CloseIcon />
      </ListItemIcon>
      <ListItemText primary="Closed" />
    </NavListItem>
    <NavListItem pathname={PagePaths.GASTROS_PAGE_SUBMISSIONS}>
      <ListItemIcon>
        <ListIcon />
      </ListItemIcon>
      <ListItemText primary="Submissions" />
    </NavListItem>
    <NavListItem pathname={PagePaths.GASTRO_PAGE_NEW}>
      <ListItemIcon>
        <AddIcon />
      </ListItemIcon>
      <ListItemText primary="New" />
    </NavListItem>
  </>
);

const secondaryListItems = (
  <NavListItem pathname={PagePaths.PROFILE_PAGE}>
    <ListItemIcon>
      <AccountBoxIcon />
    </ListItemIcon>
    <ListItemText primary="Profile" />
  </NavListItem>
);

const DrawerList = () => (
  <>
    <List>{mainListItem}</List>
    <Divider />
    <List>{secondaryListItems}</List>
  </>
);

export default DrawerList;
