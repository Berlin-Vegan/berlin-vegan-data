import { useMemo } from 'react';

import { type Theme, useTheme } from '@mui/material/styles';

const useStyles = (): {
  paper: React.CSSProperties;
  avatar: React.CSSProperties;
  form: React.CSSProperties;
  submit: React.CSSProperties;
  noError: React.CSSProperties;
  error: React.CSSProperties;
} => {
  const theme: Theme = useTheme();
  return useMemo(
    () => ({
      paper: {
        marginTop: theme.spacing(8),
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center',
      },
      avatar: {
        margin: theme.spacing(1),
        backgroundColor: theme.palette.secondary.main,
      },
      form: {
        width: '100%', // Fix IE 11 issue.
        marginTop: theme.spacing(1),
      },
      submit: {
        margin: theme.spacing(3, 0, 2),
      },
      noError: {
        display: 'none',
      },
      error: {
        color: theme.palette.error.main,
        textAlign: 'center',
      },
    }),
    [theme],
  );
};

export default useStyles;
