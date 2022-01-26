export const GASTRO: string = 'GASTRO';
export const SHOPPING: string = 'SHOPPING';

export type LocationType = typeof GASTRO | typeof SHOPPING;

const API = '/api/';
export const V1 = `${API}v1/`;
export const V2 = `${API}v2/`;
