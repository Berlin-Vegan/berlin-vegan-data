import { compose, curry, defaultTo, nth } from 'ramda';

export const nthOr = curry((defaultVal, list) =>
  compose(defaultTo(defaultVal), nth)(list)
);
