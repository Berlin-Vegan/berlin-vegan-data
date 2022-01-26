import { pipe, toLower } from 'ramda';
import { LocationType, V1, V2 } from './constants';

//
export const buildReviewListUrl: string = `${V1}review/`;
export const buildReviewDetailUrl = (id: number): string =>
  `${buildReviewListUrl}${id}/`;

// API V2 urls
export const buildListUrl = (type: LocationType): string =>
  pipe(toLower, (lowerType: string) => `${V2}${lowerType}/`)(type);
export const buildDetailUrl = (type: LocationType, id: string): string =>
  pipe(toLower, buildListUrl, (baseUrl: string) => `${baseUrl}${id}/`)(type);
// FE urls
export const buildFEDetailUrl = (type: LocationType, id: string): string =>
  pipe(toLower, (lowerType: string) => `/${lowerType}/${id}/edit`)(type);
