import { css } from '@emotion/react';

import theme from '@/theme';

export const styles = {
  toolbar: css`
    padding-right: 24px;
  `,
  menuButtonHidden: css`
    display: none;
  `,
  menuButton: css`
    margin-right: 36px;
  `,
  logo: css`
    margin-right: 20px;
    width: 50px;
    height: 50px;
  `,
  title: css`
    flex-grow: 1;
  `,
  logout: css`
    margin: ${theme.spacing(1)};
  `,
};
