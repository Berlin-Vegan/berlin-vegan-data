import type { SxProps, Theme } from '@mui/material';

export const styles: {
  flexContainerSpinner: SxProps<Theme>;
  reviewLabelSpinner: SxProps<Theme>;
  reviewRightSpinner: SxProps<Theme>;
} = {
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
};
