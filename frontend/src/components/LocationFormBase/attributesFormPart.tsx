import { Grid } from '@mui/material';
import Typography from '@mui/material/Typography';

import booleanAttributesFormPart from './booleanAttributesFormPart';
import positiveIntegerAttributesFormPart from './positiveIntegerAttributesFormPart';

type IAttributesFormPartProps = {
  booleanAttrList: string[];
  positiveIntegerAttrList: string[];
};

const AttributesFormPart = ({
  booleanAttrList,
  positiveIntegerAttrList,
}: IAttributesFormPartProps) => (
  <>
    <Typography variant="h5">Attributes</Typography>
    <Grid container spacing={1}>
      {booleanAttributesFormPart(booleanAttrList)}
      {positiveIntegerAttributesFormPart(positiveIntegerAttrList)}
    </Grid>
  </>
);

export default AttributesFormPart;
