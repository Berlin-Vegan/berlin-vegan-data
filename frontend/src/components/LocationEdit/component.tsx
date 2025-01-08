import { FC, useContext, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';

import * as Yup from 'yup';
import getReview from '@components//Review';
import LocationBaseFormEdit from '@components/LocationBaseFormEdit';
import LocationBaseType from '@components/LocationFormBase/locationBaseType';
import PaperDefault from '@components/PaperDefault';
import { isEmpty, pathOr } from 'ramda';

import NotFoundPage from '@/pages/NotFoundPage';
import { AuthContext } from '@/providers/UserProvider';
import { LocationType } from '@/utils/constants';
import { authorizedFetch } from '@/utils/fetch';
import { buildDetailUrl } from '@/utils/utils';
import ImageList from '@components/ImageList';

type LocationEditType = {
  type: LocationType;
  label: string;
  locationForm: FC;
  locationFormSchema: Yup.AnySchema;
};

type LocationDataStateType = object | LocationBaseType;

const LocationEdit: FC<LocationEditType> = ({ type, label, locationForm, locationFormSchema }) => {
  const { dispatch } = useContext(AuthContext);
  const { id } = useParams();
  const [locationData, setLocationDataState] = useState<LocationDataStateType>({});
  const [notFound, setNotFound] = useState(false);

  const locationUrl = buildDetailUrl(type, id ?? '');

  useEffect(() => {
    const fetchData = async () => {
      const res = await authorizedFetch(dispatch, locationUrl);
      const data = await res.json();
      if (res.status === 200) {
        setLocationDataState(data);
      }
      if (res.status === 404) {
        setNotFound(true);
      }
    };
    fetchData();
  }, [id, dispatch, locationUrl]);

  return notFound ? (
    <NotFoundPage />
  ) : (
    <>
      {isEmpty(locationData) ? (
        <PaperDefault>
          <div>Loading</div>
        </PaperDefault>
      ) : (
        <>
          <LocationBaseFormEdit
            label={label}
            locationUrl={locationUrl}
            locationForm={locationForm}
            locationData={locationData as LocationBaseType}
            locationFormSchema={locationFormSchema}
            setLocationDataState={setLocationDataState}
          />
          {getReview(pathOr(null, ['review'], locationData))}
          <ImageList />
        </>
      )}
    </>
  );
};

export default LocationEdit;
