import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import DrawerList from './component';
import { standardComponentTest } from '../../utils/testing';

const DrawerListWrapper = () => (
  <MemoryRouter>
    <DrawerList />
  </MemoryRouter>
);

standardComponentTest(DrawerListWrapper);
