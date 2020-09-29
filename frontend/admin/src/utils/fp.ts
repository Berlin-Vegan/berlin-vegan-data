import { addIndex, compose, curry, defaultTo, map, nth } from 'ramda';

export const nthOr = curry((defaultVal, list) =>
  compose(defaultTo(defaultVal), nth)(list)
);

export const mapIndexed = addIndex(map);
