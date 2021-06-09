import React from 'react';
import { MemoryRouter } from 'react-router-dom';
import { standardComponentTestMockFetch } from '../../utils/testing';
import LocationEdit from './component';
import {
  initialLocationBooleanAttributeData,
  initialLocationData,
} from '../LocationBaseFormNew/initialData';
import { GASTRO } from '../../utils/constants';
import {
  testBaseForm,
  testFormSchema,
} from '../LocationBaseFormEdit/component.test';

const fakeResponse = {
  created: '2000-11-22T04:01:00.000',
  updated: '2000-11-22T04:01:00.000',
  lastEditor: 'testEditor',
  ...initialLocationData,
  attributes: {
    ...initialLocationBooleanAttributeData,
  },
};

const props = {
  type: GASTRO,
  label: 'Gastro List',
  locationForm: testBaseForm,
  locationFormSchema: testFormSchema,
};

const LocationEditWrapper = () => (
  <MemoryRouter>
    <LocationEdit {...props} />
  </MemoryRouter>
);

standardComponentTestMockFetch(LocationEditWrapper, {}, fakeResponse);
