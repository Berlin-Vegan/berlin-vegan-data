export const VEGAN_OPTIONS_FIELD = new Map<number, string>([
  [2, 'Ominvore (vegan labeled)'],
  [4, 'Vegetarian (vegan labeled)'],
  [5, 'Vegan'],
]);

export const nullToEmptyString = (value: string | null | undefined) =>
  value === null ? '' : value;
export const emptyStringToNull = (value: string) => (value === '' ? null : value);
