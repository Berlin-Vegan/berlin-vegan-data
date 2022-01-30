import React, { FC, useContext, useEffect, useState } from 'react';

import Grid from '@material-ui/core/Grid';

import { MUIDataTableOptions } from 'mui-datatables';
import { authorizedFetch } from '../../utils/fetch';
import { AuthContext } from '../../providers/UserProvider';
import LocationTable from '../LocationTable';

type LocationListType = {
  label: string;
  url: string;
  overwriteTableOptions?: MUIDataTableOptions;
};

const LocationList: FC<LocationListType> = ({
  label,
  url,
  overwriteTableOptions = {},
}) => {
  const { dispatch } = useContext(AuthContext);
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await authorizedFetch(dispatch, url).then((res) =>
        res.json(),
      );
      setData(result);
    };

    fetchData();
  }, [dispatch, url]);
  return (
    <Grid container spacing={3}>
      <Grid item xs={12}>
        <LocationTable
          title={label}
          data={data}
          overwriteOptions={overwriteTableOptions}
        />
      </Grid>
    </Grid>
  );
};

export default LocationList;
