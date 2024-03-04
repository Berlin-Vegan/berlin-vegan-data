import { css } from '@emotion/react';

import theme from '@/theme';

export const styles = {
  review: css`
    margin-top: 32px;
  `,
  reviewList: css`
    display: flex;
    flex-wrap: wrap;
    justify-content: space-around;
    overflow: hidden;
    background-color: ${theme.palette.background.paper};
  `,
};
