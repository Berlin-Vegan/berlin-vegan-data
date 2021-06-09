import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(() => ({
  capitalizeTitle: {
    textTransform: 'capitalize',
  },
  chips: {
    display: 'flex',
    flexWrap: 'wrap',
  },
  chip: {
    margin: 2,
  },
}));

export default useStyles;
