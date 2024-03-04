import { PropsWithChildren } from 'react';
import { NavLink, useLocation } from 'react-router-dom';

import ListItem from '@mui/material/ListItem';

type NavListItemProps = {
  pathname: string;
};

const NavListItem = ({ children, pathname }: PropsWithChildren<NavListItemProps>) => {
  const location = useLocation();

  return (
    <ListItem button component={NavLink} to={pathname} selected={location.pathname === pathname}>
      {children}
    </ListItem>
  );
};

export default NavListItem;
