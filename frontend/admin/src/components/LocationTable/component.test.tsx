import React from 'react';
import { standardComponentTest } from '../../utils/testing';
import LocationTable, { ILocationTableProps } from './component';
import { FilterProvider } from '../../providers/FilterProvider';

const LocationTableWrapper = (props: ILocationTableProps) => (
  <FilterProvider>
    <LocationTable {...props} />
  </FilterProvider>
);

standardComponentTest(LocationTableWrapper, { title: '', data: [] });
const dataID = {
  id: 'fwfwgeg345egetg34',
  name: 'TestName',
  postalCode: '12345',
  city: 'Berlin',
  vegan: 5,
  hasReviewLink: true,
};
standardComponentTest(LocationTableWrapper, {
  title: 'TestTable',
  data: [dataID],
});

const dataIDString = {
  idString: 'fwfwgeg345egetg34',
  name: 'TestName',
  postalCode: '12345',
  city: 'Berlin',
  vegan: 5,
  hasReviewLink: false,
};
standardComponentTest(LocationTableWrapper, {
  title: 'TestTable',
  data: [dataIDString],
});
