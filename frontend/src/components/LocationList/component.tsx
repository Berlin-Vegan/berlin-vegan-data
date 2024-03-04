import { useContext, useEffect, useState } from 'react';

import Grid from '@mui/material/Grid';
import Typography from '@mui/material/Typography';

import LocationTable from '@components/LocationTable';

import { AuthContext } from '@/providers/UserProvider';
import { LocationType } from '@/utils/constants';
import { authorizedFetch } from '@/utils/fetch';

type LocationListType = {
  label: string;
  url: string;
  type: LocationType;
};

const LocationList = ({ label, url, type }: LocationListType) => {
  const { dispatch } = useContext(AuthContext);
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await authorizedFetch(dispatch, url).then((res) => res.json());
      setData(result);
    };

    fetchData();
  }, [dispatch, url]);
  return (
    <Grid container spacing={3}>
      <Grid item xs={12}>
        <Typography variant="h6">{`${label} (${data.length})`}</Typography>
        <LocationTable data={data} type={type} />
      </Grid>
    </Grid>
  );
};

export default LocationList;
