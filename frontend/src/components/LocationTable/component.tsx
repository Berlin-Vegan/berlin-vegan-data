import { useContext } from 'react';
import { useNavigate } from 'react-router-dom';

import { DataGrid, GridColDef, GridEventListener, GridToolbar } from '@mui/x-data-grid';

import { FilterContext } from '@/providers/FilterProvider';
import { LocationType } from '@/utils/constants';
import { buildFEDetailUrl } from '@/utils/utils';

type LocationListData = {
  id: string;
  name: string;
  street: string;
  postalCode: string;
  city: string;
  vegan: number;
  hasReviewLink: boolean;
};

export interface ILocationTableProps {
  data: LocationListData[];
  type: LocationType;
}

const LocationTable = ({ data, type }: ILocationTableProps) => {
  const navigate = useNavigate();
  const { filterState, setFilterState } = useContext(FilterContext);

  const columns: GridColDef[] = [
    { field: 'name', headerName: 'Name', flex: 1, type: 'string' },
    { field: 'street', headerName: 'Street', flex: 1, type: 'string' },
    { field: 'postalCode', headerName: 'Postal Code', flex: 0.3, type: 'string' },
    {
      field: 'hasReviewLink',
      headerName: 'Review',
      flex: 0.3,
      type: 'boolean',
    },
  ];

  const handleRowClick: GridEventListener<'rowClick'> = (params) => {
    navigate(buildFEDetailUrl(type, params.id as string));
  };

  return (
    <DataGrid
      rows={data}
      columns={columns}
      disableColumnFilter
      disableColumnSelector
      disableDensitySelector
      slots={{ toolbar: GridToolbar }}
      slotProps={{
        toolbar: {
          showQuickFilter: true,
          csvOptions: {
            fileName: `${type.toLowerCase()}`,
          },
        },
      }}
      onRowClick={handleRowClick}
      sortModel={filterState}
      onSortModelChange={(newSortModel) => setFilterState(newSortModel)}
    />
  );
};

export default LocationTable;
