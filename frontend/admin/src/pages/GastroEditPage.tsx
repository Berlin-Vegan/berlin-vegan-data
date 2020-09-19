import React, { useEffect, useState } from 'react';
import { Paper } from '@material-ui/core';
import { useParams } from 'react-router-dom';
import { makeStyles } from '@material-ui/core/styles';
import { isEmpty } from 'ramda';
import GastroFormEdit from '../components/GastroFormEdit';
import { authorizedFetch } from '../utils/fetch';
import NotFoundPage from './NotFoundPage';
import { GastroDataType } from '../components/GastroFormEdit/types';

const useStyles = makeStyles(() => ({
  paper: {
    padding: '16px',
  },
}));

const fetchGastro = async (id: string) =>
  authorizedFetch(`/api/v1/gastros/${id}`);

interface IParams {
  id: string;
}

const GastroEditPage = () => {
  const classes = useStyles();
  const { id } = useParams<IParams>();
  const [gastroData, setGastroState] = useState<object | GastroDataType>({});
  const [notFound, setNotFound] = useState(false);

  useEffect(() => {
    const fetchData = async () => {
      const res = await fetchGastro(id);
      const data = await res.json();
      if (res.status === 200) {
        setGastroState(data);
      }
      if (res.status === 404) {
        setNotFound(true);
      }
    };
    fetchData();
  }, [id]);

  return notFound ? (
    <NotFoundPage />
  ) : (
    <Paper className={classes.paper}>
      {isEmpty(gastroData) ? (
        <div>Loading</div>
      ) : (
        <GastroFormEdit gastroData={gastroData as GastroDataType} />
      )}
    </Paper>
  );
};

export default GastroEditPage;
