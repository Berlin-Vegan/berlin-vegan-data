import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import { standardComponentTest } from '../../utils/testing';
import NavListItem from './component';

const NavListItemWrapper = () => (
  <MemoryRouter>
    <NavListItem pathname="test" />
  </MemoryRouter>
);

standardComponentTest(NavListItemWrapper);
