import { type Theme, useTheme } from '@mui/material/styles';
import { useMemo } from 'react';

export const drawerWidth = 240;

export const useStyles = (): {
  root: React.CSSProperties;
  appBarSpacer: React.CSSProperties;
  content: React.CSSProperties;
  container: React.CSSProperties;
} => {
  const theme: Theme = useTheme();
  return useMemo(
    () => ({
      root: {
        display: 'flex',
      },
      appBarSpacer: theme.mixins.toolbar as unknown as React.CSSProperties,
      content: {
        flexGrow: 1,
        height: '100vh',
        overflow: 'auto',
      },
      container: {
        paddingTop: theme.spacing(4),
        paddingBottom: theme.spacing(4),
      },
    }),
    [theme],
  );
};
