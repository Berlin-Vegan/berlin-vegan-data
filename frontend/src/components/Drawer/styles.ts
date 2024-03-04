import { css } from '@emotion/react';

export const styles = {
  toolbarIcon: css`
    display: flex;
    align-items: center;
    justify-content: flex-end;
    padding: 0 8px;
    ...theme.mixins.toolbar
  `,
};
