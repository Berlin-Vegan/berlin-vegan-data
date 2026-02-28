import type { SxProps, Theme } from '@mui/material';

import theme from '@/theme';

export const styles: { review: SxProps<Theme>; reviewList: SxProps<Theme> } = {
  review: {
    mt: 4, // 32px
  },
  reviewList: {
    display: 'flex',
    flexWrap: 'wrap',
    justifyContent: 'space-around',
    overflow: 'hidden',
    backgroundColor: theme.palette.background.paper,
  },
};
