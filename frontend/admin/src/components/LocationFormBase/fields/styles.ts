import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
  flexContainerSpinner: {
    display: 'flex',
  },
  reviewLabelSpinner: {
    flex: 1,
    margin: 'auto',
  },
  reviewRightSpinner: {
    flex: 1,
  },
}));

export default useStyles;
