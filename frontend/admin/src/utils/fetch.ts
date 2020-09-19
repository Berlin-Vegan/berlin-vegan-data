import { getCSRFToken } from './cookie';
import { store } from '../store/store';

export const authorizedFetch = async (
  url: string,
  method: string = 'GET',
  body: object | Array<unknown> | null = null
): Promise<Response> => {
  const response = await fetch(url, {
    method,
    body: body ? JSON.stringify(body) : body,
    headers: {
      'Content-Type': 'application/json',
      'X-CSRFToken': getCSRFToken(),
    },
  });

  if (response.status === 403) {
    store.dispatch({ type: 'LOGOUT_USER' });
  }

  return response;
};

export const fetchGastroList = async (filter: string): Promise<Response> =>
  authorizedFetch(`/api/v1/gastros/?${filter}`);
