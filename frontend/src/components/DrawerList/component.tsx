import React from 'react';

import AccountBoxIcon from '@mui/icons-material/AccountBox';
import AddIcon from '@mui/icons-material/Add';
import CloseIcon from '@mui/icons-material/Close';
import DashboardIcon from '@mui/icons-material/Dashboard';
import ListIcon from '@mui/icons-material/List';
import { ListSubheader } from '@mui/material';
import Divider from '@mui/material/Divider';
import List from '@mui/material/List';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';

import NavListItem from '@components/NavListItem';

import { PagePaths } from '@/pages/constants';

const gastroListItems = (
  <>
    <ListSubheader>Gastro</ListSubheader>
    <NavListItem pathname={PagePaths.GASTRO_DASHBOARD}>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Dashboard" />
    </NavListItem>
    <NavListItem pathname={PagePaths.GASTROS_CLOSED_PAGE}>
      <ListItemIcon>
        <CloseIcon />
      </ListItemIcon>
      <ListItemText primary="Closed" />
    </NavListItem>
    <NavListItem pathname={PagePaths.GASTROS_SUBMISSIONS_PAGE}>
      <ListItemIcon>
        <ListIcon />
      </ListItemIcon>
      <ListItemText primary="Submissions" />
    </NavListItem>
    <NavListItem pathname={PagePaths.GASTRO_NEW_PAGE}>
      <ListItemIcon>
        <AddIcon />
      </ListItemIcon>
      <ListItemText primary="New" />
    </NavListItem>
  </>
);

const shoppingListItems = (
  <>
    <ListSubheader>Shopping</ListSubheader>
    <NavListItem pathname={PagePaths.SHOPPING_PAGE}>
      <ListItemIcon>
        <DashboardIcon />
      </ListItemIcon>
      <ListItemText primary="Dashboard" />
    </NavListItem>
    <NavListItem pathname={PagePaths.SHOPPING_CLOSED_PAGE}>
      <ListItemIcon>
        <CloseIcon />
      </ListItemIcon>
      <ListItemText primary="Closed" />
    </NavListItem>
    <NavListItem pathname={PagePaths.SHOPPING_SUBMISSION_PAGE}>
      <ListItemIcon>
        <ListIcon />
      </ListItemIcon>
      <ListItemText primary="Submissions" />
    </NavListItem>
    <NavListItem pathname={PagePaths.SHOPPING_NEW_PAGE}>
      <ListItemIcon>
        <AddIcon />
      </ListItemIcon>
      <ListItemText primary="New" />
    </NavListItem>
  </>
);

const settingsItemsList = (
  <NavListItem pathname={PagePaths.PROFILE_PAGE}>
    <ListItemIcon>
      <AccountBoxIcon />
    </ListItemIcon>
    <ListItemText primary="Profile" />
  </NavListItem>
);

const DrawerList = () => (
  <>
    <List>{gastroListItems}</List>
    <Divider />
    <List>{shoppingListItems}</List>
    <Divider />
    <List>{settingsItemsList}</List>
  </>
);

export default DrawerList;
