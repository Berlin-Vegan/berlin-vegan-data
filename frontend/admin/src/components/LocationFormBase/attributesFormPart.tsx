import React, { FC } from 'react';
import Typography from '@material-ui/core/Typography';
import { Grid } from '@material-ui/core';
import booleanAttributesFormPart from './booleanAttributesFormPart';

type IAttributesFormPartProps = {
  booleanAttrList: string[];
};

const AttributesFormPart: FC<IAttributesFormPartProps> = ({
  booleanAttrList,
}) => (
  <>
    <Typography variant="h5">Attributes</Typography>
    <Grid container spacing={1}>
      {booleanAttributesFormPart(booleanAttrList)}
    </Grid>
  </>
);

export default AttributesFormPart;
