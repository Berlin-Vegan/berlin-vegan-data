import { pipe, toLower } from 'ramda';
import { LocationType } from './constants';

// API urls
export const buildListUrl = (type: LocationType): string =>
  pipe(toLower, (lowerType: string) => `/api/v2/${lowerType}/`)(type);
export const buildDetailUrl = (type: LocationType, id: string): string =>
  pipe(toLower, buildListUrl, (baseUrl: string) => `${baseUrl}${id}/`)(type);
// FE urls
export const buildFEDetailUrl = (type: LocationType, id: string): string =>
  pipe(toLower, (lowerType: string) => `/${lowerType}/${id}/edit`)(type);
