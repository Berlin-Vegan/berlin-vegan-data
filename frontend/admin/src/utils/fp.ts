import {
  addIndex,
  compose,
  curry,
  defaultTo,
  join,
  map,
  nth,
  pipe,
  splitAt,
  toLower,
  toUpper,
} from 'ramda';

export const nthOr = curry((defaultVal, list) =>
  compose(defaultTo(defaultVal), nth)(list),
);

export const nthOrEmpty = nthOr('');

export const mapIndexed = addIndex(map);

export const capitalizeWord = pipe(
  toLower,
  splitAt(1),
  (splitted) => [toUpper(nthOrEmpty(0)(splitted)), nthOrEmpty(1)(splitted)],
  join(''),
);
