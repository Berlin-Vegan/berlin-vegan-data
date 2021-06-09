import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import DrawerComponent from './component';
import { standardComponentTest } from '../../utils/testing';

const BaseFormWrapper = (props: {
  open: boolean;
  handleDrawerClose: () => void;
}) => (
  <MemoryRouter>
    <DrawerComponent {...props} />
  </MemoryRouter>
);

standardComponentTest(BaseFormWrapper, {
  open: true,
  handleDrawerClose: () => {},
});
