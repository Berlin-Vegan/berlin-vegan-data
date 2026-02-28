import { PropsWithChildren } from 'react';
import { NavLink, useLocation } from 'react-router-dom';

import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';

type NavListItemProps = {
  pathname: string;
};

const NavListItem = ({ children, pathname }: PropsWithChildren<NavListItemProps>) => {
  const location = useLocation();

  return (
    <ListItem disablePadding>
      <ListItemButton component={NavLink} to={pathname} selected={location.pathname === pathname}>
        {children}
      </ListItemButton>
    </ListItem>
  );
};

export default NavListItem;
