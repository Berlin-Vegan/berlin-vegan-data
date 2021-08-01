import React from 'react';
import * as Yup from 'yup';
import { SnackbarProvider } from 'notistack';
import { standardComponentTest } from '../../utils/testing';
import { initialLocationData } from '../LocationBaseFormNew/initialData';
import LocationBaseFormEdit from './component';
import locationBaseSchema, {
  BASE_BOOLEAN_ATTRIBUTES,
  booleanAttributeSchema,
} from '../LocationFormBase/formSchema';
import LocationFormBase from '../LocationFormBase';
import {
  GASTRO_POSITIVE_INTEGER_ATTRIBUTES,
  positiveIntegerAttributeSchema,
} from '../GastroFormBase/gastroFormSchema';
import {
  initialGastroLocationBooleanAttributeData,
  initialGastroLocationPositiveIntegerAttributeData,
} from '../GastroFormBase/initialData';

const locationData = {
  created: '2000-11-22T04:01:00.000',
  updated: '2000-11-22T04:01:00.000',
  lastEditor: 'testEditor',
  ...initialLocationData,
  attributes: {
    ...initialGastroLocationBooleanAttributeData,
    ...initialGastroLocationPositiveIntegerAttributeData,
  },
};

const tags = ['testTag'];

export const testBaseForm = () => (
  <LocationFormBase
    booleanAttrList={BASE_BOOLEAN_ATTRIBUTES}
    tagList={tags}
    positiveIntegerAttrList={GASTRO_POSITIVE_INTEGER_ATTRIBUTES}
  />
);

export const testFormSchema = locationBaseSchema.shape({
  tags: Yup.array().of(Yup.string().oneOf(tags)),
  attributes: Yup.object()
    .shape(booleanAttributeSchema(BASE_BOOLEAN_ATTRIBUTES))
    .shape(positiveIntegerAttributeSchema(GASTRO_POSITIVE_INTEGER_ATTRIBUTES)),
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
