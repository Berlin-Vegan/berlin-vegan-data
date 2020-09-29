import React, {
  Context,
  createContext,
  Dispatch,
  SetStateAction,
  useState,
} from 'react';
import { MUIDataTableColumnDef } from 'mui-datatables';

type FilterState = MUIDataTableColumnDef[];

interface IFilterContext {
  filterState: FilterState;
  setFilterState: Dispatch<SetStateAction<FilterState>>;
}

const FilterContext: Context<IFilterContext> = createContext(
  {} as IFilterContext
);

const FilterProvider: React.FC = ({ children }) => {
  const [filterState, setFilterState] = useState<FilterState>([]);

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
