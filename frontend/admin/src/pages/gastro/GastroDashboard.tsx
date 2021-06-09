import React, { useContext, useEffect, useState } from 'react';

import Grid from '@material-ui/core/Grid';
import { AuthContext } from '../../providers/UserProvider';
import { fetchGastroList } from '../../utils/fetch';
import LocationTable from '../../components/LocationTable';

const GastroDashboard = () => {
  const { dispatch } = useContext(AuthContext);
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchGastroList(
        dispatch,
        'closed=false&is_submission=false',
      ).then((res) => res.json());
      setData(result);
    };

    fetchData();
  }, [dispatch]);

  return (
    <Grid container spacing={3}>
      <Grid item xs={12}>
        <LocationTable title="Gastro" data={data} />
      </Grid>
    </Grid>
  );
};

export default GastroDashboard;
