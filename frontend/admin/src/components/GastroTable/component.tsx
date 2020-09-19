import React from 'react';

import CheckIcon from '@material-ui/icons/Check';
import ClearIcon from '@material-ui/icons/Clear';
import MUIDataTable, { MUIDataTableOptions } from 'mui-datatables';
import { useHistory } from 'react-router-dom';

const veganColumnBody: any = {
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
      customBodyRender: (value: number, tableMeta: any, updateValue: any) => {
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
      customBodyRender: (value: number, tableMeta: any, updateValue: any) => {
        return value ? <CheckIcon /> : <ClearIcon />;
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

  const options: MUIDataTableOptions = {
    selectableRows: 'none',
    pagination: false,
    onRowClick: (_rowData, rowMeta) =>
      history.push(`/gastro/${data[rowMeta.dataIndex].idString}/edit`),
  };

  return (
    <MUIDataTable
      title={`Gastros (${data.length})`}
      data={data}
      columns={columns}
      options={options}
    />
  );
};

export default GastroTable;
