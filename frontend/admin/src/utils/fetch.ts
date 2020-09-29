import { getCSRFToken } from './cookie';
import { UserDispatch, TYPE_USER_LOGOUT } from '../providers/UserProvider';

export const authorizedFetch = async (
  userDispatch: UserDispatch,
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
    userDispatch({ type: TYPE_USER_LOGOUT });
  }

  return response;
};

export const fetchGastroList = async (
  userDispatch: UserDispatch,
  filter: string
): Promise<Response> =>
  authorizedFetch(userDispatch, `/api/v1/gastros/?${filter}`);
