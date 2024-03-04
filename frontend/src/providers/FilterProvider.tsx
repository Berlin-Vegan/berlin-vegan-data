import {
  Context,
  Dispatch,
  PropsWithChildren,
  SetStateAction,
  createContext,
  useState,
} from 'react';

import { GridSortModel } from '@mui/x-data-grid';

interface IFilterContext {
  filterState: GridSortModel;
  setFilterState: Dispatch<SetStateAction<GridSortModel>>;
}

const FilterContext: Context<IFilterContext> = createContext({} as IFilterContext);

const FilterProvider = ({ children }: PropsWithChildren) => {
  const [filterState, setFilterState] = useState<GridSortModel>([]);

  return (
    <FilterContext.Provider
      value={{
        filterState,
        setFilterState,
      }}
    >
      {children}
    </FilterContext.Provider>
  );
};

export { FilterContext, FilterProvider };
