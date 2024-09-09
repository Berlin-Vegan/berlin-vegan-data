import { PropsWithChildren } from 'react';

import Grid from '@mui/material/Grid';

import AttributesFormPart from './attributesFormPart';
import DetailsFormPart from './detailsFormPart';
import SubmitEmailField from './fields/SubmitEmailField';
import GeneralFormPart from './generalFormPart';
import metaFormPart from './metaFormPart';
import openingHoursFormPart from './openingHoursFormPart';
import TagsFormPart from './tagsFormPart';

type LocationFormBaseProps = {
  booleanAttrList: string[];
  positiveIntegerAttrList: string[];
  tagList: string[];
  veganOption?: boolean;
};

const LocationFormBase = ({
  children,
  booleanAttrList,
  positiveIntegerAttrList,
  tagList,
  veganOption = false,
}: PropsWithChildren<LocationFormBaseProps>) => (
  <Grid container direction="column" spacing={1}>
    <SubmitEmailField />
    <GeneralFormPart veganOption={veganOption} />
    {openingHoursFormPart}
    <DetailsFormPart />
    <AttributesFormPart
      booleanAttrList={booleanAttrList}
      positiveIntegerAttrList={positiveIntegerAttrList}
    />
    <TagsFormPart tagList={tagList} />
    {metaFormPart}
    {children}
  </Grid>
);

export default LocationFormBase;
