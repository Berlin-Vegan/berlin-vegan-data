import { TYPE_USER_LOGOUT, UserDispatch } from '../providers/UserProvider';
import { getCSRFToken } from './cookie';

export const authorizedFetch = async (
  userDispatch: UserDispatch,
  url: string,
  method = 'GET',
  body: object | Array<unknown> | null = null,
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

export const authorizedFetchPostFile = async (
  userDispatch: UserDispatch,
  url: string,
  formData: FormData,
): Promise<Response> => {
  const response = await fetch(url, {
    method: 'POST',
    body: formData,
    headers: {
      'X-CSRFToken': getCSRFToken(),
    },
  });

  if (response.status === 403) {
    userDispatch({ type: TYPE_USER_LOGOUT });
  }

  return response;
};
