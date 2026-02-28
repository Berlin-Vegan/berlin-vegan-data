import type { SxProps, Theme } from '@mui/material';

import theme from '@/theme';

export const styles: {
  toolbar: SxProps<Theme>;
  menuButtonHidden: SxProps<Theme>;
  menuButton: SxProps<Theme>;
  logo: SxProps<Theme>;
  title: SxProps<Theme>;
  logout: SxProps<Theme>;
} = {
  toolbar: {
    pr: '24px',
  },
  menuButtonHidden: {
    display: 'none',
  },
  menuButton: {
    mr: '36px',
  },
  logo: {
    mr: '20px',
    width: '50px',
    height: '50px',
  },
  title: {
    flexGrow: 1,
  },
  logout: {
    margin: theme.spacing(1),
  },
};
