import { useMemo } from 'react';

const useStyles = (): {
  capitalizeTitle: React.CSSProperties;
  chips: React.CSSProperties;
  chip: React.CSSProperties;
} => {
  return useMemo(
    () => ({
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
    }),
    [],
  );
};

export default useStyles;
