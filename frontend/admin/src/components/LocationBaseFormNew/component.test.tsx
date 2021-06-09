import React from 'react';
import * as Yup from 'yup';
import { SnackbarProvider } from 'notistack';
import { standardComponentTest } from '../../utils/testing';
import {
  initialLocationBooleanAttributeData,
  initialLocationData,
} from './initialData';
import LocationBaseFormNew from './component';
import { GASTRO } from '../../utils/constants';
import locationBaseSchema, {
  BASE_BOOLEAN_ATTRIBUTES,
  booleanAttributeSchema,
} from '../LocationFormBase/formSchema';
import LocationFormBase from '../LocationFormBase';

const initialFormData = {
  ...initialLocationData,
  attributes: {
    ...initialLocationBooleanAttributeData,
  },
};
const tags = ['testTag'];

const form = () => (
  <LocationFormBase booleanAttrList={BASE_BOOLEAN_ATTRIBUTES} tagList={tags} />
);

const formSchema = locationBaseSchema.shape({
  tags: Yup.array().of(Yup.string().oneOf(tags)),
  attributes: Yup.object().shape(
    booleanAttributeSchema(BASE_BOOLEAN_ATTRIBUTES),
  ),
});

const LocationBaseFormNewWrapper = () => (
  <SnackbarProvider maxSnack={3}>
    <LocationBaseFormNew
      label="TestLabel"
      type={GASTRO}
      locationForm={form}
      locationFormSchema={formSchema}
      initialData={initialFormData}
    />
  </SnackbarProvider>
);

standardComponentTest(LocationBaseFormNewWrapper);
