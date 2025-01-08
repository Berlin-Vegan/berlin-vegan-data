import { __, concat, pipe, toLower } from 'ramda';

import { LocationType, V1, V2 } from './constants';

export const buildReviewListUrl = `${V1}review/`;
export const buildImageListUrl = `${V1}image/`;
export const buildReviewDetailUrl = (id: number): string => `${buildReviewListUrl}${id}/`;
export const buildImageDetailUrl = (id: number): string => `${buildImageListUrl}${id}/`;
export const buildImageListFilterLocationlUrl = (id: string): string =>
  `${buildImageListUrl}?location=${id}`;

// API V2 urls
export const buildListUrl = (type: LocationType): string =>
  pipe(toLower, concat(V2), concat(__, '/'))(type);
export const buildDetailUrl = (type: LocationType, id: string): string =>
  pipe(buildListUrl, concat(__, concat('/', concat(id, '/'))))(type);
// FE urls
export const buildFEDetailUrl = (type: LocationType, id: string): string =>
  pipe(toLower, (lowerType: string) => `/${lowerType}/${id}/edit`)(type);
