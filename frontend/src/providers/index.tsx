import { PropsWithChildren } from 'react';

import { FilterProvider } from './FilterProvider';
import { UserProvider } from './UserProvider';

const Providers = ({ children }: PropsWithChildren) => (
  <UserProvider>
    <FilterProvider>{children}</FilterProvider>
  </UserProvider>
);
export default Providers;
