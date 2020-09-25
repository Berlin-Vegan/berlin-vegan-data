import React, { useEffect, useState } from 'react';

import Grid from '@material-ui/core/Grid';

import GastroTable from '../components/GastroTable';
import { fetchGastroList } from '../utils/fetch';

const Submissions = () => {
  const [data, setData] = useState([]);

  useEffect(() => {
    const fetchData = async () => {
      const result = await fetchGastroList('is_submission=true').then((res) =>
        res.json()
      );
      setData(result);
    };

    fetchData();
  }, []);

  return (
    <Grid container spacing={3}>
      <Grid item xs={12}>
        <GastroTable data={data} />
      </Grid>
    </Grid>
  );
};

export default Submissions;