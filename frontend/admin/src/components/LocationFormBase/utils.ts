import { join, pipe, split } from 'ramda';

export const buildLabel = (key: string): string =>
  pipe(split(/(?=[A-Z])/), join(' '))(key);
