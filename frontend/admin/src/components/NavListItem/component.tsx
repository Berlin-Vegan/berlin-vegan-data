import React, { FunctionComponent } from 'react';
import { NavLink, useLocation } from 'react-router-dom';
import ListItem from '@material-ui/core/ListItem';

type NavListItemProps = {
  pathname: string;
};

const NavListItem: FunctionComponent<NavListItemProps> = ({
  children,
  pathname,
}) => {
  const location = useLocation();

  return (
    <ListItem
      button
      component={NavLink}
      to={pathname}
      selected={location.pathname === pathname}
    >
      {children}
    </ListItem>
  );
};

export default NavListItem;
