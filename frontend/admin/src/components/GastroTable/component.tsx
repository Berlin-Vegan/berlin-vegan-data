import React, { useContext, useState } from 'react';

import CheckIcon from '@material-ui/icons/Check';
import ClearIcon from '@material-ui/icons/Clear';
import MUIDataTable, {
  MUIDataTableColumnDef,
  MUIDataTableOptions,
} from 'mui-datatables';
import { useHistory } from 'react-router-dom';
import { assocPath } from 'ramda';
import { FilterContext } from '../../providers/FilterProvider';
import { mapIndexed, nthOr } from '../../utils/fp';

type VeganColumnBody = {
  [index: number]: string;
};

const veganColumnBody: VeganColumnBody = {
  2: 'Ominvore (vegan labeled)',
  4: 'Vegetarian (vegan labeled)',
  5: 'Vegan',
};

const columns = [
  {
    name: 'name',
    label: 'Name',
    options: {
      filter: false,
      sort: true,
    },
  },
  {
    name: 'street',
    label: 'Street',
    options: {
      filter: false,
      sort: true,
      searchable: false,
    },
  },
  {
    name: 'postalCode',
    label: 'Postal Code',
    options: {
      filter: false,
      sort: true,
      searchable: false,
    },
  },
  {
    name: 'vegan',
    label: 'Vegan',
    options: {
      filter: true,
      sort: true,
      searchable: false,
      customBodyRender: (
        value: number,
        tableMeta: never,
        updateValue: never
      ) => {
        return veganColumnBody[value];
      },
    },
  },
  {
    name: 'hasReviewLink',
    label: 'Review',
    options: {
      filter: true,
      sort: true,
      searchable: false,
      customBodyRender: (
        value: number,
        tableMeta: never,
        updateValue: never
      ) => {
        return value ? <CheckIcon /> : <ClearIcon />;
      },
      filterOptions: {
        renderValue: (v: boolean) => (v ? 'Review' : 'No Review'),
      },
      customFilterListOptions: {
        render: (v: boolean) => (v ? 'Review' : 'No Review'),
      },
    },
  },
];

type GastroData = {
  idString: string;
  lastEdit: number;
  created: string;
  updated: string;
  name: string;
  cityCode: string;
  city: string;
  latCoord: number;
  longCoord: number;
  telephone: string;
  website: string;
  email: string | null;
  hasSticker: boolean;
  vegan: number;
  hasReviewLink: boolean;
};

interface IGastroTableProps {
  data: Array<GastroData>;
}

const GastroTable = ({ data }: IGastroTableProps) => {
  const history = useHistory();
  const { filterState, setFilterState } = useContext(FilterContext);
  const [countState, setCountState] = useState(0);

  const options: MUIDataTableOptions = {
    selectableRows: 'none',
    pagination: false,
    onRowClick: (_rowData, rowMeta) =>
      history.push(`/gastro/${data[rowMeta.dataIndex].idString}/edit`),
    onFilterChange: (_changedColumn, filterList: any[], _type) =>
      setFilterState(filterList),
    onTableChange: (action, { displayData }) =>
      setCountState(displayData.length),
  };

  const columnsWithFilter: MUIDataTableColumnDef[] = mapIndexed((column, idx) =>
    assocPath(['options', 'filterList'], nthOr([], idx)(filterState), column)
  )(columns);

  return (
    <MUIDataTable
      title={`Gastros (${countState})`}
      data={data}
      columns={columnsWithFilter}
      options={options}
    />
  );
};

export default GastroTable;
