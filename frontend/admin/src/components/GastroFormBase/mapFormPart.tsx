import React, { FC, useEffect, useState } from 'react';
import { useField } from 'formik';
import ReactMapGL, { Marker, NavigationControl } from 'react-map-gl';
import RoomIcon from '@material-ui/icons/Room';

const marker = (lat: number, long: number, setLatLong: any) => (
  <Marker
    latitude={lat}
    longitude={long}
    draggable={true}
    onDragEnd={(e) => setLatLong(e.lngLat)}
  >
    <RoomIcon fontSize="large" />
  </Marker>
);

type MapProps = {
  lat: number;
  long: number;
  setLongLatFields: (long: number, lat: number) => any;
};

type ViewportState = {
  latitude: number;
  longitude: number;
  zoom: number;
};

const Map: FC<MapProps> = ({ lat, long, setLongLatFields }) => {
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

  const setLongLatViewportFields = ([longMarker, latMarker]: [
    number,
    number
  ]) => {
    setLongLatFields(longMarker, latMarker);
    setViewportState({
      ...viewportState,
      longitude: longMarker,
      latitude: lat,
    });
  };

  return (
    <ReactMapGL
      {...viewportState}
      width="100vw"
      height="25vh"
      mapStyle={process.env.REACT_APP_MAP_API_URL}
      onViewportChange={(nextViewport) =>
        setViewportState({
          latitude: nextViewport.latitude,
          longitude: nextViewport.longitude,
          zoom: nextViewport.zoom,
        })}
    >
      <div style={{ position: 'absolute', right: 0 }}>
        <NavigationControl />
      </div>
      {marker(lat, long, setLongLatViewportFields)}
    </ReactMapGL>
  );
};

const latlongEmpty = <div>Latitude & Longitude are empty.</div>;

const MapFormPart = () => {
  const [, { value: latitudeValue }, { setValue: setValueLatitude }] = useField(
    'latitude'
  );
  const [
    ,
    { value: longitudeValue },
    { setValue: setValueLongitude },
  ] = useField('longitude');

  const setNewLongLat = (long: number, lat: number) => {
    setValueLatitude(lat);
    setValueLongitude(long);
  };

  return latitudeValue && longitudeValue ? (
    <Map
      lat={parseFloat(latitudeValue)}
      long={parseFloat(longitudeValue)}
      setLongLatFields={setNewLongLat}
    />
  ) : (
    latlongEmpty
  );
};

export default MapFormPart;
