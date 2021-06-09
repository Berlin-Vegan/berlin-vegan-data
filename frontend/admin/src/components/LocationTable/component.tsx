import React, { FC, useContext, useState } from 'react';

import CheckIcon from '@material-ui/icons/Check';
import ClearIcon from '@material-ui/icons/Clear';
import MUIDataTable, {
  MUIDataTableColumnDef,
  MUIDataTableOptions,
} from 'mui-datatables';
import { useHistory } from 'react-router-dom';
import { assocPath, hasPath, ifElse, path } from 'ramda';
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
      customBodyRender: (value: number, tableMeta: never, updateValue: never) =>
        veganColumnBody[value],
    },
  },
  {
    name: 'hasReviewLink',
    label: 'Review',
    options: {
      filter: true,
      sort: true,
      searchable: false,
      customBodyRender: (value: number, tableMeta: never, updateValue: never) =>
        value ? <CheckIcon /> : <ClearIcon />,
      filterOptions: {
        renderValue: (v: boolean) => (v ? 'Review' : 'No Review'),
      },
      customFilterListOptions: {
        render: (v: boolean) => (v ? 'Review' : 'No Review'),
      },
    },
  },
];

type LocationListData = {
  id?: string;
  idString?: string;
  name: string;
  postalCode: string;
  city: string;
  vegan: number;
  hasReviewLink: boolean;
};

export interface ILocationTableProps {
  title: string;
  data: LocationListData[];
}

const getID = ifElse(hasPath(['id']), path(['id']), path(['idString']));

const LocationTable: FC<ILocationTableProps> = ({ title, data }) => {
  const history = useHistory();
  const { filterState, setFilterState } = useContext(FilterContext);
  const [countState, setCountState] = useState(0);

  const options: MUIDataTableOptions = {
    selectableRows: 'none',
    pagination: false,
    onRowClick: (_rowData, rowMeta) =>
      history.push(
        `/${title.toLowerCase()}/${getID(data[rowMeta.dataIndex])}/edit`,
      ),
    onFilterChange: (_changedColumn, filterList, _type) =>
      setFilterState(filterList),
    onTableChange: (action, { displayData }) =>
      setCountState(displayData.length),
  };

  const columnsWithFilter: MUIDataTableColumnDef[] = mapIndexed((column, idx) =>
    assocPath(['options', 'filterList'], nthOr([], idx)(filterState), column),
  )(columns);

  return (
    <MUIDataTable
      title={`${title} (${countState})`}
      data={data}
      columns={columnsWithFilter}
      options={options}
    />
  );
};

export default LocationTable;
