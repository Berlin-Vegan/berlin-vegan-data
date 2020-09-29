import React from 'react';
import { UserProvider } from './UserProvider';
import { FilterProvider } from './FilterProvider';

const Providers: React.FC = ({ children }) => (
  <UserProvider>
    <FilterProvider>{children}</FilterProvider>
  </UserProvider>
);
export default Providers;
