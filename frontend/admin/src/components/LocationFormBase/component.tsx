import React, { FC } from 'react';
import Grid from '@material-ui/core/Grid';
import SubmitEmailField from '../GastroFormBase/fields/SubmitEmailField';
import GeneralFormPart from './generalFormPart';
import openingHoursFormPart from './openingHoursFormPart';
import DetailsFormPart from './detailsFormPart';
import TagsFormPart from './tagsFormPart';
import AttributesFormPart from './attributesFormPart';
import metaFormPart from '../GastroFormBase/metaFormPart';

type LocationFormBaseProps = {
  booleanAttrList: string[];
  tagList: string[];
};

const LocationFormBase: FC<LocationFormBaseProps> = ({
  children,
  booleanAttrList,
  tagList,
}) => (
  <Grid container direction="column" spacing={1}>
    <SubmitEmailField />
    <GeneralFormPart />
    {openingHoursFormPart}
    <DetailsFormPart />
    <AttributesFormPart booleanAttrList={booleanAttrList} />
    <TagsFormPart tagList={tagList} />
    {metaFormPart}
    {children}
  </Grid>
);

export default LocationFormBase;
