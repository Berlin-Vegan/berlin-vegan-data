import React from 'react';
import * as Yup from 'yup';
import { SnackbarProvider } from 'notistack';
import { standardComponentTest } from '../../utils/testing';
import {
  initialLocationBooleanAttributeData,
  initialLocationData,
} from '../LocationBaseFormNew/initialData';
import LocationBaseFormEdit from './component';
import locationBaseSchema, {
  BASE_BOOLEAN_ATTRIBUTES,
  booleanAttributeSchema,
} from '../LocationFormBase/formSchema';
import LocationFormBase from '../LocationFormBase';

const locationData = {
  created: '2000-11-22T04:01:00.000',
  updated: '2000-11-22T04:01:00.000',
  lastEditor: 'testEditor',
  ...initialLocationData,
  attributes: {
    ...initialLocationBooleanAttributeData,
  },
};

const tags = ['testTag'];

export const testBaseForm = () => (
  <LocationFormBase booleanAttrList={BASE_BOOLEAN_ATTRIBUTES} tagList={tags} />
);

export const testFormSchema = locationBaseSchema.shape({
  tags: Yup.array().of(Yup.string().oneOf(tags)),
  attributes: Yup.object().shape(
    booleanAttributeSchema(BASE_BOOLEAN_ATTRIBUTES),
  ),
});

const LocationBaseFormNewWrapper = () => (
  <SnackbarProvider maxSnack={3}>
    <LocationBaseFormEdit
      label="TestLabel"
      locationUrl="/api/vX/location"
      locationForm={testBaseForm}
      locationData={locationData}
      locationFormSchema={testFormSchema}
    />
  </SnackbarProvider>
);

standardComponentTest(LocationBaseFormNewWrapper);
