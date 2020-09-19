import React, { FunctionComponent } from 'react';
import clsx from 'clsx';
import IconButton from '@material-ui/core/IconButton';
import ChevronLeftIcon from '@material-ui/icons/ChevronLeft';
import Divider from '@material-ui/core/Divider';
import Drawer from '@material-ui/core/Drawer';
import { useStyles } from './styles';
import DrawerList from '../DrawerList';

type DrawerComponentProps = {
  open: boolean;
  handleDrawerClose: () => void;
};

const DrawerComponent: FunctionComponent<DrawerComponentProps> = ({
  open,
  handleDrawerClose,
}) => {
  const classes = useStyles();

  return (
    <Drawer
      variant="permanent"
      classes={{
        paper: clsx(classes.drawerPaper, !open && classes.drawerPaperClose),
      }}
      open={open}
    >
      <div className={classes.toolbarIcon}>
        <IconButton onClick={handleDrawerClose}>
          <ChevronLeftIcon />
        </IconButton>
      </div>
      <Divider />
      <DrawerList />
    </Drawer>
  );
};

export default DrawerComponent;
