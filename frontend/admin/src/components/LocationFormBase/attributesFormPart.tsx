import React, { FC } from 'react';
import Typography from '@material-ui/core/Typography';
import { Grid } from '@material-ui/core';
import booleanAttributesFormPart from './booleanAttributesFormPart';
import positiveIntegerAttributesFormPart from './positiveIntegerAttributesFormPart';

type IAttributesFormPartProps = {
  booleanAttrList: string[];
  positiveIntegerAttrList: string[];
};

const AttributesFormPart: FC<IAttributesFormPartProps> = ({
  booleanAttrList,
  positiveIntegerAttrList,
}) => (
  <>
    <Typography variant="h5">Attributes</Typography>
    <Grid container spacing={1}>
      {booleanAttributesFormPart(booleanAttrList)}
      {positiveIntegerAttributesFormPart(positiveIntegerAttrList)}
    </Grid>
  </>
);

export default AttributesFormPart;
