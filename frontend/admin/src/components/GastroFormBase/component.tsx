import React, { FC } from 'react';
import Grid from '@material-ui/core/Grid';
import GeneralFormPart from './generalFormPart';
import openingHoursFormPart from './openingHoursFormPart';
import DetailsFormPart from './detailsFormPart';
import tagsFormPart from './tagsFormPart';
import metaFormPart from './metaFormPart';
import SubmitEmailField from './fields/SubmitEmailField';

const GastroBaseForm: FC = ({ children }) => {
  return (
    <Grid container direction="column" spacing={1}>
      <SubmitEmailField />
      <GeneralFormPart />
      {openingHoursFormPart}
      <DetailsFormPart />
      {tagsFormPart}
      {metaFormPart}
      {children}
    </Grid>
  );
};

export default GastroBaseForm;
