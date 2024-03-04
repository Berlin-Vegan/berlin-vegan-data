import { Paper } from '@mui/material';
import { styled } from '@mui/material/styles';

const PREFIX = 'PaperDefault';

const classes = {
  paper: `${PREFIX}-paper`,
};

const StyledPaper = styled(Paper)(() => ({
  [`&.${classes.paper}`]: {
    padding: '16px',
  },
}));

const PaperDefault = ({ children }: { children: JSX.Element | JSX.Element[] }) => {
  return <StyledPaper className={classes.paper}>{children}</StyledPaper>;
};

export default PaperDefault;
