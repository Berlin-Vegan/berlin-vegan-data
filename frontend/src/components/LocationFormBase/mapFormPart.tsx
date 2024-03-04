import { useCallback, useEffect, useState } from 'react';
import type { MarkerDragEvent } from 'react-map-gl/maplibre';
import Map, { Marker, NavigationControl } from 'react-map-gl/maplibre';

import RoomIcon from '@mui/icons-material/Room';

import { useField } from 'formik';
import 'maplibre-gl/dist/maplibre-gl.css';

type MapProps = {
  lat: number;
  long: number;
  setLongLatFields: (long: number, lat: number) => void;
};

type ViewportState = {
  latitude: number;
  longitude: number;
  zoom: number;
};

const BVMap = ({ lat, long, setLongLatFields }: MapProps) => {
  const [viewportState, setViewportState] = useState<ViewportState>({
    latitude: lat,
    longitude: long,
    zoom: 15,
  });

  useEffect(() => {
    const setLongLatViewport = (longViewport: number, latViewport: number) =>
      setViewportState((state) => ({
        ...state,
        latitude: latViewport,
        longitude: longViewport,
      }));

    setLongLatViewport(long, lat);
  }, [lat, long]);

  const onMarkerDragEnd = useCallback(
    (event: MarkerDragEvent) => {
      setLongLatFields(event.lngLat.lng, event.lngLat.lat);
    },
    [setLongLatFields],
  );

  return (
    <Map
      initialViewState={viewportState}
      mapStyle={`https://api.maptiler.com/maps/streets-v2/style.json?key=${
        import.meta.env.VITE_MAP_API_URL
      }`}
      style={{ width: '70vw', height: '20vh', marginTop: '10px' }}
    >
      <Marker
        longitude={viewportState.longitude}
        latitude={viewportState.latitude}
        draggable
        onDragEnd={onMarkerDragEnd}
      >
        <RoomIcon />
      </Marker>
      <NavigationControl />
    </Map>
  );
};

const latLongEmpty = <div>Latitude & Longitude are empty.</div>;

const MapFormPart = () => {
  const [, { value: latitudeValue }, { setValue: setValueLatitude }] = useField('latitude');
  const [, { value: longitudeValue }, { setValue: setValueLongitude }] = useField('longitude');

  const setNewLongLat = (long: number, lat: number): void => {
    setValueLatitude(lat);
    setValueLongitude(long);
  };

  return latitudeValue && longitudeValue ? (
    <BVMap
      lat={parseFloat(latitudeValue)}
      long={parseFloat(longitudeValue)}
      setLongLatFields={setNewLongLat}
    />
  ) : (
    latLongEmpty
  );
};

export default MapFormPart;
