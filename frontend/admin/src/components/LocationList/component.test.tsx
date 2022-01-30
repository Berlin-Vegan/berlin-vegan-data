import React from 'react';
import { standardComponentTestMockFetch } from '../../utils/testing';
import LocationList from './component';
import { FilterProvider } from '../../providers/FilterProvider';

const LocationListWrapper = () => (
  <FilterProvider>
    <LocationList
      label="TestList"
      url="/api/vX/list"
      overwriteTableOptions={{ tableId: 'testID' }}
    />
  </FilterProvider>
);

standardComponentTestMockFetch(LocationListWrapper, {}, []);
