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
import { ListSubheader } from '@material-ui/core';
import NavListItem from '../NavListItem';
import { PagePaths } from '../../pages/constants';

const gastroListItems = (
  <>
    <ListSubheader>Gastro</ListSubheader>
    <NavListItem pathname={PagePaths.GASTRO_DASHBOARD}>
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

const shoppingListItems = (
  <>
    <ListSubheader>Shopping (Test/Not Live)</ListSubheader>
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
    <NavListItem pathname={PagePaths.SHOPPING_PAGE_NEW}>
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
