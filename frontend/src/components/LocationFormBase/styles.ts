import makeStyles from '@mui/styles/makeStyles';

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
