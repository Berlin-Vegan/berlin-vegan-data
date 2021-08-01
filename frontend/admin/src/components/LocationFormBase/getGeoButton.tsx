import React from 'react';
import Button from '@material-ui/core/Button';
import { useField } from 'formik';
import { useSnackbar } from 'notistack';
import { nth, prop, propOr } from 'ramda';

const GetGeoButton = () => {
  const [, streetMeta] = useField('street');
  const [, cityMeta] = useField('city');
  const [, postalCodeMeta] = useField('postalCode');
  const [, , { setValue: setValueLatitude }] = useField('latitude');
  const [, , { setValue: setValueLongitude }] = useField('longitude');

  const { enqueueSnackbar } = useSnackbar();

  const fetchGeoLocation = async () => {
    const res = await fetch(
      `https://nominatim.openstreetmap.org/search?format=json&limit=1&q=${streetMeta.value},${postalCodeMeta.value},${cityMeta.value}`,
    );
    if (res.status === 200) {
      const data = await res.json();

      if (
        nth(0, data) &&
        propOr(false, 'lat', nth(0, data)) &&
        propOr(false, 'lon', nth(0, data))
      ) {
        setValueLongitude(prop('lon', data[0]));
        setValueLatitude(prop('lat', data[0]));
        enqueueSnackbar('Geo data found', { variant: 'success' });
      } else {
        enqueueSnackbar('Not geo data found', { variant: 'error' });
      }
    }
  };

  return (
    <Button variant="contained" size="small" onClick={fetchGeoLocation}>
      Get Geo data
    </Button>
  );
};
export default GetGeoButton;
