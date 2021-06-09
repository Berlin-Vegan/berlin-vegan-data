import React, { FC, useContext, useEffect, useState } from 'react';
import { useParams } from 'react-router-dom';
import { isEmpty } from 'ramda';
import * as Yup from 'yup';
import { AuthContext } from '../../providers/UserProvider';
import { authorizedFetch } from '../../utils/fetch';
import NotFoundPage from '../../pages/NotFoundPage';
import LocationBaseFormEdit from '../LocationBaseFormEdit';
import PaperDefault from '../PaperDefault';
import LocationBaseType from '../LocationFormBase/locationBaseType';
import { buildDetailUrl } from '../../utils/utils';
import { LocationType } from '../../utils/constants';

interface IParams {
  id: string;
}

type LocationEditType = {
  type: LocationType;
  label: string;
  locationForm: FC;
  locationFormSchema: Yup.AnySchema;
};

const LocationEdit: FC<LocationEditType> = ({
  type,
  label,
  locationForm,
  locationFormSchema,
}) => {
  const { dispatch } = useContext(AuthContext);
  const { id } = useParams<IParams>();
  const [locationData, setLocationDataState] = useState<
    object | LocationBaseType
  >({});
  const [notFound, setNotFound] = useState(false);

  const locationUrl = buildDetailUrl(type.toLowerCase(), id);

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
    <PaperDefault>
      {isEmpty(locationData) ? (
        <div>Loading</div>
      ) : (
        <LocationBaseFormEdit
          label={label}
          locationUrl={locationUrl}
          locationForm={locationForm}
          locationData={locationData as LocationBaseType}
          locationFormSchema={locationFormSchema}
        />
      )}
    </PaperDefault>
  );
};

export default LocationEdit;
